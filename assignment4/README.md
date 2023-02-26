# Assignment 4 - Web scraping

## Function/purpose

Web scraping program with implementation for scraping different type of information from different web pages such as:
- requesting_urls.py -> Gets an HTML page and returns its content.

- filter_urls.py -> contains three different functions:
  - *find_urls* for finding all urls of an HTML text.
  - *find_articles* for finding all wikipedia articles inside an HTML text.
  - *find_img_src* for finding all src attributes of img tags in an HTML text.

- time_planner.py -> program for extracting events from the FIS Alpine Ski World Cup wikipedia page and rendering it to markdown:
  - *extraxt_events* for extracting the events and returning it as a pandas dataframe.
  - *render-schedule* for rendering the pandas dataframe to markdown.
  - *strip_text* for returning a nice string from the HTML table data.
  - *expand_row_col_span* expands the columns and rows to correspond with the HTML table. 

- fetch_player_statistics.py -> program for extracting the player statistics for the eight best team of the NBA 2021-22 season:
  - *get_players* extracts all the player urls from a teams wikipedia page.
  - *get_player_stats* extracts the stats for a given player.
  - *find_best_players* extracts the stats for the best players (top 3 scorers) of the semifinals in the NBA.
  - *plot_best* plots the stats found with the *find_best_players* function, and then creates a new directory and saves the stats to this directory.   

## Version

This program runs with Python3

## Installation/Dependencies 

To use this web scraping program you will need to install BeautifulSoup4 and the python ```requests``` module, which can be done using pip:
```
pip install beautifulsoup4
pip install requests
```
## Execution

Clone the assignment4 folder to your local computer, then open a terminal inside of the folder. From here, you can run:
```
1. python3 fetch_player_statistics.py
2. python3 time_planner.py
```
1. To see the player statistics of the top players in the eight best teams in the 2022 NBA playoffs
2. To see the markdown for the FIS Alpine Ski World Cup for the years 2020-21, 2021-22 and 2022-23.

## Testing

To run the tests for the assignement, run:
```
pytest
```
In the assignment4 folder.
All the tests should pass except *test_collect_dates.py*, as *collect_dates.py* is not implemented.