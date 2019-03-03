from django.db import models


# Create your models here.


class student_class(models.Model):
    name = models.CharField(primary_key=True, max_length=10)

    def __str__(self):
        return self.name


class user(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=6)
    pwd = models.CharField(max_length=20)
    stu_class = models.ForeignKey(student_class, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=3, choices=(
        ('s', '班级'),
        ('m', '年级会'),
        ('t', '辅导员')
    ))

    def __str__(self):
        return str(self.name) + '(' + str(self.id) + ')'


class item(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    date = models.DateField()
    number = models.IntegerField()
    others = models.TextField(max_length=200, null=True, blank=True)
