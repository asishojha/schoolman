from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),  # Add this URL pattern for adding a student
    path('students/<int:student_id>/', views.student_profile, name='student_profile'),
    path('students/<int:student_id>/edit/', views.edit_student_profile, name='edit_student_profile'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/add/', views.add_subject, name='add_subject'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('teachers/<int:teacher_id>/edit/', views.edit_teacher, name='edit_teacher'),
    path('teachers/<int:teacher_id>/delete/', views.delete_teacher, name='delete_teacher'),
    # Add more URL patterns for other views if needed
]
