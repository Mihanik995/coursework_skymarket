from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Ad(models.Model):
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000, **NULLABLE)
    image = models.ImageField(upload_to='ads/', **NULLABLE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, **NULLABLE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'ad'
        verbose_name_plural = 'ads'


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, **NULLABLE)
    ad = models.ForeignKey(to=Ad, on_delete=models.CASCADE, **NULLABLE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
