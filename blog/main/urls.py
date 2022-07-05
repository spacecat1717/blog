from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    #path('topics/<topic_id>/', views.topic, name='topic'),
    #path('topics/<topic_id>/<note_id>/', views.note, name='note'),

]