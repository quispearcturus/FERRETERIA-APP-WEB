from django.shortcuts import render, redirect, get_object_or_404


class CreateUpdateViewMx:
    model = None
    form_class = None
    template_name = None
    success_url = None
    success_url_id = False

    def get(self, request, pk=None):
        if pk:
            obj = get_object_or_404(self.model, pk=pk)
            form_obj = self.form_class(instance=obj)
        else:
            form_obj = self.form_class()

        context = self.get_context_data(obj_form=form_obj, is_editing = pk is not None, pk = pk, obj=obj if pk else None)
        return render(request, self.template_name, context)

    def post(self, request, pk=None):
        if pk:
            obj = get_object_or_404(self.model, pk=pk)
            form_obj = self.form_class(request.POST, instance=obj)
        else:
            form_obj = self.form_class(request.POST)

        if form_obj.is_valid():
            return self.form_valid(form_obj)

        context = self.get_context_data(obj_form=form_obj, is_editing = pk is not None, pk = pk, obj=obj if pk else None)
        return render(request, self.template_name, context)

    def form_valid(self, form):
        obj_form = form.save(commit=False)
        obj_form.save()
        if self.success_url_id:
            return redirect(self.success_url, pk=obj_form.pk)
        else:
            return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = {
            **kwargs,
        }
        return context

