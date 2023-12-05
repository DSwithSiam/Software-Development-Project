from django.shortcuts import render
from datetime import datetime  

# Create your views here.
def homepage(request):
    
    school = {
        'school_name': 'TPI',
        'dipertment': ['cse','eee', 'cs', 'food'],
        
        'teacher':[
             {'name': 'Rofik', 'age': 23},
             {'name': 'Siam', 'age': 24},
             {'name': 'lamim', 'age': 25},
             {'name': 'Tuser', 'age': 26},
             {'name': 'Akbor', 'age': 27},
             {'name': 'Joni', 'age': 28},
             {'name': 'Mimi', 'age': 29},
             {'name': 'Topu', 'age': 30},
        ],
              
        'student': {
            '1': {'name': 'Tamim', 'roll': 1},   
            '2': {'name': 'Hamim', 'roll': 2},   
            '3': {'name': 'Famim', 'roll': 3},   
            '4': {'name': 'Mou', 'roll': 4},   
            '5': {'name': 'Tuba', 'roll': 5},   
            '6': {'name': 'Muhi', 'roll': 6},   
            '7': {'name': 'Marium', 'roll': 7},   
        },
    }
    p = {
        'text': ' “I’m Jai”',
        'text2': 'my name is tamim',
        'datetime': datetime.now(),
        'emptytext': "",
        'number': 12,
        'list': [1,2,3,4,5,6,7,8,9,10],
        'value': 123452345,
        'text3': 'It is used to join a list with a string',
        'multiline': """ ONE 
                        TWO 
                        THREE""",
        
        
        
        
        
    }
    return render(request, 'index.html', {'school': school, 'p': p})