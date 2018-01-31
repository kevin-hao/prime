#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse

from .models.servers import Server
from .models.business import Business


from .forms import BusinessAddForm, BusinessUpdateForm

def GetServer(request):
    hostslist = Server.objects.all()
    return render(request, 'falcon/servers_list.html', {'hosts': hostslist})

# 业务视图
def BusinessAdd(request):
    form = BusinessAddForm(request.POST)
    if form.is_valid():
        name = request.POST.get('name',)
        Busi = Business.objects.filter(name=name).first()
        if Busi is None:
            Busi = Business(name=name)
            Busi.save()
        return HttpResponseRedirect(reverse('falcon:serverlist'))
    return render(request, 'falcon/business_add.html',{'form':form})

def BusinessList(request):
    businesslist = Business.objects.all()
    return render(request,'falcon/businesslist.html', {'businesslist':businesslist})

def BusinessUpdate(request, business_id):
    business = get_object_or_404(Business, id=business_id)
    if request.method == 'POST':
        form = BusinessUpdateForm(request.POST,instance=business)
        if form.is_valid():
            business = form.save(commit=False)
            business.save()
            return HttpResponseRedirect(reverse('falcon:listbusiness'))
    form = BusinessUpdateForm(instance=business)
    return render(request, 'falcon/businessupdate.html', {'form': form })
