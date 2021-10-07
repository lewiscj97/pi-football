from random import randint

from scraper import Scraper
from displayer import DisplayText

if __name__ == '__main__':
    scraper = Scraper()
    scraper.main()
    matches = scraper.matches
    random_match = matches[randint(0, len(matches))]

    displayer = DisplayText()
    displayer.display(random_match.to_array())
    random_match.to_string()
