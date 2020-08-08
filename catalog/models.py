from django.db import models


class Author (models.Model):
    id=models.IntegerField(primary_key=True,null=False)
    name=models.CharField(max_length=255)
  
    def __str__(self):
        return self.name



class Book (models.Model):
    id=models.IntegerField(primary_key=True,null=False)
    name=models.CharField(max_length=255)
    author=models.OneToOneField(Author,db_column="author_id",on_delete=models.CASCADE)
    status=models.IntegerField()
    takenBy=models.CharField(max_length=255)
    taken_at=models.DateTimeField(null=True)
    returned_at=models.DateTimeField(null=True)

    def __str__(self):
        return self.name

