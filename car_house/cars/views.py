from django.shortcuts import render, redirect
from .models import Car, Comments
from .forms import CommentForm
from django.contrib import messages

# Create your views here.
def car_details(request, id):
    car = Car.objects.get(pk=id)
    comment = Comments.objects.filter(car_id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
            messages.success(request, 'Comment added successfully')
            return redirect('car_details', id=id)
        else:
            messages.error(request, 'Error adding comment')
    else:
        form = CommentForm()
    return render(request, 'car.html', {'car': car, 'form': form})