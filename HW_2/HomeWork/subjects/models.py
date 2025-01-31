from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} (Преподаватель: {self.author})"