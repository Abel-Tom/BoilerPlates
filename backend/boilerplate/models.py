from django.db import models
from django.contrib.auth.models import User

class Basetable(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_createdby')
    is_trashed = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def trash(self):
        self.is_trashed = True
        self.save(update_fields=['is_trashed'])

    def restore(self):
        self.is_trashed = False
        self.save(update_fields=['is_trashed'])
        

class Something(Basetable):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


from django.contrib.auth.models import User


        

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_createdby')

    def __str__(self):
        return self.title
