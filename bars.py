import json
import sys
import os
from math import cos, sqrt
import argparse

def parse_args(args):

    parser = argparse.ArgumentParser(description='Pritty print for JSON')
    parser.add_argument('filepath', help='File path to JSON file', type=argparse.FileType('r'))

    return parser.parse_args(args)


def load_json_data(file_path):

    if not file_path or not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as json_file:
        try:
            return json.load(json_file)

        except AssertionError:
            print('Specified file is not a JSON type or empty')



def get_biggest_bar(data):

    if not data:
        return None

    return max(data, key=lambda bar_data: bar_data['SeatsCount']).get('Name')


def get_smallest_bar(data):

    if not data:
        return None

    return min(data, key=lambda bar_data: bar_data['SeatsCount']
    if bar_data['SeatsCount'] > 4 else 100).get('Name')


def get_user_coordinates(prompt):

    try:
        lat, lon = [float(x) for x in ((input(prompt)).split(','))]
        return [lat, lon]

    except ValueError:
        print("Invalid input")
        return [None, None]


def get_gps_distance(latitude_a, longitude_a, latitude_b, longitude_b):
    """
    Calculate distance between two GPS points
    (specified in decimal degrees)
    Use Equirectangular approximation. Faster than haversine
    Suitable for relatively small distance. Accuracy about 100 meters at 1000 km.
    """
    if not latitude_a or not longitude_a or not latitude_b or not longitude_b:
        return None

    x = (longitude_b - longitude_a) * cos(0.5 * (latitude_b + latitude_a))
    y = latitude_b - latitude_a
    earth_radius = 6371  # in kilometers. Use 3956 for miles
    return earth_radius * (sqrt(x * x + y * y))


def get_closest_bar(data, latitude, longitude):

    if not data or not latitude or not longitude:
        return None

    return min(data, key=lambda bar_data: get_gps_distance(latitude, longitude,
                                                           float(bar_data.get('Latitude_WGS84')),
                                                           float(bar_data.get('Longitude_WGS84')))

                                                if bar_data['SeatsCount'] > 4 else 1000).get('Name')


if __name__ == '__main__':

    try:
        parser = parse_args(sys.argv[1:])

        json_file_path = parser.filepath.name
    except IOError:
        json_file_path = None

    bars_data = load_json_data(json_file_path)

    print('Biggest bar is: %s' % str(get_biggest_bar(bars_data)))

    print('Smallest bar is: %s' % str(get_smallest_bar(bars_data)))

    user_latitude, user_longitude = get_user_coordinates \
        ('Input GPS decimal coordinates in format Latitude, Longitude :')

    print('Closest bar is: %s' % str(get_closest_bar(bars_data, user_latitude, user_longitude)))
