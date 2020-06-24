from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'w-full text-gray-800 font-sm px-2 py-2 border-2 border-green-200 focus:outline-none rounded-md shadow-sm',
            'placeholder': 'Add a new Task'}
        ))