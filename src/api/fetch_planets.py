import requests

def fetch_and_store_planets(db, Planets):
    url = "https://www.swapi.tech/api/planets"
    response = requests.get(url)
    if response.status_code == 200:
        planets_data = response.json().get('results', [])
        for planet in planets_data:
            planet_details_url = planet['url']
            planet_response = requests.get(planet_details_url)
            if planet_response.status_code == 200:
                planet_details = planet_response.json().get('result', {}).get('properties', {})
                name = planet_details.get('name', 'N/A')
                description = planet_details.get('terrain', 'N/A') 

                new_planet = Planets(name=name, description=description)
                db.session.add(new_planet)
        
        db.session.commit()