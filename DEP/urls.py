"""DEP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
removed no need for send post script command
    re_path('^run-sh/$', views.api_command_method, name='run_sh'),
"""
from django.contrib import admin
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    re_path('^admin/', admin.site.urls),
    re_path('^logout/?$', views.logout_method, name='logout_method'),
    re_path('^login/?$', views.login_method, name='login_method'),
    re_path('^add/?$', views.add_method, name='add_method'),
    re_path('^remove/?$', views.remove_method, name='remove_method'),
    re_path('^modular/?$', views.modular_method, name='modular_method'),
    re_path('^apply/?$', views.apply_method, name='apply_method'),
    re_path('^get_json/?$', views.get_json_method, name='get_json_method'),
    re_path('^$', views.main_method, name='main_method'),
    re_path('^add_device/?$', views.add_device_method, name='add_device_method'),
    re_path('^remove_device/?$', views.remove_device_method, name='remove_device_method'),
    re_path('^show_devices/?$', views.show_devices_method, name='show_devices_method'),
    re_path('^api_command/?$', views.api_command_method, name='api_command_method'),
    re_path('^service_status/?$', views.service_status_method, name='service_status_method'),
    re_path('^system_journal/?$', views.system_journal_method, name='system_journal_method'),
    re_path('^webhook/?$', views.webhook_method, name='webhook_method'),
    re_path('^manifest/?$', views.manifest_method, name='manifest_method'),
    re_path('^enroll/?$', views.enroll_method, name='enroll_method'),
    re_path('^no_perm/?$', views.no_perm_method, name='no_perm_method'),
    re_path('^munkireport/?$', views.munkireport_method, name='munkireport_method'),
    re_path('^munkimanifest/?$', views.munkimanifest_method, name='munkimanifest_method'),
    re_path('^munkipkginfo/?$', views.munkipkginfo_method, name='munkipkginfo_method'),
    re_path('^howto/?$', views.howto_method, name='howto_method'),
    re_path('^renewmdm/?$', views.renewmdm_method, name='renewmdm_method'),
    re_path('^setupdep/?$', views.setupdep_method, name='setupdep_method'),
    re_path('^regional_fleet/?$', views.regional_fleet_method, name='regional_fleet_method'),
    re_path('^managed_profiles/?$', views.managed_profiles_method, name='managed_profiles_method'),
    re_path('^asus/?$', views.asus_method, name='asus_method'),
    re_path('^vpp/?$', views.vpp_method, name='vpp_method'),
    re_path('.*', views.not_present_method, name='not_present_method'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    