from django.http import HttpResponse

def index(request):
    return HttpResponse('''Harry django CodeWithHarry''')

def about(request):
    return HttpResponse("About HarryBhai")

