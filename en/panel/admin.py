from django.contrib import admin

# Register your models here.
from .models import HomeSlider, Project, Plans, OurTeam

admin.site.register(HomeSlider)

admin.site.register(Project)

admin.site.register(Plans)

admin.site.register(OurTeam)
