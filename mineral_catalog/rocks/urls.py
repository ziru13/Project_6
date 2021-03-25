from django.urls import path
from . import views

app_name = 'rocks'

# make our variable, a list, in the old Django, it didn't use to be a list, now it's just a list
urlpatterns = [
    path('', views.rock_list, name='rock_list'),
    path('load-rocks/', views.load_rocks, name='load_rocks'),
    # path('<int:course_pk>/<int:step_pk>/', views.step_detail, name='step_detail'),
    # path('<int:pk>/', views.course_detail, name='course_detail'),
]