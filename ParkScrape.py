from bs4 import BeautifulSoup
import requests
import re
import os
import csv

def scrape_coordinates(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(class_="geo-dec")
    coordinates = []

    for element in elements:
        lat = element.text.split()[0]
        long = element.text.split()[1]
        coordinates.append((lat,long))
    
    return coordinates

def write_coordinates(coordinates, output_file_name):
    with open(output_file_name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Latitude', 'Longitude'])  # Write header row
        writer.writerows(coordinates)  # Write coordinates

def main(url, output_file_name):
    coordinates = scrape_coordinates(url)
    write_coordinates(coordinates,output_file_name)

main("https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States", "ParksCoords.csv")
