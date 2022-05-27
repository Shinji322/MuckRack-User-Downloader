#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests

def get_all_stories(html_file:str) -> list[str]:
    links = []
    with open(html_file, "r+") as f:
        soup = BeautifulSoup(f, 'lxml')
        for div in soup.find_all("div", class_="news-story"):
            links.append(
                    div.find('a').get('href')
            )
    print(links)
    return links


counter = 0
# Downloads the data from the stories
def download_story_data(link:str):
    print(f"Downloading story: {link}")

    global counter
    counter += 1
    res = requests.get(url=link)
    if res.status_code != 200:
        print(f"Status code: ${res.status_code}\n Error occurred with link: ${link}\n\n")
        return
    soup = BeautifulSoup(res.content, 'lxml')
    filename = f"output/{counter}__{link.split('/')[-2]}.html"

    article_body = soup.find("div", id="article-body")
    if not article_body:
        print(f"Article body not found for ${link} ")
        return


    with open(filename, 'a') as f:
        for text in article_body.find_all("p"):
            f.write(f"{text}\n")


def main():
    for story in get_all_stories("file.html"):
        download_story_data(story)


if __name__ == "__main__":
    main()
