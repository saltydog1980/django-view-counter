from django.shortcuts import render
from urllib import response
import random
import datetime

users = {}
# Create your views here.

def index (request):
    print(users)
    user_id_number = request.COOKIES.get('user_id_number')
    user = users.get(user_id_number)
    if not user:
        user_id_number = str(random.randint(1000, 9999))

        users[user_id_number] = {
            'count': 1,
            'start_time': datetime.datetime.now()
        }
    else:
        users[user_id_number]['count'] += 1
    response = render(request, 'pages/index.html', users[user_id_number])
    response.set_cookie('user_id_number', user_id_number)
    return response