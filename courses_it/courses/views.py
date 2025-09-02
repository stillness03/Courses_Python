from rest_framework import viewsets, permissions
from .serializers import CourseSerializer, LessonSerializer, QuizSerializer, QuestionSerializer, AnswerSerializer
from .models import Course, Lesson, Quiz, Question, Answer, Topic
from django.shortcuts import get_object_or_404, render


class IsAdminOrReadOnly:
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
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



# HTML Views

def course_topics(request, course_id):
    topics = Topic.objects.filter(course_id=course_id).order_by('created_at')
    course = get_object_or_404(Course, id=course_id)
    total_lessons = Lesson.objects.filter(topic__course=course).count()

    return render(request, 'course_topics.html', {
        'course': course,
        'topics': topics,
        'total_lessons': total_lessons
    })

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    lesson_count = topic.lessons.count()

    course = topic.course
    total_lessons = Lesson.objects.filter(topic__course=course).count()

    return render(request, 'course_detail.html', {
        'topic': topic,
        'lesson_count': lesson_count,
        'total_lessons': total_lessons,
        'course': course
    })