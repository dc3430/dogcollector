from django.db import models
# Import the reverse function
from django.urls import reverse
# add this import
from datetime import date

# A tuple of 2-tuples, MEALS is like a constant dont change
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)




# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    # new code below
    def __str__(self):
        return f'{self.name} ({self.id})'

    # Add new method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})

      # add this new method
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

# Add new Feeding model below Cat model
class Feeding(models.Model):
    date = models.DateField()
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