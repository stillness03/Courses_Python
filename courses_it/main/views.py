from django.shortcuts import render, get_object_or_404
from django.views import View
from courses.models import Course
from django.core.paginator import Paginator
from django.conf import settings

def popular_list(request):
    courses = Course.objects.filter()[:3]
    return render(request,
                  'main/index/index.html',
                  {
                      'courses': courses,
                      'is_index_page': True
                  })


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, "courses/course_detail.html", {"course": course})


#def course_list(request, category_slug=None):
#   page = request.GET.get('page', 1)

#   courses = Course.objects.filter()

#   if category_slug:
#         courses = courses.filter(category__slug=category_slug)

#   paginator = Paginator(courses, 10)
#   current_page = paginator.get_page(page)

#    return render(request,
#                 'main/course/list.html',
#                 {
#                     'category_slug': category_slug,
#                     'courses': current_page,
#                     'is_index_page': False
#                 })

def courses_new(request):
    courses = Course.objects.all()
    new_courses = Course.objects.order_by('-created_at')[:6]

    return render(request, "main/base.html", {
        "courses": courses,
        "new_courses": new_courses,
    })

# in future i addad it
# def stats_view(request):
#     students_count = Student.objects.count()
#     mentors_count = Mentor.objects.count()
#     courses_count = Course.objects.count()
#     completion_rate = 96  

#     return render(request, "stats.html", {
#         "students_count": students_count,
#         "mentors_count": mentors_count,
#         "courses_count": courses_count,
#         "completion_rate": completion_rate,
#     })

def about_us(request):
    return render(request, 'main/nav_link/about-us.html')

def cost_page(request):
    return render(request, 'main/nav_link/cost.html')

class CourseDetail(View):
    def get(self, request, slug):
        course = get_object_or_404(Course, slug=slug)

        forpagecourse = getattr(course, 'extended_info', None)

        topics = course.topics.all().order_by('created_at')
        total_lessons = course.lessons.count()
        avg_salary = "$2500"

        images_raw = settings.COURSE_CONTENT.get(slug, [])

        images = [
            {
                "file": f"{slug}/{img.get('file', '')}",
                "class": img.get("class", "")
            }
            for img in images_raw if img.get("file")
        ]

        return render(request, 'courses/course_detail.html', {
            'course': course,
            'images': images,
            'topics': topics,
            'forpagecourse': forpagecourse,
            'total_lessons': total_lessons,
            'avg_salary': avg_salary
        })