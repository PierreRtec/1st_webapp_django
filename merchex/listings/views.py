from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  # pointe vers le nouveau nom de modèle
           {'bands': bands})

def aboutus(request):
    return HttpResponse('<h1>About us</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>Liste des annonces</h1> <p>Annonces des articles :</p>')

def contactus(request):
    return HttpResponse('<h1>Contactez-nous ! </h2> Formulaire de contact</h2>')
