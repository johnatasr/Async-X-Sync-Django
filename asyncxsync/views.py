from django.shortcuts import render
from django.views import View


class Index(View):
    template_name: str = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

