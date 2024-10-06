from django.shortcuts import render,redirect
import csv

def student_view(request):
    students = []
    with open(r'C:\Users\ganes\OneDrive\Desktop\training\student_data.txt', 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            students.append(row)  
    
    
    context = {
        'students': students
      
    }

    return render(request,'student.html',context)


