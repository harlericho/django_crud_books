from django.db import models
import uuid
# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title