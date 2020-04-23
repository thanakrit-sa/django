from django.shortcuts import render
# from django.http import HttpResponse


def hello(request):
    catagory = ['น้ำตก','ภูเขา','ทะเล','ใกล้เมือง']
    rating = 4
    return render(request, 'index.html',
                  {
                      'name': 'บทความการท่องเที่ยว',
                      'lastname': 'ธนากฤต สหชาติชัย',
                      'tage': catagory,
                      'rating': rating
                  })
