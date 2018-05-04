from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
import time
# Create your views here.

class VCommunity(TemplateView):
  template_name="monitor/community.html"
  def get_context_data(self,*args, **kwargs):
    day = time.strftime("%d")
    if(day[0]=='0'): day =day[1:]
    ctx = {
      "day": day,
      "month": time.strftime("%B"),
      "year": time.strftime("%Y"),
    }
    return ctx

class VActions(TemplateView):
  template_name="monitor/actions.html"
  def get_context_data(self,*args, **kwargs):
    day = time.strftime("%d")
    if(day[0]=='0'): day =day[1:]
    ctx = {
      "day": day,
      "month": time.strftime("%B"),
      "year": time.strftime("%Y"),
    }
    return ctx

class VCalendar(TemplateView):
  template_name="monitor/calendar.html"
  def get_context_data(self,*args, **kwargs):
    day = time.strftime("%d")
    if(day[0]=='0'): day =day[1:]
    ctx = {
      "day": day,
      "month": time.strftime("%B"),
      "year": time.strftime("%Y"),
    }
    return ctx

class VStatus(LoginRequiredMixin, TemplateView):
  template_name = "monitor/home.html"
  login_url = 'account:login'

  def adjust_goal(self, value):
    stm = value * 900 / 45000
    return int(stm)
  def adjust_sub_goala(self, value):
    stm = value * 900 / 20000
    return int(stm)
  def adjust_sub_goalb(self, value):
    stm = value * 900 / 14500
    return int(stm)
  def adjust_sub_goalc(self, value):
    stm = value * 900 / 6500
    return int(stm)
  def adjust_sub_goald(self, value):
    stm = value * 900 / 5000
    return int(stm)
  def get_context_data(self,*args, **kwargs):
    consumption_goal = 45000
    consumption_current_month =37500
    consumption_a = 18800
    consumption_b = 11500
    consumption_c = 4200
    consumption_d = 3000
    day = time.strftime("%d")
    if(day[0]=='0'): day =day[1:]
    ctx ={
      "consumption_goal": self.adjust_goal(consumption_goal),
      "consumption": consumption_current_month,
      "consumption_a": consumption_a,
      "consumption_a_goal": self.adjust_sub_goala(consumption_a),
      "consumption_b": consumption_b,
      "consumption_b_goal": self.adjust_sub_goalb(consumption_b),
      "consumption_c": consumption_c,
      "consumption_c_goal": self.adjust_sub_goalc(consumption_c),
      "consumption_d": consumption_d,
      "consumption_d_goal": self.adjust_sub_goald(consumption_d) ,
      "day": day,
      "month": time.strftime("%B"),
      "year": time.strftime("%Y"),
    }
    print(ctx)
    return ctx
