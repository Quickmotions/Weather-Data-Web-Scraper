import sys

import requests
from bs4 import BeautifulSoup
from collections import defaultdict

temperature_value_class = '.wr-value--temperature--c'
time_data_value_class = '.wr-time-slot-secondary__value'


def main(loc: str) -> str:
    loc_dict = defaultdict(str)

    with open('C:\Program Files (x86)\pyWet\locations.dat', 'r') as FH:
        for file in FH.readlines():
            line = file.strip()
            try:
                id_num, location = line.split(' ', 1)
            except ValueError:
                print(f"Record: {line}")
                raise ValueError("Failed while unpacking. Not enough arguments to supply.")

            loc_dict[location.lower()] = id_num

    if loc.lower() not in loc_dict:
        raise IndexError(f"Failed to find location ID for {loc}. Supply BBC weather ID in locations.dat file.")
    loc_id = loc_dict[loc.lower()]

    r = requests.get(f'https://www.bbc.co.uk/weather/{loc_id}', auth=('user', 'pass'))
    soup = BeautifulSoup(r.text, 'html.parser')

    highest_temp = soup.select(temperature_value_class)[0].text
    lowest_temp = soup.select(temperature_value_class)[1].text
    current_temp = soup.select(temperature_value_class)[28].text

    humiditiy = soup.select(time_data_value_class)[0].text
    pressure = soup.select(time_data_value_class)[1].text
    visibility = soup.select(time_data_value_class)[2].text

    feels_life = soup.select('.wr-time-slot-secondary__feels-like-temperature-value')[0].text
    rain_chance = soup.select('.wr-time-slot-primary__precipitation')[0].text.split("c")[0]
    wind_speed = soup.select('.wr-value--windspeed--mph')[28].text

    return f"High {highest_temp} | Low {lowest_temp} | Current {current_temp} | Feels Like {feels_life}\n" \
           f"Humidity {humiditiy} | Pressure {pressure} | {visibility} Visibility\n" \
           f"Precipitation {rain_chance} | Wind Speed {wind_speed}"


if __name__ == "__main__":
    print(main(sys.argv[1]))
