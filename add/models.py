from django.db import models

class Items(models.Model):
    name = models.CharField(max_length = 35)
    price = models.IntegerField()
    exp_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Items'
