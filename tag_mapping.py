import requests


def get_film_genre_from_chatgpt(music_tags, genre_list):
    api_url = "https://api.openai.com/v1/chat/completions"  # Modification ici
    prompt = (
        f"Select a film genre that closely corresponds to the music tags '{', '.join(music_tags)}'. "
        f"Your choice should encapsulate the mood and themes expressed in these music tags. "
        f"From the following less common options, excluding 'Independent Film' unless it's unequivocally the most suitable, "
        f"pick the genre that best matches: {', '.join(genre for genre in genre_list if genre != 'Independent Film')}. "
        f"Please respond with only the genre name, and make sure it's a genre from this specific list. "
        f"Do not provide explanations or additional commentary. Just the genre name. Your selection must be from this list. "
    )

    headers = {
        "Authorization": "Bearer OPEN_AI_TOKEN",
        "Content-Type": "application/json",
    }

    data = {
        "model": "gpt-4",  # Assurez-vous d'utiliser le bon modèle de chat ici
        "messages": [
            {"role": "system", "content": prompt}
        ],  # Format pour chat/completions
    }

    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()

        # Extraire le genre du film
        if "choices" in response_data and len(response_data["choices"]) > 0:
            film_genre = response_data["choices"][0]["message"]["content"].strip()
            if film_genre.lower() in lower_genre_list:
                return film_genre
            else:
                print(
                    f"Genre reçu '{film_genre}' n'est pas dans la liste des genres autorisés. Retour par défaut à 'Nature'."
                )
                return "Nature"  # Retourne "Nature" par défaut si le genre n'est pas dans la liste
        else:
            print("La réponse de l'API ne contient pas le format attendu")
            return "Nature"  # Retourne "Nature" par défaut si la réponse n'est pas formatée correctement
    else:
        print("Failed to get response from ChatGPT API")
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        return "Nature"  # Retourne "Nature" par défaut en cas d'échec de la requête


def get_explaination(movies, artist_name, film_tags, film_genre):
    api_url = "https://api.openai.com/v1/chat/completions"
    prompt = f"Imagine you are an artist, and I'm seeking your suggestions for eco-friendly films that align with my musical tastes to help me become more environmentally conscious. My favorite artist is {artist_name}, and you've recommended these genres associated with ecology: {', '.join(film_genre)}. You've also provided me with your top 5 film recommendations related to ecology and the other genre: {', '.join(movie[0] for movie in movies)}. Along with your recommendations, please provide very concise explanations for some of these film choices, linking them with the provided information. Keep your suggestions and explanations insightful yet brief."

    headers = {
        "Authorization": "Bearer OPEN_AI_TOKEN",
        "Content-Type": "application/json",
    }

    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": ""},
        ],
    }

    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()

        if "choices" in response_data and len(response_data["choices"]) > 0:
            explanation = response_data["choices"][0]["message"]["content"].strip()
            return explanation
        else:
            print("La réponse de l'API ne contient pas le format attendu")
            return "?"
    else:
        print("Failed to get response from ChatGPT API")
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        return "?"


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
