from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from histogram_app.char_frequency_histogram_maker import CharFrequencyHistogramMaker
from histogram_app.form import HistogramMainForm


class HistogramView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HistogramView, self).get_context_data(**kwargs)
        context['source_text'] = 'aa;sfkja;dskfj;asdkf;alskdf;alsdk;f'
        context['histogram_answer'] = 'Text for test'
        return context


def get_histogram(request):
    test_val = ''
    if request.method == 'POST':
        form = HistogramMainForm(request.POST)
        if form.is_valid():
            if form.fields['text_for_make_histogram'] != '':
                v = CharFrequencyHistogramMaker()
                request.session['var'] = v.run(form.cleaned_data['text_for_make_histogram'])
            return HttpResponseRedirect('/histogram/')
    else:
        if 'var' in request.session:
            test_val = request.session['var']
            del request.session['var']
        form = HistogramMainForm()
    return render(request, 'histogram.html', {'form': form, 'histogram_output': test_val})
