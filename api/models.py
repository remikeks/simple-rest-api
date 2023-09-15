from django.db import models

# Create your models here.
class Person(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return  self.name