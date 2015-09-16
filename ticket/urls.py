from django.conf.urls import patterns, url

from ticket import views

urlpatterns = patterns('',
	url(r'^createEvent/$', views.create_event, name='createEvent'),
	url(r'^createTicket/$',views.create_ticket, name='createTicket'),
	url(r'^createUser/$',views.create_user, name='createUser'),
	
	url(r'^updateEvent/(?P<event_id>\d+)/$',views.update_event,name='updateEvent'),
	url(r'^updateTicket/(?P<ticket_id>\d+)/$',views.update_ticket,name='updateTicket'),
	url(r'^updateUser/(?P<userp_id>\d+)/$',views.update_user,name='updateUser'),
	
	url(r'^event/(?P<event_id>\d+)/$',views.event,name='event'),
	url(r'^ticket/(?P<ticket_id>\d+)/$',views.ticket,name='ticket'),
	url(r'^user/(?P<userp_id>\d+)/$',views.user,name='user'),
	
	
)