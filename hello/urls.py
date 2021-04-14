from django.urls import path
from . import views

urlpatterns = [
    # アドレス部：[http://〇〇/hello/]以降に続くアドレスを指定（ここでは空文字）
    # 実行処理部：views.index
    # パス名部：このPathに'index'という名前を設定
    path('', views.index, name='index'),
    path('next', views.next, name='next')
]