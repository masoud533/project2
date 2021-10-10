from django.contrib import admin

# Register your models here.
from .models import HomeSlider, Project, Plans, OurTeam, WhoWeAre, WhatWeDo, WorkProcess, OurSkills, BodySlider, \
    FooterSwiper, About, FeedBack, OtherWorkProcess

admin.site.register(HomeSlider)

admin.site.register(BodySlider)

admin.site.register(FooterSwiper)

admin.site.register(Project)

admin.site.register(FeedBack)

admin.site.register(About)

admin.site.register(Plans)

admin.site.register(OurTeam)

admin.site.register(WorkProcess)

admin.site.register(OtherWorkProcess)

admin.site.register(WhatWeDo)

admin.site.register(WhoWeAre)

admin.site.register(OurSkills)
