from bs4 import BeautifulSoup
import requests

index = 0
topScoreList = []

response = requests.get(url="https://news.ycombinator.com/news")
# response = requests.get("https://news.ycombinator.com/news", verify=False)
# response.raise_for_status()
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, "html.parser")
soup = BeautifulSoup(markup=response.text,features="html.parser")
# get the segment with title and link
titleList = soup.select(selector=".titleline > a")
# get the segment with score
scoreList = soup.select(selector=".subtext")

for title in titleList:
    # we have to create a dictionary every time, otherwise we only have the
    # last dictionary in the list....ermmm what happened to me ;-)
    dictEntry = {}
    dictEntry["Title"] = title.getText()
    dictEntry["Link"] = title.get(key="href")
    # using an index to get the score information
    scoreString = scoreList[index].select_one(selector=".score")
    # it's possible, that the post is too new to have a score
    print(scoreString)
    if scoreString == None:
        score = 0
    else:
        # we only want the score and not the text "points". so split it
        score = int(scoreString.getText().split(sep=" ")[0])
    dictEntry["Score"] = score
    # append dictionary to the list
    topScoreList.append(dictEntry)
    index +=1

# using lambda to sort dictionary in lists... gave me quite some headache ;-)
sortedList = sorted(topScoreList, key=lambda x: x['Score'], reverse=True)
for entry in sortedList:
    print(f"Score: {entry['Score']}\nTitle: {entry['Title']}\nLink : {entry['Link']}\n")




