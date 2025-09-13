from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from courses.models import FAQ, Course, ForPageCourse, Lesson, Quiz, Topic
from accounts.models import CustomUser
from payment.models import Purchase


def admin_required(view_func):
    decorated = login_required(user_passes_test(lambda u: u.is_superuser)(view_func))
    return decorated

@admin_required
def admin_dashboard(request):
    return render(request, "admin_panel/dashboard.html")

@admin_required
def admin_courses(request):
    courses = Course.objects.all()
    forcourse = ForPageCourse.objects.all()
    faq = FAQ.objects.all()
    return render(request, "admin_panel/courses.html", {"courses": courses,
                                                        "forcourse": forcourse,
                                                        "faq": faq})

@admin_required
def admin_topic(request):
    topic = Topic.objects.all()
    return render(request, "admin_panel/topic.html", {"topic": topic})

@admin_required
def admin_lessons(request):
    lessons = Lesson.objects.all()
    return render(request, "admin_panel/lessons.html", {"lessons": lessons})

@admin_required
def admin_quizzes(request):
    quizzes = Quiz.objects.all()
    return render(request, "admin_panel/quizzes.html", {"quizzes": quizzes})

@admin_required
def admin_payments(request):
    payments = Purchase.objects.all()
    return render(request, "admin_panel/payments.html", {"payments": payments})

@admin_required
def admin_users(request):
    users = CustomUser.objects.all()
    return render(request, "admin_panel/users.html", {"users": users})