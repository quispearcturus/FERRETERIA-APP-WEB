import os
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from django.conf import settings
from io import BytesIO
from xhtml2pdf import pisa

class GeneratePDFView(View):
    model = None
    template_name = None
    obj_name = 'obj'

    def get(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        template = get_template(self.template_name)
        context = {
            self.obj_name: obj,
        }
        html = template.render(context)
        result = BytesIO()
        ticket_width = 80  # 80mm
        ticket_height = 200  # 200mm
        pdf = pisa.CreatePDF(
            html,
            dest=result,
            encoding='utf-8',
            link_callback=lambda uri, rel: self._fetch_resources(uri, rel),
            pageSize=(ticket_width * 2.83465, ticket_height * 2.83465)
        )
        if pdf.err:
            return HttpResponse('Error generating PDF')
        pdf_content = result.getvalue()
        response = HttpResponse(content_type='application/pdf')
        name_pdf = f'{obj.__str__()}.pdf'
        response['Content-Disposition'] = f'inline; filename={name_pdf}'
        response.write(pdf_content)
        return response

    def _fetch_resources(self, uri, rel):
        if uri.startswith(settings.STATIC_URL):
            path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
            if os.path.exists(path):
                return path
        elif uri.startswith(settings.MEDIA_URL):
            path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
            if os.path.exists(path):
                return path

        return None
    
    def reduce_word(self, prayer):
        sum_text = 0
        letters = ""
        for word in prayer.split():
            sum_text += len(word)
            if sum_text < 40:
                letters += word + " "
            elif sum_text > 40:
                letters += word[0] + "."
        return letters
    

from apps.sales.models.sale import Sale
class SalePDFView(GeneratePDFView):
    model = Sale
    template_name = 'sales/sale_pdf.html'
    obj_name = 'obj_sale'