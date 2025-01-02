import json
import logging

from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from cinema.model.film import Film
from cinema.models import FilmEntity


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    # return render(request, 'cinema/templates/main.html', {})


@csrf_exempt
def getAll(request):
    """
       Retrieve all films from the database and return them as an HTTP response.
       This function queries the database for all FilmEntity objects, converts them to Film objects,
       and then to dictionaries. It also prints the total count of films and each film's name.
       Args:
           request (HttpRequest): The HTTP request object.
       Returns:
           HttpResponse: A response containing the count of films and a list of all films in the database.
                         The response text is formatted as a string.
       """
    count = FilmEntity.objects.count()
    print(count)
    films: list[Film] = [FilmEntity.to_film(film) for film in FilmEntity.objects.all()]
    films_json = [film.to_dict() for film in films]
    for e in films:
        print(e)
    return JsonResponse(films_json, safe=False)


@csrf_exempt
def read(request, id):
    try:
       film = FilmEntity.to_film(FilmEntity.objects.get(id=id))
       return HttpResponse(film.__str__())
    except:
        return HttpResponse(f"Can't get film with id:{id}", status=503)


@csrf_exempt
def create(request):
    if request.method == "POST":
      try:
          body = request.POST
          data = json.loads(request.body)
          print(f"Creating film {data.get("title")}")
          rating=data['rating']
          if (type(rating) == int):
              print('Creating')
              film = FilmEntity.objects.create(
                 name=data['title'],
                 rating=rating,
                 description=data['description']
                 )
              print(film)
              film.save()
              return HttpResponse(f"Film {body.get("title")} created successfully", status=200)
          else:
              return HttpResponse(f"Film rating must be a number(int)", status=400)
      except:
          return HttpResponse(f"Can't create film", status=503)
    else:
        return HttpResponse("Get method not allowed",status=400)
