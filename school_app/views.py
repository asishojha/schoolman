from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login
from .models import Student,Attendance,ClassSection,Subject,Teacher
from .forms import StudentForm,AttendanceForm
import datetime

def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    if request.method == 'POST':
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.email = request.POST.get('email')
        teacher.phone_number = request.POST.get('phone_number')
        subjects = request.POST.getlist('subjects')
        teacher.subjects.set(subjects)
        teacher.save()
        return redirect('teacher_list')

    subjects = Subject.objects.all()
    return render(request, 'edit_teacher.html', {'teacher': teacher, 'subjects': subjects})

def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')

    return render(request, 'delete_teacher.html', {'teacher': teacher})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        subjects = request.POST.getlist('subjects')  # Get selected subjects as a list
        teacher = Teacher.objects.create(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number)
        teacher.subjects.set(subjects)  # Associate selected subjects with the teacher
        return redirect('teacher_list')

    subjects = Subject.objects.all()
    return render(request, 'add_teacher.html', {'subjects': subjects})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

def add_subject(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Subject.objects.create(name=name)
        return redirect('subject_list')

    return render(request, 'add_subject.html')

def mark_attendance(request):
    class_sections = ClassSection.objects.all()
    selected_class = request.GET.get('class')
    selected_section = request.GET.get('section')

    if selected_class and selected_section:
        students = Student.objects.filter(classes_sections__class_name=selected_class, classes_sections__section=selected_section)
    else:
        students = Student.objects.all()

    # Get today's date
    today_date = datetime.date.today()

    if request.method == 'POST':
        for student in students:
            attendance_status = request.POST.get(str(student.id))
            Attendance.objects.create(
                student=student,
                date=today_date,
                status=attendance_status
            )

    context = {
        'students': students,
        'class_sections': class_sections,
        'selected_class': selected_class,
        'selected_section': selected_section,
        'today_date': today_date,
    }

    return render(request, 'mark_attendance.html', context)

def student_list(request):
    class_sections = ClassSection.objects.all()

    selected_class = request.GET.get('class')
    selected_section = request.GET.get('section')

    if selected_class and selected_section:
        students = Student.objects.filter(classes_sections__class_name=selected_class, classes_sections__section=selected_section)
    else:
        students = Student.objects.all()

    context = {
        'students': students,
        'class_sections': class_sections,
        'selected_class': selected_class,
        'selected_section': selected_section,
    }

    return render(request, 'student_list.html', context)

def student_profile(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'student_profile.html', {'student': student})

def edit_student_profile(request, student_id):
    # Get the student object based on the student_id
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        # If the form has been submitted, process the data
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            # Redirect to the student profile page after successful form submission
            return redirect('student_profile', student_id=student_id)
    else:
        # If the request method is GET, display the form with the current student data
        form = StudentForm(instance=student)

    return render(request, 'edit_student_profile.html', {'form': form, 'student': student})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to the student list after successful form submission
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})
def home(request):
    # Add any context data you want to pass to the home template
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            # The user is valid. Log in the user.
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard URL

        else:
            # Invalid login credentials. Add an error message to display on the login form.
            error_message = 'Invalid username or password. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})

    # If the request method is GET, simply render the login template.
    return render(request, 'login.html')

def dashboard(request):
    # Add any context data you want to pass to the dashboard template
    return render(request, 'dashboard.html')