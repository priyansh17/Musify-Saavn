import json
import requests
import endpoints

newAlbumImage = "https://hollywoodlife.com/wp-content/uploads/2021/05/Post-Malone-New-Album-Shutterstock-embed-1.jpg"
newPlaylistImage = "https://images.genius.com/2850aca0dd580af5b1d50d47136eae74.1000x1000x1.png"
recentlyplayed = "https://allthings.how/wp-content/uploads/2021/11/allthings.how-how-to-queue-songs-on-spotify-for-desktop-and-mobile-song-queue.png"
artistImage = "https://themusicessentials.com/wp-content/uploads/2018/12/Drake-spotify-most-streamed-artist.jpg"
moodImage = "https://i.scdn.co/image/ab67706f00000003bd0e19e810bb4b55ab164a95"


def getHomePage():
    search_base_url = endpoints.homepage_url
    response = requests.get(search_base_url).text.encode()
    response = json.loads(response)
    getHomeList = []

    allAlbums = response['new_albums']
    NewAlbumDict = {'topic': "New Albums", 'urlTopicImage': newAlbumImage}
    Albums = []
    for album in allAlbums:
        tempAlbum = {'name': album['query'], 'urlTopicImage': album['image'], 'albumId': album['albumid']}
        Albums.append(tempAlbum)
    NewAlbumDict['playlists'] = Albums
    getHomeList.append(NewAlbumDict)

    allPlaylist = response['featured_playlists']
    NewPlaylistDict = {'topic': "Featured Playlist", 'urlTopicImage': newPlaylistImage}
    Playlist = []
    for pl in allPlaylist:
        tempPlaylist = {'listId': pl['listid'], 'urlTopicImage': pl['image'], 'name': pl['listname'],
                        'count': pl['count']}
        Playlist.append(tempPlaylist)
    NewPlaylistDict['playlists'] = Playlist
    getHomeList.append(NewPlaylistDict)

    RecentlyPlayed = {'topic': "Recently Played", 'urlTopicImage': recentlyplayed}
    Playlist = []
    RecentlyPlayed['playlists'] = Playlist
    getHomeList.append(RecentlyPlayed)

    Artists = {'topic': "Your Artists", 'urlTopicImage': artistImage}
    Playlist = []
    Artists['playlists'] = Playlist
    getHomeList.append(Artists)

    Moods = {'topic': "Mood Swingies", 'urlTopicImage': moodImage}
    Playlist = []
    Moods['playlists'] = Playlist
    getHomeList.append(Moods)

    return json.dumps(getHomeList)
