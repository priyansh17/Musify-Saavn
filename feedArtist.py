import pandas as pd
import json

artists = pd.read_csv('artists.csv')
artistsDf = pd.DataFrame(artists)
artistNames = artistsDf['Artist Name'].tolist()

listOfArtist = []
for name in artistNames:
    tempDict = {'name': name}
    listOfArtist.append(tempDict)

artistsJSON = json.dumps(listOfArtist)


def returnArtists():
    return artistsJSON


