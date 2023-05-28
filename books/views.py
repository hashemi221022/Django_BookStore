from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Book
# from .forms import BookForm
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin #! for fonction allow with login
from django.contrib.auth.decorators import login_required #! for class allow with login
from django.contrib.auth.mixins import UserPassesTestMixin


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    template_name = 'books/book_list.html'
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'
@login_required #! for finction
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comments = book.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = comment_form

    else:
        comment_form = CommentForm()
    return render(request, 'books/book_detail.html', {'book': book, 'comments': book_comments, 'comment_form': comment_form})


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ['title', 'description', 'author', 'price', 'cover']
    template_name = 'books/book_create.html'
    # form_class = BookForm #1 bedone sakhtane forms az roye ModelForms ham emkan pazire va forms.py ke sakhtam kare azafe bod


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):

    model = Book
    template_name = 'books/book_update.html'
    fields = ['title', 'description', 'author', 'cover']


    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user