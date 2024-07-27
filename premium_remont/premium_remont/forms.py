from django import forms

class ClientInfo(forms.Form):
    name=forms.CharField(label='name',
                         help_text='Укажите Ваше имя',
                         max_length=60,
                         widget=forms.TextInput(attrs={
                             # имеет виджет Textinput соответсвующий однострочному текстовому полю. Виджету задан аргумент attrs, которому передаются свойства которыми будет наделен HTML элемент
                             'placeholder': 'Введите Ваше имя',  # и подсказака в виде фразы "Ваше имя"
                         })
                         )

    otchestvo=forms.CharField(label='otchestvo',
                            help_text='Укажите Ваше отчество',
                            max_length=60,
                            required=False,
                            widget=forms.TextInput(attrs={
                                # имеет виджет Textinput соответсвующий однострочному текстовому полю. Виджету задан аргумент attrs, которому передаются свойства которыми будет наделен HTML элемент
                                'placeholder': 'Введите Ваше отчество',  # и подсказака в виде фразы "Ваше имя"
                            })
                            )
