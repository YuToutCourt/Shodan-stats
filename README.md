# TP Shodan

## Installation

```bash
git clone https://github.com/YuToutCourt/Shodan-stats.git
cd app/
pip install -r requirements.txt
```

## Usage

```bash
usage: main.py [-h] [-key API_KEY] [-q QUERY] [-s SAVE] [-g GRAPH] [-t TAGS]

Script make statistics on Shodan results

options:
  -h, --help            show this help message and exit
  -key API_KEY, --api_key API_KEY
                        Shodan API key
  -q QUERY, --query QUERY
                        Query to send to Shodan
  -s SAVE, --save SAVE  Save the result of the query in a file, ex: -s resultats.txt
  -g GRAPH, --graph GRAPH
                        Create statistics and graph using a file, ex: -g resultats.txt
  -t TAGS, --tags TAGS  Tag to create statistics, ex: -t os,versions,domains. If not specified, port,location:country_name,org will be used
```

You can use the `-g` alone if you already have a file with the results of a query. Otherwise, you can use the `-q` option to make a query and save the results in a file with the `-s` option. Don't forget to specify your API key with the `-key` option.

Use the `-t` option to specify the tags you want to use to make statistics. 
If you don't specify any tags, the script will use the following tags: 
- port
- location:country_name
- org
- domains
- os
- location:city

## Example

```bash
python main.py -key "YOUR_API_KEY" -q "apache" -s apache.json -g apache.json
```


![Alt text](/image/screen.png)
