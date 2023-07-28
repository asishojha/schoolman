from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50)  # 'student', 'teacher', 'parent', 'admin', etc.

class ClassSection(models.Model):
    class_name = models.CharField(max_length=100, null=True)
    section = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"{self.class_name} - Section {self.section}"

class Student(models.Model):
    first_name = models.CharField(max_length=100, null=True)  # Add a default value (an empty string in this case)
    last_name = models.CharField(max_length=100, null=True)
    roll_number = models.CharField(max_length=10, null=True)
    date_of_birth = models.DateField(null=True)
    address = models.TextField(null=True)
    classes_sections = models.ManyToManyField(ClassSection, related_name='students')

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add more fields specific to parents/guardians



class Subject(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} "
    # Add more fields specific to subjects

class Teacher(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    subjects = models.ManyToManyField(Subject, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    # Add more fields specific to teachers

class Class(models.Model):
    name = models.CharField(max_length=20, unique=True)
    section = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student)
    # Add more fields specific to classes

class Attendance(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)  # 'present', 'absent', etc.

class Exam(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    # Add more fields specific to exams

class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    # Add more fields specific to exam results

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    # Add more fields specific to assignments/homework

class Timetable(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)
    period = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # Add more fields specific to timetable

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    # Add more fields specific to events

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(max_length=20)  # 'paid', 'pending', etc.
    # Add more fields specific to fee management

class Library(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    # Add more fields specific to library management

class Transport(models.Model):
    route_name = models.CharField(max_length=100)
    stops = models.TextField()
    # Add more fields specific to school transportation

class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # Add more fields specific to notices/communications
