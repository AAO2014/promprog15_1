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
        return render(request, self.template_name, {'histogram_output': res})




