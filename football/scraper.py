from bs4 import BeautifulSoup
from selenium import webdriver
import time
from match import Match

class Scraper:
    def __init__(self):
        self.link = "https://www.bbc.co.uk/sport/football/scores-fixtures"
        self.browser = webdriver.Chrome('/Users/lewis.jones/PycharmProjects/pi-football/chromedriver')
        self.matches = []
        self.home_teams = []
        self.away_teams = []
        self.home_scores = []
        self.away_scores = []
        self.times = []


    def open_pages(self):
        self.browser.get(self.link)
        time.sleep(1)
        content = self.browser.page_source
        soup = BeautifulSoup(content, features='html.parser')
        self.browser.close()
        return soup

    def get_match_blocks(self, soup):
        match_blocks = soup.find_all('div', class_='qa-match-block')
        return match_blocks

    def identify_league_block(self, match_blocks, league):
        result = ""
        for block in match_blocks:
            if block.h3.text.strip() == league:
                result = block
        return result

    def find_all_matches(self, container):
        return container.find_all('li', class_='gs-o-list-ui__item gs-u-pb-')

    def find_team_names(self, matches):
        team_names = []
        for match in matches:
            # in play
            if "sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--live-sport" in str(match):
                team_name = match.find_all('span',
                                           class_="gs-u-display-none gs-u-display-block@m qa-full-team-name sp-c-fixture__team-name-trunc")
                team_names.append(team_name)
            # full time
            elif "sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--ft" in str(match):
                team_name = match.find_all('span',
                                           class_="gs-u-display-none gs-u-display-block@m qa-full-team-name sp-c-fixture__team-name-trunc")
                team_names.append(team_name)

        for x in range(len(team_names)):
            self.home_teams.append(team_names[x][0].text)
            self.away_teams.append(team_names[x][1].text)

    def get_scores(self, matches):
        home_scores = []
        away_scores = []

        for match in range(len(matches)):
            # In play
            if "sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--live-sport" in str(matches[match]):
                home_scores.append(matches[match].find_all('span',
                                                           class_="sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--live-sport"))
                away_scores.append(matches[match].find_all('span',
                                                           class_="sp-c-fixture__number sp-c-fixture__number--away sp-c-fixture__number--live-sport"))

            # Full time
            elif "sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--ft" in str(matches[match]):
                home_scores.append(matches[match].find_all('span',
                                                           class_="sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--ft"))
                away_scores.append(matches[match].find_all('span',
                                                           class_="sp-c-fixture__number sp-c-fixture__number--away sp-c-fixture__number--ft"))

        # Home
        for x in range(len(home_scores)):
            self.home_scores.append(home_scores[x][0].text)

        # Away
        for x in range(len(away_scores)):
            self.away_scores.append(away_scores[x][0].text)

    def get_times(self, matches):
        times = []

        for match in matches:
            if "sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--live-sport" in str(match):
                time = match.find_all('span',
                                      class_="sp-c-fixture__status gel-brevier sp-c-fixture__status--live-sport")
                times.append(time)

            elif "sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--ft" in str(match):
                time = match.find_all('span',
                                      class_="sp-c-fixture__status sp-c-fixture__status--ft gel-minion")
                times.append(time)

        for time in times:
            self.times.append(time[0].text)

    def create_matches(self):
        for i in range(len(self.home_teams)):
            home_team = self.home_teams[i]
            away_team = self.away_teams[i]
            home_score = self.home_scores[i]
            away_score = self.away_scores[i]
            time = self.times[i]
            self.matches.append(Match(home_team, away_team, home_score, away_score, time))

    def main(self):
        soup = self.open_pages()
        blocks = self.get_match_blocks(soup)
        block = self.identify_league_block(blocks, "UEFA Nations League")
        matches = self.find_all_matches(block)
        self.find_team_names(matches)
        self.get_scores(matches)
        self.get_times(matches)
        self.create_matches()
