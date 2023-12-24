from django.shortcuts import render, redirect
from author.models import AddCardModel
from car.forms import CommentForm
from car.models import CarModel, CommentModel
from django.contrib.auth.decorators import login_required

# Create your views here.

    
    
def CarDetails(request, pk):
    data = CarModel.objects.get(pk=pk)
    cmt = CommentModel.objects.filter(post = data)
    
    if request.method == 'POST':
        cmt_form = CommentForm(request.POST)
        if cmt_form.is_valid():
            comment = cmt_form.save(commit=False)
            comment.post = data
            comment.save()
            return redirect('car_details', pk)
    else:
        cmt_form = CommentForm()
    return render(request, 'car_view_page.html', {'data': data, 'cmt_form': cmt_form, 'cmt_data': cmt })


@login_required(login_url='user_login')
def bay_now(request, id):
    car = CarModel.objects.get(pk=id)
    car.car_quantity = car.car_quantity - 1
    car.save()
    print(id)
    
    add = AddCardModel.objects.filter(car_card_pk=id).first()
    if add:
        add.car_quantity =  add.car_quantity + 1
        add.save()
    else:
        add_card = AddCardModel()
        add_card.car_card_pk = id
        add_card.car_image =  car.car_image 
        add_card.car_name =  car.car_name 
        add_card.car_price =  car.car_price 
        add_card.car_quantity =  1
        add_card.car_decription = car.car_decription
        add_card.car_brand =  car.car_brand 
        add_card.user_id = request.user
        add_card.save()
    
    return redirect('car_details', id)
    
