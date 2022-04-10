import pandas as pd
import json

artists = pd.read_csv('artists.csv')
artistsDf = pd.DataFrame(artists)
artistNames = artistsDf['Artist'].tolist()
artistImages = artistsDf['image'].tolist()

listOfArtist = []
for index in range(0, len(artistNames)):
    tempDict = {'name': artistNames[index], 'image': artistImages[index]}
    listOfArtist.append(tempDict)

artistsJSON = json.dumps(listOfArtist)


def returnArtists():
    return artistsJSON
