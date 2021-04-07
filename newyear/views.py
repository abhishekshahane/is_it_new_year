from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    x = datetime.now()
    if x.month==1 and x.day==1:
        new_year = "Yes."
        title = "It is the new year."
    else:
        new_year = "No."
        title = "It isn't the new year."
    return render(request, "newyear/index.html", {
        "year": new_year, 
        "title": title
    })