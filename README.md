Project Overview
MusicToMovies is a unique web application that bridges the gap between musical tastes and eco-conscious cinema. Users share their favorite musical artists, and the app curates a list of environmentally themed films matching the style and ethos of the chosen musicians. It's a novel way to explore the connection between music and environmental awareness through films.

Features
Artist-Based Movie Recommendations: Users enter their favorite artist's name, and the app suggests eco-friendly films.
IMDb and Last.fm Integration: Leverages data from IMDb and Last.fm to provide accurate film suggestions and artist genres.
Diverse Genre Coverage: Includes a wide range of ecological and environmental themes.
Tech Stack
FastAPI: For building the API and serving the web application.
Jinja2Templates: For rendering HTML templates.
BeautifulSoup & Requests: Used in scraping IMDb and Last.fm.
How It Works
Artist Input: Users input their favorite music artist's name.
Tag Mapping: The app maps the artist's music style to a corresponding film genre using tags from Last.fm.
Film Recommendation: Based on the mapped genre, the app scrapes IMDb for films that match these tags.
Display: The app displays a list of recommended films along with an explanation of why they were chosen.
