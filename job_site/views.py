from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Person
from .forms import PersonForm
from django.http import HttpResponse

class JobLV(ListView):
    model = Person

class JobDV(DetailView):
    model = Person

def image_upload_view(request):
    # GET 방식으로 들어오면 입력 폼을 보내주고
    if request.method == 'GET':
        form = PersonForm()
        context = {'form': form }
        return render(request, 'job/data_write.html', context)
    # POST 방식으로 들어오면 저장하기
    elif request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lion:index')
        else:
            return HttpResponse("문제가 있네요.")