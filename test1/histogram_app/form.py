from django import forms


class HistogramMainForm(forms.Form):
    text_for_make_histogram = forms.CharField(label='1) Введите текст и нажмите кнопку:',
                                              max_length=400, widget=forms.Textarea(attrs={'cols':"40", 'rows':"10"}))
    # histogram_output = forms.CharField(label='Частотная диаграмма')

