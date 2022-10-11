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
    analyzed = ""
    punc = """!()-{}[];:'"\,<>./?@#$%^&*_~"""
    if remove == 'on':
        for i in djtext:
            if i not in punc:
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
