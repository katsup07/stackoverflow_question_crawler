import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
# soup document mirrors the structure of an html doc, so is easy to navigate to find elements
# Creates object from string with content and a specified parser
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary--content-title")
count = 0;
for question in questions:
    print(count, question.select_one(".s-link").get_text())
    count+=1
