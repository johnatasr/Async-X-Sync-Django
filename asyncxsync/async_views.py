from django.shortcuts import render
# from django.views import View
# from django.utils.decorators import classonlymethod
from .utils import fetch
import time, aiohttp, asyncio


async def async_view(request):
    start_time = time.time()
    template_name: str = 'results.html'
    urls: list = ['https://swapi.dev/api/people/', 'https://swapi.dev/api/starships/']

    async with aiohttp.ClientSession() as client:
        tasks: list = []
        for url in urls:
            task = asyncio.ensure_future(fetch(client, url))
            tasks.append(task)
        data = await asyncio.gather(*tasks)
        end_time = time.time() - start_time

    payload = {
        'peoples': data[0],
        'spaceships': data[1],
        'time': format(end_time, '.2f'),
        'type': 'async_view'
    }

    return render(request, template_name, payload)

# class AsyncIndex(View):
#     template_name: str = 'results.html'
#     urls: list = ['https://swapi.dev/api/people/', 'https://swapi.dev/api/starships/']
#     tasks: list = []
#
#     @classonlymethod
#     def as_view(cls, **initkwargs):
#         view = super().as_view(**initkwargs)
#         view._is_coroutine = asyncio.coroutines._is_coroutine
#         return view
#
#     async def get(self, request, *args, **kwargs):
#         start_time = time.time()
#
#         async with aiohttp.ClientSession() as client:
#             for url in self.urls:
#                 task = asyncio.ensure_future(fetch(client, url))
#                 self.tasks.append(task)
#             data = await asyncio.gather(*self.tasks)
#             end_time = time.time() - start_time
#
#         payload = {
#             'peoples': data[0],
#             'spaceships': data[1],
#             'time': format(end_time, '.2f'),
#             'type': self.__class__.__name__
#         }
#
#         return render(request, self.template_name, payload)