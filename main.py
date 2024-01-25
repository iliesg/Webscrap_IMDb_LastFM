from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import scraper
import tag_mapping

app = FastAPI()

# Montez un dossier statique où se trouvent les fichiers HTML et CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

from fastapi.templating import Jinja2Templates

# Configure Jinja2 pour qu'il utilise le dossier des templates
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root():
    # Retourne le fichier HTML lors de l'accès à la racine
    return FileResponse("static/index.html")


from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


@app.get("/movies/{artist_name}", response_class=HTMLResponse)
async def get_movies(request: Request, artist_name: str):
    try:
        artist_tag = scraper.scrape_artist_tags(artist_name)
        film_tags = tag_mapping.map_music_tags_to_film_tags(
            artist_tag, tag_mapping.tag_map
        )
        movies = scraper.scrape_top_movies(film_tags)
        return templates.TemplateResponse(
            "movies_template.html",
            {"request": request, "artist_name": artist_name, "movies": movies},
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
