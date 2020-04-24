from django.shortcuts import render
# from django.http import HttpResponse


def hello(request):
    # catagory = ['น้ำตก', 'ภูเขา', 'ทะเล', 'ใกล้เมือง']
    # rating = 4
    # return render(request, 'index.html',
    #               {
    #                   'name': 'บทความการท่องเที่ยว',
    #                   'lastname': 'ธนากฤต สหชาติชัย',
    #                   'tage': catagory,
    #                   'rating': rating
    #               })
    return render(request,'index.html')


def on(request):
    return render(request, 'page1.html')

def writetopic(request):
    return render(request,'writetopic.html')

def result(request):
    name = request.POST['nametopic']
    description = request.POST['description']
    return render(request,'result.html',{'name':name,'description':description})
