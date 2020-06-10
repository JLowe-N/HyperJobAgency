from django.shortcuts import render
from django.views import View

links_from_index = ['login', 'signup', 'vacancies', 'resumes', 'home']

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context={'links': links_from_index})
