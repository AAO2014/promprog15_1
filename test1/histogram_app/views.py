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
                res = v.run(form.cleaned_data['text_for_make_histogram'])
        return render(request, self.template_name, {'histogram_output': res})

# context['form'] = HistogramMainForm()
# это самый простой способ вывести форму - лучше использовать цикл по полям формы
# http://djbook.ru/rel1.8/topics/forms/index.html#looping-over-the-form-s-fields
    # А вот это я не понял
# когда в форме NN полей все их перечислять замумукаешься, поэтому легче циклом.

# у тебя пока одно поле в форме. давай сделаем еще два - min_frequency и max_frequency
# и передавай Вовану в .run()
# сделай проверку на целое неотрицательное число для этих полей


#  TODO старый код удаляй!! и шаблоны которые не нужны - тоже удаляй
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



