# Weather Data Web Scraper

This is a Python program that scrapes weather data from a website and presents it in a readable format. It fetches current weather conditions (temperature, humidity, wind speed) for a specific location from a chosen weather website.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Installation](#installation)
- [Configuration](#configuration)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This program demonstrates web scraping techniques using Python. It retrieves weather data by sending HTTP requests to a weather website and parsing the HTML content to extract relevant information using the BeautifulSoup library.

## Requirements

- Python 3.x
- Beautiful Soup library (install using `pip install beautifulsoup4`)
- Requests library (install using `pip install requests`)

## Usage

1. Clone this repository using `git clone https://github.com/Quickmotions/Weather-Data-Web-Scraper`.
2. Navigate to the project directory: `cd weather-scraper`.
3. Run the program: `python weather_scraper.py`.
4. Follow the on-screen instructions to input the desired location.

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries using the following command:
`pip install beautifulsoup4 requests`

## Configuration

No specific configuration is required for this program. However, you can customize the target website and the specific elements you're scraping by modifying the code in `weather_scraper.py`.

## Known Issues

- The program might break if the target website's structure changes. Regular updates might be needed to adapt to such changes.
- Limited amount of Ids, BBC Weather website addresses for locations are stored at 7 digit codes, these must be manually inputted into `locations.dat` in order to get weather data.
- If the website blocks too many requests in a short time, you might encounter issues. Consider adding rate-limiting or using proxies if needed.

## Contributing

Contributions are welcome! If you encounter any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
