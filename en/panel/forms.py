from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['pub_date']
        # fields = ['title', 'header_image', 'thumbnail', 'header_text', 'content']
