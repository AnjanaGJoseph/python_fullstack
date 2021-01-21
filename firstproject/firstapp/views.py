from django.shortcuts import render
from django.shortcuts import HttpResponse
import math 
# Create your views here.

def index(request):
    return render(request,'page.html')
 


def index2(request):
    st = request.POST["box2"]
    ans = math.ceil(math.log2(int(st)))
    ans = str(ans)
    res = "<h1>" + ans + "rats are required" "</h1>"
    return HttpResponse(res)
    
def index3(request):
    st = request.POST["box3"]
    if(st==st[::-1]):
        st += "is a Palindrome"
    else:
        st += "is not a Palindrome"
    st = "<h1>" + st + "</h1>"
    return HttpResponse(st)

#def index4(request):
#    st = request.POST["box1"]
#   ls = list(map(int,st.split(' ')))
#   even,odd = [],[]
#    for i in ls:
#        if i%2 == 0:
#            even.append(str(i))
#        else:
#            odd.append(str(i))
#        even = ' '.join(even)
#        odd = ' '.join(odd)
#        res = "<h1>" +even+"are even nos."
#        res += "<br>"
#        res += odd+ "are odd nos."
#        res += "</h1>"
#        return HttpResponse(res)



    




