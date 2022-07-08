from django.shortcuts import render
from .models import Double


def nameIsValid(name):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '

    for c in name:
        if c not in alpha:
            return False
    return True


def double(request):
    doubles = Double.objects.all()

    if request.method == 'GET':
        return render(request, 'double_list.html', {'doubles': doubles})

    value = int(request.POST.get('value'))
    if value > 1000 or value < -1000:
        error = 'Maximum value 1000 and minimum -1000'
        return render(request, 'double_list.html', {'doubles': doubles, 'error': error})

    person_name = request.POST.get('person_name')
    if not nameIsValid(person_name):
        error = 'Plaese dont use characters'
        return render(request, 'double_list.html', {'doubles': doubles, 'error': error})

    alreadyExist = Double.objects.filter(name=person_name, value=value)

    if alreadyExist.count() == 0:
        Double.objects.create(name=person_name, value=value, double_value=value*2)
    return render(request, 'double_list.html', {'doubles': doubles})


