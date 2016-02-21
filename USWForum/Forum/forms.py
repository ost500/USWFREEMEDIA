from django import forms

class InsertForm(forms.Form):
    title = forms.CharField(label = "title")
    content = forms.CharField(label = "content")
    author = forms.CharField(label = "author")
    
    def submitted(self, request):
        print "submitted!"
        print request.POST['title']
        print request.POST['content']