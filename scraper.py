# A scraper to get games prices from Steam and show it
# Must have BeautifulSoup and tkinter installed

from bs4 import BeautifulSoup as bs
import tkinter as tk
import requests

games = [
  {
    "url": "https://store.steampowered.com/app/642280/Grim_Dawn__Ashes_of_Malmouth_Expansion/",
    "name": 'Grim Dawn: Ashes of Malmouth'
  },
  {
    "url": "https://store.steampowered.com/app/897670/Grim_Dawn__Forgotten_Gods_Expansion/",
    "name": "Grim Dawn: Forgoten Gods"
  }
]


for i in range(len(games)):
  name = games[i]['name']

  page = requests.get(games[i]['url'])
  soup = bs(page.content, 'html.parser')
  try:
    price = soup.find("div", {"class": "game_purchase_price price"}).get_text().strip()
  except:
    price = soup.find("div", {"class": "discount_final_price"}).get_text().strip()

  games[i]['price'] = price


window = tk.Tk()
window.title('Game Price')

for i in range(len(games)):
  tk.Label(window, text=games[i]['name'], borderwidth=10).grid(column=0, row=i)
  tk.Label(window, text=games[i]['price'], borderwidth=10).grid(column=1, row=i)

window.mainloop()
