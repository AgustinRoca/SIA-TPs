from matplotlib import pyplot as plt


def _finish_plt(ax, x_label, y_label, min_v, max_v):
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    if min_v is not None and max_v is not None:
        ax.set_ylim([min_v, max_v])

    plt.grid()
    plt.tight_layout()
    plt.show(block=False)


def plot_values(x, x_label, y, y_label, min_v=None, max_v=None):
    _, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(x, y)  # Plot some data on the axes

    _finish_plt(ax, x_label, y_label, min_v, max_v)


def plot_multiple_values(x, x_label, y, y_label, legends, min_v=None, max_v=None):
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    fig.legend(loc='upper right', ncol=2)

    colors = []
    for i in range(len(x)):
        p = ax.plot(x[i], y[i], label=legends[i], markersize=3)  # Plot some data on the axes
        colors.append(p[-1].get_color())

    _finish_plt(ax, x_label, y_label, min_v, max_v)
