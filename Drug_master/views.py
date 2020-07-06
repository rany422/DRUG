from django.shortcuts import render, redirect,get_object_or_404
from .models import Drug_Master, Generic_Information
from .forms import ProductForm, Generic_InformationForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse ,QueryDict, JsonResponse


def createdrug(request):
    company_name = request.POST.get('company_name')
    brand_name = request.POST.get('brand_name')
    dosage_type = request.POST.get('dosage_type')
    dosage_form = request.POST.get('dosage_form')
    schedule_type = request.POST.get('schedule_type')
    sheif_life = request.POST.get('sheif_life')
    speciality = request.POST.get('speciality')
    HSN_CODE = request.POST.get('HSN_CODE')
    drug_indication = request.POST.get('drug_indication')
    warning = request.POST.get('warning')
    gst = request.POST.get('gst')
    print(company_name, brand_name, dosage_type, dosage_form, schedule_type, sheif_life, speciality, HSN_CODE, drug_indication, warning, gst)
    qs = Drug_Master.objects.create(company_name=company_name, brand_name=brand_name, dosage_type=dosage_type, dosage_form=dosage_form, schedule_type=schedule_type, sheif_life=sheif_life, speciality=speciality, HSN_CODE=HSN_CODE, drug_indication=drug_indication,warning=warning, gst=gst)
    context = {"message":qs.id}
    return JsonResponse(context)


def list_display(request):
    data = request.GET
    min_date = data.get('minDate', None)
    max_date = data.get('maxDate', None)
    context = {}
    products_list = Drug_Master.objects.all()
    if(min_date):
        products_list = products_list.filter(publish_date__gte=min_date)
    
    if(max_date):
        products_list = products_list.filter(publish_date__lte=max_date)
   
    context['minDate']= min_date if min_date else ""
    context['maxDate']= max_date if max_date else ""
    context['products_list'] = products_list
    return render(request, 'dashboard.html', context) 
def new_DrugMaster(request):
    generic_list= Generic_Information.objects.all()
    product_form = ProductForm()
    generic_form = Generic_InformationForm()

    content= {}
    if request.method=='POST': 
        company_name = request.GET('company_name')
        product_form = ProductForm(request.POST)
        generic_form = Generic_InformationForm(request.POST)
        if product_form.is_valid():  
            product = product_form.save(commit=False)
            generic_form = Generic_InformationForm(request.POST)

            if generic_form.is_valid():
                generic_form.product_form=product_form
                generic_form.save()
                product_form.save()
        else:
            product_form = ProductForm()
            generic_form = Generic_InformationForm()

    context = {
        'product_form': product_form,
        'generic_form' : generic_form,
        'generic_list' : generic_list,
    }   
    return render(request, 'new_master.html', context)  


def edit_drug(request, id):
    product = Drug_Master.objects.get(id=id)
    return render(request, 'edit_drug.html', {'product':product})


def edit_generic(request, id):
    item = Generic_Information.objects.get(id=id)
    return render(request, 'edit_generic.html', {'item':item})

def update_drug(request, id):
    product = Drug_Master.objects.get(id=id)
    form = ProductForm(request.POST, instance = product)
    if form.is_valid():
        form.save()
        return redirect('/drug_master', messages.success(request, 'Module is successfully updated.', 'alert-success'))
    return render(request, 'edit_drug.html', {'product': product}) 
       

def update_generic(request, id):
    item = Generic_Information.objects.get(id=id)
    form = Generic_InformationForm(request.POST, instance = item)
    if form.is_valid():
        form.save()
        return redirect('/add_new', messages.success(request, 'Module is successfully updated.', 'alert-success'))
    return render(request, 'edit_generic.html', {'item': item})        
def destroy_drug(request, id):
    product = Drug_Master.objects.get(id=id)
    if request.method =='POST':
        product.delete()
        messages.success(request, 'Deleted succesfully')

        return redirect('/drug_master')
    return render(request, 'delete.html') 

def destroy_generic(request, id):
    item = Generic_Information.objects.get(id=id)
    if request.method =='POST':
        item.delete()
        messages.success(request, 'deleted succesfully')
        return redirect('/add_new')

