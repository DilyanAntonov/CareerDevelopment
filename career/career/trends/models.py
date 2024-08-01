from django.db import models


class JobTrend(models.Model):
    programming_language = models.CharField(max_length=50)
    date = models.DateField()
    number_of_jobs = models.IntegerField()

    def __str__(self):
        return f"{self.programming_language} - {self.date} - {self.number_of_jobs} jobs"
