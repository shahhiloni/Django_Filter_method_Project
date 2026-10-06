import json 
import os 

from django.shortcuts import render 

def Home(request): 
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), 
        "JSON", 
        "flats.json"
    )

    # // mkdir folder_name

    with open(file_path, "r")as file:
        flats = json.load(file)
    
    search = request.GET.get("search", "")
    if search : 

        flats = [
            flat for flat in flats 

            if search.lower() in flat['name'].lower()
            or search.lower() in flat['category'].lower()
            or search.lower() in flat["area"].lower()
        ]
 
    context = {"flats": flats,
               "search": search }
    
    return render(request, "home.html", context)


