from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Link(models.Model):
    url = models.URLField()
    category = models.ForeignKey(Category, related_name='links', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        if len(self.url) < 20:
            return self.url
        else:
            return self.url[:17] + "..."
