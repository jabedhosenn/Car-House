from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name