from bs4 import BeautifulSoup
import requests
import re
import csv
import sys

def scrape_coordinates(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(class_="geo-dec")
    park_tags = soup.find_all("a", href=lambda href: href and href.startswith("/wiki/"))
    coordinates = []
    titles = []

    for element in elements:
        lat = element.text.split()[0]
        long = element.text.split()[1]
        coordinates.append((lat, long))

    for park in park_tags:
        title = park.get("title")
        if title and isinstance(title, str):
            titles.append(title)

    parks = []
    for title in titles:
        if re.search(".+ National Park$", title) or re.search(".+ National Park and Preserve$", title):
            if title not in parks:
                parks.append(title)

    sorted_parks = sorted(parks)

    park_cords = []
    for park, coords in zip(sorted_parks, coordinates):
        park_cords.append((park, coords[0], coords[1]))

    return park_cords

def write_csv(park_cords, output_file_name):
    with open(output_file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Park', 'Latitude', 'Longitude'])  # Write header row
        writer.writerows(park_cords)  # Write coordinates

def main(url, output_file_name):
    park_cords = scrape_coordinates(url)
    write_csv(park_cords, output_file_name)

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States"
    output_file_name = "ParksCoords.csv"
    main(url, output_file_name)
