from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages


def news(request):
    if not request.session.get("number"):
        request.session['number'] = 0
    request.session['number'] = request.session['number']+1
    return render(request, 'news.html')


def add_display_show(request, id):
    if request.method == 'POST':
        errors = shows.objects.basic_validtor(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            if shows.objects.filter(id=id).exists():
                return redirect(f'/shows/{id}/edit')
            else:
                return redirect('/show/new')
        _title = request.POST['title']
        _network = request.POST['network']
        _relase_date = datetime.strptime(
            request.POST['relase_date'], "%Y-%m-%d")
        _desc = request.POST['desc']
        if shows.objects.filter(id=id).exists():
            shows._update(id, _title, _network, _relase_date, _desc)
            show = shows.objects.get(id=id)
        else:
            shows._create(_title, _network, _relase_date, _desc)
            show = shows.objects.last()
        return redirect(f'/shows/{show.id}')
    else:
        context = {
            'show': shows.objects.get(id=id)
        }
        return render(request, 'details_show.html', context=context)


def show(request):
    context = {
        'shows': shows.objects.all()
    }
    return render(request, 'shows.html', context=context)


def edit_show(request, id):
    _show = shows.objects.get(id=id)
    context = {
        'show': _show
    }
    return render(request, 'edit_show.html', context=context)


def delete_show(request, id):
    shows.objects.get(id=id).delete()
    # show(request)
    return redirect('/shows')

# def action(request,id,flag):
#     _show=shows.objects.get(id=id)
#     if flag == 1 :
#         return redirect(f'/shows/{_show.id}')
#     elif flag == 2 :
#         return redirect(f'/shows/{_show.id}/edit')
#     return HttpResponse("Scuuess")
