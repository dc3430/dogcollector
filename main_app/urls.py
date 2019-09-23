#routes page
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),# home page/ base
    path('about/', views.about, name='about'), # about page
    path('dogs/', views.dogs_index, name='index'), # route for cats index
    path('dogs/<int:dog_id>', views.dogs_detail, name="detail"), # detail page
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'), # new route used to show a form and create a dog
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'), # new route update dog
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'), # delete dog 
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'), # Add feeding route

    path('dogs/<int:dog_id>/add_photo/', views.add_photo, name='add_photo'), # new path photos
   
]