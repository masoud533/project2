from django.urls import path, re_path

from . import views

urlpatterns = [

    # # ex: /
    path(r'', views.HomePageView.as_view(), name='home'),

    # # ex: /about
    path(r'about/', views.AboutPageView.as_view(), name='about'),

    # # ex: /services
    path(r'services/', views.ServicesPageView.as_view(), name='services'),

    # # ex: /other-services
    path(r'other-services/', views.OtherServicesPageView.as_view(), name='other-services'),

    # # ex: /work
    path(r'work/', views.WorkPageView.as_view(), name='work'),

    # # ex: /contact
    path(r'contact/', views.ContactPageView.as_view(), name='contact'),

    # # ex: /portfolio
    path(r'portfolio/', views.PortfolioPageView.as_view(), name='portfolio'),

    # # ex: /payment
    path(r'payment/', views.PaymentPageView.as_view(), name='payment'),

    # # ex: /project
    path(r'project/', views.ProjectPageView.as_view(), name='project'),

]
