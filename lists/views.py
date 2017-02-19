from django.shortcuts import render, redirect

from .models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'lists/home.html', {'items': items})

    # else:
    #     new_item_text = ''

    # return HttpResponse(request.POST['item_text'])
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()

    # return render(request, 'lists/home.html', {
    #     'new_item_text': new_item_text,
    # })
