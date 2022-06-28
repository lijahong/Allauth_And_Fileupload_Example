from django.db import models

# Create your models here.

class board(models.Model):
    title = models.TextField()
    contents = models.TextField()


class PostImage(models.Model):
    image = models.ImageField(upload_to= 'images/', null=True, blank =True)
    post = models.ForeignKey(board, on_delete=models.CASCADE)

