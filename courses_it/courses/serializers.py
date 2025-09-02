from rest_framework import serializers
from .models import Course, Lesson, Quiz, Question, Answer, Topic

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "text", "is_correct"]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "text", "answers"]


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    lesson_title = serializers.CharField(source="lesson.title", read_only=True)

    class Meta:
        model = Quiz
        fields = ["id", "title", "lesson", "lesson_title", "questions"]


class LessonSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ["id", "title", "content", "order", "quizzes", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class TopicSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ["id", "title", "content", "lessons", "created_at", "updated_at"]


class CourseSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True, source="topic")

    class Meta:
        model = Course
        fields = [
            "id", "title", "description", "type_course",
            "tags", "price", "duration",
            "topics", "created_at", "updated_at"
        ]
        read_only_fields = ["created_at", "updated_at"]