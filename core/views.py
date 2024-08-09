from django.shortcuts import render, redirect
from .models import Event, Submission
from django.db.models import Q
from django.template.defaulttags import register
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .export import submissionExport
from django.http import HttpResponse

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
    if not model.closed: 
        return render(request, 'applications/mechmayhem.html', {"data":model})
    else:
        return redirect('/registrationclosed')

def designcon(request):
    model = Event.objects.get(name="Design Con")
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
     
    if not model.closed:
        return render(request, 'applications/designcon.html', {"data":model})
    else:
        return redirect('/registrationclosed')


# min team 1, max 3
def blueprintbash(request):
    model = Event.objects.get(name="Blueprint Bash")
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
            
    if not model.closed:
        return render(request, 'applications/blueprintbash.html', {"data":model})
    else:
        return redirect('/registrationclosed')

# min team 1, max 3
def sketchup(request):
    model = Event.objects.get(name="SketchUp")
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
        
    if not model.closed:    
        return render(request, 'applications/sketchup.html', {"data":model})
    else:
        return redirect('/registrationclosed')

#max team 1
def boardbonanza(request):
    model = Event.objects.get(name="Board Bonanza")
    if request.method == 'POST':
        if Submission.objects.filter(event=model).count() <= model.limit:
                submit = Submission.objects.create(
                    event=model, 
                    teamname = request.POST.get('teamname'),
                    participant1 = request.POST.get('p1'),
                    mail1 = request.POST.get('e1'),
                    
                    contact = request.POST.get('contact'),
                    )
                
                return redirect(reverse('successfull', kwargs={"event": submit.event.name, "refid": submit.id}))   
        
        else:
            model.closed = True
            model.save()
    if not model.closed:
        return render(request, 'applications/boardbonanza.html', {"data":model})
    else:
        return redirect('/registrationclosed')


def foundersfest(request):
    model = Event.objects.get(name="Founder's Fest")
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
            
    if not model.closed:
        return render(request, 'applications/foundersfest.html', {"data" : model})
    else:
        return redirect('/registrationclosed')


def challengeshowcase(request):
    model = Event.objects.get(name="Challenge Showcase")
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
    if not model.closed:            
        return render(request, 'applications/challengeshowcase.html', {"data":model})
    else:
        return redirect('/registrationclosed')
    
    
def dataexport(request):
    fielddata = Event.objects.all()
    if request.method == "POST":
        eventname = request.POST.get('eventname')
        queryset = Submission.objects.filter(event__name=eventname)
        obj = submissionExport()
        data = obj.export(queryset)
        
        response = HttpResponse(data.xlsx, content_type='application/ms-excel')
        response['Content-Disposition'] = f"attachment; filename={eventname}_studentdata.xlsx"

        return response
        
    context = {"fields": fielddata}
    return render(request, 'core/export.html', context)