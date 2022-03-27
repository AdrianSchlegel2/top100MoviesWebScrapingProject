from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# get the website contents

response = requests.get(URL)

# create a soup

soup = BeautifulSoup(response.text, "html.parser")

# load the movie titles

all_titles = soup.findAll(class_="title")
all_titles_text = [soup.getText() for soup in all_titles]
movie_titles_text = []

# get rid of any titles which are not the movies

for title in all_titles_text:
    split_title = title.split(" ")
    if ")" in split_title[0]:
        movie_titles_text.append(title)

movie_titles_text.reverse()

# append the list to the movies.txt document

for title in movie_titles_text:
    with open("movies.txt", "a") as file:
        file.write(f"{title}\n")
