from django.shortcuts import render, redirect
from .models import Event, Submission
from django.db.models import Q
from django.template.defaulttags import register
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

@register.filter
@register.filter(name='split')
def split(value, key): 
 
    value.split("key")
    return value.split(key)

# def registerevents(request,):
#     return render(request, 'core/webfusion')

def signup(request):
    return render(request, 'authentication/signup.html')

def signin(request):
    return render(request, 'authentication/signin.html')

def home(request):
    topevents = [9,10]
    data = Event.objects.all().exclude(id__in=topevents)
    topcats = Event.objects.filter(id__in=topevents)
    
    context = {"data": data, "topcats": topcats}
    return render(request, 'core/index.html', context)  

def successfull(request, refid, event):
    return render(request, 'core/successfull.html', {"refid":refid, "event": event})

def closed(request):
    return render(request, 'core/failed.html')

# Events

def wf(request):
    model = Event.objects.get(name="Web Fusion Meet")
    
    if request.method == 'POST':
        if Submission.objects.filter(event=model).count() <= model.limit:
            submit = Submission.objects.create(
                event=model, 
                teamname = request.POST.get('name'),
                participant1 = request.POST.get('name'),
                mail1 = request.POST.get('mail'),
                contact = request.POST.get('contact'),
                )
            return redirect(reverse('successfull', kwargs={"event": submit.event.name, "refid": submit.id}))   
            
        else:
            model.closed = True
            model.save()
            return redirect('/registrationclosed')       
        
    if not model.closed:
        return render(request, "applications/webfusionmeet.html", {"data": model})
    else:
        return redirect('/registrationclosed')       


def bitwisebattle(request):
    model = Event.objects.get(name="Bitwise Battle")
    
    if request.method == 'POST':
        if Submission.objects.filter(event=model).count() <= model.limit:
            submit = Submission.objects.create(
                event=model, 
                teamname = request.POST.get('teamname'),
                participant1 = request.POST.get('p1'),
                mail1 = request.POST.get('e1'),
                participant2 = request.POST.get('p2'),
                mail2 = request.POST.get('e2'),
                
                contact = request.POST.get('contact'),
                )
            
            return redirect(reverse('successfull', kwargs={"event": submit.event.name, "refid": submit.id}))   
            
        else:
            model.closed = True
            model.save()
            
            return redirect('/registrationclosed')   
    if not model.closed:
        return render(request, 'applications/bitwisebattle.html', {"data": model})
    else:
        return redirect('/registrationclosed')
    
def mechmayhem(request):
    model = Event.objects.get(name="Mechanical Mayhem")
    if request.method == 'POST':
        if Submission.objects.filter(event=model).count() <= model.limit:
            submit = Submission.objects.create(
                event=model, 
                teamname = request.POST.get('teamname'),
                participant1 = request.POST.get('p1'),
                mail1 = request.POST.get('e1'),
                participant2 = request.POST.get('p2'),
                mail2 = request.POST.get('e2'),
                participant3 = request.POST.get('p3'),
                mail3 = request.POST.get('e3'),
                
                contact = request.POST.get('contact'),
                )
            
            return redirect(reverse('successfull', kwargs={"event": submit.event.name, "refid": submit.id}))   
            
        else:
            model.closed = True
            model.save()
            
            return redirect('/registrationclosed')   
    return render(request, 'applications/mechmayhem.html', {"data":model})

def designcon(request):
    model = Event.objects.get(name="Design Con")
    return render(request, 'applications/designcon.html', {"data":model})

def blueprintbash(request):
    model = Event.objects.get(name="Blueprint Bash")
    return render(request, 'applications/blueprintbash.html', {"data":model})

def sketchup(request):
    model = Event.objects.get(name="SketchUp")
    return render(request, 'applications/sketchup.html', {"data":model})

def boardbonanza(request):
    model = Event.objects.get(name="Board Bonanza")
    return render(request, 'applications/boardbonanza.html', {"data":model})

def challengeshowcase(request):
    model = Event.objects.get(name="Challenge Showcase")
    return render(request, 'applications/challengeshowcase.html', {"data":model})

def foundersfest(request):
    model = Event.objects.get(name="Founder's Fest")
    return render(request, 'applications/foundersfest.html', {"data" : model})