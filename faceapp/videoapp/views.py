from django.shortcuts import render, redirect
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Video
from .forms import VideoForm
from .serializers import FaceplusAPISerializer
from .utils import faceplusplus

def home(request):
    video = Video.objects.all()
    #print (video[0].file)
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


class FacePlusAPIView(APIView):
    renderer_classes = (JSONRenderer,)

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        serializer = FaceplusAPISerializer(data=request.data)
        if serializer.is_valid():
            path = serializer.data['path']
            api_res = faceplusplus(path)
            
            status_dict = dict()
            status_dict["code"] = 200
            status_dict["error"] = {}
            status_dict["message"] = "Success"

            data_dict = dict()
            data_dict["faceplus_res"] = api_res
            return Response({"status": status_dict, "data": data_dict}, status=status.HTTP_200_OK)

        else:
            status_dict = dict()
            status_dict["code"] = 400
            status_dict["error"] = serializer.errors
            status_dict["message"] = "Bad Request"
            return Response({"status": status_dict, "data": {}}, status=status.HTTP_400_BAD_REQUEST)