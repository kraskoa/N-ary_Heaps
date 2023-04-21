from matplotlib import pyplot as plt


def combined_3_graph_maker(
    times_1,
    times_1_name,
    times_2,
    times_2_name,
    times_3,
    times_3_name,
    # In graph name we will write, for example, "Combined node adding times"
    graph_name,
):
    plt.plot(
        list(times_1.keys()),
        list(times_1.values()),
        label=times_1_name,
        markersize=3,
    )
    plt.plot(
        list(times_2.keys()),
        list(times_2.values()),
        label=times_2_name,
        markersize=3,
    )
    plt.plot(
        list(times_3.keys()),
        list(times_3.values()),
        label=times_3_name,
        markersize=3,
    )
    plt.legend()
    plt.title(label=graph_name)
    figure = plt.gcf()
    plt.show()
    figure.savefig(f"{graph_name}.png", format="png")
