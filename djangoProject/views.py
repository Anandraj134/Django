from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return HttpResponse("This is about page")


def ex1(request):
    return HttpResponse("""
    <h1>Click Below Links to listen your favorite song</h1>
    <a href="https://www.youtube.com/watch?v=ZIihoTi4pzI"> Rasiya from Brahmastra </a><br>
    <a href="https://www.youtube.com/watch?v=aDFEb_W2t1Y"> Pal from Jaledi </a><br>
    <a href="https://www.youtube.com/watch?v=OljkSVLIt6c"> Saturday Saturday From Humpty Sharma ki Dulhaniya </a><br>
    <a href="https://www.youtube.com/watch?v=SOessajf_Ik"> Baatein Ye Kabhi Na from Khamoshiyan </a><br>
    <a href="https://www.youtube.com/watch?v=GLGuLXKT9Ng"> Raataan Lambiyan from Shershaah </a><br>
    """)


def analyze(request):
    djtext = request.GET.get('text', 'default')
    remove = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    lowercaps = request.GET.get('lowercaps', 'off')
    extraspace = request.GET.get('extraspace', 'off')
    newline = request.GET.get('newline', 'off')

    analyzed = ""
    punc = """!()-{}[];:'"\,<>./?@#$%^&*_~"""
    if remove == 'on':
        for i in djtext:
            if i not in punc:
                analyzed += i
    elif fullcaps == 'on':
        analyzed = str(djtext).upper()
    elif lowercaps == 'on':
        analyzed = str(djtext).lower()
    elif extraspace == 'on':
        for i in range(len(djtext)):
            if djtext[i] == ' ' and djtext[i+1] == ' ':
                pass
            else:
                analyzed += djtext[i]
    elif newline == 'on':
        for i in djtext:
            if i != "\n":
                analyzed += i
    else:
        analyzed = "You haven't checked the checkbox"
    params = {
        'purpose': 'Removed Punctuations',
        'analyzed_text': analyzed
    }
    return render(request, 'analyze.html', params)


def textanalyzer(request):
    return HttpResponse("Text Analyzer")


def removepunc(request):
    return HttpResponse("Text Analyzer")
