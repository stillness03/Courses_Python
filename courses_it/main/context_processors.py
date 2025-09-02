from courses.models import Course

def courses_processor(request):
    return {
        'all_courses': Course.objects.all(),
        'new_courses': Course.objects.order_by('-created_at')[:5],
    }