from django.shortcuts import render
from django.http import HttpResponse

# Webブラウザからアクセスしたときの処理
def index(request):
    params = {
        'title':'Hello/Index',
        'msg':'お名前は？',
    }
    return render(request, 'hello/index.html', params)

# form送信を受け取った時の処理
def form(request):
    msg = request.POST['msg']
    params = {
        'title':'Hello/Form',
        'msg':'こんにちは、' + msg + 'さん。',
    }
    return render(request, 'hello/index.html', params)