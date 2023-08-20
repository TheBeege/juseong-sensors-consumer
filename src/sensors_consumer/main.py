#!/usr/bin/env python

import requests
import datetime


def main():
    # Requests library is for requesting data from a page on the internet
    # This requests a list of sensors from the fake API
    sensors_list_response = requests.get('http://localhost:8000/sensors/')
    # Example output:
    # [
    #   {'id': '4c039a7e-3f1d-11ee-aff8-0242ac110002', 'type': 'TemperatureSensor'},
    #   {'id': '4c039c7c-3f1d-11ee-aff8-0242ac110002', 'type': 'TemperatureSensor'},
    #   {'id': '4c039d1c-3f1d-11ee-aff8-0242ac110002', 'type': 'TemperatureSensor'}
    # ]

    # This assumes the response body is JSON format and pulls the response body out 
    # into a Python dictionary
    sensors_list = sensors_list_response.json()

    # Now, let's look at each sensor in the list response
    for sensor in sensors_list:
        # Let's request the metric data for the current sensor
        sensor_metric_response = requests.get(f'http://localhost:8000/sensors/{sensor["id"]}/metric')
        # Example output:
        # {'unit': 'DEGREES_CELSIUS', 'measure': 29.196583214370886, 'timestamp': 1692511151}
        # Note that the timestamp is a Unix timestamp or epoch time

        # Again, parse the JSON response into a Python dictionary
        sensor_metric = sensor_metric_response.json()
        # Print stuff
        print(f'Got temperature {sensor_metric["measure"]}')
        print(f'Unit: {sensor_metric["unit"]}')
        metric_timestamp = sensor_metric["timestamp"]
        # The below converts from a Unix timestamp to a Python datetime object
        datetime_from_timestamp = datetime.datetime.fromtimestamp(metric_timestamp)
        # This formats the datetime object into a time string according to the local 
        # computer's regional settings
        # You'll want to Google for `strftime` and what the %c means
        timestamp_as_human_readable_string = datetime_from_timestamp.strftime("%c")
        print(f'At time: {timestamp_as_human_readable_string}')
        print('======================================')
    

if __name__ == '__main__':
    main()

# TODO: Stop printing stuff and dump it into your database instead
