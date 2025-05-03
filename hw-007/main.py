import csv
import functools
import json
import os
import re
import time

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/"
TIMEOUT_S = 1
RETRIES = 3
BACKOFF_FACTOR = 0.5


def retry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        retries_left = RETRIES
        while retries_left:
            delay = BACKOFF_FACTOR * (2 ** (RETRIES - retries_left))
            try:
                result = func(*args, **kwargs)
            except requests.HTTPError as e:
                print(
                    "HTTP Error: {}. Retrying {} ...".format(
                        e.response.status_code, RETRIES - retries_left + 1
                    )
                )
                time.sleep(delay)
                retries_left -= 1
                if not retries_left:
                    print(f'The page "{URL+args[0]}" is not found.')
            else:
                return result
        return None

    return wrapper


@retry
def download_wiki_page(country):
    response = requests.get(URL + country, timeout=TIMEOUT_S)
    response.raise_for_status()
    return response.text


def data_caching(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if os.path.exists("countries_data_cache.json"):
            with open("countries_data_cache.json") as fh:
                countries_data_cache = json.loads(fh.read())
        else:
            countries_data_cache = dict()
        country = args[0]
        if country not in countries_data_cache:
            res = func(*args, **kwargs)
            if res is not None:
                countries_data_cache[country] = [res[1], res[2], res[3]]
                with open("countries_data_cache.json", "w") as fh:
                    json.dump(countries_data_cache, fh, indent="    ")
        else:
            res = [
                country,
                countries_data_cache[country][0],
                countries_data_cache[country][1],
                countries_data_cache[country][2],
            ]
        return res

    return wrapper


@data_caching
def parse_web_page(country):
    web_page = download_wiki_page(country)

    if web_page is None:
        return None

    capital = (
        BeautifulSoup(web_page, "lxml")
        .find(string=re.compile("Capital"))
        .find_next("td")
        .find("a")
        .text
    )

    area = (
        BeautifulSoup(web_page, "lxml")
        .find("a", string=re.compile("Area"))
        .find_next("td")
        .text.replace(",", "")
    )

    area = area[: area.find("km") - 1][::-1]
    a = ""
    for i in area:
        if not i.isdigit():
            break
        a = i + a
    area = a

    population = (
        BeautifulSoup(web_page, "lxml")
        .find(string=re.compile("[Ee]stimate"))
        .find_next("td")
        .text.strip()
        .replace(",", "")
    )
    a = ""
    for i in population:
        if not i.isdigit():
            break
        a += i
    population = a

    result = [country, capital, area, population]

    return result


def name_validate(name):
    for i in '\\/:*?"<>|+,':
        if i in name:
            return False
    return True


def main():

    input_file_name = "countries.txt"

    while True:
        user_input = input(
            f"Enter a file name to open "
            f"or enter an empty string to open "
            f'the default "{input_file_name}": '
        )
        if user_input == "":
            break
        elif user_input[0] == " ":
            print("Please check if the file name you entered is correct")
            continue
        else:
            if os.path.exists(user_input):
                input_file_name = user_input
                break
            else:
                print("File does not exist")
                continue

    with open(input_file_name) as fh:
        countries = fh.read().splitlines()

    data = [
        ["country", "city", "area", "population"],
    ]

    for country in countries:
        new_row = parse_web_page(country)
        if new_row is not None:
            data.append(new_row)

    output_file_name = "countries_data.csv"

    while True:
        user_input = input(
            f"Enter the file name to save "
            f'or press enter save default "{output_file_name}": '
        )
        if user_input == "":
            break
        elif os.path.exists(user_input):
            output_file_name = user_input
            break
        elif " " in user_input:
            print(
                "Please check if the file name you entered is correct. "
                "The file name must not contain spaces."
            )
            continue
        elif len(user_input) == 1:
            print("File name must contain more than one character")
            continue
        elif user_input[-1] == "." or user_input[0] == ".":
            print(
                "Please check if the file name you entered is correct. "
                "Dot cannot be at the start or end of file name."
            )
            continue
        elif not name_validate(user_input):
            print("Please check if the file name you entered is correct")
            continue
        else:
            output_file_name = user_input
            break

    with open(output_file_name, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data)

    print(
        f"Data on requested countries "
        f'has been saved to a file: "{output_file_name}".'
    )


main()
