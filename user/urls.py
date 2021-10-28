from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns =[
    # path('',views.my_view,name='my_view'),
    path('',views.IndexView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)