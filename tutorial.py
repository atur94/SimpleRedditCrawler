import requests
from nice_wait import wait_message
from urllib import request
from bs4 import BeautifulSoup
import time
def trade_spider(max_pages):
    page = 1
    first_url = "https://www.reddit.com/"           #starting address +
    next_pages_count = "?count="                    #+ place for count number + count(default for reddit equals 25 * page) +
    last_tag = "&after="                            #+ place for last tag + data["tag"]

    status = False

    while page <= max_pages:
        if page == 1:
            url = first_url
        else:
            url = first_url + next_pages_count + str(page*25) + last_tag + data['tag']
        while (status == False):
            source_code = requests.get(url)             #WAITING FOR REDDIT RESPONS. DID IT BECAUSE REDDIT IS BLOCKING EVENTS THAT REPEATS TOO OFTEN
            if (source_code.status_code == 200):        #CHECKING FOR STATUS CODE 200. SOMETIMES SITE RETURNS STATUS CODE 429 SO YOU NEED TO WAIT
                status = True
                print("\r")
                break                                   #IF STATUS CODE HAPPENS AFTER GETTING CORRECT REQUEST THERE IS NOT NEED TO PRINT                                                       #WAITING MESSAGES
            wait_message(str(source_code.status_code))

        plain_text = source_code.text.encode(('utf-8'))
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('div', {"class": 'link'}):
            comments_number = link.get("data-comments-count")
            vote_score = link.get("data-score")
            data_fullname = link.get("data-fullname")
            for in_link in link.findAll('a', {'data-event-action':'title'}):
                title = in_link.string
                source = in_link.get('href')
                if "http" not in source:
                    source = "https://www.reddit.com/" + source
                data_href_url ="https://www.reddit.com/" +  in_link.get("data-href-url")
                data = { 'title'    : title,
                         'source'   : source,
                         'reddit_url':data_href_url,
                         'tag': data_fullname,
                         'score': vote_score,
                         'comments': comments_number}
                print("Page:\t\t\t\t\t" + str(page))
                print("title:\t\t\t\t\t" + data['title'])
                # print(url)
                print("reddit source url:\t\t" + data['source'])
                print("reddit comments url:\t" + data['reddit_url'])
                print("score:\t\t\t\t\t" + data['score'])
                print("comments:\t\t\t\t" + data['comments'])
                print("\n")
        status = False
        page += 1
