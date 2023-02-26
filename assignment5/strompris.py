#!/usr/bin/env python3
"""
Fetch data from https://www.hvakosterstrommen.no/strompris-api
and visualize it.

Assignment 5
"""

import datetime
import re

import altair as alt
import pandas as pd
import requests
import requests_cache

# install an HTTP request cache
# to avoid unnecessary repeat requests for the same data
# this will create the file http_cache.sqlite
requests_cache.install_cache()


# task 5.1:


def fetch_day_prices(date: datetime.date = None, location: str = "NO1") -> pd.DataFrame:
    """Fetch one day of data for one location from hvakosterstrommen.no API

    arguments:
        date (datetime.date) : a date to fetch the prices from
        location (str) : the location code from where the prices are fetched
    return:
        df (DataFrame) : A pandas DataFrame with information about the prices for the given date and location
    """
    if date is None:
        date = date = datetime.date.today()

    year = date.year
    month = date.month
    day = date.day

    assert date >= datetime.date(2022, 10, 2)

    # Make sure the dates have leading zeros if necessary
    if len(str(date.month)) == 1:
        month = "0"+str(date.month)
    else:
        month = date.month

    if len(str(date.day)) == 1:
        day = "0"+str(date.day)
    else:
        day = date.day

    url = "https://www.hvakosterstrommen.no/api/v1/prices/{year}/{month}-{day}_{location}.json".format(
        year = year, 
        month = month,
        day = day,
        location = location)
    
    req = requests.get(url)
    html_str = req.text
    
    
    # Regex for selecting the wanted information from the html_str
    nok_per_kwh = '(("NOK_per_kWh"):([0-9.-]+))'
    time_start = '(("time_start"):"([0-9-T:+]+))'

    match_nok = re.findall(nok_per_kwh, html_str)
    match_time = re.findall(time_start, html_str)

    dict = {}
    dict["NOK_per_kWh"] = []
    dict["time_start"] = []
    

    for m in range((len(match_time))):
        dict["NOK_per_kWh"].append(float(match_nok[m][2]))
        time = match_time[m][2].split("T")
        # dict["time_start"].append(str(time[0])+" "+str(time[1].split("+")[0]))
        dict["time_start"].append(str(time[0]+" "+str(time[1])))

    # Create the DataFrame
    df = pd.DataFrame.from_dict(dict)
    

    df["time_start"] = pd.to_datetime(df["time_start"], utc=True).dt.tz_convert("Europe/Oslo")
    
    # Handles Daylight Savings
    # Checks if the date is the day for daylight savings, which is the 30th of October
    if month == 10 and day == 30:
        df = df.drop(2)
    
    return df
    


# LOCATION_CODES maps codes ("NO1") to names ("Oslo")
LOCATION_CODES = {
    "NO1" : "Oslo",
    "NO2" : "Kristiansand",
    "NO3" : "Trondheim",
    "NO4" : "Tromsø",
    "NO5" : "Bergen"
}

# task 1:


def fetch_prices(
    end_date: datetime.date = None,
    days: int = 7,
    locations=tuple(LOCATION_CODES.keys()),
) -> pd.DataFrame:
    """Fetch prices for multiple days and locations into a single DataFrame

    arguments:
        end_date (datetime.date) : the end date for the period of time the prices are fetched from
        days (int) : number days before the end_date
        location (str) : tuple with all location codes
            Each location code is a key to a dictionary of {'location_code' : location_name}
    return:
        df (pd.DataFrame) : dataframe with the fetched prices for the given period
    """
    if end_date is None:
        end_date = datetime.date.today()
    
    
    end_date = end_date + datetime.timedelta(days = 1)

    start_date = end_date - datetime.timedelta(days = days)

    df = pd.DataFrame({'A' : []})
    for day in range(days):
        current_date = start_date + datetime.timedelta(days = day)
        for loc in locations:
            temp = fetch_day_prices(current_date, loc)
            temp["location_code"] = loc
            temp["location"] = LOCATION_CODES[loc]
            df = pd.concat([df, temp], ignore_index=True)

    df.pop("A")

    return df


# task 5.1:


def plot_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot energy prices over time

    x-axis should be time_start
    y-axis should be price in NOK
    each location should get its own line

    arguments:
        df (pd.DataFrame) : dataframe with the prices to be plotted
    return:
        plot (altair.Chart) : plot for a pd.DataFrame showing its data
    """
    plot = alt.Chart(df).mark_line().encode(
        x = "time_start:T",
        y = "NOK_per_kWh",
        color = "location:N",
    )
    return plot


# Task 5.4


def plot_daily_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot the daily average price

    x-axis should be time_start (day resolution)
    y-axis should be price in NOK

    You may use any mark.

    Make sure to document arguments and return value...
    """
    ...


# Task 5.6

ACTIVITIES = {
    # activity name: energy cost in kW
    ...
}


def plot_activity_prices(
    df: pd.DataFrame, activity: str = "shower", minutes: float = 10
) -> alt.Chart:
    """
    Plot price for one activity by name,
    given a data frame of prices, and its duration in minutes.

    Make sure to document arguments and return value...
    """

    ...


def main():
    """Allow running this module as a script for testing."""

    df = fetch_prices()
    chart = plot_prices(df)
    # showing the chart without requiring jupyter notebook or vs code for example
    # requires altair viewer: `pip install altair_viewer`
    chart.show()


if __name__ == "__main__":
    main()
