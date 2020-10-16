from django.shortcuts import render


# Create your views here.

# render image upload page
def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'image-process/input.html')