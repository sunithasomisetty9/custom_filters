from django.shortcuts import render

# Create your views here.
def usdf(request):
    d={'data':'Hi SuniTha  how  are  you','fruits':'orange apple guava pomegranete pineapple'}
    return render(request,'usdf.html',d)