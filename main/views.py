from django.views.generic import TemplateView
from django.shortcuts import render
from accounts.models import Router,FileRouter
from datetime import datetime
import os
class IndexPageView(TemplateView):
    template_name = 'main/index.html'

def test_form(request):
    info = FileRouter.objects.all()
    return render(request, "main/index.html",{"info":info})

def test_form1(request):
    info = FileRouter.objects.all()
    for i in info:
        print("INFO -----------------------> ",i.specifications)
    if request.method == "POST":
        user = request.POST.get('username')
        if user in ["+998973873723","+998998887766","+998977776655"]:
            ffmpegCommand = """ffmpeg -y -i content/media/router_specifications/21/input1.mp4 -preset ultrafast -vf drawtext="fontsize=15:fontcolor=black@0.2: box=1: boxcolor=white@0.1:fontfile=/Windows/Fonts/arial.ttf:text='{}':x=if(eq(mod(n\\,1200)\\,0)\\,rand(0\\,(w-text_w))\\,x):y=if(eq(mod(n\\,1200)\\,0)\\,rand(0\\,(h-text_h))\\,y):enable=lt(mod(n\\,1200)\\,100),drawtext=text='{}': x=(w-text_w)/2:y=(h-text_h)/2: fontsize=215:fontcolor=black@0.2: box=1: boxcolor=white@0.1 :y=if(eq(mod(n\\,1200)\\,0)\\,rand(0\\,(h-text_h))\\,y):enable=lt(mod(n\\,1200)\\,1100)" -c:v libx264 -crf 24 -c:a copy content/media/router_specifications/21/output1.mp4"""
            f = open("usersLog.txt", "a")
            f.write(str(datetime.now()) + " " + str(user) + "\n")
            f.close()
            render(request, "main/index.html",{"info":info})
            a = True
            print("-------+++++--------:    ",a)
            os.system(ffmpegCommand.format(user[4:],user[4:]))
            a = False
            print("-------+++++--------:    ",a)
            return render(request,"main/video.html")
        else:
            return render(request, "main/index11.html")
def test_video(request):
    return render(request, "main/video.html")
class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
