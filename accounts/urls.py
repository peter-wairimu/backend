from .views import LoginAPI, RegisterAPI, UserAPI
from django.urls import path
from django.conf.urls import url
from .import views




urlpatterns = [
	path("login/", LoginAPI.as_view()),
	path("register/", RegisterAPI.as_view()),
	path("user/", UserAPI.as_view()),
	url(r'^course/$',views.coursesApi),
    url(r'^course/([0-9]+)$',views.coursesApi),
    
]
