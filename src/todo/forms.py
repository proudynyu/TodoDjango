from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
	title = forms.CharField(max_length=200, required=True, label="Task", strip=True)

	title.widget.attrs.update({'class': 'insert'})

	class Meta:
		model = Todo
		fields = [
			'title',
		]