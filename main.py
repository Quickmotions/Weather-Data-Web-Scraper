import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from pprint import pprint


def main(loc: str) -> None:

    loc_dict = defaultdict(str)

    with open('locations.dat', 'r') as FH:
        for file in FH.readlines():
            line = file.strip()
            try:
                id, location = line.split(' ', 1)
            except ValueError as error:
                print(f"Record: {line}")
                raise Exception("Failed while unpacking. Not enough arguments to supply.")

            loc_dict[location.lower()] = id

    if loc not in loc_dict:
        raise Exception(f"Failed to find location ID for {loc}. Supply BBC weather ID in locations.dat file.")
    loc_id = loc_dict[loc.lower()]

    r = requests.get(f'https://www.bbc.co.uk/weather/{loc_id}', auth=('user', 'pass'))
    soup = BeautifulSoup(r.text, 'html.parser')
    highestTemp = soup.select('.wr-value--temperature--c')[0].text
    lowestTemp = soup.select('.wr-value--temperature--c')[1].text
    currentTemp = soup.select('.wr-value--temperature--c')[28].text

    humiditiy = soup.select('.wr-time-slot-secondary__value')[0].text
    pressure = soup.select('.wr-time-slot-secondary__value')[1].text
    visibility = soup.select('.wr-time-slot-secondary__value')[2].text

    feels_life = soup.select('.wr-time-slot-secondary__feels-like-temperature-value')[0].text
    rain_chance = soup.select('.wr-time-slot-primary__precipitation')[0].text.split("c")[0]
    wind_speed = soup.select('.wr-value--windspeed--mph')[28].text

    return f"High {highestTemp} | Low {lowestTemp} | Current {currentTemp} | Feels Like {feels_life}\nHumidity {humiditiy} | Pressure {pressure} | {visibility} Visibility\nPrecipitation {rain_chance} | Wind Speed {wind_speed}"


if __name__ == "__main__":
    print(main(input("Enter Location: ")))