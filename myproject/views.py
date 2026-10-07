from django.shortcuts import render,redirect
from myBook.models import *
 
def book(request):
    book=bookModel.objects.all()
    context={
        'book':book
    }
    return render(request,'book.html',context)

def addbook(request):
    if request.method=='POST':  
        booktitle=request.POST.get('booktitle')
        author=request.POST.get('author')
        publish_date=request.POST.get('publish_date')

        book=bookModel(
            booktitle=booktitle,
            author=author,
            publish_date=publish_date,
        )
        book.save()
        return redirect('book')
    return render(request,'addbook.html')

    