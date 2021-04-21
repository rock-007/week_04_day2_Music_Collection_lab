import pdb
from models.album import Album
from models.artist import Artist


import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist_01 = Artist("Junaid_jumshaid")
artist_repository.save(artist_01)
#artist_repository.delete_all() it must delete from album too

artist_02 = Artist("Shafqat Amanat Ali")
artist_repository.save(artist_02)
artist_03 = Artist("Ali Zafar")
artist_repository.save(artist_03)

album_1 = Album("Jalwa-e-Janan","Rock", artist_01)
print(album_1.title)
album_repository.save(album_1)
album_repository.delete_all()

album_2 = Album("Fuzon","Rock", artist_02)
album_repository.save(album_2)
album_repository.delete_by_id(album_2)
album_3 = Album("Jhoom","Pop", artist_03)
album_repository.save(album_3)

item_selected_2 = album_repository.select_by_id(album_3.id)
artist_selected_2 = artist_repository.select_by_id(artist_02.id)
artist_repository.albums(artist_03)


pdb.set_trace()

