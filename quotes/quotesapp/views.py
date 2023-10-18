from django.shortcuts import get_object_or_404, redirect, render
from .forms import QuoteForm, AuthorForm, TagForm
from .models import Author, Quote, Tag

# Create your views here.


def main(request):
    quotes = Quote.objects.all()
    return render(request, 'quotesapp/index.html', {"quotes": quotes})


def tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "quotesapp/tags.html", {"form": form})

    return render(request, "quotesapp/tags.html", {"form": TagForm()})


def author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "quotesapp/author.html", {"form": form})

    return render(request, "quotesapp/author.html", {"form": AuthorForm()})


def quote(request):
    authors = Author.objects.all()
    tags = Tag.objects.all()

    if request.method == "POST":
        form = QuoteForm(request.POST)

        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(
                name__in=request.POST.getlist("tags"))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to="quotesapp:main")
        else:
            return render(request, "quotesapp/quote.html", {"authors": authors, "tags": tags, "form": form})

    return render(request, "quotesapp/quote.html", {"authors": authors, "tags": tags, "form": QuoteForm()})


def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    author = Author.objects.get(id=quote.author_id)

    return render(request, "quotesapp/detail.html", {"quote": quote, "author": author})


def about_author(request, author_id):
    author = Author.objects.get(id=author_id)

    return render(request, 'quotesapp/about_author.html', {"author": author})
