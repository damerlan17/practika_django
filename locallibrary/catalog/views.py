from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применён по умолчанию.

    # Подсчет жанров
    num_genres = Genre.objects.count()

    #количество книг, которые содержат в своих заголовках какое-либо слово
    search_word = 'z'
    num_books_with_world = Book.objects.filter(title__icontains=search_word).count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books': num_books,
                 'num_instances': num_instances,
                 'num_instances_available': num_instances_available,
                 'num_authors': num_authors,
                 'num_visits': num_visits,
                 'num_genres': num_genres,
                 'search_word': search_word,
                 'num_books_with_world': num_books_with_world,
                 },  # num_visits appended

    )


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # ваше собственное имя переменной контекста в шаблоне
    queryset = Book.objects.filter(title__icontains='war')[:5]  # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'book/my_arbitrary_template_name_list.html'  # Определение имени вашего шаблона и его расположения


class BookDetailView(generic.DetailView):
    model = Book


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'  # ваше собственное имя переменной контекста в шаблоне
    template_name = 'book/my_arbitrary_template_name_list.html'  # Определение имени вашего шаблона и его расположения


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
