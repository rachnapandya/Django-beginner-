from django.shortcuts import get_object_or_404, render,get_list_or_404, redirect
from .models import Product
from django.http import Http404
from .forms import RawProductForm,ProductForm

# Create your views here.
def product_create_view(request):
    my_form = RawProductForm() #get method to see what it looks like
    if request.method=="POST":
        my_form = RawProductForm(request.POST) #created instance of RawProductForm class
        #also does validation
    #to render out the data we used POST to add it into the database
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form" : my_form
    }
    return render(request, 'products/product_create.html',context)

#Bad method
# def product_create_view(request):
#    if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#    context = {}
#    return render(request,'products/product_create.html',context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
    
#     context = {
#         'form' : form
#     }
#     return render(request,'products/product_create.html',context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    #context = {
    #    'title' : obj.title,
    #   'description' : obj.description,
    #    'summary' : obj.summary,
    #    'price' : obj.price
    #}
    context = {
        'object' : obj
    }
    return render(request,'products/product_detail.html',context)

#dynamic lookup 
def dynamic_lookup_view(request,my_id):
    #obj = Product.objects.get(id=my_id)
    #obj = get_list_or_404(Product,id=my_id)
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object" : obj
    }
    return render(request,'products/product_detail.html', context)

#delete an object in the database
# def product_delete_view(request,id):
#     obj = get_object_or_404(Product,id=my_id)
#     if request.method == "POST" : #confirming delete
#         obj.delete()
#         return redirect('../../')
#     context = {
#         'object' : obj
#     }
#     return render(request,'products/product_delete.html', context)

#get list of objects from database
def product_list_view(request):
    queryset = Product.objects.all() #list of objects
    context ={
        'object_list' : queryset
    }
    return render(request,'products/product_list.html',context)