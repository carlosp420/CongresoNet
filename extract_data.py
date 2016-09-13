# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup


def extract_data(url_input):
    """
    Este codigo permite extraer el texto de cualquier pagina de internet que
    usa HTML usando la libreria BeautifulSoup4

    * Deberia ser más eficiente con este codigo
    * Extraido del codigo de PeYoTlL en StackOverFLow URL:
      http://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
    """
    url = url_input
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    
    # get text
    text = soup.get_text()
    
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    
    return text
