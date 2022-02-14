from django.db import models


class Upcycle(models.Model):
    """ Gives user information regarding upcycling processes and ethical credentials"""
    title = models.CharField(max_length=600)
    information = models.TextField()
    author = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
