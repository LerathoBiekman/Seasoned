from django.contrib import admin
from .models import Recipe
from .models import Ingredient
from .models import Appliances
from .models import Nationalities
from .models import Wishes
from .models import SeasonsHolidays


admin.site.register(Ingredient)
admin.site.register(Appliances)
admin.site.register(Nationalities)
admin.site.register(Wishes)
admin.site.register(SeasonsHolidays)
admin.site.register(Recipe)