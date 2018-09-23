#!/usr/local/bin/python3

"""Make a program, which asks URL from the user.
If the URL can be opened, write the URL contents into a local file path defined by the user.
Use binary mode"""

from urllib.request import urlopen

def urlDownloadSave(url, fileName):
    """Accepts url and filename as arguments in string format. Returns a binary file."""
    with urlopen(url) as urlResponse:
        content = urlResponse.read()
        with open(fileName, "wb") as urlFile:
            urlFile.write(content)

def main():
    urlDownloadSave(input("Enter valid url: "), input("Enter a filename where to save the url-data: "))


if __name__ == '__main__':
    main()
