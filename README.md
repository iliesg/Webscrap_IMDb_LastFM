# MusicToMovies

## Project Overview

MusicToMovies is a unique web application that bridges the gap between musical tastes and eco-conscious cinema. Users share their favorite musical artists, and the app curates a list of environmentally themed films matching the style and ethos of the chosen musicians. It's a novel way to explore the connection between music and environmental awareness through films.

## Features

- **Artist-Based Movie Recommendations**: Users enter their favorite artist's name, and the app suggests eco-friendly films.
- **IMDb and Last.fm Integration**: Leverages data from IMDb and Last.fm to provide accurate film suggestions and artist genres.
- **Diverse Genre Coverage**: Includes a wide range of ecological and environmental themes.

## Tech Stack

- **FastAPI**: For building the API and serving the web application.
- **Jinja2Templates**: For rendering HTML templates.
- **BeautifulSoup & Requests**: Used in scraping IMDb and Last.fm.

## How It Works

1. **Artist Input**: Users input their favorite music artist's name.
2. **Tag Mapping**: The app maps the artist's music style to a corresponding film genre using tags from Last.fm.
3. **Film Recommendation**: Based on the mapped genre, the app scrapes IMDb for films that match these tags.
4. **Display**: The app displays a list of recommended films along with an explanation of why they were chosen.

## Project Structure

- `main.py`: The main FastAPI application file.
- `scraper.py`: Contains functions for scraping data from IMDb and Last.fm.
- `tag_mapping.py`: Handles the mapping of music tags to film genres.
- `templates/`: HTML templates for the web pages.
- `static/`: Static files like CSS and images.

## Usage

1. Navigate to the index page.
2. Enter the name of your favorite music artist.
3. View the list of recommended eco-conscious films.

---

Created by Lila Allanic and Ilies Gourri.
