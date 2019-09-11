# main_app/views.py/ controllers
from django.shortcuts import render, redirect
# Add import Create, UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the following import
from .models import Dog
# Add feeding form
from .forms import FeedingForm

#add Create view
class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    success_url = '/dogs/'

class DogUpdate(UpdateView):
    model = Dog
    # Let's disallow the renaming of a Dog by excluding the name field!
    fields = ['name', 'breed', 'description', 'age']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

# Create your views here, Define the home view
def home(request):
    return render(request, 'home.html')
# Add show view
def about(request):
    return render(request, 'about.html')
# Add new view
def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', { 'dogs': dogs })
# Add detail view
def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'dogs/detail.html', { 
        # include the Dog and feeding_form in the context
        'dog': dog, 'feeding_form': feeding_form
    })

# add this new function below dogs_detail
def add_feeding(request, dog_id):
    # create the ModelForm using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
      # don't save the form to the db until it
      # has the dog_id assigned
      new_feeding = form.save(commit=False)
      new_feeding.dog_id = dog_id
      new_feeding.save()
    return redirect('detail', dog_id=dog_id)

