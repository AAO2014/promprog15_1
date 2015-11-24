from django import forms


class HistogramMainForm(forms.Form):
    text_for_make_histogram = forms.CharField(label='Введите текст для построения частотной гистограммы', max_length=400)
    # histogram_output = forms.CharField(label='Частотная диаграмма')

