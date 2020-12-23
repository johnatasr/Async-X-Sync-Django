from django.shortcuts import render
from django.views import View
import requests, time


class SyncIndex(View):
    template_name: str = 'results.html'
    urls: list = ['https://swapi.dev/api/people/', 'https://swapi.dev/api/starships/']
    data: list = []

    def get(self, request, *args, **kwargs):
        start_time = time.time()
        for url in self.urls:
            self.data.append(requests.get(url).json())

        end_time = time.time() - start_time

        payload = {
            'peoples': self.data[0],
            'spaceships': self.data[1],
            'time': format(end_time, '.2f'),
            'type': self.__class__.__name__
        }
        return render(request, self.template_name, payload)

