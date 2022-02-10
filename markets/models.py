from django.db import models


class Markets(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    when = models.TextField()
    where = models.TextField()
    cost = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
