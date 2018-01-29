#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

def Index(request):
    return render(request,'../templates/index.html')