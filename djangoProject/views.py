from django.http import HttpResponse


def index(request):
    return HttpResponse("My Name is Anand")


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