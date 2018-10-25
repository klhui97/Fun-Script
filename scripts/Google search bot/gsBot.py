import requests, sys, webbrowser, bs4
import schedule
import time

def job():
    keyword = 'Hui Kam Leung'
    res = requests.get('https://google.com/search?q=' + keyword)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    linkElements = soup.select('.r a')
    linkToOpen = min(10, len(linkElements))
    for i in range(linkToOpen):
        if 'My personal website' in linkElements[i].text:
            webbrowser.open('https://google.com' + linkElements[i].get('href'))
            print("opened")

schedule.every(5).to(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)