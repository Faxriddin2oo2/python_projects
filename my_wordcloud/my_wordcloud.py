# Bismillah
"""
Created on Fri Sep 13 23:05:02 2024

@author: Faxriddin
"""

import os
from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt



current_directory = os.path.dirname(__file__)

bowie_image_path = os.path.join(current_directory, "image1.png")
bowie_image = Image.open(bowie_image_path)


bowie_mask = np.array(bowie_image)

# print(bowie_mask)

with open(os.path.join(current_directory, "believer.txt")) as f:
  lyrics = f.read()


wordcloud = WordCloud(background_color="white", mask=bowie_mask, collocations=False, stopwords=STOPWORDS, contour_color="white", contour_width=1)
wordcloud.generate(lyrics)
image_colors = ImageColorGenerator(bowie_mask)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()