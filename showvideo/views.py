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
    Comment.objects.create(text=request.POST["com"], comment_video_id=id)
    print(request.POST["pwd"])
    return redirect("main_page")


def one_video(request, id):
    response = {"video":Video.objects.get(id=id)}
    return render(request, "one_video.html", response)


def add_like(request, id):
    video = Video.objects.get(id=id)
    video.likes += 2
    video.save()
    return redirect("main_page")


def ajax_like(request):
    id = request.GET["id"]
    video = Video.objects.get(id=id)
    video.likes += 1
    video.save()
    return HttpResponse(video.likes)
