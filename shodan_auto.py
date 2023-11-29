import shodan
import argparse
from rich.console import Console
from tabulate import tabulate
from matplotlib import pyplot as plt

black_list = ["screenshot", "_shodan"]

def display_stats(query):
    pass

def get_key(result):
    for key in result:
        if key in black_list: continue
        print(f"{key}: {result[key]}")


def shodan_search(api_key, query):
    # Initialisation de l'objet Shodan avec la clé API
    api = shodan.Shodan(api_key)

    try:
        # Effectuer la recherche
        console = Console()
        with console.status("[bold green]Shodan Search..."):
            results = api.search(query)
        console.log("Complete")

        print(f"Nombre de résultats: {results['total']}")
        print(f"Requête: {results['matches'][1]}")

        for result in results['matches']:
            # table.append([result['ip_str'], result['port'], result['org'], result['location']['city'], result['location']['country_name'], result['os']])
            get_key(result)
            print("-" * 50)
        # print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))

    except shodan.APIError as e:
        print(f'Erreur Shodan: {e}')

def main():
    parser = argparse.ArgumentParser(description='Script de recherche Shodan')
    parser.add_argument('-key', "--api_key", type=str, help='Clé API Shodan')
    parser.add_argument('-q', '--query', type=str, help='Requête de recherche')

    args = parser.parse_args()

    shodan_search(args.api_key, args.query)

if __name__ == "__main__":
    main()
