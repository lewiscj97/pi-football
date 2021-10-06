from scraper import Scraper


class Formatter:
    def __init__(self):
        scraper = Scraper()
        scraper.main()
        self.matches = scraper.matches


for match in Formatter().matches:
    match.to_string()
