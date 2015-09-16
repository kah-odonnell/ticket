from django.shortcuts import render
from ticket.models import UserProfile, Event, Ticket, Purchase

# response
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

# authenticate
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import hashers
# Create your views here.
def index(request):
	return HttpResponse('Hello!')

def create_event(request):
	if request.method != 'POST':
		return HttpResponse('must make POST request')
	name = request.POST['name']
	description = request.POST['description']
	start_time = request.POST['start_time']
	location = request.POST['location']
	event = Event(name=name,description=description,start_time=start_time,location=location)
	try:
		event.save()
	except db.Error:
		return HttpResponse('db error')

	return HttpResponse('success')

def update_event(request,event_id):
	if request.method != 'POST':
		return HttpResponse('must make POST request')
	try:
		event = Event.objects.get(pk=event_id)
	except models.Event.DoesNotExist:
		return HttpResponse('event not found')

	changed = False
	if 'name' in request.POST:
		event.name=request.POST['name']
		changed=True
	if 'description' in request.POST:
		event.description=request.POST['description']
		changed=True
	if 'start_time' in request.POST:
		event.start_time=request.POST['start_time']
		changed=True
	if 'location' in request.POST:
		event.location=request.POST['location']
		changed=True

	if not changed:
		return HttpResponse('no field updated')
	event.save()
	return HttpResponse('success')

def event(request,event_id):
	if request.method != 'GET':
		return HttpResponse('must make GET request')
	try:
		event = Event.objects.get(pk=event_id)
	except:
		return HttpResponse('event not found')

	return HttpResponse(event)

def create_ticket(request):
	if request.method != 'POST':
		return HttpResponse('must make POST request')
	name = request.POST['name']
	price = request.POST['price']
	event_id = request.POST['event_id']
	amount = request.POST['amount']
	event = Event.objects.get(pk=event_id)
	ticket = Ticket(name=name,price=price,event=event,amount=amount)
	try:
		ticket.save()
	except db.Error:
		return HttpResponse('db error')
	return HttpResponse('success')

def update_ticket(request,ticket_id):
	if request.method != 'POST':
		return HttpResponse('must make POST request')
	try:
		ticket = Ticket.objects.get(pk=ticket_id)
	except models.Ticket.DoesNotExist:
		return HttpResponse('ticket not found')

	changed = False
	if 'name' in request.POST:
		ticket.name = request.POST['name']
		changed = True
	if 'price' in request.POST:
		ticket.price = request.POST['price']
		changed = True
	if 'amount' in request.POST:
		ticket.amount = request.POST['amount']
		changed = True

	if not changed:
		return HttpResponse('no field updated')
	ticket.save()

	return HttpResponse('success')

def ticket(request,ticket_id):
	if request.method != 'GET':
		return HttpResponse('must make GET request')
	try:
		ticket = Ticket.objects.get(pk=ticket_id)
	except:
		return HttpResponse('ticket not found')

	return HttpResponse(ticket)


def create_user(request):
	if request.method != 'POST':
		return HttpResponse('must make POST request')
	username = request.POST['username']
	password = hasher.make_passworkd(request.POST['password'])
	firstname = request.POST['firstname']
	lastname = request.POST['lastname']
	user = User(username=username,password=password)
	try:
		user.save()
	except:
		return HttpResponse('db error')
	user_profile = UserProfile(firstname=firstname,lastname=lastname,user=user)
	try:
		user_profile.save()
	except:
		return HttpResponse('db error')
	return HttpResponse('success')

def update_user(request,userp_id):
	if request.method != 'POST':
		return HttpResponse('must make POST request')
	try:
		user_p = UserProfile.objects.get(pk=userp_id)
	except models.UserProfile.DoesNotExist:
		return HttpResponse('User not found')
	changed = False
	user = user_p.user

	if 'firstname' in request.POST:
		user_p.firstname=request.POST['firstname']
		changed=True
	if 'lastname' in request.POST:
		user_p.lastname=request.POST['lastname']
		changed=True
	if 'password' in request.POST:
		user.password = hasher.make_password(request.POST['password'])
		changed=True

	if not changed:
		return HttpResponse('no field updated')
	user_p.save()
	user.save()
	return HttpResponse('success')

def user(request,userp_id):
	if request.method != 'GET':
		return HttpResponse('must make GET request')
	try:
		user_p = UserProfile.objects.get(pk=userp_id)
		user = user_p.user
	except:
		return HttpResponse('user not found')

	return HttpResponse(user_p)