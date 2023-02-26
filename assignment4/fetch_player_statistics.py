import os
import re
from operator import itemgetter
from typing import Dict, List
from urllib.parse import urljoin

import numpy as np
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from requesting_urls import get_html

## --- Task 8, 9 and 10 --- ##

try:
    import requests_cache
except ImportError:
    print("install requests_cache to improve performance")
    pass
else:
    requests_cache.install_cache()

base_url = "https://en.wikipedia.org"


def find_best_players(url: str) -> None:

    """Find the best players in the semifinals of the nba.

    This is the top 3 scorers from every team in semifinals.
    Displays plot over points, assists, rebounds

    arguments:
        - html (str) : html string from wiki basketball
    returns:
        - None
    """
    # gets the teams
    teams = get_teams(url)
    
    # Gets the player for every team and stores in dict (get_players)
    all_players = {}
    for team in teams:
        name = team["name"]
        all_players[name] = get_players(team["url"])
        for player in all_players[name]:
            player_stats = get_player_stats(player["url"],name)
            player_name = player["name"]
            player.update(player_stats)


    # get player statistics for each player,
    # using get_player_stats
    for team, players in all_players.items():
    # at this point, we should have a dict of the form:
    # {
    #     "team name": [
    #         {
    #             "name": "player name",
    #             "url": "https://player_url",
    #             # added by get_player_stats
    #             "points": 5,
    #             "assists": 1.2,
    #             # ...,
    #         },
    #     ]
    # }
        ...

    # Select top 3 for each team by points:
    best = {}
    top_stat = ...
    for team, players in all_players.items():
        # Sort and extract top 3 based on points
        best[team] = []
        # for player in players:
        #     # dict = {}
        #     # dict["name"] = player["name"]
        #     # player = player.sort(key="points")
        #     break
        sorted_players = sorted(players, key=itemgetter('points'), reverse=True)
      
        best[team].append(sorted_players[0])
        best[team].append(sorted_players[1])
        best[team].append(sorted_players[2])
        # top_3 = ...
    stats_to_plot = ["points", "assists", "rebounds"]
    for stat in stats_to_plot:
        plot_best(best, stat=stat)


def plot_best(best: Dict[str, List[Dict]], stat: str = "points") -> None:
    """Plots a single stat for the top 3 players from every team.

    Arguments:
        best (dict) : dict with the top 3 players from every team
            has the form:

            {
                "team name": [
                    {
                        "name": "player name",
                        "points": 5,
                        ...
                    },
                ],
            }

            where the _keys_ are the team name,
            and the _values_ are lists of length 3,
            containing dictionaries about each player,
            with their name and stats.

        stat (str) : [points | assists | rebounds] which stat to plot.
            Should be a key in the player info dictionary.
    """
    stats_dir = "NBA_player_statistics"
    labels = [
    "Miami",
    "Phoenix",
    "Golden State",
    "Milwaukee",
    "Philadelphia",
    "Boston",
    "Dallas",
    "Memphis"]
    count_so_far = 0
    all_names = []

    first = []
    first_names = []

    second = []
    second_names = []

    third = []
    third_names = []

    teams = []
    # iterate through each team and the
    for team, players in best.items():
        teams.append(team)
        points = [player[stat] for player in players]
        names = [player["name"] for player in players]
        first.append(points[0])
        second.append(points[1])
        third.append(points[2])
        first_names.append(names[0])
        second_names.append(names[1])
        third_names.append(names[2])
    
    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars   
    # print(first_names)

    fig, ax = plt.subplots()
    # Creates the different bar plots for first, second and third for every team
    rects1 = ax.bar(x - width, first, width, label='First')
    rects2 = ax.bar(x, second, width, label='Second')
    rects3 = ax.bar(x + width, third, width, label='Third')

    ax.set_ylabel("Scores")
    ax.set_title(stat+" for top 3 players in all teams")
    ax.set_xticks(x, teams)
    ax.legend()

    # Sets the labels for each bar according to player names.
    ax.bar_label(rects1, labels = first_names, label_type='center', padding=3, rotation=90)
    ax.bar_label(rects2, labels = second_names, label_type='center', padding=3, rotation=90)
    ax.bar_label(rects3, labels = third_names, label_type='center', padding=3, rotation=90)

    fig.tight_layout()
    filename = stat+".png"
    print("made file:", filename)
    directory = "NBA_player_statistics"
    # Create a new directory if it does not already exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    path = os.path.join(directory,filename)
    print(path)
    # Save plot of stats in given directory
    plt.savefig(path)

def get_teams(url: str) -> list:
    """Extracts all the teams that were in the semi finals in nba

    arguments:
        - url (str) : url of the nba finals wikipedia page
    returns:
        teams (list) : list with all teams
            Each team is a dictionary of {'name': team name, 'url': team page
    """
    # Get the table
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="Bracket").find_next("table")

    # find all rows in table
    rows = table.find_all("tr")
    rows = rows[2:]
    # maybe useful: identify cells that look like 'E1' or 'W5', etc.
    seed_pattern = re.compile(r"^[EW][1-8]$")

    # lots of ways to do this,
    # but one way is to build a set of team names in the semifinal
    # and a dict of {team name: team url}

    team_links = {}  # dict of team name: team url
    in_semifinal = set()  # set of teams in the semifinal

    # Loop over every row and extract teams from semi finals
    # also locate the links tot he team pages from the First Round column
    for row in rows:
        cols = row.find_all("td")
        # useful for showing structure
        # print([c.get_text(strip=True) for c in cols])

        # TODO:
        # 1. if First Round column, record team link from `a` tag
        # 2. if semifinal column, record team name

        # quarterfinal, E1/W8 is in column 1
        # team name, link is in column 2
        if len(cols) >= 3 and seed_pattern.match(cols[1].get_text(strip=True)):
            team_col = cols[2]
            a = team_col.find("a")
            team_links[team_col.get_text(strip=True)] = urljoin(base_url, a["href"])

        elif len(cols) >= 4 and seed_pattern.match(cols[2].get_text(strip=True)):
            team_col = cols[3]
            in_semifinal.add(team_col.get_text(strip=True))

        elif len(cols) >= 5 and seed_pattern.match(cols[3].get_text(strip=True)):
            team_col = cols[4]
            in_semifinal.add(team_col.get_text(strip=True))

    # return list of dicts (there will be 8):
    # [
    #     {
    #         "name": "team name",
    #         "url": "https://team url",
    #     }
    # ]

    assert len(in_semifinal) == 8
    return [
        {
            "name": team_name.rstrip("*"),
            "url": team_links[team_name],
        }
        for team_name in in_semifinal
    ]


def get_players(team_url: str) -> list:
    """Gets all the players from a team that were in the roster for semi finals
    arguments:
        team_url (str) : the url for the team
    returns:
        player_infos (list) : list of player info dictionaries
            with form: {'name': player name, 'url': player wikipedia page url}
    """
    print(f"Finding players in {team_url}")
    base_url = "https://en.wikipedia.org"

    # Get the table
    html = get_html(team_url)
    soup = BeautifulSoup(html, "html.parser")
    roster = soup.find(id="Roster")
    player_table = roster.find_next("table", {"class": "toccolours"}).find_next("table")
    
    players = []
    headings = player_table.find_all("th")
    labels = [th.text.strip() for th in headings]

    # Loop over every row and get the names from roster
    rows = player_table.find_all("tr")
    rows = rows[1:]
    for row in rows:
        # Get the columns
        cols = row.find_all("td")
        for col in cols:

            # regex to find url and player name
            # find name links (a tags)
            name_pat = re.findall(r'href="(/wiki/[()a-zA-z.-]+)".+>([a-zA-Z.-]+, [a-zA-Z. -]+)', str(col))
            # dict to add the player and the url
            dict = {}
            if len(name_pat) > 0:
                # and add to players a dict with
                # {'name':, 'url':}
                dict["name"] = name_pat[0][1]
                dict["url"] = urljoin(base_url, name_pat[0][0])
                players.append(dict)
        
    # return list of players
    return players


def get_player_stats(player_url: str, team: str) -> dict:
    """Gets the player stats for a player in a given team
    arguments:
        player_url (str) : url for the wiki page of player
        team (str) : the name of the team the player plays for
    returns:
        stats (dict) : dictionary with the keys (at least): points, assists, and rebounds keys
    """
    print(f"Fetching stats for player in {player_url}")

    # Get the table with stats
    html = get_html(player_url)
    soup = BeautifulSoup(html, 'html.parser')
    regular_season = soup.find(id="Regular_season")
    nba = soup.find(id="NBA")

    if regular_season is None:
        table = nba.find_next("table")
    else:
        table = regular_season.find_next("table")

    headings = table.find_all("th")
    labels = [th.text.strip() for th in headings]
    # print(labels)

    stats = {}

    rows = table.find_all("tr")
    rows = rows[1:]

    stats["rebounds"] = 0
    stats["assist"] = 0
    stats["steals"] = 0
    stats["blocks"] = 0
    stats["points"] = 0
    # Loop over rows and extract the stats
    for row in rows:
        cols = row.find_all("td")    
         
        # print(cols[0].text.strip())
        if "2021" in cols[0].text.strip():
            # Check correct team (some players change team within season)
            if cols[1].text.strip() == team:
                stats["rebounds"] = float(re.sub('\*','',cols[labels.index("RPG")].text.strip()))
                stats["assists"] = float(re.sub('\*','',cols[labels.index("APG")].text.strip()))
                stats["steals"] = float(re.sub('\*','',cols[labels.index("SPG")].text.strip()))
                stats["blocks"] = float(re.sub('\*','',cols[labels.index("BPG")].text.strip()))
                stats["points"] = float(re.sub('\*','',cols[labels.index("PPG")].text.strip()))
        
        

        # load stats from columns
        # keys should be 'points', 'assists', etc.
        ...
    # print(stats)
    return stats


# run the whole thing if called as a script, for quick testing
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/2022_NBA_playoffs"
    find_best_players(url)
