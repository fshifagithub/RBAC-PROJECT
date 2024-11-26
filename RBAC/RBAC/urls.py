"""
URL configuration for RBAC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("index",views.IndexView.as_view(),name="index"),
    path("create",views.RbacCreateView.as_view(),name="item-create"),
    path('listall',views.RbacListView.as_view(),name="list-all"),
    path("logout",views.SignOutView.as_view(),name="signout"),
    path('rbac/<int:pk>/update',views.RbacUpdateView.as_view(),name="rbac-update"),
    path('rbac/<int:pk>/update',views.RbaceDelete.as_view(),name="rbac-delete")
]
