# Bismillah
"""
Created on Mon Oct 28 20:13:39 2024

@author: Faxriddin
"""

import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="lxml")
 

for story_heading in soup.find_all(class_="summary-class"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())
        







