import argparse

from shodan_api.shodan_api import execute_query, parse_data
from file_manager.file_manager import save_data, load_data
from statistics.stats import create_pie_chart


def main():
    parser = argparse.ArgumentParser(
        description="Script make statistics on Shodan results"
    )

    parser.add_argument(
        "-key", "--api_key", type=str, help="Shodan API key"
    )
    parser.add_argument(
        "-q", "--query", type=str, help="Query to send to Shodan"
    )
    parser.add_argument(
        "-s",
        "--save",
        type=str,
        help="Save the result of the query in a file, ex: -s resultats.txt",
    )

    parser.add_argument(
        "-g",
        "--graph",
        type=str,
        help="Create statistics and graph using a file, ex: -g resultats.txt",
    )
    parser.add_argument(
        "-t",
        "--tags",
        type=str,
        help="Tag to create statistics, ex: -t os,versions,domains. If not specified, port,location:country_name,org will be used",
    )

    args = parser.parse_args()

    if args.query:
        parsed_results = parse_data(execute_query(args.query, args.api_key))

    if args.save:
        save_data(parsed_results, args.save)

    if args.graph:
        tags = None
        if args.tags:
            tags = "".join(args.tags).split(',')

        parsed_results = load_data(args.graph)

        create_pie_chart(parsed_results, args.graph, tags)

if __name__ == "__main__":
    main()
