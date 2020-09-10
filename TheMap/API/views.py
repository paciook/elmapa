from django.shortcuts import render
from django.template import loader
from django.db import models
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random

# Create your views here.

"""
def create_map(request):
	casillas = []
	for x in range(30):
		for y in range(30):
			casillas.append(Casilla(x = x, y = y, color = 'col0', borde = '0'))
	
	for casilla in casillas:
		casilla.save()
		"""

keys = {
	'W': [-1,0],
	'S': [1,0],
	'A': [0, -1],
	'D': [0, 1],
	'X': [0, 0]
}

@csrf_exempt
def get_map(request):
	estados = {}

	if(request.method == 'GET'):

		request.session['pos'] = [random.randint(0,30),random.randint(0,30)]
		request.session['col'] = random.randint(0,15)

	pos = request.session['pos']
	col = request.session['col']

	if (request.method == 'POST'):

		keypress = request.POST.get('move')

		if keypress in keys:

			if keypress == 'X':
				pintar = Casilla.objects.get(x=str(pos[0]),y=str(pos[1]))
				pintar.color = 'col' + str(col)
				pintar.save()

			keypress = keys[keypress]
			for x in range(2):

				pos[x] += keypress[x]

		colpress = request.POST.get('color')
		if colpress is not None:
			request.session['col'] = int(colpress)

		request.session['pos'] = pos

	casillas = Casilla.objects.all()

	for casilla in casillas:
		puntero = [int(casilla.x), int(casilla.y)]
		
		aux = (puntero == pos)
		
		estados[str(puntero[0])+ "," + str(puntero[1])] = casilla.color + " bor" + str(int(aux)) + "3"

	return render(request, 'mapa.html', {"dic": estados, "pos": pos, "str": str})
