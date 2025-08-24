from rest_framework import serializers
from .models import Course, Lesson, Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'question', 'answer']

class LessonSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, read_only=True)  # related_name='quizzes'

    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'content', 'quizzes', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)  # related_name='lessons'

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'lessons', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
