def make_album(title, artist, tracks=None):
	album_info = {
		'artist': artist.title(),
		'title': title.title()
	}
	if tracks:
		album_info['tracks'] = tracks
	return album_info

#make the query for interactions
def album_query():
	prompt_0 = "Please, specify the title: "
	prompt_1 = "Please, specify the artist: "
	prompt_2 = "Please, specify the number of tracks: "
	title = input(prompt_0)
	artist = input(prompt_1)
	tracks = input(prompt_2)
	result = make_album(title, artist, tracks)
	print(result)

album_query()