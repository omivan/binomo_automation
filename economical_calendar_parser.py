import requests
from datetime import date
from bs4 import BeautifulSoup


def get_quotes(my_event_title_rus, my_event_title_eng):
    current_date = str(date.today().strftime("%Y-%m-%d"))
    page = requests.get('https://teletrade.com.ua/analytics/economical_calendar')
    soup = BeautifulSoup(page.text, 'html.parser')
    events = soup.find("div", {"class": "clndr__body date-container", "data-date": current_date})

    for event in events.findAll("div", {"class": "clndr__itm"}):
        rows = event.find("div", {"class": "row"})
        title_div = rows.find("div", {"title": "Событие"}).find("div", {"class": "clndr__td-innr"}).find("div", {
            "class": "clndr__event"})
        event_title = (str(title_div.text).replace('\n', "").replace("  ", "").strip("  "))
        # print('-'*34)
        # print(event_title)
        # print(my_event_title_rus+my_event_title_eng)
        # print(event_title == my_event_title_rus+my_event_title_eng)
        if my_event_title_rus+my_event_title_eng == event_title:

            previous_quote = float(
                str(rows.find("div", {"title": "Предыдущее"}).find("div", {"class": "clndr__td-innr"}).text).strip())
            current_quote = (
                str(rows.find("div", {"title": "Фактическое"}).find("div", {"class": "clndr__td-innr"}).text).strip())
            if len(current_quote) == 0:
                return previous_quote, False
            else:
                current_quote = float(current_quote)
                return previous_quote, current_quote
