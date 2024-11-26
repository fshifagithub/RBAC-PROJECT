from django.shortcuts import render,redirect
from django.views.generic import FormView,CreateView,View,UpdateView,DetailView,ListView
from users.forms import LoginForm,RegistrationForm,UserProfileForm
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from users.models import User
from django.http import Http404
from django.views import View




class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm

    def get_success_url(self) -> str:
        return reverse("signin")
    
class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                print("logged in successfully..........")
                return redirect("index")
            
        print("error in login")
        messages.error(request,"invalid login credentials")
        return render(request,"login.html",{"form":form})
    
class IndexView(CreateView,ListView):
    template_name="index.html"
     #create and list post view in the index page
    form_class=UserProfileForm
    model=User
    context_object_name="data"

    def form_valid(self, form) :
        #form.instance ponits to postform user
        form.instance.user=self.request.user
        return super().form_valid(form)
  
    #after create sucessfully, the url needs to redirect to another view.so below fun implimented
    def get_success_url(self) -> str:
        return reverse("index")
    
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    

class RbacCreateView(View):
    def get(self,request,*args,**kwargs):
        form=UserProfileForm()
        return render(request,"Rbac_create.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=UserProfileForm(request.POST,files=request.FILES)
        if form.is_valid():
                # form.instance.user=request.user
                form.save()
                messages.success(request,"....new data created successfully....")
                return redirect('list-all')
        else:
                messages.error(request,"....error on create new data....")
                return render(request,"Rbac_create.html",{"form":form})
            


class RbacListView(View):
    def get(self,request,*args,**kwargs):
        qs=User.objects.all
        return render(request,"index.html",{"data":qs})
    
class RbacUpdateView(View):
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        obj=User.objects.get(id=id)
        form=UserProfileForm(instance=obj)
        return render(request,"rbac-update.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=User.objects.get(id=id)
        form=UserProfileForm(request.POST,instance=obj,files=request.FILES)
        if (form.is_valid()):
            form.save()
            messages.success(request,"data updated successfully....")
            return redirect("list-all")
        else:
            messages.error(request,"can't update data....error...")
            return render(request,"rbac-update.html",{"form":form})
        
        
class RbaceDelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        User.objects.get(id=id).delete()
        messages.success(request,"selected  data deleted successfully....")

        #we have to redirect to list view name of list view in urls.py is: mobile-all
        return redirect("list-all")
    



# class RbaceDelete(View):
#     def get(self, request, *args, **kwargs):
#         # Get the user id from URL
#         user_id = kwargs.get("pk")
        
#         # Check if the current user is an admin or has the delete permission
#         if not request.user.is_authenticated or not request.user.is_staff:
#             # If the user is not authenticated or not an admin, deny access
#             messages.error(request, "You do not have permission to perform this action.")
#             return redirect('list-all')

#         try:
#             # Get the user to be deleted
#             user_to_delete = User.objects.get(id=user_id)

#             # Delete the user
#             user_to_delete.delete()

#             # Success message
#             messages.success(request, "Selected data deleted successfully.")

#         except User.DoesNotExist:
#             # If the user does not exist
#             messages.error(request, "User not found.")

#         # Redirect to the 'list-all' view after deletion
#         return redirect("list-all")
