import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np


# https://stackoverflow.com/questions/25750170/show-decimal-places-and-scientific-notation-on-the-axis-of-a-matplotlib-plot
class MathTextSciFormatter(mticker.Formatter):
    def __init__(self, fmt="%1.2e"):
        self.fmt = fmt

    def __call__(self, x, pos=None):
        s = self.fmt % x
        dec_point = '.'
        pos_sign = '+'
        tup = s.split('e')
        significand = tup[0].rstrip(dec_point)
        sign = tup[1][0].replace(pos_sign, '')
        exponent = tup[1][1:].lstrip('0')
        if not exponent:
            exponent = 0
        exponent = '10^{%s%s}' % (sign, exponent)
        if significand and exponent:
            s = r'%s{\times}%s' % (significand, exponent)
        else:
            s = r'%s%s' % (significand, exponent)
        return "${}$".format(s)


def init_plotter():
    plt.rcParams.update({'font.size': 20})


def plot_values(x_values, x_label, y_values, y_label, precision=2, sci_x=False, sci_y=True, min_val=None, max_val=None,
                log=False, save_name=None, ticks=None):
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.plot(x_values, y_values, marker='o', markersize=3)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    if min_val is not None and max_val is not None:
        ax.set_xlim([min_val, max_val])
        ax.set_ylim([min_val, max_val])

    if log:
        ax.set_yscale('log')

    if sci_x:
        if not log:
            ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
        ax.xaxis.set_major_formatter(MathTextSciFormatter(f'%1.{precision}e'))
    if sci_y:
        if not log:
            ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
        ax.yaxis.set_major_formatter(MathTextSciFormatter(f'%1.{precision}e'))

    if ticks:
        plt.xticks(ticks)

    plt.grid()
    plt.tight_layout()
    if save_name:
        plt.savefig(save_name)
    else:
        plt.show(block=False)


def plot_latent_space(matrix, labels, min_val=None, max_val=None):
    fig, ax = plt.subplots(figsize=(12, 10))
    plt.scatter(matrix[:, 0], matrix[:, 1], s=[60 for _ in range(len(matrix[:, 0]))])

    for i in range(len(labels)):
        ax.annotate(labels[i], (matrix[i, 0], matrix[i, 1]), fontsize=20)

    if min_val is not None and max_val is not None:
        ax.set_xlim([min_val, max_val])
        ax.set_ylim([min_val, max_val])

    plt.tight_layout()
    plt.show(block=False)


def print_pattern(pattern, side):
    for i in range(len(pattern)):
        car = '*' if pattern[i] > 0 else ' '
        print(car, end='')
        if i != 0 and (i + 1) % side == 0:
            print('\n', end='')


def plot_stackbars(x_values_superlist, x_label, y_values_superlist, y_label, legend_list, precision=2, sci_x=False,
                   sci_y=True, min_val_x=None, max_val_x=None, min_val_y=None, max_val_y=None, log_x=False, log_y=False,
                   legend_loc='upper right', xticks=None, width=0.2, save_name=None):
    fig, ax = plt.subplots(figsize=(12, 10))

    for i in range(len(x_values_superlist)):
        plt.bar(
            np.array(x_values_superlist[i]) + i * width,
            y_values_superlist[i],
            label=legend_list[i],
            width=width
        )

    if log_x:
        ax.set_xscale('log')
    if log_y:
        ax.set_yscale('log')

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    if min_val_x is not None and max_val_x is not None:
        ax.set_xlim([min_val_x, max_val_x])
    if min_val_y is not None and max_val_y is not None:
        ax.set_ylim([min_val_y, max_val_y])

    if sci_x:
        if not log_x:
            ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
        ax.xaxis.set_major_formatter(MathTextSciFormatter(f'%1.{precision}e'))
    if sci_y:
        if not log_y:
            ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
        ax.yaxis.set_major_formatter(MathTextSciFormatter(f'%1.{precision}e'))

    if xticks:
        plt.xticks(x_values_superlist[0], xticks)

    plt.tight_layout()
    plt.grid()
    plt.legend(loc=legend_loc)
    if save_name:
        plt.savefig(save_name)
    else:
        plt.show(block=False)


def plot_multiple_values(x_values_superlist, x_label, y_values_superlist, y_label, legend_list, precision=2,
                         sci_x=False, sci_y=True, min_val_x=None, max_val_x=None, min_val_y=None, max_val_y=None,
                         log_x=False, log_y=False, legend_loc='upper right', xticks=None, save_name=None):
    fig, ax = plt.subplots(figsize=(12, 10))

    colors = []
    for i in range(len(x_values_superlist)):
        p = ax.plot(x_values_superlist[i], y_values_superlist[i], label=legend_list[i])
        colors.append(p[-1].get_color())

    if log_x:
        ax.set_xscale('log')
    if log_y:
        ax.set_yscale('log')

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    if min_val_x is not None and max_val_x is not None:
        ax.set_xlim([min_val_x, max_val_x])
    if min_val_y is not None and max_val_y is not None:
        ax.set_ylim([min_val_y, max_val_y])

    if sci_x:
        if not log_x:
            ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
        ax.xaxis.set_major_formatter(MathTextSciFormatter(f'%1.{precision}e'))
    if sci_y:
        if not log_y:
            ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
        ax.yaxis.set_major_formatter(MathTextSciFormatter(f'%1.{precision}e'))

    if xticks:
        plt.xticks(x_values_superlist[0], xticks)

    plt.tight_layout()
    plt.grid()
    plt.legend(loc=legend_loc)
    if save_name:
        plt.savefig(save_name)
    else:
        plt.show(block=False)

    return colors
