from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet, 
    LessonViewSet, 
    QuizViewSet, 
    QuestionViewSet, 
    AnswerViewSet,
    TopicViewSet
)

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'topic', TopicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]