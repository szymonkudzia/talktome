from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'(?:^$)|(?:#/login/(?:true)|(?:false))', 'python.views.default', name='default'),
    url(r'^service/login', 'python.services.login', name='login_service'),
	url(r'^service/register', 'python.services.register', name='login_service'),
    url(r'^service/localization', 'python.services.localization', name='localization_service'),
	url(r'^service/confirm', 'python.services.confirm', name='confirm'),
	url(r'^service/changePassword', 'python.services.changePassword', name='change_password'),
    # url(r'^TalkToMe/', include('TalkToMe.TalkToMe.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
