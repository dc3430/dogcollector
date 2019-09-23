#routes page
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),# home page/ base
    path('about/', views.about, name='about'), # about page
    path('dogs/', views.dogs_index, name='index'), # route for dogs index
    path('dogs/<int:dog_id>', views.dogs_detail, name="detail"), # detail page
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'), # new route used to show a form and create a dog
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'), # new route update dog
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'), # delete dog 
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'), # Add feeding route

    # associate a toy with a dog (M:M)
    path('dogs/<int:dog_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    # unassociate a toy and dog
    path('dogs/<int:dog_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),

    path('dogs/<int:dog_id>/add_photo/', views.add_photo, name='add_photo'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),

    path('dogs/<int:dog_id>/add_photo/', views.add_photo, name='add_photo'), # new path photos
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),

]