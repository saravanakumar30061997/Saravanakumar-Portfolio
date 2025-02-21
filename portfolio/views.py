from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from . import models

# Create your views here.
def index(request):
    certs = models.PortfolioItem.objects.all().order_by('id')
    paginator = Paginator(certs, 3)  # Show 3 items per page
    page_number = request.GET.get('page')  # Get page number from URL query params
    page_obj = paginator.get_page(page_number)  # Get the paginated page
    return render(request,'portfolio/index.html',{'page_obj': page_obj,'context':certs})

def detail(request,id):
    cert = get_object_or_404(models.PortfolioItem,pk=id)
    return render(request,'portfolio/detail.html',{"context":cert})


