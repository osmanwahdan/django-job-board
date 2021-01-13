from django.db import models

# Create your models here.


class Job(models.Model):
    JOB_TYPE = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]


    title = models.CharField(max_length=100)
    job_tybe = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experince = models.IntegerField(default=1)


    def __str__(self):
        return self.title