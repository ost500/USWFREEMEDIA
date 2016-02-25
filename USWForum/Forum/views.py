import datetime

from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from Forum import models
from Forum.models import Article, Category

from .forms import InsertForm


# from Forum.models import Article, Author, Publisher
class HomeView(ListView, FormView):
    
    template_name = 'Articles/newspeed_list.html'
    success_url = '/forum/'
    form_class = InsertForm
     
    context_object_name = 'object_list'
     
    def get_queryset(self):
        a=Article.objects.all().order_by('publication_date')[:7]
        return a
     
#     def form_valid(self, form):
#         form.submitted(self.request)
#         new_name = form.cleaned_data['title']
#         new2_name = form.cleaned_data['content']
#         new3_name = form.cleaned_data['author']
#         text1 = Article(title = new_name,content = new2_name
#                         ,authors = new3_name,publication_date= datetime.datetime.now())
#         text1.save()
#         return super(HomeView, self).form_valid(form)
    
class CategoryView(ListView):
    template_name = 'Category/list/category_list.html'
    model = Article
    
    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['object_list']=Category.objects.all().order_by('id')
        context['new_list']=Article.objects.all().order_by('publication_date')[:7]
        return context
class EachCateView(ListView):
    template_name ='Category/list/eachcate_list.html'
    model = Article
    
    def get_context_data(self, **kwargs):
        
        context = super(EachCateView, self).get_context_data(**kwargs)
        context['object_list'] = Article.objects.filter(category=self.args[0])
        context['new_list'] = Article.objects.filter(category=self.args[0])
        print(self.args[0])
        return context

class ArticleView(DetailView):
    template_name ='Category/list/article_detail.html'
    model = Article
    
    def get_object(self):
        return get_object_or_404(Article, pk=self.args[0])
    
    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['object'] = Article.objects.filter(id=self.args[0])
        context['new_list']=Article.objects.all().order_by('publication_date')[:7]
        print(context['object'])
        return context    

class NewView(ListView):
    template_name ='Category/list/new_list.html'
    model = Article
    
    
    def get_context_data(self, **kwargs):
        context = super(NewView, self).get_context_data(**kwargs)
        context['object_list'] = Article.objects.all().order_by('publication_date')[:7]
        return context
    
    
     
    
    
    
#     def get_queryset(self):
#         cate = self.kwargs['cate']       
    
#     def get_queryset(self):
#         return Article.objects.all()

# class InsertFormView(FormView):
#     template_name = 'insert.html'
#     success_url = '/forum/'
#     form_class = InsertForm
#     
#     def form_valid(self, form):
#         form.submitted(self.request)
#         return super(InsertFormView, self).form_valid(form)
#         
# Create your views here.
