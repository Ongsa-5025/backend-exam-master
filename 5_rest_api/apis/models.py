from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=500)
    school_short_name = models.CharField(max_length=500)
    address = models.TextField(max_length=1000)

    def __nonzero__(self):
        return str(self.id)
    
    def __str__(self):
        return str(self.school_name)

class ClassRoom(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    grade = models.IntegerField(default=0)
    room = models.IntegerField(default=0)

    def __nonzero__(self):
        return str(self.id)
    
    def __str__(self):
        return str(self.school_id.school_name) + " " + str(self.grade) + " / " + str(self.room)
    
class Teacher(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    class_id = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    gender = models.CharField(max_length=500)

    def __nonzero__(self):
        return str(self.id)
    
    def __str__(self):
        return str(self.first_name + " " + self.last_name)

class Student(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    class_id = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    gender = models.CharField(max_length=500)

    def __nonzero__(self):
        return str(self.id)
    
    def __str__(self):
        return str(self.first_name + " " + self.last_name)