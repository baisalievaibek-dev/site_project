from django.shortcuts import render
from library.models import Book


def home(request):
    query = request.GET.get('q', '').strip()
    books = Book.objects.all()
    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)

    return render(request, 'sitea.html', {'books': books, 'query': query})