from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib import auth
from LoLpossessions import models
from django.contrib.auth.models import User
import requests

def registro(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect('/')
	else:
		form = UserCreationForm()
	return render(request, "registro.html", {
		'form': form,
})

def check(request):
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			auth.login(request,user)
			request.session['username'] = username
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('<p>Usuario inactivo</p>')
	else:
		return HttpResponse('<p>Login Incorrecto.<a href="/">Intentar de nuevo </a></p>')

def login(request):
	if request.session.get("username"):
		todo = models.Campeon.objects.all()
		return render_to_response("principal.html",{"todo":todo})
	else:
		return render(request, 'login.html', {})

def campeon(request,campeon_id):
	campeon_concreto = models.Campeon.objects.get(id=campeon_id)
	return render_to_response('campeon.html', {"info_campeon":campeon_concreto},)

def posesion(request,campeon_id):
	user = request.session.get('username')
	username = User.objects.get(username=user)
	campeon_concreto = models.Campeon.objects.get(id=campeon_id)
	if len(models.PosesionCampeon.objects.filter(Campeon=campeon_id).values('Posesion')) == 0:
		insert_posesion = models.PosesionCampeon(Usuario=username,Campeon=campeon_concreto,Posesion=1)
		insert_posesion.save()
		return HttpResponse('<p>Campeon agregado a tu lista en propiedad</p><a href="/enpropiedad"><p>Ir a tu lista de Campeones en propiedad</p></a><a href="/"><p>Volver a los Campeones</p></a>')
	else:
		return HttpResponse('<p>Ya posees este campeon</p>')

def enpropiedad(request):
	user = request.session.get("username")
	username = User.objects.get(username=user)
	posesion_campeones = models.PosesionCampeon.objects.filter(Usuario=username,Posesion=True).values('Campeon')
	enpropiedad = models.Campeon.objects.filter(id__in=posesion_campeones)
	return render_to_response('propiedad.html', {'enpropiedad': enpropiedad},)

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')