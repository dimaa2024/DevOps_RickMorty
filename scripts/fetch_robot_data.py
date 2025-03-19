import requests
import csv

def fetch_robot_data():
    url = 'https://rickandmortyapi.com/api/character/?species=Robot&status=Dead'
    robots = []

    while url:
        response = requests.get(url)
        data = response.json()
        for character in data['results']:
            if character['origin']['name'] == 'Earth':
                robots.append({
                    'Name': character['name'],
                    'Location': character['location']['name'],
                    'Image': character['image']
                })
        url = data['info']['next']

    with open('robots.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Location', 'Image']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(robots)

if __name__ == '__main__':
    fetch_robot_data()