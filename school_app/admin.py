from django.contrib import admin
from .models import Student, ClassSection, Attendance, Exam, ExamResult, Assignment, Timetable, Event, Fee, Library, Transport, Notice

# Register your models here.
admin.site.register(Student)
admin.site.register(ClassSection)
admin.site.register(Attendance)
admin.site.register(Exam)
admin.site.register(ExamResult)
admin.site.register(Assignment)
admin.site.register(Timetable)
admin.site.register(Event)
admin.site.register(Fee)
admin.site.register(Library)
admin.site.register(Transport)
admin.site.register(Notice)
