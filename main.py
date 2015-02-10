__author__ = 'rawaid'
import Spider
from google import search

books = open("cache/items/book.txt", "r")
bookList = []
for book in books:
    bookList.append(book.rstrip())
print(bookList)

movies = open("cache/items/movie.txt", "r")
movieList = []
for movie in movies:
    movieList.append(movie.rstrip())
print(movieList)

songs = open("cache/items/music.txt", "r")
songList = []
for song in songs:
    songList.append(song.rstrip())
print(songList)
spider = Spider.Spider()
print("Book Sites Found:\n")
for item in bookList:
    for url in search(item + " book", stop=10):
        if type(url) is str:
            #print(spider.parser(url))
            print(spider.parser(url, "book"))
print("Movie Sites Found:\n")
for item in movieList:
    for url in search(item + " movie", stop=10):
        if type(url) is str:
            #print(spider.parser(url))
            print(spider.parser(url, "movie"))
print("Musician Sites Found:\n")
for item in songList:
    for url in search(item + " song", stop=10):
        if type(url) is str:
            #print(spider.parser(url))
            print(spider.parser(url, "music"))

books.close()
movies.close()
songs.close()