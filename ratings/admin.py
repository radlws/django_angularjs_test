from django.contrib import admin

# Register your models here.


from ratings.models import WeeklyRating


admin.site.register(WeeklyRating)