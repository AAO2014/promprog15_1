from django import forms


class HistogramMainForm(forms.Form):
    source_text1 = forms.CharField(label='Введите текст для построения частотной гистограммы', max_length=400)
    # histogram_output = forms.CharField(label='Частотная диаграмма')


