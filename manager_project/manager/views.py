from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView


from manager.models import *

get_object_or_404(Person, id=20)


class WorkerListView(TemplateView):
    template_name = "worker_list.html"

    # def get(self, request, *args, **kwargs):
    #     context = super(WorkerListView, self).get_context_data(**kwargs)
    #     return render(self.request, self.template_name, context)


# Create your views here.
    def get(self, request, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)

        workers = Worker.objects.all() # データベースからオブジェクトを取得して
        context['workers'] = workers  # 入れ物に入れる

        return render(self.request, self.template_name, context)


def index(request):
    form = forms.SwitchLanguageForm(request.POST or None)
    if form.is_valid():
        lang = form.cleaned_data['language']
        # リクエスト中の言語設定切り替え
        translation.activate(lang)
        # セッションの言語設定切り替え
        request.session['django_language'] = lang
    return render(request, 'index.html', {'form': form})