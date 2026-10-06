from django.shortcuts import render
from library.models import Book


def home(request):
    query = request.GET.get('q', '').strip()
    books = Book.objects.all()
    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)

    return render(request, 'sitea.html', {'books': books, 'query': query})

def hudoj_literatura(request):
    query = request.GET.get('q', 'hudoj_literatura').strip()
    books = Book.objects.all()

    books = [
        {
            "title": "Война и мир",
            "author": "Лев Толстой",
            "cover_class": "green",
            "cover_text": "Война и мир"
        },
        {
            "title": "Мастер и Маргарита",
            "author": "Михаил Булгаков",
            "cover_class": "brown",
            "cover_text": "Мастер\nи Маргарита"
        },
        {
            "title": "Преступление и наказание",
            "author": "Фёдор Достоевский",
            "cover_class": "purple",
            "cover_text": "Преступление\nи наказание"
        },
        {
            "title": "Евгений Онегин",
            "author": "Александр Пушкин",
            "cover_class": "red",
            "cover_text": "Евгений\nОнегин"
        },
    ]

    return render(request, "hudoj_letur.html", {"books": books})


def business_books(request):
    query = request.GET.get('q', 'business_books').strip()
    books = Book.objects.all()
    books = [
        {
            "title": "Психология денег",
            "author": "Морган Хаузел",
            "cover_class": "green",
            "cover_text": "Психология\nденег",
        },
        {
            "title": "Бизнес с нуля",
            "author": "Эрик Рис",
            "cover_class": "brown",
            "cover_text": "Бизнес\nс нуля",
        },
        {
            "title": "От хорошего к великому",
            "author": "Джим Коллинз",
            "cover_class": "purple",
            "cover_text": "От хорошего\nк великому",
        },
        {
            "title": "Сам себе MBA",
            "author": "Джош Кауфман",
            "cover_class": "red",
            "cover_text": "Сам себе\nMBA",
        },
    ]

    return render(request, "bisnes.html", {"books": books})


def history_books(request):
    query = request.GET.get('q', 'history_books').strip()
    histor = Book.objects.all()
    books = [
        {
            "title": "История государства Российского",
            "author": "Николай Карамзин",
            "cover_class": "green",
            "cover_text": "История государства\nРоссийского",
        },
        {
            "title": "История России с древнейших времен",
            "author": "Сергей Соловьёв",
            "cover_class": "brown",
            "cover_text": "История России\nс древнейших времен",
        },
        {
            "title": "История Древнего мира",
            "author": "Александр Немировский",
            "cover_class": "purple",
            "cover_text": "История\nДревнего мира",
        },
        {
            "title": "Вторая мировая война",
            "author": "Уинстон Черчилль",
            "cover_class": "red",
            "cover_text": "Вторая мировая\nвойна",
        },
    ]

    return render(request, "histori.html", {"books": books})


def psychology_books(request):
    query = request.GET.get('q', 'psychology_books').strip()
    books = Book.objects.all()
    books = [
        {
            "title": "Думай медленно... решай быстро",
            "author": "Даниэль Канеман",
            "cover_class": "green",
            "cover_text": "Думай медленно...\nрешай быстро",
        },
        {
            "title": "Психология влияния",
            "author": "Роберт Чалдини",
            "cover_class": "brown",
            "cover_text": "Психология\nвлияния",
        },
        {
            "title": "Человек в поисках смысла",
            "author": "Виктор Франкл",
            "cover_class": "purple",
            "cover_text": "Человек в поисках\nсмысла",
        },
        {
            "title": "Игры, в которые играют люди",
            "author": "Эрик Берн",
            "cover_class": "red",
            "cover_text": "Игры, в которые\nиграют люди",
        },
    ]

    return render(request, "psihologia.html", {"books": books})



def science_books(request):
    query = request.GET.get('q', 'science_books').strip()
    books = Book.objects.all()
    books = [
        {
            "title": "Краткая история времени",
            "author": "Стивен Хокинг",
            "cover_class": "green",
            "cover_text": "Краткая история\nвремени",
        },
        {
            "title": "Космос",
            "author": "Карл Саган",
            "cover_class": "brown",
            "cover_text": "Космос",
        },
        {
            "title": "Эгоистичный ген",
            "author": "Ричард Докинз",
            "cover_class": "purple",
            "cover_text": "Эгоистичный\nген",
        },
        {
            "title": "Краткая история почти всего на свете",
            "author": "Билл Брайсон",
            "cover_class": "red",
            "cover_text": "Краткая история\nпочти всего",
        },
    ]

    return render(request, "nauk.html", {"books": books})