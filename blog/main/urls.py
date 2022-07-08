from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<topic_id>/', views.topic, name='topic'),
    #forms patterns
    path('new_topic/', views.new_topic, name='new_topic'),
    path('<int:topic_id>/new_note/', views.new_note, name='new_note'),

]