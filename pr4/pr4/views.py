from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Home")
    return render(request,'index.html')

# def removepunc(request):
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("remove Punc")

# def capfirst(request):
#     return HttpResponse("capitaliZe First")

# def newlineremove(request):
#     return HttpResponse("New line removal")

# def spaceremove(request):
#     return HttpResponse("Space Remover")

# def charcount(request):
#     return HttpResponse("character count")

def ex1(request):
    sites = ['''<h1>For Entertainment  </h1> <a href="https://www.youtube.com/"> Youtube Videos</a> ''',
             '''<h1>For Interaction  </h1> <a href="https://www.facebook.com/"> Facebook</a> ''',
             '''<h1>For Insight  </h1> <a href="https://www.ted.com/talks"> Ted Talks</a> ''',
             '''<h1>For Internship  </h1> <a href="https://www.internshala.com">Internship</a> ''']
    return HttpResponse((sites))

def analyze(request):

    # Get the text
    djtext = request.POST.get('text', 'default')
    
    # check the checkboxvalue
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')


    if removepunc=="on":
        punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""

        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        params= {'purpose':'Removed Punctuation','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    
    if (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        
        params={'purpose':'Changed to UpperCase','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    
    if (extraspaceremover=="on"):
        analyzed=""

        for index,char in enumerate(djtext):
            if not (djtext[index]==" "  and djtext[index+1]==" "):
                analyzed=analyzed+char

        params={'purpose':'Removed ExtraSpaces','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    
    if (newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char != "\n":
                analyzed=analyzed+char
        params={'purpose':"New Line Removal",'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if (removepunc !="on" and newlineremover!="on" and extraspaceremover != "on" and fullcaps !="on"):
        return HttpResponse("Please select any operation and try again")
    
    return render(request,'analyze.html',params)
    
    