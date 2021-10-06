from scraper import Scraper


class Formatter:
    def __init__(self):
        scraper = Scraper()
        scraper.main()
        self.matches = scraper.matches

formatter = Formatter()
for match in formatter.matches:
    match.to_string()