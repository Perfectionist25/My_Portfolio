from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import *

def index(request):
    iam = Iam.objects.all()
    work = Work.objects.all()
    paginator = Paginator(work, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    carousel = Carousel.objects.all()
    return render(request, 'portfolio/index.html', {
    'iam': iam,
    'work': page_obj.object_list,
    'carousel': carousel,
    'page_obj': page_obj
})


def about(request):
    iam = Iam.objects.all()
    return render(request, 'portfolio/about.html', {
        'iam': iam
    })


def work_detail_json(request, pk):
    try:
        work = Work.objects.get(pk=pk)
        return JsonResponse({
            'title': work.title,
            'description': work.description,
            'image': work.image.url,
        })
    except Work.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)
