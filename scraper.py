from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import urllib.parse


def scrape_artist_tags(artist_name):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    try:
        formatted_artist = urllib.parse.quote(artist_name)
        url = f"https://www.last.fm/music/{formatted_artist}/+tags"
        print(url)
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        tag_elements = soup.find_all("a", class_="link-block-target")
        tags = [
            tag.get_text().strip()
            for tag in tag_elements
            if tag.get_text().strip()[0].islower()
        ]
        print(tags)
        return tags[0].lower() if tags else None

    finally:
        driver.quit()


def scrape_top_movies(film_tags):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    try:
        film_titles = []
        for tag in film_tags:
            formatted_tags = (
                urllib.parse.quote(f"ecology") + "%2C" + urllib.parse.quote(tag)
            )
            url = f"https://www.imdb.com/search/keyword/?keywords={formatted_tags}&ref_=kw_ref_key&sort=moviemeter,asc&mode=detail&page=1"
            driver.get(url)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            list_items = soup.find_all("div", class_="lister-item mode-detail")
            for item in list_items:
                title_tag = item.find("h3", class_="lister-item-header").find("a")
                image = item.find("img")
                if title_tag and image:
                    link = "https://www.imdb.com" + title_tag["href"]
                    image_src = image.get("loadlate", image["src"])
                    film_titles.append((title_tag.get_text().strip(), link, image_src))
                if len(film_titles) >= 5:
                    break
            if len(film_titles) >= 5:
                break
        print(film_titles)
        return film_titles
    finally:
        driver.quit()
