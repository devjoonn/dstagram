from django.shortcuts import render, redirect
from .models import Photo
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required()
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos': photos})

class PhotoUploadView(LoginRequiredMixin,CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id  # authro_id: foreign key의 경우 _id suffix가 자동으로 붙는다.
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})


class PhotoDeleteView(LoginRequiredMixin,DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'


class PhotoUpdateView(LoginRequiredMixin,UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo/detail.html'
