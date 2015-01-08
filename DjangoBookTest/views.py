# -*- coding: utf-8 -*-
__author__ = 'Yun'
__project__ = 'DjangoBookTest'

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime
from books.models import Book


def hello(request):
    return HttpResponse("Hello World!")


def current_datetime(request):
    """
    # Use HttpResponse
    now = datetime.datetime.now()
    html = "<html><body>It is %s.</body></html>" % now
    return HttpResponse(html)
    """

    # Use render_to_response
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())


def hours_ahead(request, offset):
    """
    # Use HttpResponse
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
    """

    # Use render_to_response
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})


def display_meta(request):
    values = request.META.items()
    # context_meta = {'values': {'A': 'a', 'B': 'b'}, }
    context_meta = {'values': values, }
    return render_to_response('display_meta.html', context_meta)


def display_meta2(request):
    values = request.META.items()
    # values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    error = False
    if request.GET.get('q') and request.GET['q']:
        q = request.GET['q']
        if q is None:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books': books, 'query': q})
    message = 'Please submit a search term.'
    return render_to_response('search_form.html', {'error': error, 'message': message})
    # message = 'You searched for: {}'.format(request.GET['q'])
    # return HttpResponse(message)


def display_get(request):
    # values = request.GET
    value = type(request.GET['q'])
    return render_to_response('display_get.html', {'value': value, 'variable': 'q'})