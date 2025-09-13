from django.shortcuts import render, get_object_or_404
from courses.models import Course
from django.core.paginator import Paginator

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

def about_us(request):
    return render(request, 'main/nav_link/about-us.html')

def cost_page(request):
    return render(request, 'main/nav_link/cost.html')