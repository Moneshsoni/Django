#This file created by monesh soni
#This is lecture 7 Exercise
from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
#   return HttpResponse('''<h1>This is my favorate website  class number one </h1><a href="https://stackoverflow.com/questions/62967190/vuejs-rendering-lists"> World best query solving websitet        </a>''')
#def monesh(request):

#    return HttpResponse("Hi i am software engineer in Banglore city ")
#def tutor(request):
 #   return HttpResponse('''<h2>This is my second url of the website</h2><a href="https://www.tutorialspoint.com/index.htm">tutorial points </a>''')

def index(request):
    return render(request,"index.html")


def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)


    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")


#def capatilizefirst(request):
#    return HttpResponse("capatilizefirst page <a href='/'>back</a>")

#def newlineremove(request):
#    return HttpResponse("newlineremove page <a href='/'>back</a>")

#def spaceremove(request):
#    return HttpResponse("spaceremove page <a href='/'>back</a>")

#def charcount(request):
#    return HttpResponse("Character count page <a href='/'>back</a>")