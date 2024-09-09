from django.shortcuts import render

def show_main(request):
    context = {
        'app' : 'Words of Affir-MACHINE',
        'name': 'Haliza Arfa',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)