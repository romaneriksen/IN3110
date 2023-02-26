# Assignment 5 - Strømpris

## Function/purpose

The purpose of this program is to show the electricity prices for the different electricity zones in Norway in a nice plot. The prices have been fetched from the hvakosterstrommen.no/strompris-api API, and are nicely displayed in a plot on a webpage.

### strompris.py

A python program for fetching the acutal information about the electricity prices for a given day or a time period. It then takes the found data and creates a plot from the price and the time of day the price is from. 

### app.py

A python program utilizing FastAPI to generate a plot of electricity prices by date and dsiplay it on a webpage.

## Version

This program runs with Python3

## Installation/Dependencies

To use this program you will need to insatll 
```
altair
altair-viewer
beautifulsoup4
fastapi[all]
pandas
pytest
requests
requests-cache
uvicorn
```
This can be done using pip

## Execution

Clone the assignment5 folder to your local computer, then open a terminal inside of the folder. From here, you can run:
```
python3 strompris.py
``` 
To fetch the prices and show the plot using altair
```
python3 app.py
```
To fetch the prices and show the plot on a webpage by using FastAPI and HTML

## Testing

To run the tests for the assignment, run:
```
pytest
```
in the assignement folder.
All the test should pass except test_plot_daily_prices and test_form_input
