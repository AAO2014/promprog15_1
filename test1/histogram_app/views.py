from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from histogram_app.char_frequency_histogram_maker import CharFrequencyHistogramMaker
from histogram_app.form import HistogramMainForm


class HistogramView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = HistogramMainForm()
        return render(request, self.template_name, {'form': form})


class HistogramResultView(TemplateView):
    template_name = 'result.html'

    def post(self, request, *args, **kwargs):
        form = HistogramMainForm(request.POST)
        res = ''
        if form.is_valid():
            if form.fields['text_for_make_histogram'] != '':
                v = CharFrequencyHistogramMaker()
                res = v.run(form.cleaned_data['text_for_make_histogram'],
                            form.cleaned_data['min_frequency'],
                            form.cleaned_data['max_frequency'])
        # вот тут на else по идее и нужно отработать ошибку.
        # но ты в другом шаблоне... надо менять всю структуру вызовов.

        # пусть форма идет на HistogramView, там валидируется,
        # и если все норм - идет редирект на HistogramResultView
        # причем в HistogramResultView можно постить уже готовую гистограмму :)

        # форму в HistogramView обрабатывать тоже на post
        # на get в HistogramView оставь начальное формирование формы,
        # например можно выдать текст по умолчанию для пробы
        # это случай, когда узер первый раз заходит на сайт
        return render(request, self.template_name, context={'histogram_output': res})




