from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from product.models import Categori,Comment,ContentForm
from home.models import Ayarlar,UserProfile
from user.forms import UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from product.models import Urun, Images, ImageFormContent


@login_required(login_url='/login')
def index(request):
    if request.user is not None:
        current_user=request.user
        profile=UserProfile.objects.get(user_id=current_user.id)
        ayar= Ayarlar.objects.get(pk=1)
        categori= Categori.objects.filter(tip = "categori")
        menu = Categori.objects.filter(tip = "menu")
        menu_icerik = Urun.objects.filter(tip = "menu")
        context={
            'ayar':ayar,
            'categori':categori,
            'profile':profile,
            'menu':menu,
            'menu_icerik':menu_icerik,
            }
        return render(request, 'user.html',context)
    else:
        return redirect('/login')

@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form=UserUpdateForm(request.POST, instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Profiliniz Guncellendi")
            return redirect('/user')

    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.userprofile)
        categori= Categori.objects.filter(tip = "categori")
        menu = Categori.objects.filter(tip = "menu")
        menu_icerik = Urun.objects.filter(tip = "menu")
        ayar= Ayarlar.objects.get(pk=1)
        context={
            'ayar':ayar,
            'categori':categori,
            'user_form':user_form,
            'profile_form':profile_form,
            'menu':menu,
            'menu_icerik':menu_icerik,
        }
        return render(request,'bilgi_yenile.html',context)


@login_required(login_url='/login')
def addcontent(request):
    if request.method == 'POST':
        form=ContentForm(request.POST,request.FILES)
        if form.is_valid():
            current_user=request.user
            data=Urun()
            data.User_id=current_user.id
            data.title=form.cleaned_data['title']
            data.keywords=form.cleaned_data['keywords']
            data.description=form.cleaned_data['description']
            data.tip=form.cleaned_data['tip']
            data.slug=form.cleaned_data['slug']
            data.image=form.cleaned_data['image']
            data.detail=form.cleaned_data['detail']
            data.status='False'
            data.save()
            messages.success(request,"İçerik başarıyla eklendi")
            return HttpResponseRedirect("/user/contents")
        else:
            messages.warning(request,"İçerik eklenmedi"+str(form.errors))
            return HttpResponseRedirect("/user/contents")
            

    else:
        form=ContentForm()
        categori= Categori.objects.filter(tip = "categori")
        menu = Categori.objects.filter(tip = "menu")
        menu_icerik = Urun.objects.filter(tip = "menu")
        ayar= Ayarlar.objects.get(pk=1)
        context={
            'ayar':ayar,
            'categori':categori,
            'form':form,
            'menu':menu,
            'menu_icerik':menu_icerik,
        }
        return render(request,'user_addcontent.html',context)
@login_required(login_url='/login')
def editcontent(request,id):
    content=Urun.objects.get(id=id)
    if request.method == 'POST':
        form=ContentForm(request.POST,request.FILES,instance=content)
        if form.is_valid():
            form.save()
            messages.success(request,"İçerik başarıyla düzenlendi")
            return HttpResponseRedirect("/user/contents")
        else:
            messages.warning(request,"İçerik düzenlenemedi"+str(form.errors))
            return HttpResponseRedirect("/user/editcontent"+str(id))
            

    else:
        form=ContentForm(instance=content)
        categori= Categori.objects.filter(tip = "categori")
        menu = Categori.objects.filter(tip = "menu")
        menu_icerik = Urun.objects.filter(tip = "menu")
        ayar= Ayarlar.objects.get(pk=1)
        context={
            'ayar':ayar,
            'categori':categori,
            'form':form,
            'menu':menu,
            'menu_icerik':menu_icerik,
        }
        return render(request,'user_addcontent.html',context)

@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user) # Important!
            messages.success(request, 'Şifreniz başarıyla değiştirildi')
            return redirect('/user')
        else:
            messages.warning(request, 'Lütfen hatalara dikkat ediniz.<br>'+str(form.errors))

    
    ayar=Ayarlar.objects.get(pk=1)
    categori= Categori.objects.filter(tip = "categori")
    menu = Categori.objects.filter(tip = "menu")
    menu_icerik = Urun.objects.filter(tip = "menu")
    form = PasswordChangeForm(request.user)
    context={
            'ayar':ayar,
            'categori':categori,
            'form':form,
            'menu':menu,
            'menu_icerik':menu_icerik,
        }
    return render(request, 'sifre_yenile.html',context)

@login_required(login_url='/login') # Check togin
def comments (request):
    ayar=Ayarlar.objects.get(pk=1)
    categori= Categori.objects.filter(tip = "categori")
    menu = Categori.objects.filter(tip = "menu")
    menu_icerik = Urun.objects.filter(tip = "menu")
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {
        'ayar':ayar,
        'categori': categori,
        'comments': comments,
        'menu':menu,
        'menu_icerik':menu_icerik,
      }
    return render(request, 'user_comment.html', context)

@login_required(login_url='/login')
def deletecomment(request,id):
    Comment.objects.filter(id=id).delete()
    messages.warning(request,"Yorumunuz  silinmiştir.")
    return HttpResponseRedirect("/user/comments")
    


@login_required(login_url='/login')
def deletecontent(request,id):
    Urun.objects.filter(id=id).delete()
    messages.warning(request,"Yorumunuz  silinmiştir.")
    return HttpResponseRedirect("/user/contents")
    



@login_required(login_url='/login')
def contents(request):
    ayar=Ayarlar.objects.get(pk=1)
    categori= Categori.objects.filter(tip = "categori")
    menu = Categori.objects.filter(tip = "menu")
    menu_icerik = Urun.objects.filter(tip = "menu")
    current_user = request.user
    contents = Urun.objects.filter(User_id=current_user.id)
    context = {
        'ayar':ayar,
        'categori': categori,
        'contents': contents,
        'menu':menu,
        'menu_icerik':menu_icerik,
      }
    return render(request, 'user_content.html', context)

def addgaleri(request,id):
    if request.method=='POST':
        lasturl=request.META.get('HTTP_REFERER')
        form =ImageFormContent(request.POST,request.FILES)
        if form.is_valid():
            data=Images()
            data.title=form.cleaned_data['title']
            data.urun_id=id
            data.image=form.cleaned_data['image']
            data.save()
            messages.success(request, 'Resim yuklendi')
            return HttpResponseRedirect(lasturl)
        else:
            messages.warning(request, 'Yukleme hatasi.<br>'+str(form.errors))
            return HttpResponseRedirect(lasturl)

    else:
        content=Urun.objects.get(id=id)
        image=Images.objects.filter(urun_id=id)
        context={
            'content':content,
            'images':image,
            'form':ImageFormContent()
        }
        return render(request,'user_galeri.html',context)
