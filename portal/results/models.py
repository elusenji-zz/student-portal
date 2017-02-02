from __future__ import unicode_literals

from django.db import models


class Results(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    surname = models.CharField(max_length=21, blank=True, null=True)
    othernames = models.CharField(max_length=22, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    nationality = models.CharField(max_length=14, blank=True, null=True)
    program = models.CharField(max_length=69, blank=True, null=True)
    regnumber = models.CharField(max_length=18, blank=True, null=True)
    entrymode = models.CharField(max_length=14, blank=True, null=True)
    doe = models.CharField(max_length=18, blank=True, null=True)
    dob = models.CharField(max_length=19, blank=True, null=True)
    academicyear = models.CharField(max_length=9, blank=True, null=True)
    examperiod = models.CharField(max_length=14, blank=True, null=True)
    coursecode = models.CharField(max_length=49, blank=True, null=True)
    coursename = models.CharField(max_length=89, blank=True, null=True)
    coursework = models.CharField(max_length=4, blank=True, null=True)
    exam = models.CharField(max_length=4, blank=True, null=True)
    programcode = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'results'

    def __str__(self):
    	return self.regnumber