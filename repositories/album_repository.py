from db.run_sql import run_sql
import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository

# SAVE

def save(album):
    sql = "INSERT INTO albums(title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values= [album.title, album.genre, album.artist.id]
    results = run_sql(sql,values)
    album.id = results[0]['id']
    return album

#DELETE_ALL

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

#SELECT_BY_ID_AND_RETURN_RELEVANT_ALBUMS   

def select_by_id(id):
    sql ="SELECT * FROM albums where artist_id = %s"
    value = [id]
    result= run_sql(sql, value)
    albums= []

    for row in result:
        artist = artist_repository.select_by_id(row['artist_id'])
        results = Album(row['id'], row['title'], row['genre'], artist ) 
        albums.append(results)
    return albums

#DELETE_BY_ID

def delete_by_id(album):
    sql ="DELETE FROM albums where id = %s "
    value = [album.id]
    run_sql(sql, value)

