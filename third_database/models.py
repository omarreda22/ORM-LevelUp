from django.db import models



class ThirdModel(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name
    

class ThirdModelMore(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name
    