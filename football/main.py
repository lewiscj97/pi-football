from scraper import Scraper


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scraper = Scraper()
    scraper.main()
    matches = scraper.matches

    displayer = DisplayText()
    displayer.display(matches[0].to_array())
