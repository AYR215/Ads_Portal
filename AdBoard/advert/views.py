from django.shortcuts import render, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import *
from .forms import *
from .filters import ResponseFilter

from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст

from random import randint


class AdsList(ListView):
    model = Ad
    template_name = 'ads.html'
    context_object_name = 'adslist'
    queryset = Ad.objects.order_by('-id')
    paginate_by = 5


class AdsDetail(DetailView):
    model = Ad
    template_name = 'adsdetail.html'
    context_object_name = 'ads'


class AdsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'ads_add.html'
    form_class = AdsForm


class AdsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'ads_edit.html'
    form_class = AdsForm

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return Ad.objects.get(pk=pk)


class AdsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'ads_delete.html'
    queryset = Ad.objects.all()
    success_url = '/ads/'


class AuthorCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'author_add.html')

    def post(self, request, *args, **kwargs):
        authoruser = request.user
        name = request.POST['name']
        if not Author.objects.filter(name=name):  # проверка уникальности имени
            newauthor = Author(name=name, authorUser=authoruser)
            newauthor.save()
        else:
            raise ValueError('Name already used')
        return redirect('/personal/')


class ResponseList(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'personal.html'
    context_object_name = 'responselist'
    queryset = Response.objects.order_by('-id')
    paginate_by = 10

    def get_filter(self):
        return ResponseFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {**super().get_context_data(*args, **kwargs),
                'filter': self.get_filter(),
                }


class ResponseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'response_add.html'
    form_class = ResponseForm
    success_url = '/ads/'


class ResponseDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'response_delete.html'
    queryset = Response.objects.all()
    success_url = '/ads/'


class ResponseAcceptView(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        response = Response.objects.get(pk=pk)
        response.accept_response()
        return render(request, 'response_accept.html', {})
