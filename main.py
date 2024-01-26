from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


genre_list = [
    "Ecology",
    "Environment",
    "Nature",
    "Environmental Issue",
    "Wildlife",
    "Forest",
    "Environmental",
    "Water",
    "Environmentalism",
    "Ocean",
    "Pollution",
    "River",
    "Climate Change",
    "Sea",
    "Beach",
    "Animal",
    "Independent Film",
    "Australia",
    "Death",
    "Science",
    "Sustainability",
    "Coast",
    "Conservation",
    "Fish",
    "Global Warming",
    "Scientist",
    "Politics",
    "Tree",
    "Underwater Scene",
    "Ecosystem",
    "Father Son Relationship",
    "Boat",
    "Lake",
    "Agriculture",
    "Landscape",
    "Photograph",
    "Blood",
    "Countryside",
    "Fire",
    "Husband Wife Relationship",
    "Friendship",
    "Island",
    "Airplane",
    "Biology",
    "Bird",
    "Dog",
    "Environmental Protection",
    "Fishing",
    "Land",
    "Deforestation",
    "Explosion",
    "Family Relationships",
    "Interview",
    "Nature Conservation",
    "Adelaide Australia",
    "Doctor",
    "Flashback",
    "Murder",
    "Natural Resources",
    "Village",
    "Community",
    "Farmer",
    "Activist",
    "Based On Novel",
    "Cigarette Smoking",
    "Desert",
    "Ecological Footprint",
    "F Rated",
    "Father Daughter Relationship",
    "Female Nudity",
    "Mother Son Relationship",
    "Singing",
    "Telephone Call",
    "Travel",
    "Vegetation",
    "Activism",
    "Australian",
    "Biodiversity",
    "Car",
    "Earth",
    "Environmental Documentary",
    "Habitat",
    "Protest",
    "Psychotronic Film",
    "Education",
    "Gun",
    "Map",
    "Rain",
    "Rescue",
    "Sand",
    "Voice Over",
    "Wilderness",
    "Camera",
    "Ecological",
    "Helicopter",
    "Mountain",
    "Natural History",
    "Police",
    "Restaurant",
    "School",
]

lower_genre_list = [genre.lower() for genre in genre_list]

import scraper
import tag_mapping

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root():
    return FileResponse("static/index.html")


@app.get("/movies/{artist_name}", response_class=HTMLResponse)
async def get_movies(request: Request, artist_name: str):
    try:
        artist_tags = scraper.scrape_artist_tags(artist_name)
        film_genre = tag_mapping.get_film_genre_from_chatgpt(artist_tags, genre_list)
        film_tags = [film_genre]  # Convert genre to a list for the scraper function
        movies = scraper.scrape_top_movies(film_tags)
        explaination = tag_mapping.get_explaination(
            movies, artist_name, artist_tags, film_genre
        )
        return templates.TemplateResponse(
            "movies_template.html",
            {
                "request": request,
                "artist_name": artist_name,
                "movies": movies,
                "explain": explaination,
            },
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
