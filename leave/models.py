from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

TIME_CHOICES = (
    ( 0, '오전'),
    ( 1, '오후'),
)

class Employee(models.Model):
    name = models.CharField(max_length=10)
    employed_date = models.DateField()
    givenLeave = models.DecimalField(default=15, max_digits=3, decimal_places=1,
    validators = [MinValueValidator(0.0), MaxValueValidator(50)])
    usedLeave = models.DecimalField(default=0, max_digits=3, decimal_places=1,
    validators = [MinValueValidator(0.0), MaxValueValidator(50)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Leave(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    startDate = models.DateField()
    startTime = models.PositiveSmallIntegerField(choices=TIME_CHOICES)
    endDate = models.DateField()
    endTime = models.PositiveSmallIntegerField(choices=TIME_CHOICES)
    briefs = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.briefs

'''
class Choice(models.Model):
    poll = models.ForeignKey('Poll', on_delete = models.CASCADE)
    candidate = models.ForeignKey('Candidate', on_delete = models.CASCADE)
    votes = models.IntegerField(default=0)
'''
