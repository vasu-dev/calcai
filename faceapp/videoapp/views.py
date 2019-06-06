from django.shortcuts import render, redirect
from django.conf import settings

from .models import Video
from .forms import VideoForm

def home(request):
    video = Video.objects.all()
    return render(request, 'videoapp/home.html', { 'video': video })

def video_form(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'videoapp/video_form.html', {
        'form': form
    })