from .models import Links

def links_processor(request):
    return {
        'links': Links.objects.all()
    }
