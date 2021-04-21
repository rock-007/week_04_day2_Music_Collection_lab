import pdb
from models.album import Album
from models.artist import Artist


import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist_01 = Artist("Junaid_jumshaid")
artist_repository.save(artist_01)
#artist_repository.delete_all() it must delete from album too

#ADDING ARTIST_02&_03 AND SAVING IN DB
artist_02 = Artist("Shafqat Amanat Ali")
artist_repository.save(artist_02)
artist_03 = Artist("Ali Zafar")
artist_repository.save(artist_03)

#ADDING ALBUM_01 AND THEN DELETING ALL THE ALBUMS
album_1 = Album("Jalwa-e-Janan","Rock", artist_01)
album_repository.save(album_1)
album_repository.delete_all()

#ADDING ALBUM_02 AND THEN DELETING BY ID
album_2 = Album("Fuzon","Rock", artist_02)
album_repository.save(album_2)
album_repository.delete_by_id(album_2)

#ADDING ALBUM_03 
album_3 = Album("Jhoom","Pop", artist_03)
album_repository.save(album_3)

# SELECTING ALL ALBUM FOR SPECIFIC ARTIST
item_selected_2 = album_repository.select_by_id(album_3.artist.id)

# SELECTING ARTIST DETAILS WITH AN ID
artist_selected_2 = artist_repository.select_by_id(artist_02.id)
artist_repository.albums(artist_03)


pdb.set_trace()

