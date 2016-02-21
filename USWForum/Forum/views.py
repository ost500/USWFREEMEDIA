import datetime

from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from Forum.models import Article

from .forms import InsertForm


# from Forum.models import Article, Author, Publisher
class HomeView(ListView, FormView):
    model = Article
    template_name = 'index.html'
    success_url = '/forum/'
    form_class = InsertForm
    
    def form_valid(self, form):
        form.submitted(self.request)
        new_name = form.cleaned_data['title']
        new2_name = form.cleaned_data['content']
        new3_name = form.cleaned_data['author']
        text1 = Article(title = new_name,content = new2_name
                        ,authors = new3_name,publication_date= datetime.datetime.now())
        text1.save()
        return super(HomeView, self).form_valid(form)
    
def examples(request):
    return render_to_response('examples.html')

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
