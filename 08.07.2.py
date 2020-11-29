def make_album():
	prompt_0 = "Please, specify the album: "
	prompt_1 = "Please, specify the artist: "
	res_album = input(prompt_0)
	res_artist = input(prompt_1)
	album_info = {'album': res_album, 'res_artist': res_artist}
	print(album_info)
make_album()
make_album()
make_album()