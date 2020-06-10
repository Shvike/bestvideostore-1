from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video, Comment


def hello(request):
    return HttpResponse("<h1>hello world</h1>")


def world(request):
    response = {"name":"Bogdan", "d":34, "arr":[1,2,3,4,5]}
    response["content"] = Video.objects.all()
    return render(request, "index.html", response)


def accept_comment(request, id):
    # 1
    Comment.objects.create(text=request.GET["com"], comment_video_id=id)
    # 2
    # video = Video.objects.get(id=id)
    # Comment.objects.create(text="hello world", comment_video=video)
    # 3
    # c = Comment(text=request.GET['com'], comment_video_id=id)
    # c.save()
    # print(id)
    # print(request.GET["com"])
    return redirect("main_page")


def one_video(request, id):
    response = {"video":Video.objects.get(id=id)}
    return render(request, "one_video.html", response)