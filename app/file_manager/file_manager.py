import os
import json

from typing import Dict, List

def create_data_folder():
    """
    Create the data folder if it does not exist
    """
    if not os.path.exists("./data"):
        os.makedirs("./data")

def save_data(data: List[Dict], file_name: str):
    """
    Save the data in a file
    :param data: The data to save
    :param file_name: The file name to save the data in
    """

    if not os.path.exists("./data"):
        create_data_folder()

    with open(f"./data/{file_name}", "w") as file:
        json.dump(data, file, indent=4)


def load_data(file_name: str) -> List[Dict]:
    """
    Load the data from a file
    :param file_name: The file name to load the data from
    :return: The data
    """
    with open(f"./data/{file_name}", "r") as file:
        data = json.load(file)

    return data
