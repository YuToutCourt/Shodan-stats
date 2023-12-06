import shodan

from rich.console import Console
from typing import List, Dict


def execute_query(query: str, api_key: str) -> List[Dict]:
    """
    Execute a Shodan search query and return the results
    :param query: The Shodan search query
    :param api_key: The Shodan API key

    :return: The Shodan results
    """
    shodan_api = shodan.Shodan(api_key)

    # Use console to display a spinner while the query is being executed
    console = Console()
    with console.status("[bold green]Shodan Search..."):
        results = shodan_api.search(query)
    console.log("Complete")

    return results["matches"]

def is_forbidden(value):
    """
    Check if the value is forbidden: "", [], {}, None
    :param value: The value to check
    
    :return: True if the value is forbidden, False otherwise
    """
    return any(value == forbidden_value for forbidden_value in ["", [], {}, None])

def parse_value(key, value):
    """
    Parse the value to remove the forbidden values: "", [], {}, None
    :param key: The key of the value
    :param value: The value to parse

    :return: The parsed value
    """
    if isinstance(value, dict):
        return {f"{key}:{child_key}": child_value for child_key, child_value in value.items() if not is_forbidden(child_value)}

    elif isinstance(value, list):
        if not value:
            return {}
        elif len(value) == 1:
            return {key: value[0]} if not is_forbidden(value[0]) else {}
        else:
            return {f"{key}:{i}": child_value for i, child_value in enumerate(value) if not is_forbidden(child_value)}

    return {key: value} if not is_forbidden(value) else {}


def parse_data(results:List[Dict]) -> List[Dict]:
    """
    Remove data that are None in the results: [], {}, None, etc.
    :param results: The results to parse

    :return: The parsed results 
    """

    parsed_results = []

    for result in results:
        parsed_result = {}

        for key, value in result.items():
            parsed_result.update(parse_value(key, value))

        parsed_results.append(parsed_result)

    return parsed_results