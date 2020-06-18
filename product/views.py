from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from product.models import CommentForm
from product.models import Comment
from django.contrib import messages


def index(request):

    return HttpResponse("Product Page")

def addcomment(request,id):
    url=request.META.get("HTTP_REFERER")
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            current_user=request.user

            data=Comment()
            data.user_id=current_user.id
            data.product_id=id
            data.subject=form.cleaned_data['subject']
            data.comment=form.cleaned_data['comment']
            data.rate=form.cleaned_data['rate']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Yorumunuz başarıyla gönderilmiştir.")
            return HttpResponseRedirect(url)

    messages.warning(request,"Yorumunuz gönderilemedi. Lütfen puan belirtiniz.")
    return HttpResponseRedirect(url)
            



    