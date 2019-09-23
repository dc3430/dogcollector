# main_app/views.py/ controllers
from django.shortcuts import render, redirect
# Add import Create, UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# new/updated imports below
import uuid
import boto3
# Add the following import
from .models import Dog, Photo
# Add feeding form
from .forms import FeedingForm

# Add these "constants" below the imports
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'dogcollector-dc'

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

def add_photo(request, dog_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to dog_id or dog (if you have a dog object)
            photo = Photo(url=url, dog_id=dog_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', dog_id=dog_id)
