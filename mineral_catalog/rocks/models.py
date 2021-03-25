from django.db import models


# Create your models here.
class Rock(models.Model):
    name = models.CharField(max_length=255)
    category = models.TextField(blank=True, default='')
    formula = models.TextField(blank=True, default='')
    strunz_classification = models.TextField(blank=True, default='')
    unit_cell = models.TextField(blank=True, default='')
    color = models.TextField(blank=True, default='')
    crystal_system = models.TextField(blank=True, default='')
    crystal_symmetry = models.TextField(blank=True, default='')
    cleavage = models.TextField(blank=True, default='')
    mohs_scale_hardness = models.TextField(blank=True, default='')
    luster = models.TextField(blank=True, default='')
    streak = models.TextField(blank=True, default='')
    diaphaneity = models.TextField(blank=True, default='')
    optical_properties = models.TextField(blank=True, default='')
    refractive_index = models.TextField(blank=True, default='')
    crystal_habit = models.TextField(blank=True, default='')
    specific_gravity = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name


# class RockDetail(models.Model):
#     category = models.CharField(max_length=255)
#     formula = models.CharField(max_length=255)
#     strunz_classification = models.CharField(max_length=255)
#     unit_cell = models.CharField(max_length=255)
#     color = models.CharField(max_length=255)
#     crystal_symmetry = models.CharField(max_length=255)
#     mohs_scale_hardness = models.IntegerField()
#     name = models.OneToOneField(Rock, on_delete=models.CASCADE)



