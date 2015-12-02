from django import forms


class HistogramMainForm(forms.Form):
    text_for_make_histogram = forms.CharField(label='Введите текст для исследования',
                                              max_length=400, widget=forms.Textarea(attrs={'cols':"40", 'rows':"10"}))
    min_frequency = forms.IntegerField(min_value=0, label='Минимальная граница частоты:', initial=0)
    max_frequency = forms.IntegerField(min_value=0, label='Максимальная граница частоты:', initial=0)

