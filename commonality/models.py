from django.db import models

class TypeOfNeed(models.Model):
    type_of_need = models.CharField(max_length=200)

    def __str__(self):
        return self.type_of_need

class Need(models.Model):
    type_of_need = models.ForeignKey(TypeOfNeed)
    title = models.CharField(max_length=200)
    description = models.TextField()
    need_expires = models.DateTimeField()

    def __str__(self):
        return self.title