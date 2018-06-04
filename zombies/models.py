from django.utils.timezone import now

from django.db import models


class Map(models.Model):
    map_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField(default=now())

    def __str__(self):
        return self.name


class Perk(models.Model):
    perk_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    location = models.TextField(null=True)
    map = models.ForeignKey('zombies.Map', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('map', 'perk_id')

    def __str__(self):
        return self.name


class RandomFact(models.Model):
    description = models.TextField()


class MapFact(models.Model):
    description = models.TextField()
    map = models.ForeignKey(Map, on_delete=models.CASCADE)


class GobbleGum(models.Model):
    gobblegum_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=(
        ('mega_common', 'Mega Common'),
        ('whimsical', 'Whimsical'),
        ('classic', 'Classic'),
        ('mega_rare', 'Mega rare'),
        ('mega_ultra_rare', 'Mega ultra rare'),
    ))
