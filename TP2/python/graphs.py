import os
import subprocess
import sys
from platform import system
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


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

    'fraction': {
        'force': 'fraction_force',
        'agility': 'fraction_agility',
        'endurance': 'fraction_endurance',
        'expertise': 'fraction_expertise',
        'health': 'fraction_health',
    },
}

PLOTS = {
    'max': {
        'n': 1,
        'x': [],
        'y': [],
        'subplot': None,
        'l': None,
        'initialized': False,
    },
    'min': {
        'n': 2,
        'x': [],
        'y': [],
        'subplot': None,
        'l': None,
        'initialized': False,
    },
    'median': {
        'n': 3,
        'x': [],
        'y': [],
        'subplot': None,
        'l': None,
        'initialized': False,
    },
    'avg': {
        'n': 4,
        'x': [],
        'y': [],
        'subplot': None,
        'l': None,
        'initialized': False,
    },
    'diversity': {
        'n': 5,
        'subplot': None,
        'initialized': False,
        'x': [],

        'boots': {
            'l': None,
            'y': [],
            'bottom': [],
        },
        'gloves': {
            'l': None,
            'y': [],
            'bottom': [],
        },
        'helmet': {
            'l': None,
            'y': [],
            'bottom': [],
        },
        'vest': {
            'l': None,
            'y': [],
            'bottom': [],
        },
        'weapon': {
            'l': None,
            'y': [],
            'bottom': [],
        },
        'height': {
            'l': None,
            'y': [],
            'bottom': [],
        },
    },
    'fraction': {
        'n': 6,
        'subplot': None,
        'l': None,
        'initialized': False,
        'x': [],

        'force': [],
        'health': [],
        'endurance': [],
        'expertise': [],
        'agility': []
    }
}


HEADERS_DIVERSITY_KEYS = list(HEADERS['diversity'].keys())
HEADERS_FRACTION_KEYS = list(HEADERS['fraction'].keys())
formatted_lines = []
last_len_formatted_lines = 0


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


def plot_all(title, formatted_line: dict, titles, keys, ax):
    for i, key in enumerate(keys):
        generation_number = get_formatted_line_generation(formatted_line)

        PLOTS[key]['x'].append(generation_number)
        PLOTS[key]['y'].append(float(formatted_line[HEADERS[key]]))

    if not PLOTS[key]['initialized']:
        for i, key in enumerate(keys):
            l, = ax.plot(PLOTS[key]['x'], PLOTS[key]['y'], label=titles[i])
            PLOTS[key]['l'] = l

        PLOTS[key]['initialized'] = True
        ax.set_title(title)
        ax.legend(bbox_to_anchor=(1.325, 1.1))
    else:
        max_x = 0
        max_y = 0
        for i, key in enumerate(keys):
            l = PLOTS[key]['l']
            l.set_data(PLOTS[key]['x'], PLOTS[key]['y'])
            if PLOTS[key]['x'][-1] > max_x:
                max_x = PLOTS[key]['x'][-1]
            if PLOTS[key]['y'][-1] > max_y:
                max_y = PLOTS[key]['y'][-1]

        ax.axes.axis([1, max_x, 0, max_y * 1.25])


def plot_diversity(formatted_line: dict):
    ax = PLOTS['diversity']['subplot']

    generation_number = get_formatted_line_generation(formatted_line)

    PLOTS['diversity']['x'].append(generation_number)
    # cumulative = 0
    for i in range(len(HEADERS_DIVERSITY_KEYS)):
        diversity = HEADERS_DIVERSITY_KEYS[i]

        y = float(formatted_line[HEADERS['diversity'][diversity]])
        PLOTS['diversity'][diversity]['y'].append(y)
        # PLOTS['diversity'][diversity]['bottom'].append(cumulative)
        # cumulative += y

    ax.cla()

    ys = []
    labels = []
    for i in range(len(HEADERS_DIVERSITY_KEYS)):
        diversity = HEADERS_DIVERSITY_KEYS[i]
        ys.append(PLOTS['diversity'][diversity]['y'])
        labels.append(diversity.capitalize())

    ax.stackplot(PLOTS['diversity']['x'], *ys, labels=labels)

    if not PLOTS['diversity']['initialized']:
        PLOTS['diversity']['initialized'] = True
        ax.set_title('Diversidad')

    ax.legend(bbox_to_anchor=(1.325, 1.3))


def plot_fraction(formatted_line: dict):
    ax = PLOTS['fraction']['subplot']

    generation_number = get_formatted_line_generation(formatted_line)

    PLOTS['fraction']['x'].append(generation_number)
    for i in range(len(HEADERS_FRACTION_KEYS)):
        diversity = HEADERS_FRACTION_KEYS[i]

        y = float(formatted_line[HEADERS['fraction'][diversity]])
        PLOTS['fraction'][diversity].append(y)

    ax.cla()

    ys = []
    labels = []
    for i in range(len(HEADERS_FRACTION_KEYS)):
        fraction = HEADERS_FRACTION_KEYS[i]
        ys.append(PLOTS['fraction'][fraction])
        labels.append(fraction.capitalize())

    ax.stackplot(PLOTS['fraction']['x'], *ys, labels=labels)

    if not PLOTS['fraction']['initialized']:
        PLOTS['fraction']['initialized'] = True
        ax.set_title('Fraction')

    ax.legend(bbox_to_anchor=(1.325, 1.3))


def plot_min_max(formatted_line: dict):
    plot_all('Fitness maximo y minimo', formatted_line,
             ['Maximo', 'Minimo', 'Promedio'],
             ['max', 'min', 'avg'],
             PLOTS['max']['subplot']
     )


def update_plot(frame):
    global last_len_formatted_lines

    if len(formatted_lines) != last_len_formatted_lines:
        last_len_formatted_lines = len(formatted_lines)

        plot_min_max(formatted_lines[-1])
        plot_diversity(formatted_lines[-1])
        plot_fraction(formatted_lines[-1])


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
    PLOTS['min']['subplot'] = axs[0]
    PLOTS['avg']['subplot'] = axs[0]
    PLOTS['diversity']['subplot'] = axs[1]
    PLOTS['fraction']['subplot'] = axs[2]

    anim = FuncAnimation(fig, update_plot, interval=25)

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

            formatted_lines.append(format_line(header, line))
        plt.pause(0.001)

    plt.pause(0.001)
    print('Finished!')

    plt.show(block=True)


if __name__ == '__main__':
    run()
