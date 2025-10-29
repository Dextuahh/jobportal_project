from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Job
from .forms import JobForm

class JobListView(ListView):
    model = Job
    template_name = 'jobs/organism/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 10

class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/organism/job_detail.html'
    context_object_name = 'job'

class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/organism/job_form.html'

class JobUpdateView(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/organism/job_form.html'

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'jobs/organism/job_confirm_delete.html'
    success_url = reverse_lazy('jobs:job_list')

# Create your views here.
