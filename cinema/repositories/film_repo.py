import logging


from cinema import models as model
from cinema.model.film import Film


def create(table: model.FilmEntity, film: Film):
    logging.debug("Creating new film")
    table.save(
        film
    )


def read(table: model.FilmEntity, id: int):
    logging.debug(f"Reading film {id}")
    return table.objects.filter(id=id)

def read_all(table: model.FilmEntity):
    logging.debug(f"Reading all films")
    return table.objects.all()

def getCount(table: model.FilmEntity):
    logging.debug(f"Getting films count")
    return table.objects.count()