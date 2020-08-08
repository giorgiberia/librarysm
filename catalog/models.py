from django.db import models


STATUS_CHOICES = (
    (1, "in library"),
    (2, "taken")
)

class Author (models.Model):
    id=models.IntegerField(primary_key=True,null=False)
    name=models.CharField(max_length=255)
  
    def __str__(self):
        return self.name



class Book (models.Model):
    id=models.IntegerField(primary_key=True,null=False)
    name=models.CharField(max_length=255)
    author=models.ForeignKey(Author,db_column="author_id",on_delete=models.CASCADE)
    status=models.IntegerField(choices=STATUS_CHOICES,default=1)
    takenBy=models.CharField(max_length=255)
    taken_at=models.DateTimeField(null=True,blank=True)
    returned_at=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name

