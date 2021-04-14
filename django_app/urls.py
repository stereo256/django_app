"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 「どのアドレスにアクセスしたら、どの処理を実行するか」の情報を管理
    # path(アクセスするアドレス,　呼び出す処理)
    # include：引数に指定したモジュールを呼び出す。
    # ⇒「hello」フォルダ内のurls.pyが読込まれ、'hello/'のアドレスに割当てられる。
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
]
