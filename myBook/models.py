from django.db import models

# Create your models here.
class bookModel(models.Model):
    booktitle=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publish_date=models.DateField(null=True, blank=True) 
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField (auto_now=True)

def __str__(self):
    return self.booktitle
