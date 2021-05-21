from django.db import models

# Create your models here.
class teacher(models.Model):
    username = models.CharField(max_length = 255)
    category = models.CharField(max_length = 255)
    numb_of_subs = models.CharField(max_length = 255,null=True, blank=True)
    about = models.TextField()
    price1 = models.CharField(max_length = 255,null=True, blank=True)
    price2 = models.CharField(max_length = 255,null=True, blank=True)
    price3 = models.CharField(max_length = 255,null=True, blank=True)
    slug = models.CharField(max_length = 255,null=True, blank=True)
    usr_pic = models.CharField(max_length = 255,null=True, blank=True)

    def __str__(self):
        return '{}, {}'.format(self.id,self.username)