from django.shortcuts import render,redirect
from .models import Contact


# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(Name__icontains = search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ""
    return render(request,'index.html',{'contacts':contacts,'search_input' : search_input })

def add(request):
    if request.method == 'POST':
        new_contact = Contact(
            Name =request.POST['Name'],
            Realtionship=request.POST['Realtionship'],
            Phone_no=request.POST['Phone_no'],
            address=request.POST['address'],
        )
        new_contact.save()
        return redirect('/')
    return render(request,'new.html')

def profile(request,pk):
    contact = Contact.objects.get(id=pk)
    return render(request,'contact-profile.html',{"contact":contact })

def edit(request,pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.Name = request.POST['fullname']
        contact.Realtionship = request.POST['fullname']
        contact.Phone_no = request.POST['phone-number']
        contact.address = request.POST['address']
        contact.save()
        return redirect('/profile/' +str( contact.id))
    return render(request,'edit.html',{"contact":contact })

def delete(request,pk):
    contact = Contact.objects.get(id=pk)
    
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request,'delete.html',{"contact":contact })