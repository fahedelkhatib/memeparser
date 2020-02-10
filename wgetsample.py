import wget
import os

urlInput = input("enter a url for wget to scrape\n")


filename = wget.download(urlInput)
currentFilePath = str(os.getcwd())

print("\nDownloaded: " + currentFilePath + filename)

print("done!\nterminating")