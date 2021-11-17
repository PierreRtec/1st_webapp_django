from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def aboutus(request):
    return HttpResponse('<h1>About us</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>Liste des annonces</h1> <p>Annonces des articles :</p>')

def contactus(request):
    return HttpResponse('<h1>Contactez-nous ! </h2> Formulaire de contact</h2>')
