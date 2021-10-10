from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import TemplateView

from .models import HomeSlider, Plans, Project, OurTeam, WhoWeAre, WorkProcess, WhatWeDo, OurSkills, BodySlider, \
    FooterSwiper, About, FeedBack, OtherWorkProcess


# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        slider_list = HomeSlider.objects.order_by('-pub_date')[:5]
        body_slider_list = BodySlider.objects.order_by('-pub_date')[:5]
        project_list = Project.objects.order_by('-pub_date')[:5]
        team_members = OurTeam.objects.order_by('pk')
        what_we_do = WhatWeDo.objects.order_by('pk')[:5]
        work_process = WorkProcess.objects.order_by('pk')[:4]
        our_skills = OurSkills.objects.order_by('pk')[:5]
        for skill in our_skills:
            skill.feature = skill.feature.split('\r\n')[:3]

        wo_we_are = WhoWeAre.objects.order_by('pk')[0]
        wo_we_are.Strategy = wo_we_are.Strategy.split('\r\n')
        wo_we_are.Development = wo_we_are.Development.split('\r\n')
        footer_swiper = FooterSwiper.objects.get(id=1)
        context = {
            'slider_list': slider_list,
            'body_slider_list': body_slider_list,
            'project_list': project_list,
            'team_members': team_members,
            'wo_we_are': wo_we_are,
            'what_we_do': what_we_do,
            'work_process': work_process,
            'our_skills': our_skills,
            'footer_swiper': footer_swiper,

        }
        return render(request, 'panel/index.html', context)


class ProjectPageView(TemplateView):
    def get(self, request, **kwargs):
        project_id = request.GET.get('id')
        project = Project.objects.get(id=project_id)
        context = {
            'project': project
        }
        return render(request, 'panel/project_01.html', context)


class AboutPageView(TemplateView):
    def get(self, request, **kwargs):
        about = About.objects.order_by('-pk')[:5]
        footer_swiper = FooterSwiper.objects.get(id=1)
        feed_back = FeedBack.objects.order_by('-pk')
        team_members = OurTeam.objects.order_by('pk')
        our_skills = OurSkills.objects.order_by('pk')[:5]
        for skill in our_skills:
            skill.feature = skill.feature.split('\r\n')[:3]

        context = {
            'about': about,
            'footer_swiper': footer_swiper,
            'feed_back': feed_back,
            'team_members': team_members,
            'our_skills': our_skills,

        }
        return render(request, 'panel/about.html', context)


class ServicesPageView(TemplateView):
    def get(self, request, **kwargs):
        plans_list = Plans.objects.order_by('-pub_date')
        footer_swiper = FooterSwiper.objects.get(id=1)
        work_process = WorkProcess.objects.order_by('pk')[:4]

        for plan in plans_list:
            plan.feature = plan.feature.split('\r\n')
        context = {
            'plans_list': plans_list,
            'footer_swiper': footer_swiper,
            'work_process': work_process,

        }
        return render(request, 'panel/services.html', context)


class OtherServicesPageView(TemplateView):
    def get(self, request, **kwargs):
        work_process = OtherWorkProcess.objects.order_by('pk')[:4]

        context = {
            'work_process': work_process,

        }
        return render(request, 'panel/other-services.html', context)

class WorkPageView(TemplateView):
    template_name = "panel/work.html"


class ContactPageView(TemplateView):
    template_name = "panel/contact.html"


class PortfolioPageView(TemplateView):
    def get(self, request, **kwargs):
        project_list = Project.objects.order_by('-pub_date')[:5]

        context = {
            'project_list': project_list,
        }
        return render(request, 'panel/portfolio.html', context)


class PaymentPageView(TemplateView):
    def get(self, request, **kwargs):
        project_id = request.GET.get('id')
        plans = Plans.objects.get(pk=project_id)
        context = {
            'plans': plans,
        }
        return render(request, 'panel/payment.html', context)
