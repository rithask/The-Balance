from unicodedata import category
from django.shortcuts import render, redirect

from .models import Date, Shopping
from django import forms
import datetime


class ExpenseForm(forms.Form):
    item = forms.CharField(label="Item", max_length=200)
    price = forms.FloatField(label="Price")
    # Drop down field for category
    # category = forms.ChoiceField(
    #     label="Category",
    #     choices=[
    #         ("Food", "Food"),
    #         ("Clothing", "Clothing"),
    #         ("Entertainment", "Entertainment"),
    #         ("Transportation", "Transportation"),
    #         ("Other", "Other"),
    #         ("Debt", "Debt"),
    #     ],
    # )
    date = forms.DateField(label="Date", initial=datetime.date.today())

# Create your views here.
def index(request):
    return render(request, 'thebalance/index.html', {
        "shopping_list": Shopping.objects.all()
    })

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data["item"]
            price = form.cleaned_data["price"]
            date = form.cleaned_data["date"]
            d = Date(date=date)
            d.save()
            shopping = Shopping(item=item, price=price, date=d)
            shopping.save()
            return redirect('/thebalance/')
    else:
        form = ExpenseForm()
        return render(request, 'thebalance/add_expense.html', {
            "dates": Date.objects.all(),
            "form": ExpenseForm()
        })