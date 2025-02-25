from django.shortcuts import render, get_object_or_404
from .models import Skills

# Create your views here.
def skills_list(request):
    skills = Skills.objects.all()
    return render(request, 'skills/skill-list.html',{"skills":skills})

def skills_detail(request,skill_id):
    skill = get_object_or_404(Skills,id=skill_id)
    certifications = skill.certifications.all()
    projects = skill.projects.all()
    return render(request,'skills/skill-detail.html',{'skill':skill,'certifications':certifications,'projects':projects})
