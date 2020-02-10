import wget

urlInput = input("enter a url for wget to scrape\n")


filename = wget.download(urlInput)

print("Downloaded: " + filename)

print("done!\nterminating")