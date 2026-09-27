import osmnx as ox

def download_city_boundary(city: str, country: str, output_dir: str = "."):
    """
    Descarga el límite administrativo de una ciudad desde OpenStreetMap
    y lo guarda como GeoJSON.
    """
    place_name = f"{city}, {country}"
    print(f"Descargando límite de: {place_name}")

    gdf = ox.geocode_to_gdf(place_name)

    filename = f"{output_dir}/{city.lower().replace(' ', '_')}_boundary.geojson"
    gdf.to_file(filename, driver="GeoJSON")

    print(f"Guardado en: {filename}")
    return filename


if __name__ == "__main__":
    cities = [
        ("Cochabamba", "Bolivia"),
        ("Leuven", "Belgium"),
    ]

    for city, country in cities:
        download_city_boundary(city, country)