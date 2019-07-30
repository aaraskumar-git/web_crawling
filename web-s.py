from urllib import request
from bs4 import BeautifulSoup as soup
from bs4 import NavigableString

url = "https://cslide.ctimeetingtech.com/esmo2019/attendee/confcal/session/calendar/2019-09-27"
html = request.urlopen(url)

html_page = html.read()
html.close()
page_soup = soup(html_page, "html.parser")

all_events = page_soup.findAll("li", {"class": "itinerary-item"})

for event in all_events:
    for schedule in event.findAll("div", {"class": "property-container"}):
        for att in schedule:
            if not isinstance(att, NavigableString):
                print(att.text)
    print("===========================================================")
