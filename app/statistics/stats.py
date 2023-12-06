from matplotlib import pyplot as plt
from typing import Dict, List


def random_color(length: int):
    """
    Generate a random color in hexadecimal format
    :return: The random color
    """
    import random

    return ["#" + "".join([random.choice("0123456789ABCDEF") for _ in range(6)]) for _ in range(length)]

def parse_data(data:List[Dict], tags:List[str]=None):
    """
    Parse the data to count the number of each tags
    :param data: The data to parse
    :param tags: The tags to count

    :return: The number of each tags
    """
    if tags is None:
        tags = ["port", "location:country_name", "org", "domains", "os", "location:city"]
   
    values = {key:{} for key in tags}

    for result in data:
        for tag in tags:
            value = result.get(tag, None)

            if value is not None:
                if value in values[tag]:
                    values[tag][value] += 1
                else:
                    values[tag][value] = 1

    return values, tags


def create_pie_chart(data: List[Dict], title: str, tags:List[str]=None):
    """
    Create a pie chart from the data of the tags specified, Show only the 5 biggest values
    
    :param data: The data to create the pie chart
    :param title: The title of the pie chart
    :param tags: The tags to use to create the pie chart
    """
    values, new_tags = parse_data(data, tags)

    num_plots = len(new_tags)
    MAX_PLOTS_BY_COLUMN = 2
    rows = (num_plots + 1) // MAX_PLOTS_BY_COLUMN

    fig, axs = plt.subplots(rows, MAX_PLOTS_BY_COLUMN, figsize=(15, 15))

    for i, tag in enumerate(new_tags):
        row = i // MAX_PLOTS_BY_COLUMN
        col = i % MAX_PLOTS_BY_COLUMN
        ax = axs[row, col] if rows > 1 else axs[col]

        values_to_plot = sorted(values[tag].items(), key=lambda x: x[1], reverse=True)[:5]
        labels = [value[0] for value in values_to_plot]
        data_ = [value[1] for value in values_to_plot]

        ax.pie(data_, labels=labels, autopct='%1.1f%%', shadow=True, colors=random_color(5), explode=[0.1] * len(data_))
        ax.set_title(tag)

    fig.suptitle(title, fontsize=16)
    plt.show()