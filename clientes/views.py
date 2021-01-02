from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm


# Create your views here.

@login_required
def persons_list(resquest):
    persons = Person.objects.all()
    return render(resquest, "person.html", {'persons': persons})


@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    else:
        return render(request, 'person_form.html', {'form': form})


@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    else:
        return render(request, 'person_delete.html', {'person': person})
