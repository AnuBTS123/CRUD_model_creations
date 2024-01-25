from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q


def display_topics(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')
    QLTO=Topic.objects.all().order_by(Length('topic_name'))
    QLTO=Topic.objects.all().order_by(Length('topic_name').desc())
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.filter(topic_name__startswith='b')
    QLTO=Topic.objects.filter(topic_name__endswith='t')
    QLTO=Topic.objects.filter(topic_name__contains='a')
    d={'QLTO':QLTO}
    return render(request,'display_topics.html',d)



def display_webpages(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('topic_name')
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-topic_name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('topic_name'))
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    QLWO=Webpage.objects.all()[2:5:]
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(name__startswith='j')
    QLWO=Webpage.objects.filter(name__endswith='n')
    QLWO=Webpage.objects.filter(name__contains='a')
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(topic_name='cricket',name__endswith='t')
    QLWO=Webpage.objects.filter(Q(topic_name='cricket') | Q(url__endswith='in'))
    QLWO=Webpage.objects.filter(Q(topic_name='cricket') & Q(url__endswith='in'))
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpages.html',d)



def display_accessrecords(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.all().order_by('author')
    QLAO=AccessRecord.objects.all().order_by('name')
    QLAO=AccessRecord.objects.all().order_by('-author')
    QLAO=AccessRecord.objects.all().order_by('-name')
    QLAO=AccessRecord.objects.all().order_by(Length('author'))
    QLAO=AccessRecord.objects.all().order_by(Length('name'))
    QLAO=AccessRecord.objects.all().order_by(Length('author').desc())
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(date__month__gt='10')
    QLAO=AccessRecord.objects.filter(date__month__gte='4')
    QLAO=AccessRecord.objects.filter(date__month__lt='2000')
    QLAO=AccessRecord.objects.filter(date__month__lte='6')
    QLAO=AccessRecord.objects.filter(date__year__gte='2020')
    QLAO=AccessRecord.objects.filter(date__day__gt='10')
    QLAO=AccessRecord.objects.filter(author__startswith='j')
    QLAO=AccessRecord.objects.filter(author__endswith='n')
    QLAO=AccessRecord.objects.filter(author__contains='a')
    d={'QLAO':QLAO}
    return render(request,'display_accessrecords.html',d)



def insert_topic(request):
    tn=input('enter topic name')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    return render(request,'display_topics.html')



def insert_webpages(request):
    tn=input('enter topic name')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    TO=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    NWO.save()
    return render(request,'display_webpages.html')



def insert_accessrecords(request):
    pk=int(input('enter pk value of webpage'))
    a=input('enter author')
    d=input('enter date')
    WO=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    NAO.save()
    return render(request,'display_accessrecords.html')

def update_webpage(request):
    #Webpage.objects.filter(topic_name='cricket').update(name='Rohit')
    #Webpage.objects.filter(topic_name='Basketball').update(name='min yongi')
    #Webpage.objects.update_or_create(topic_name='Football',defaults={'name':'messi'})
    CTO=Topic.objects.get_or_create(topic_name='Rugby')[0]
    CTO.save()
    Webpage.objects.update_or_create(topic_name=CTO,defaults={'name':'jungkook'})
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpages.html',d)
