from weasyprint import HTML
from django.template.loader import render_to_string
from .models import Package

def generate_pdf(package_id):
    package = Package.objects.get(id=package_id)
    html_string = render_to_string('package_detail_pdf.html', {'package': package})
    html = HTML(string=html_string)
    return html.write_pdf() 