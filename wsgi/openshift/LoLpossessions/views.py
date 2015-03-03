from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib import auth
from LoLpossessions import models
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