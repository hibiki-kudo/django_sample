#TODO

todoファイルだけどもうやった後の感想とやったこと

## やったこと
- [ ] まずターミナル上でdjungoプロジェクトを作成する
    - [ ]  django-admin startproject <プロジェクト名>でプロジェクトが立ち上がる
    - [ ]  python3 manage.py startapp manager
    - [ ]  上を実行すると以下のプロジェクトができていればよい
```
-- <保存先のディレクトリ名>/
    -- <プロジェクト名>/
        -- __init__.py
        -- setting.py
        -- urls.py
        -- wsgi.py
    -- manage.py
        -- migrations
        -- __init__.py
        -- admin.py
        -- apps.py
        -- models.py
        -- tests.py
        -- views.py
```
   - [ ] ファイル多いな...
   - [ ] これら全てが機能して回すって言うことでおけ？


- [ ] 次にプログラムの方を付け加えていく
    - [ ] setting.pyの中に以下を付け足す
```buildoutcfg
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'manager',  # 追加部分
]
```
   - [ ] 上記はプロジェクトの構成をプログラムで指定してあげるための部分だよ

以上でアプリの下準備は終了！<br>
処理の記述は主にmodel,view,testで書くみたいだけど、まだこれからの話になるなぁ

###以下は追記
bootstrapを使ってみた。freeなのにしっかりできていて、デザインも使い方次第で良さそうな感じ。<br>
####使いかた
staticフォルダの中にbootstrapフォルダを作成してその中にdist,js,venderファイルを入れる。あと、staticファイル直下にcssフォルダを作成してその中にtemplatesの中にあるbase.htmlと紐付けをするためのstatic.cssを作成する。
<br>
次にプロジェクトの中にあるtemplatesフォルダの中にbase.htmlを作成する。base.htmlは他のhtmlファイルのヘッダ部分を担う内容を記述してある。
```buildoutcfg
{% extends "base.html" %}
{% block title %}Worker List{% endblock %}
{% load staticfiles %}

      {% block body %}
      
~~~~bodyの内容~~~~~

      {% endblock %}
```
以上の部分を他のhtmlファイルに記載することによってbootstrapのデザインを使用することができた。
    