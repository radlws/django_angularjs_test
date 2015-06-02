from django.db import models

# Create your models here.


class WeeklyRating(models.Model):

    date = models.DateField(auto_now_add=True, unique=True)
    average = models.DecimalField(max_digits=3, decimal_places=1)
    median = models.DecimalField(max_digits=3, decimal_places=1)
    count = models.IntegerField()

    def __unicode__(self):
        return "{}: {}".format(self.date, self.average)