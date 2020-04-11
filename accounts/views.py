from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Create your views here.
from accounts.forms import UpdateUser
from accounts.models import CompletedRegister


def register(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user taken already")
                return redirect("Register")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect("Register")

            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                                password=password1)
                user.save()
                user=authenticate(request,username=username,password=password1)
                if user is not None:
                    login(request, user)
                    return redirect('Register1')
        else:
            messages.info(request, "Password not matching")
        return redirect("Register")

    else:
         return render(request,'account/register.html')
def loginuser(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == 'POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('Homepage')
            else:
                messages.info(request,"Enter correct username and password")
                return redirect('Login')

        else:
            return render(request,'account/loginuser.html')

def logout_view(request):
        logout(request)
        return redirect('Login')
def dashbord(request):
    return render(request,'account/dashboard.html')
def profile_view(request):
    file=CompletedRegister.objects.get(user=get_object_or_404(User,username=request.user))
    return render(request,'account/profile.html',{'file':file})

# def profile_update(request):
#     task = Userprofile.objects.get(user=get_object_or_404(User, username=request.user))
#     post_data=request.POST or None
#     file_data=request.FILES or None
#     if request.method=="POST":
#         form=Updateprofile(post_data,file_data,instance=task)
#         form1=UpdateUser(post_data,instance=User.objects.get(username=request.user))
#         if form.is_valid() and form1.is_valid():
#             form.save()
#             form1.save()
#             messages.success(request,"Profile update successfully")
#             return redirect('profile')
#     else:
#         form=Updateprofile(instance=task)
#         form1=UpdateUser(instance=User.objects.get(username=request.user))
#     return render(request,'account/updateprofile.html',{'form':form,'task':task,'form1':form1})

def first(request):
    post_data = request.POST or None
    if request.method == "POST":
        phone_=request.POST['phone']
        nid_=request.POST['nid']
        gender_=request.POST['gender']
        date_=request.POST['date']
        height_=request.POST['height']
        maritalstatus_=request.POST['maritalstatus']
        child_=request.POST['child']
        bodyshap_=request.POST['bodyshap']
        complexion_=request.POST['complexion']
        bloodgroup_=request.POST['bloodgroup']
        website_=request.POST['website']
        photo_=request.FILES['img']
        father_=request.POST['father']
        mother_=request.POST['mother']
        brother_=request.POST['brother']
        sister_=request.POST['sister']
        religion_=request.POST['religion']
        mothertongue_=request.POST['mothertongue']
        familyvalue_=request.POST['familyvalue']
        livingcountry_=request.POST['livingcountry']
        livingcity_=request.POST['livingcity']
        livingarea_=request.POST['livingarea']
        resedentalstatus_=request.POST['resedentalstatus']
        homecountry_=request.POST['homecountry']
        homedistrict_=request.POST['homedistrict']
        aboutyourself_=request.POST['aboutyourself']
        aboutyourfamily_=request.POST['aboutyourfamily']
        education_=request.POST['education']
        universitycollege_=request.POST['universitycollege']
        profession_=request.POST['profession']
        designstion_=request.POST['designstion']
        preferedage_=request.POST['preferedage']
        preferedmaritalstatus_=request.POST['preferedmaritalstatus']
        preferedreligion_=request.POST['preferedreligion']
        preferedcountry_=request.POST['preferedcountry']
        preferedlivingarea_=request.POST['preferedlivingarea']
        preferededucation_=request.POST['preferededucation']
        preferedprofession_=request.POST['preferedprofession']
        aboutpatner_=request.POST['aboutpatner']
        task=CompletedRegister(user=get_object_or_404(User,username=request.user),nationalID=nid_,phone=phone_,gender=gender_,
                               birth=date_,maritalStatus=maritalstatus_,Children=child_,height=height_,bodyType=bodyshap_,
                               Complexion=complexion_,blodGroup=bloodgroup_,religon=religion_,mothertongue=mothertongue_,
                               familyvalue=familyvalue_,father=father_,mother=mother_,sister=sister_,brother=brother_,
                               education=education_,universitycollege=universitycollege_,profession=profession_,designation=designstion_,
                               currentlivingcourtry=livingcountry_,currentlivingcity=livingcity_,currentlivingarea=livingarea_,
                               residentialstatus=resedentalstatus_,homecountry=homecountry_,homedistrict=homedistrict_,aboutyou=aboutyourself_,
                               aboutfamily=aboutyourfamily_,preferredage=preferedage_,preferredmarrige=preferedmaritalstatus_,
                               patnerreligon=preferedreligion_,patnerhomecountry=preferedcountry_,patnercurrentliving=preferedlivingarea_,
                               patnereducation=preferededucation_,patnerprofession=preferedprofession_,aboutpatner=aboutpatner_,
                               website=website_,thumb=photo_
                               )
        task.save()
        return redirect('Homepage')
    return render(request,'account/first.html')
def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.error(request, "Password changed.well done! ")
            return redirect('profile')
        else:
            messages.error(request,"Input password is incorrect ")
            return redirect('change_password')

    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'account/change_password.html',{'form':form})
def viewp_rofile(request):
    file = CompletedRegister.objects.get(user=get_object_or_404(User, username=request.user))
    return render(request,'account/viewp_rofile.html',{'file':file})