import csv
import requests
import pandas as pd
import os
from bs4 import BeautifulSoup

url = "https://store.steampowered.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

game_items = soup.find_all(class_='tab_item')

judul = []
genre = []
harga = []

for item in game_items:
    title = item.find(class_='tab_item_name').text.strip()

    categories = item.find_all(class_='tab_item_top_tags')
    if categories:
        categories = [c.text.strip() for c in categories]
    else:
        categories = ['None']

    price = item.find(class_='discount_final_price')
    if price is not None:
        price = price.text.strip()
    else:
        price = 'None'

    judul.append(title)
    genre.append(categories)
    harga.append(price)

data = {
    'Judul': judul,
    'Genre': genre,
    'Harga': harga
}

df = pd.DataFrame(data)

directory = "C:/Users/ekyfe/Documents/college/Semester 2/Pemrosesan Data/Project_UAS"

if not os.path.exists(directory):
    os.makedirs(directory)

filename = os.path.join(directory, 'data_games.csv')
df.to_csv(filename, index=False)

print(df)
print(f"\nData berhasil disimpan dalam file {filename}.")
