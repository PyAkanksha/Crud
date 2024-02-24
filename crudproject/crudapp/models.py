from django.db import models

# Create your models here.


class crud(models.Model):
    cname = models.CharField(max_length=30)
    clname = models.CharField(max_length=30)
    cadd = models.TextField(max_length=200)
    cphone = models.IntegerField()
    csalary = models.FloatField()


def __str__(self):
    return self.cname
