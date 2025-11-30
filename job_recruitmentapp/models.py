from django.db import models

# Create your models here. 

class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    job_position = models.CharField(max_length=100)
    slots = models.IntegerField()
    status = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title