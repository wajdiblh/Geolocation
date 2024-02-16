# Script python pour géolocaliser les bâtiments publics chauffés au fioul
import csv
import googlemaps

# Remplacer par votre clé API Google Maps
API_KEY = "Google maps personal API Key"

# Initialiser le client Google Maps
gmaps = googlemaps.Client(key=API_KEY)

# Lire le fichier CSV et géocoder chaque site
with open('input file name.csv', 'r') as csv_file, open('output file name.csv', 'w', newline='') as output_file:
    csv_reader = csv.reader(csv_file)
    csv_writer = csv.writer(output_file)

    header = next(csv_reader)  # Lecture de l'en-tête du fichier d'entrée
    header.extend(["Latitude", "Longitude"])  # Ajouter les colonnes Latitude et Longitude
    csv_writer.writerow(header)  # Écrire l'en-tête dans le fichier de sortie

    for row in csv_reader:
        nom_com_actee = row[0]
        nom_site = row[1]
        dept_nom = row[2]
        dept_insee = row[3]
        com_nom = row[4]
        com_insee = row[5]

        # Construction de l'adresse
        address = f"{nom_site}, {com_nom}, {com_insee}, {dept_nom}, {dept_insee}"

        try:
            # Géocodage à l'aide de l'API de géocodage de Google Maps
            geocode_result = gmaps.geocode(address)

            if geocode_result:
                location = geocode_result[0]['geometry']['location']
                latitude = location['lat']
                longitude = location['lng']
                csv_writer.writerow(row + [latitude, longitude])  # Ecrire une ligne avec des données géocodées
            else:
                csv_writer.writerow(row + ["Location not found", ""])
        except Exception as e:
            csv_writer.writerow(row + [f"Error: {str(e)}", ""])