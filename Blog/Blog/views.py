from django.http import HttpResponse

def index(request):
    return HttpResponse("Root Dir's View...")