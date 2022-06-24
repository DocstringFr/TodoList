from django.db import models
from django.utils.text import slugify


class Collection(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

    @classmethod
    def get_default_collection(cls):
        try:
            return Collection.objects.get(slug="_defaut")
        except Collection.DoesNotExist:
            return cls.objects.create(name="Défaut", slug="_defaut")


class Task(models.Model):
    name = models.CharField(max_length=128)
    done = models.BooleanField(default=False)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
