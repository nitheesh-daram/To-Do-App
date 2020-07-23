from django.shortcuts import render,redirect
from .models import item,create_form
# Create your views here.


def main_page(request):
    data=item.objects.order_by('due_date')
    new_form=create_form(request.POST or None)
    if new_form.is_valid():
        new_form.save()
        return redirect("main_page")
    items={
        "items":data,
        "forms":new_form
    }
    return render(request,"to-do/index.html",items)

def view_item(request,id):
    data=item.objects.get(id=id)
    if not request.POST:
        new_form=create_form(instance=data)
    else:
        new_form=create_form(request.POST or None,instance=data)
        if new_form.is_valid():
            new_form.save()
            return redirect("main_page")
    items={
        "items":new_form,
        "id":data
    }
    return render(request,"to-do/view.html",items)

def delete(request,id):
    item.objects.get(id=id).delete()
    return redirect("main_page")
    