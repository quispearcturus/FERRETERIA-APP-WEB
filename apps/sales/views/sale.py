import json
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View

from apps.templifys.builders.table import WidgetTable
from apps.templifys.views.viewmx import CreateUpdateViewMx
from apps.sales.models.sale import Sale, SaleDetail
from apps.sales.models.voucher import SerieVoucher, NumerationVoucher
from apps.sales.forms.sale import SaleForm

from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class SaleListView(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'sales/sale_list.html'
    context_object_name = 'sale_list'
    # paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        queryall = (Q(customer__icontains=query),
                    Q(customer__icontains=query))
        queryset = Sale.objects.filter(reduce(OR, queryall))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_table'] = WidgetTable(context)
        return context



class SaleCreateUpdateView(LoginRequiredMixin, View, CreateUpdateViewMx):
    model = Sale
    form_class = SaleForm
    template_name = 'sales/sale_form.html'
    success_url = 'sales:sale_list'

    def gen_numeration(self, id):
        get_serie_voucher = SerieVoucher.objects.filter(pk=id).first()
        last_number = NumerationVoucher.objects.filter(serie_voucher=get_serie_voucher).order_by('-number').first()
        gen_number = last_number.number + 1 if last_number else 1
        return gen_number, get_serie_voucher

    def create_numeration(self):
        id =  self.request.GET.get('type_voucher') if self.request.GET.get('type_voucher') is not None else 1
        n, serie = self.gen_numeration(id)
        obj_numeration = NumerationVoucher.objects.create(serie_voucher=serie, number=n)
        return obj_numeration
    
    # def get(self, request, pk=None, *args, **kwargs):
    #     response = super().get(request, pk, *args, **kwargs)
        
    #     return response
    
    def get_serie_voucher(self):
        return SerieVoucher.objects.filter(serial_status=True)

    def form_valid(self, form):
        from decimal import Decimal
        new_detail = False
        detail_sales = eval(self.request.POST.get('datos'))
        obj_form = form.save(commit=False)
        if obj_form.pk is None:
            new_detail = True
            new_nv = self.create_numeration()
            obj_form.numeration_voucher = new_nv
        obj_form.save()
        if new_detail:
            for detail in detail_sales:
                SaleDetail.objects.create(sale_id=obj_form.id, product_id=detail['id'], quantity=int(detail['quantity']), unit_price=Decimal(detail['unit_price']))
            new_detail = False
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if kwargs.get('pk'):
            s, n = kwargs.get('obj').get_serie_number()
        else:
            id =  self.request.GET.get('type_voucher') if self.request.GET.get('type_voucher') is not None else 1
            n, s = self.gen_numeration(id)
        context['numeration'] = n
        context['serial'] = s.serial_number
        context['type_vouchers'] = self.get_serie_voucher()
        return context


from apps.products.models.product import Product
class ProductAutocompleteView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        queryall = (Q(profile_steels_product__name_origin__icontains=query),
                    # Q(customer__icontains=query)
        )
        queryset = Product.objects.filter(reduce(OR, queryall))
        data_query = []
        for obj in queryset:
            data_query.append({
                'id': obj.id,
                'name': obj.__str__(),
            })
        return JsonResponse(data_query, safe= False)