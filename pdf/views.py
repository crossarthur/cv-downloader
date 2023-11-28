from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import io

# Create your views here.


def accept(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm()

    return render(request, 'pdf/accept.html', {'form': form})


def resume(request):
    single = Profile.objects.all()
    return render(request, 'pdf/resume.html', {'single': single})


def resume_view(request,pk):
    row = Profile.objects.get(id=pk)
    template_path = 'pdf/resume_view.html'
    context = {'row': row}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report0.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def resume_download(request, pk):
    row = Profile.objects.get(id=pk)
    template_path = 'pdf/resume_download.html'
    context = {'row': row}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
