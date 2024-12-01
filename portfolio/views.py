from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from .models import Portfolio,Blog
from django.views.generic.edit import FormView
from .bot import send_message
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse
from .models import Contact

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        content = form.cleaned_data.get('content')
        Contact.objects.create(name=name, email=email, content=content)
        text = f"Name: {name}\nEmail: {email}\nText: {content}"
        send_message(text)
        return super().form_valid(form)


class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio.html'
    context_object_name = "portfolios"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Portfolio.objects.all()
        return context


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'project.html'
    context_object_name = "portfolio"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio_pk = self.kwargs.get('pk')
        context['portfolios'] = Portfolio.objects.filter(pk=portfolio_pk)
        return context

    
class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = "blogs"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        # blogs = Blog.objects.all()

        return context
    

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'publication.html'
    context_object_name = "blog"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_pk = self.kwargs.get('pk')
        context['blogs'] = Blog.objects.filter(pk=blog_pk)
        return context
    


def home1_view(request):
    return render(request,'home-1.html')

def home2_view(request):
    return render(request,'home-2.html')


def service_view(request):
    return render(request,'service.html')

def error_view(request):
    return render(request,'404.html')