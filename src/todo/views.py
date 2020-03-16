from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

def home(request): 
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			task = form.save(commit=False)
			task.title = form.cleaned_data.get('title')
			task.save()
			return redirect('/')
	else:
		form = TodoForm
		context = {
			'todo': Todo.objects.all(),
			'form': form,
		}
		return render(request, 'todo/index.html', context)

def delete(request, pk):
	Todo.objects.filter(id=pk).delete()
	return redirect('/')
	
def edit(request, pk):
	pass