"""dreamventure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name="index"),
    path('services', views.serv , name="serv"),
    path('contact_us', views.cont_us , name="cont_us"),
    path('log', views.login , name="login"),
    path('reg', views.reg , name="register"),
    path('reg_company', views.reg_company , name="register_company"),
    path('reg_student', views.reg_student , name="register_student"),
    path('all_type', views.all_type, name="all_type"),
    path('comp_it', views.comp_it, name="comp_it"),
    path('digit_mrkt', views.digit_mrkt, name="digit_mrkt"),
    path('desigin', views.desigin, name="desigin"),
    path('accessories', views.accessories, name="accessories"),
    path('about_us', views.about_us, name="about_us"),
    path('career', views.career, name="career"),
    path('srch_rslt', views.srch_rslt, name="srch_rslt"),
    path('services', views.services, name="services"),
    path('privacy_policy', views.privacy_policy, name="privacy_policy"),
    path('reset_password',views.reset_password,name="reset_password"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
