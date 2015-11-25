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

    # def get_context_data(self, **kwargs):
    #     context = super(HistogramView, self).get_context_data(**kwargs)
    #     # context['form'] = HistogramMainForm()
    #     # это самый простой способ вывести форму - лучше использовать цикл по полям формы
    #     # http://djbook.ru/rel1.8/topics/forms/index.html#looping-over-the-form-s-fields
    #     # а экшн у формы ставим на урл, за которым стоит HistogramResultView
    #     return context


# def get_histogram(request):
#     # это все можно сделать в HistogramView,
#     # и как говорили - разнести форму и результат работы по разным view
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


class HistogramResultView(TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            context = super(HistogramResultView, self).get_context_data(self, **kwargs)
            source_text = self.request.POST['source_text']
            v = CharFrequencyHistogramMaker()
            context['histogram_output'] = v.run(source_text)
        return context
