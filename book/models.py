from django.db import models
class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30, default="book")
    email = models.EmailField(blank = True)
    describe = models.TextField(default ="book")

    def __str__(self):
        return self.name
