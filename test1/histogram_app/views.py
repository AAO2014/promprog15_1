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
    if request.method == 'POST':
        form = HistogramMainForm(request.POST)
        if form.is_valid():
            if form.fields['text_for_make_histogram'] != '':
                # v = CharFrequencyHistogramMaker()
                # form.fields['histogram_output'].initial = v.run(form.fields['text_for_make_histogram'])
                form.fields['histogram_output'] = form.fields['text_for_make_histogram']
            return HttpResponseRedirect('/histogram/')

    else:
        form = HistogramMainForm()

    return render(request, 'histogram.html', {'form': form})

