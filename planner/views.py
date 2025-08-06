from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect

def home(request):
    if request.method == 'POST':
        destination = request.POST.get('destination')
        days = request.POST.get('days')

        # Redirect to /plan/ with data in query string
        return redirect(f'/plan/?destination={destination}&days={days}')

    return render(request, 'planner/home.html')
