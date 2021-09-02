import os
import subprocess
import sys
from platform import system


from matplotlib import pyplot as plt


HEADERS = {
    'generation': 'generation',
    'min': 'min',
    'max': 'max',
    'median': 'median',
    'avg': 'avg',

    'diversity': {
        'boots': 'diversity_boots',
        'gloves': 'diversity_gloves',
        'helmet': 'diversity_helmet',
        'vest': 'diversity_vest',
        'weapon': 'diversity_weapon',
        'height': 'diversity_height',
    },
}

PLOTS = {
    'max': {
        'n': 1,
        'x': [],
        'y': [],
        'subplot': None,
        'initialized': False,
    },
    'min': {
        'n': 2,
        'x': [],
        'y': [],
        'subplot': None,
        'initialized': False,
    },
    'median': {
        'n': 3,
        'x': [],
        'y': [],
        'subplot': None,
        'initialized': False,
    },
    'avg': {
        'n': 4,
        'x': [],
        'y': [],
        'subplot': None,
        'initialized': False,
    },
    'diversity': {
        'n': 5,
        'subplot': None,
        'initialized': False,
        'x': [],

        'boots': {
            'y': [],
            'bottom': [],
        },
        'gloves': {
            'y': [],
            'bottom': [],
        },
        'helmet': {
            'y': [],
            'bottom': [],
        },
        'vest': {
            'y': [],
            'bottom': [],
        },
        'weapon': {
            'y': [],
            'bottom': [],
        },
        'height': {
            'y': [],
            'bottom': [],
        },
    },
}


HEADERS_DIVERSITY_KEYS = list(HEADERS['diversity'].keys())


def open_file_pipe(filename: str):
    if os.name == 'nt':
        return subprocess.Popen(['powershell', 'Get-Content', filename, '-Wait'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        return subprocess.Popen(['tail', '-F', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def process_header(header: str):
    return header.split(';')


def format_line(header, line: str):
    split_line = line.split(';')
    return {header[i]: split_line[i] for i in range(len(header))}


def get_formatted_line_generation(formatted_line: dict) -> int:
    return int(formatted_line[HEADERS['generation']])


def get_plot_xlim(formatted_line: dict) -> int:
    return max(10, get_formatted_line_generation(formatted_line))


def get_diversity_list(formatted_line: dict) -> list:
    return [int(formatted_line[diversity]) for diversity in HEADERS['diversity'].values()]


def plt_maximize():
    # See discussion: https://stackoverflow.com/questions/12439588/how-to-maximize-a-plt-show-window-using-python
    backend = plt.get_backend()
    cfm = plt.get_current_fig_manager()
    if backend == "wxAgg":
        cfm.frame.Maximize(True)
    elif backend == "TkAgg":
        if system() == "Windows":
            cfm.window.state("zoomed")  # This is windows only
        else:
            cfm.resize(*cfm.window.maxsize())
    elif backend == "QT4Agg":
        cfm.window.showMaximized()
    elif callable(getattr(cfm, "full_screen_toggle", None)):
        if not getattr(cfm, "flag_is_max", None):
            cfm.full_screen_toggle()
            cfm.flag_is_max = True
    else:
        raise RuntimeError("plt_maximize() is not implemented for current backend:", backend)


def plot_two(formatted_line: dict, title: str, key1: str, title1: str, key2: str, title2: str):
    ax = PLOTS[key1]['subplot']
    generation_number = get_formatted_line_generation(formatted_line)

    PLOTS[key1]['x'].append(generation_number)
    PLOTS[key1]['y'].append(float(formatted_line[HEADERS[key1]]))

    PLOTS[key2]['x'].append(generation_number)
    PLOTS[key2]['y'].append(float(formatted_line[HEADERS[key2]]))

    if not PLOTS[key1]['initialized']:
        PLOTS[key1]['initialized'] = True
        ax.set_title(title)

    ax.cla()

    ax.plot(PLOTS[key1]['x'], PLOTS[key1]['y'], label=title1)
    ax.plot(PLOTS[key2]['x'], PLOTS[key2]['y'], label=title2)
    ax.legend(bbox_to_anchor=(1.325, 1.1))

    plt.draw()


def plot_diversity(formatted_line: dict):
    ax = PLOTS['diversity']['subplot']

    generation_number = get_formatted_line_generation(formatted_line)

    PLOTS['diversity']['x'].append(generation_number)
    cumulative = 0
    for i in range(len(HEADERS_DIVERSITY_KEYS)):
        diversity = HEADERS_DIVERSITY_KEYS[i]

        y = float(formatted_line[HEADERS['diversity'][diversity]])
        PLOTS['diversity'][diversity]['y'].append(y)
        PLOTS['diversity'][diversity]['bottom'].append(cumulative)
        cumulative += y

    if not PLOTS['diversity']['initialized']:
        PLOTS['diversity']['initialized'] = True
        ax.set_title('Diversidad')

    ax.cla()

    for i in range(len(HEADERS_DIVERSITY_KEYS)):
        diversity = HEADERS_DIVERSITY_KEYS[i]
        ax.bar(PLOTS['diversity']['x'], PLOTS['diversity'][diversity]['y'], label=diversity.capitalize(), bottom=PLOTS['diversity'][diversity]['bottom'])

    ax.legend(bbox_to_anchor=(1.325, 1.3))

    plt.draw()


def plot_min_max(formatted_line: dict):
    plot_two(formatted_line, 'Fitness maximo y minimo', 'max', 'Maximo', 'min', 'Minimo')


def plot_avg_median(formatted_line: dict):
    plot_two(formatted_line, 'Fitness promedio y mediano', 'avg', 'Promedio', 'median', 'Mediano')


def run():
    f = open_file_pipe(sys.argv[1])

    if len(sys.argv) > 2:
        step = int(sys.argv[2])
    else:
        step = 1

    print('Waiting for changes...')

    header = process_header(f.stdout.readline().strip().decode('ascii'))

    fig, axs = plt.subplots(3)
    plt.tight_layout(h_pad=3, w_pad=3, rect=(0, 0, 0.8, 0.95))

    PLOTS['max']['subplot'] = axs[0]
    PLOTS['avg']['subplot'] = axs[1]
    PLOTS['diversity']['subplot'] = axs[2]

    # plt_maximize()

    plt.ion()
    finished = False
    previous_empty_line = False
    reading = 0
    while not finished:
        line = f.stdout.readline().strip().decode('ascii')
        if len(line) == 0:
            if previous_empty_line:
                finished = True
            else:
                previous_empty_line = True
        else:
            if previous_empty_line:
                previous_empty_line = False

            reading += 1
            if reading < step:
                continue

            formatted_line = format_line(header, line)

            plot_min_max(formatted_line)
            plot_avg_median(formatted_line)
            plot_diversity(formatted_line)
        plt.pause(0.001)

    plt.pause(0.001)
    print('Finished!')

    plt.show(block=True)


if __name__ == '__main__':
    run()
