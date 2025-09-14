from rest_framework import viewsets, permissions
from django.views import View
from .serializers import CourseSerializer, FAQSerializer, ForPageCourseSerializer, LessonSerializer, QuizSerializer, QuestionSerializer, AnswerSerializer, TopicSerializer
from .models import FAQ, Course, Lesson, Quiz, Question, Answer, Topic, ForPageCourse
from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class ForPageCourseViewSet(viewsets.ModelViewSet):
    queryset = ForPageCourse.objects.all()
    serializer_class = ForPageCourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]


# HTML Views
class CourseDetail(View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)

        forpagecourse = getattr(course, 'extended_info', None)

        topics = course.topics.all().order_by('created_at')
        print(topics)
        total_lessons = course.lessons.count()

        avg_salary = "$2500"

        return render(request, 'courses/course_detail.html', {
            'course': course,
            'topics': topics,
            'forpagecourse': forpagecourse,
            'total_lessons': total_lessons,
            'avg_salary': avg_salary
        })