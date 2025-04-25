
from django.shortcuts import render
import random

def salary_form(request):
    return render(request, 'form.html')

def salary_result(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = int(request.POST['age'])
        company = request.POST['company']
        gross_salary = float(request.POST['gross_salary'])
        tax = float(request.POST['tax'])
        bonus = float(request.POST['bonus'])

        # Calculate Net Salary
        net_salary = gross_salary + (gross_salary * bonus / 100) - (gross_salary * tax / 100)

        context = {
            'name': name,
            'net_salary': round(net_salary, 2)
        }
        return render(request, 'result.html', context)
    return render(request, 'form.html')

def jumble_word(request):
    jumbled = ''
    original = ''

    if request.method == 'POST':
        original = request.POST['word']
        word_list = list(original)
        random.shuffle(word_list)
        jumbled = ''.join(word_list)
    return render(request, 'jumble.html', {'original': original, 'jumbled': jumbled})
