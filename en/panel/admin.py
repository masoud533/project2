from django.contrib import admin

# Register your models here.
from .models import HomeSlider, Project, Plans, OurTeam, WhoWeAre, WhatWeDo, WorkProcess, OurSkills

admin.site.register(HomeSlider)

admin.site.register(Project)

admin.site.register(Plans)

admin.site.register(OurTeam)

admin.site.register(WorkProcess)

admin.site.register(WhatWeDo)

admin.site.register(WhoWeAre)

admin.site.register(OurSkills)
