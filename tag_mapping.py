tag_map = {
    "ambient": [
        "Nature Conservation",
    ],
    "nature sounds": ["Environment"],
    "new age": ["Environment"],
    "world fusion": ["Wildlife"],
    "african": ["Wilderness"],
    "folk": ["Forest"],
    "celtic": ["Forest"],
    "pop": ["Friendship"],
    "experimental": ["Independent Film"],
    "progressive rock": ["Climate Change"],
    "indie rock": ["Independent Film"],
    "alternative": ["Independent Film"],
    "electronic": ["Science"],
    "techno": ["Science"],
    "acoustic": ["Travel"],
    "singer-songwriter": ["Sustainability"],
    "world": ["Travel"],
    "gothic": ["Death"],
    "metal": ["Murder"],
    "classical": ["Education"],
    "pop rock": ["Friendship"],
    "indie pop": ["Independent Film"],
    "hard rock": ["Murder"],
    "blues": ["Murder"],
    "punk": ["Activism"],
    "folk punk": ["Activism"],
    "rap": ["Activism"],
    "jazz": ["Education"],
}


def map_music_tags_to_film_tags(music_tags, tag_map):
    film_tags = set()
    if music_tags in tag_map:
        film_tags.update(tag_map[music_tags])
    return list(film_tags)
