from django.db import models
# Import the reverse function
from django.urls import reverse
<<<<<<< HEAD
# Import the date function 
from datetime import date
=======
# add this import
from datetime import date
# Import the User
from django.contrib.auth.models import User

>>>>>>> working

# A tuple of 2-tuples, MEALS is like a constant dont change
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})
=======
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

>>>>>>> working

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
<<<<<<< HEAD
    # Add the M:M relationship
    toys = models.ManyToManyField(Toy)

=======
    toys = models.ManyToManyField(Toy)
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> working

    # new code below
    def __str__(self):
        return self.name

    # Add new method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})

<<<<<<< HEAD
    # Feeding method
=======
      # add this new method
>>>>>>> working
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

# Add new Feeding model below Cat model
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS, # add the 'choices' field option
        default=MEALS[0][0]  # set the default value for meal to be 'B'
    )
    # Create a dog_id FK
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    # change the default sort
    class Meta:
        ordering = ['-date']

<<<<<<< HEAD
=======
class Photo(models.Model):
    url = models.CharField(max_length=200)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for dog_id: {self.dog_id} @{self.url}"
>>>>>>> working
