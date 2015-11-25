from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from histogram_app.char_frequency_histogram_maker import CharFrequencyHistogramMaker
from histogram_app.form import HistogramMainForm


# сделай две вьюхи за двумя урлами:
# первая отображает форму (потом в форме реализуем возможность указать файл для загрузки)
# вторая отображает результат и кнопку "Вернуться"
# ссылки в шаблонах делать через {% url "histogram_app_main" %}
# https://docs.djangoproject.com/en/1.8/ref/templates/builtins/#url


class HistogramView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = HistogramMainForm()

        return render(request, self.template_name, {'form': form, 'form.source_text': 'proba'})


class HistogramResultView(TemplateView):
    template_name = 'result.html'


    def post(self, request, *args, **kwargs):
        form = HistogramMainForm(request.POST)
        res = ''

        if form.fields['source_text1'] != '':
            v = CharFrequencyHistogramMaker()
            res = v.run(form.fields['source_text1'].label)
        return render(request, self.template_name, {'histogram_output': res})

# context['form'] = HistogramMainForm()
# это самый простой способ вывести форму - лучше использовать цикл по полям формы
# http://djbook.ru/rel1.8/topics/forms/index.html#looping-over-the-form-s-fields
# а экшн у формы ставим на урл, за которым стоит HistogramResultView


# def get_histogram(request):
#     test_val = ''
#     if request.method == 'POST':
#         form = HistogramMainForm(request.POST)
#         if form.is_valid():
#             if form.fields['text_for_make_histogram'] != '':
#                 v = CharFrequencyHistogramMaker()
#                 request.session['var'] = v.run(form.cleaned_data['text_for_make_histogram'])
#             return HttpResponseRedirect('/histogram/')
#     else:
#         if 'var' in request.session:
#             test_val = request.session['var']
#             del request.session['var']
#         form = HistogramMainForm()
#     return render(request, 'histogram.html', {'form': form, 'histogram_output': test_val})



