from django.shortcuts import render
from .models import Book,Author

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    
    num_authors = Author.objects.count()
    
    books=Book.objects.all().values()

    book_list=[]
    for book in books:
        print(book)
        if book['status'] == 1:
            status = 'in library'
        else:
            status = 'taken'
        
        if book['status'] == 1:
            taken = ''
            returned = ''
        else:
            if not book['taken_at']:
                taken = ''
            else:
                taken = book['taken_at'].strftime("%d %B, %Y %H:%M:%S")

        book_list.append({
            'id':book['id'],
            'name':book['name'],
            'author':Author.objects.filter(id=book['author_id']).values('name')[0]['name'],
            'status':status,
            'takenBy':book['takenBy'],
            'taken':taken,
        })

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'book_list':book_list
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
