from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import random


def index(request):
    station = random.choice(["東京", "品川", "渋谷", "新宿", "池袋", "上野", ])
    params = {
        'title': '駅占い',
        'station': station,
    }
    return render(request, 'firstapp/index.html', params)
