from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 255, unique = True)
    userpass = models.CharField(max_length = 255)
    useremail = models.CharField(max_length = 255,unique = True)

class Place(models.Model):
    placename = models.CharField(max_length = 255, unique = True)
    country = models.CharField(max_length = 255, null=True)

class Test(models.Model):#аналог поста
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    place = models.ForeignKey(Place,on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default = 0)
    def __str__(self):
        return self.title

class Photo(models.Model):
    post = models.ForeignKey(Test, on_delete=models.CASCADE)
    picname = models.CharField(max_length = 255)