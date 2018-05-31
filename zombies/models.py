from django.db import models


class Perk(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)


class Location(models.Model):
    description = models.TextField(default='')
    map = models.ForeignKey('zombies.Map', on_delete=models.CASCADE, default='')
    perk = models.ForeignKey(Perk, on_delete=models.CASCADE, default='')


class Map(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    perks = models.ManyToManyField(Perk, blank=True)

#
# class Map(models.Model):
#     id = models.CharField(max_length=100, primary_key=True)
#     name = models.CharField(max_length=200)
#
#
# class Location(models.Model):
#     name = models.CharField(max_length=200)
#
#
# class Perk(models.Model):
#     PERK_CHOICES = (('quick_revive',    'Quick Revive'),
#         ('juggernog',       'Juggernog'),
#         ('speed_cola',      'Speed Cola'),
#         ('double_tap',      'Double Tap Root Beer'),
#         ('phd_flopper',     'PhD Flopper'),
#         ('stamin_up',       'Stamin-Up'),
#         ('deadshot',        'Deadshot Daiquiri'),
#         ('mule_kick',       'Mule Kick'),
#         ('tombstone',       'Tombstone Soda'),
#         ('whos_who',        'Who\'s Who'),
#         ('electric_cherry', 'Electric Cherry'),
#         ('vulture_aid',     'Vulture Aid Elixir'),
#         ('widows_wine',     'Widow\'s Wine'))
#     name = models.CharField(max_length=200, choices=PERK_CHOICES, default=PERK_CHOICES[0])
#
#
# class PerkLocation(models.Model):
#     perk = models.ForeignKey('zombies.Perk', on_delete=models.CASCADE)
#     map = models.ForeignKey('zombies.Map', on_delete=models.CASCADE)
#     description = models.TextField(default='None')


class RandomFact(models.Model):
    description = models.TextField()


class Fact(models.Model):
    description = models.TextField()
    map = models.ForeignKey(Map, on_delete=models.CASCADE)


class GobbleGum(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=100)
