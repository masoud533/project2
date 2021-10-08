from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import TemplateView

from .models import HomeSlider, Plans


# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        slider_list = HomeSlider.objects.order_by('-pub_date')[:5]
        print(len(slider_list))
        context = {
            'slider_list': slider_list,
        }
        return render(request, 'panel/index.html', context)


class AboutPageView(TemplateView):
    template_name = "panel/about.html"


class ServicesPageView(TemplateView):
    def get(self, request, **kwargs):
        plans_list = Plans.objects.order_by('-pub_date')
        for plan in plans_list:
            plan.feature = plan.feature.split('\r\n')
        context = {
            'plans_list': plans_list,
        }
        return render(request, 'panel/services.html', context)



class OtherServicesPageView(TemplateView):
    template_name = "panel/other-services.html"


class WorkPageView(TemplateView):
    template_name = "panel/work.html"


class ContactPageView(TemplateView):
    template_name = "panel/contact.html"


class PortfolioPageView(TemplateView):
    template_name = "panel/portfolio.html"


class PaymentPageView(TemplateView):
    template_name = "panel/payment.html"
