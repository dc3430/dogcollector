from django.contrib import admin
# import your models here
from .models import Dog, Feeding, Toy

# Register your models here
admin.site.register(Dog)
# Register the new Feeding Model 
admin.site.register(Feeding)
# Register the new Toy Model
admin.site.register(Toy)
# Register the new Photo Model
# admin.site.register(Photo)