#preparing the prompts for  further usage
prompt_0 = "Please, specify the title: "
prompt_1 = "Please, specify the artist: "
prompt_2 = "Please, specify the number of tracks: "
#end

#function to make the album
def make_album(title, artist, tracks=None):
    album_info = {
        'artist': artist.title(),
        'title': title.title()
    }
    if tracks:
        album_info['tracks'] = tracks
    return album_info
#end

#make the query for interactions
def album_query():   
    tracks = input(prompt_2)
    result = make_album(title, artist, tracks)
    print(result)

#how to break the cycle
smsg = "Enter 'quit' at any time to stop."
print(smsg)

while True:
    title = input(prompt_0)
    if title == 'quit':
        break

    artist = input(prompt_1)
    if artist == 'quit':
        break

album_query()