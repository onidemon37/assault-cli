import click
import sys
import json
from typing import TextIO

from .http import assault
from .stats import Results

@click.command()
@click.option("--requests", "-r", default=500, help="Number of requests")
@click.option("--concurrency", "-c", default=1, help="Number of concurrent requests")
@click.option("--json-file", "-j", default=None, help="Path to output JSON file")
@click.argument("url")
def cli(requests, concurrency, json_file, url):
    total_time, request_dicts = assault(url, requests, concurrency)
    results = Results(total_time, request_dicts)
    display(results, json_file)
    
def display(results, json_file):
    if json_file:
        # write to json file
        print("We're writing to a JSON File")
    else:
        # Print screen
        print(".... Done!")
        print("--- Results ---")
        print(f"Successful requests\t{ results.successful_requests()}")
        print(f"Slowest            \t{results.slowest()}")
        print(f"Fastest            \t{results.fastest()}")
        print(f"Total Time         \t{results.total_time}")
        print(f"Requests Per Minute\t{results.requests_per_minute()}")
        print(f"Requests Per Second\t{results.requests_per_second()}")
