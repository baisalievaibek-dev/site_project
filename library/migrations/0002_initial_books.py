from django.db import migrations


def add_initial_books(apps, schema_editor):
    Book = apps.get_model('library', 'Book')
    books = [
        {
            'title': 'Маленький принц',
            'author': 'Антуан де Сент-Экзюпери',
            'cover_class': 'one',
            'cover_text': 'МАЛЕНЬКИЙ\nПРИНЦ',
        },
        {
            'title': 'Мастер и Маргарита',
            'author': 'Михаил Булгаков',
            'cover_class': 'two',
            'cover_text': 'МАСТЕР\nИ МАРГАРИТА',
        },
        {
            'title': 'Норвежский лес',
            'author': 'Харуки Мураками',
            'cover_class': 'three',
            'cover_text': 'НОРВЕЖСКИЙ\nЛЕС',
        },
        {
            'title': 'Атлант расправил плечи',
            'author': 'Айн Рэнд',
            'cover_class': 'four',
            'cover_text': 'АТЛАНТ\nРАСПРАВИЛ\nПЛЕЧИ',
        },
    ]
    for book in books:
        Book.objects.get_or_create(title=book['title'], defaults=book)


class Migration(migrations.Migration):
    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_books, migrations.RunPython.noop),
    ]