from db.run_sql import run_sql
from models.artist import Artist

import repositories.album_repository as album_repository

# CREATE

def save(artist):
    sql ="INSERT INTO artists(name) VALUES(%s) RETURNING *"
    values = [artist.name]
    results= run_sql(sql,values)
    # return from DB is like [{}{}....]
    artist.id = results[0]['id']

#DELETE_ALL

def delete_all():
    album_repository.delete_all()
    sql = "DELETE FROM artists"
    run_sql(sql)

# SELECT_BY_ID
def select_by_id(id):
    sql ="SELECT * from artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        result = Artist(result['name'], result['id'])

    return result


# return album for specific artist

def albums(artist):
    result = album_repository.select_by_id(artist.id)

    return result


