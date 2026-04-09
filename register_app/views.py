from django.shortcuts import render
from django.views.generic import View
from .models import Register
import csv
from django.http import HttpResponse

# Create your views here.
class HomePage(View):
    def get(self, request):
        return render(request, 'home.html')
    def post(self, request):
        return render(request, 'home.html')
    
class DashboardPage(View):
    def get(self, request):
        people = Register.objects.all()
        return render(request, 'dashboard.html', {
            'people': people,
        })
    def post(self, request):
        people = Register.objects.all()
        return render(request, 'dashboard.html', {
            'people': people,
        })
    
def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        schoolname = request.POST.get('schoolname')
        area = request.POST.get('area')

        if fullname == '1' and schoolname == '1' and area == '1':
            people = Register.objects.all()
            return render(request, 'dashboard.html', {
                'people': people,
            })
        else:
            user = Register.objects.create(fullname=fullname, schoolname=schoolname, area=area)
            user.save()
            return render(request, 'success.html')

    return render(request, 'register.html')  # show form on GET

def success(request):
    return render(request, 'success.html')

def export_csv(request):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=registers.csv'

    # 👇 THIS LINE FIXES YOUR PROBLEM
    response.write('\ufeff')

    writer = csv.writer(response)
    
    # Header
    writer.writerow(['Аты-жөні', 'Мектеп Атауы', 'Аймақ'])

    # Data
    for r in Register.objects.all():
        writer.writerow([r.fullname, r.schoolname, r.area])

    return response