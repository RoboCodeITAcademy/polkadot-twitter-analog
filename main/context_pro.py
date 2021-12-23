from .models import Category , Tag ,Like

def view_all(request):
    context = {
        "tags":Tag.objects.all(),
        "categories":Category.objects.all(),
        "like":Like.objects.all()
    }
    return context 