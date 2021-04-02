import plotly.figure_factory as ff
import scipy
import statistics
import pandas as pd
import random

file_data = pd.read_csv("data.csv")
population_data = file_data["reading_time"].tolist()
population_mean = statistics.mean(population_data)


def collect_random():
    collected_elements = []
    for count in range(0, 30):
        random_index = random.randint(0, len(population_data))
        collected_elements.append(population_data[random_index])

    returned_mean = statistics.mean(collected_elements)
    return returned_mean


def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["Reading Time"], show_hist=False)
    fig.show()


def setup():
    mean_list = []
    for count in range(0, 100):
        mean_example = collect_random()
        mean_list.append(mean_example)

    show_fig(mean_list)


setup()
