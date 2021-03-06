"""sundayfunday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from sundayfunday.views import index
from sundayfunday.views import user
from sundayfunday.views import register
from sundayfunday.views import event

#admin.autodiscover()

urlpatterns = [
    url(r'^$', index.UserHomePageView.as_view(), name='home'),
    url(r'^login/$', user.LoginView.as_view(), name='login'),
    url(r'^logout/$', user.LogoutView.as_view(), name='logout'),
    url(r'^register/', register.RegisterUserView.as_view(), name='register'),
    url(r'^addevent/', event.AddEventView.as_view(), name='addevent'),
    url(r'^event/(?P<pk>[0-9]+)/$', event.EventDetailView.as_view(),
        name='event-detail'),
    url(r'^edit/(?P<pk>[0-9]+)/$', user.UserEditView.as_view(),
        name='user-edit'),
    url(r'^edit-event/(?P<pk>[0-9]+)/$', event.EventEditView.as_view(),
        name='edit-event'),
    url(r'^see-upcoming/(?P<pk>[0-9]+)/$', event.SeeUpcomingEventsView.as_view(),
        name='see-upcoming'),
    url(r'^admin/', admin.site.urls),
    url(r'^u/$', index.UserHomePageView.as_view(), name='user-homepage')
]
