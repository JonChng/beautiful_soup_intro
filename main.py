from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find_all("span", class_="titleline")


article_titles = []
article_links = []

for i in range(len(title)):

    article_title = title[i].find("a")
    article_link = article_title['href']

    article_titles.append(article_title)
    article_links.append(article_link)

article_votes = [int(score.get_text().split()[0]) for score in soup.find_all("span", class_="score")]

ind = article_votes.index(max(article_votes))





