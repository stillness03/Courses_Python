from django.db import models
from django.conf import settings

class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="purchases")
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name="purchases")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=255, unique=True) 
    status = models.CharField(max_length=20, default="pending")  # pending, success, failed
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    
    def __str__(self):
        return f"{self.user.username} - {self.course.title} ({self.status})"
