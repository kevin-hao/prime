#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from django.forms import ModelForm, TextInput
from .models import Business

class BusinessAddForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name']
        widgets ={
            'name': TextInput(attrs={'placeholder':'业务名'}),
        }

class BusinessUpdateForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'placeholder': '业务名'}),
        }