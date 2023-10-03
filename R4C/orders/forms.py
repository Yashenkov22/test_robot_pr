from django import forms


class OrderForm(forms.Form):

    email = forms.EmailField(label='Ваша почта',
                             required=True)
    robot_serial = forms.CharField(label='Серийный номер робота',
                                   required=True)