from django.db import models


# Inheritance  -> Abstract

class Student(models.Model):
    name = models.CharField(max_length=125)
    age = models.IntegerField(default=6)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['-name']


class ItemA(Student):
    class_number = models.IntegerField()

    def __str__(self):
        return self.class_number

    class Meta(Student.Meta):
        ordering = ['class_number']


class ItemB(Student):
    class_number_student = models.IntegerField()

    def __str__(self):
        return self.class_number_student

    class Meta(Student.Meta):
        ordering = ['class_number_student']


# ------------------------------------------------------------------------------------------

# Inheritance  -> multi-table model Inheritance

class StudentMultiTable(models.Model):
    name = models.CharField(max_length=125, blank=True, null=True)
    age = models.IntegerField(default=6, blank=True, null=True)

    def __str__(self):
        return self.name


class MultiTable(StudentMultiTable):
    new_name = models.CharField(max_length=125, blank=True, null=True)

    def __str__(self):
        return self.age
