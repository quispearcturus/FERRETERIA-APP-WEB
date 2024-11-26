import json
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from apps.products.models.profilesteel import ProfileSteel, TypeProfileSteel
from apps.products.models.steel import Steel
from apps.products.models.welding import Welding
from apps.products.models.product import Product
from apps.products.forms.product import ProductForm, WeldingForm, ProfileSteelForm


from apps.templifys.builders.base import Scoreboard
# views.py


class ProductCountView(LoginRequiredMixin, TemplateView):
    # template_name = 'products/index.html'
    template_name = 'products/test.html'

    def get_steel_count(self):
        data_count = []
        for s in Steel.objects.all():
            data_count.append(
                {"name":s.__str__(), "value": ProfileSteel.objects.filter(steel=s).count()}
            )
        return json.dumps(data_count)
    
    def get_sales(self):
        from django.utils import timezone
        from datetime import timedelta
        from apps.sales.models.sale import Sale
        hoy = timezone.now().date()
        r = Sale.objects.filter(date_sale__date=hoy).count()
        return r
    
    def get_stock(self):
        from django.db.models import F
        from apps.branches.models.stock import Stock
        count = Stock.objects.filter(total_quantity__lt=F('min_stock')).count()
        return count
    
    def get_cash(self):
        from django.utils import timezone
        from apps.sales.models.sale import Sale
        hoy = timezone.now().date()
        objetos = Sale.objects.filter(date_sale__date=hoy)
        a = 0
        for obj in objetos:
            a += obj.total
        return a
    
    def get_brach(self):
        from apps.branches.models.branch import Branch
        r = Branch.objects.filter(branch_status=True).count()
        return r
    
    
    def get_products_sale(self):
        from django.db.models import Sum
        from apps.sales.models.sale import SaleDetail
        from django.utils import timezone
        hoy = timezone.now().date()
        from django.db.models import Prefetch
        productos_prefetch = Product.objects.all()
        detalles = (SaleDetail.objects
            .filter(sale__date_sale__date=hoy)
            .prefetch_related(Prefetch('product', queryset=productos_prefetch))
            .values('product')
            .annotate(cantidad_total=Sum('quantity')))
        
        data = []
        for detalle in detalles:
            producto = detalle['product']
            data.append({'name': Product.objects.get(id=producto).__str__(), 'value': detalle['cantidad_total']})

        return json.dumps(data)
        

    def get_context_data(self, **kwargs):
        # print(Scoreboard().render())
        context = super().get_context_data(**kwargs)
        data = [
            {"name": "Metal", "value": ProfileSteel.objects.count()},
            {"name": "Welding", "value": Welding.objects.count()},
        ]
        
        context['data'] = json.dumps(data)
        context['steel'] = self.get_steel_count()
        context['sales'] = self.get_products_sale()
        context['menu_active'] = 'dashboard'
        context['obj_stock'] = Scoreboard({'name': 'Stock Alerts', 'value': f'# { self.get_stock() }', 'icon': 'report_problem', 'color': 'red'}).render()
        context['obj_sale'] = Scoreboard({'name': 'Sales', 'value': f'# { self.get_sales() }', 'icon': 'shopping_cart', 'color': 'blue' }).render()
        context['obj_cash'] = Scoreboard({'name': 'Cash', 'value': f'S/ { self.get_cash() }', 'icon': 'attach_money', 'color': '#4b147c' }).render()
        context['obj_branch'] = Scoreboard({'name': 'Branches', 'value': f'# { self.get_brach() }', 'icon': 'business', 'color': '#4f894e' }).render()
        return context


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products_list'
    paginate_by = 7

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_active'] = 'products'
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = {
            'id': self.object.id,
            'datar': self.object.__str__(),
            'name': 'namer',
            'description': 'description',
        }
        return JsonResponse(data)


class DynamicRelationModel():
    model = None
    classes_model_form = []

    related_names = []

    def get_related_names(self):
        obj_meta = self.model._meta

        for field in obj_meta.get_fields():
            if field.is_relation and field.related_name:
                self.related_names.append(field.related_name)
        return self.related_names

    def relation_model(self, pk):
        try:
            query = self.model.objects.get(id=pk)
        except self.model.DoesNotExist:
            return None, None

        for related_name in self.get_related_names():
            related_instance = getattr(query, related_name, None)
            if related_instance is not None:
                model_obj, form_obj = self.model_classes[related_instance.__class__.__name__]
                # return related_name, related_instance.__class__.__name__
                return model_obj, form_obj
        return None, None

    def change_form(self, model_str):
        model_obj, form_obj = self.model_classes[model_str]
        return form_obj

    def get_fields(self):
        # all_fields = []
        # for field in ProfileSteel._meta.get_fields():
        #     all_fields.append(field.name)
        #     # print(f'  Campo: {field.name} - Tipo: {field.get_internal_type()}')
        # print(all_fields)
        pass
        # self.change_form('ProfileSteel')


class ProductCreateUpdateView(View, DynamicRelationModel):
    model = Product
    model_classes = {
        'ProfileSteel': (ProfileSteel, ProfileSteelForm),
        'Welding': (Welding, WeldingForm),
    }
    
    def runner(self):
        all_fields = []
        for field in Welding._meta.get_fields():
            all_fields.append(field.name)
            # print(f'  Campo: {field.name} - Tipo: {field.get_internal_type()}')
        print(all_fields)

    def get(self, request, pk=None, *args, **kwargs):
        # self.runner()
        if pk:
            product = get_object_or_404(Product, pk=pk)
            model_obj, form_obj = self.relation_model(pk=pk)
            obj_get = get_object_or_404(model_obj, product=product)
            obj_form = form_obj(instance=obj_get)

            self.get_fields()
        else:  # Creación
            type_pro = request.GET.get('type_products')
            if type_pro is None:
                type_pro = 'ProfileSteel'
            retry_form = self.change_form(type_pro)
            obj_form = retry_form()
            
        return render(request, 'products/product_form.html', {
            'obj_form': obj_form,
            'is_editing': pk is not None
        })

    def post(self, request, pk=None, *args, **kwargs):
        if pk:  # Editando
            product = get_object_or_404(Product, pk=pk)
            model_obj, form_obj = self.relation_model(pk=pk)
            obj_get = get_object_or_404(model_obj, product=product)
            obj_form = form_obj(request.POST, instance=obj_get)
        else:  # Creando
            # product = Product.objects.create()
            type_pro = request.GET.get('type_products')
            if type_pro is None:
                type_pro = 'ProfileSteel'
            retry_form = self.change_form(type_pro)
            obj_form = retry_form(request.POST)

        if obj_form.is_valid():
            if pk is None:
                product = Product.objects.create()
            obj_sub = obj_form.save(commit=False)
            obj_sub.product = product
            obj_sub.save()
            return redirect(reverse_lazy('products:product_list'))

        return render(request, 'products/product_form.html', {
            'obj_form': obj_form,
            'is_editing': pk is not None
        })
