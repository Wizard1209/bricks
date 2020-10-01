from django.db import models


class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=1024)
    year = models.CharField(max_length=10)


class History(models.Model):
    class Meta:
        ordering = ('date', )
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    bricks_num = models.IntegerField()
    date = models.DateField()
