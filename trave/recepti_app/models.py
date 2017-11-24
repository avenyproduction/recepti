from django.db import models

#Create your models here.
class Problem(models.Model):
    problem = models.CharField(max_length=256)

    def __str__(self):
        return self.problem


class Recepti(models.Model):
    probl = models.ManyToManyField(Problem, through='Trava')
    recepti = models.TextField()

    def __str__(self):
        return self.recepti

class Trava(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    rec = models.ForeignKey(Recepti, on_delete=models.CASCADE)
    trava = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='trave')

    def __str__(self):
        return self.trava
