import json
import pandas as pd
import os
from pandas import json_normalize
from textblob import TextBlob
import numpy as np
import re
import matplotlib.pyplot as plt

dir = []
for directories in os.listdir():
    dir += [directories]

dir.remove("testdate.py")
dir.remove("Import.py")
dir.remove("OldPrograms")
dir.remove("Auswertung.txt")
dir.remove("Plot.py")

# Create a  function to clean the tweets
def cleanTwt(twt):
    twt = re.sub("#bitcoin", "bitcoin", twt) #removes the hashtah from bitcoin
    twt = re.sub("#Bitcoin", "bitcoin", twt) #removes the hashtag from Bitcoin
    twt = re.sub("#[A-Za-z0-9]+", "", twt)   # removes any strings with a #
    twt = re.sub("\\n", "", twt) # removes the "\n" string
    twt = re.sub("https?:\/\/\S+", "", twt) #removes any hyperlinks
    return twt

# create a function to get the polarity
def getPolarity(twt):
    return TextBlob(twt).sentiment.polarity
    
# create a function to get the text sentiment
def getSentiment(score):
    if score<0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    else:
        return "Positive"

datum_plot = []
data_end = []
f = open("Auswertung.txt","w")

for files in dir:
    # read .json data file created by scraping
    tweets_df = pd.read_json(files, lines=True)
    # create a Panda dataFrame with tweet and date
    data_plot = pd.DataFrame(list(tweets_df.content), columns=["Tweets"])
    data_plot["Auswertung"] = data_plot["Tweets"].apply(cleanTwt).apply(getPolarity).apply(getSentiment)
    p = data_plot["Auswertung"].value_counts().Positive
    t = data_plot["Auswertung"].value_counts().Neutral
    n = data_plot["Auswertung"].value_counts().Negative
    data_end += [p/(p+n)]
    print(str(files)+": "+str(p/(p+n)))
    f.write(str(p/(p+n))+"\n")

f.close()