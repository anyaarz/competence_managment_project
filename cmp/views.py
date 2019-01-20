from django.shortcuts import render, render_to_response,redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse,Http404
from .models import User, Employee,Job,Knowledge,Proficiency,Skills
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.utils import timezone
from django.views import generic
from .forms import UserRegistrationForm,EmployeeForm, JobForm, KnowledgeForm, ProficiencyForm, SkillsForm
from django.contrib.auth.decorators import login_required, permission_required 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_employee=Employee.objects.all().count()
    num_job=Job.objects.all().count()
    num_knowledge=Knowledge.objects.all().count()
    num_proficiency = Proficiency.objects.all().count()
    num_skills = Skills.objects.all().count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_employee':num_employee,'num_job':num_job,'num_knowledge':num_knowledge,'num_proficiency':num_proficiency, 'num_skills':num_skills},
    )

@login_required   
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Employee.objects.create(user=new_user)
            return render(
                    request,
                    'cmp/profile.html',
                    context={'employee':profile},
    )
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})
'''
@login_required
def edit(request):
    try:
        profile = request.user.employee
    except Employee.DoesNotExist:
        profile = Employee(user = request.user)
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = EmployeeForm(instance=profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = Employee(instance=profile)
        return render(request,
                      'registration/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})
'''
@login_required
def competences(request):

    knowledge=Knowledge.objects.all()
    proficiency = Proficiency.objects.all()
    skills = Skills.objects.all()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'cmp/competences.html',
        context={'knowledge':knowledge,'proficiency':proficiency, 'skills':skills},
    )

@login_required
@permission_required('cmp.can_add_employee','cmp.can_change_employee','cmp.can_delete_employee')
def post_new(request):
    if not request.user.is_authenticated():
        return render(request, 'registration/login.html')
    else:
        form = EmployeeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user
            employee.avatar = request.FILES['avatar']
            file_type = employee.alvatar.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'employee': employee,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'cmp/post_new.html', context)
            employee.save()
            return render(request, 'cmp/profile.html', {'employee': employee})
        context = {
            "form": form,
        }
        return render(request, 'cmp/post_new.html', context)


'''
@login_required
@permission_required('cmp.can_add_employee','cmp.can_change_employee','cmp.can_delete_employee')
def post_new(request):
    #if request.user.is_staff():
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save(commit=False)
            form.save()
            employee.avatar = request.FILES['avatar']
            file_type = employee.avatar.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'employee': employee,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
            return redirect('/employees/')
    else:
        form = EmployeeForm()
    #else: 
     #   raise Http404("У вас нет прав!")
    return render(request, 'cmp/post_edit.html', {'form': form})
'''
@login_required
def profile(request,pk):
    
    employee = get_object_or_404(Employee, pk=pk)
    #employee = request.user.employee
    job = Job.objects.all()

    return render(
        request,
        'cmp/profile.html',
        context={'employee':employee,'job':job},
    )

@login_required
@permission_required('cmp.can_add_employee','cmp.can_change_employee','cmp.can_delete_employee')
def post_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.avatar = request.FILES['avatar']
            file_type = employee.avatar.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'employee': employee,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'cmp/post_new.html', context)
        
            form.save()

            return redirect('/employees/')
    else:
        form = EmployeeForm(instance = employee)
    return render(request, 'cmp/post_edit.html', {'form': form})

@login_required
@permission_required('cmp.can_add_job','cmp.can_change_job','cmp.can_delete_job')
def post_new_job(request):
    #if request.user.is_staff():
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            form.save()
            return redirect('/jobs/')
    else:
        form = JobForm()
    #else: 
     #   raise Http404("У вас нет прав!")
    return render(request, 'cmp/post_edit_j.html', {'form': form})

@login_required
@permission_required('cmp.can_add_employee','cmp.can_change_employee','cmp.can_delete_employee')
def post_edit_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save(commit=False)
            form.save()
            return redirect('/jobs/')
    else:
        form = JobForm(instance = job)
    return render(request, 'cmp/post_edit_j.html', {'form': form})

@login_required
def post_new_k(request):
    #if request.user.is_staff():
    if request.method == "POST":
        form = KnowledgeForm(request.POST)
        if form.is_valid():
            knowledge = form.save(commit=False)
            form.save()
            return redirect('/competences/')
    else:
        form = KnowledgeForm()

    return render(request, 'cmp/post_edit_zun.html', {'form': form})

@login_required
def post_new_p(request):
    #if request.user.is_staff():
    if request.method == "POST":
        form = ProficiencyForm(request.POST)
        if form.is_valid():
            proficiency = form.save(commit=False)
            form.save()
            return redirect('/competences/')
    else:
        form = ProficiencyForm()
    #else: 
     #   raise Http404("У вас нет прав!")
    return render(request, 'cmp/post_edit_zun.html', {'form': form})

@login_required
def post_new_s(request):
    #if request.user.is_staff():
    if request.method == "POST":
        form = SkillsForm(request.POST)
        if form.is_valid():
            skills = form.save(commit=False)
            form.save()
            return redirect('/competences/')
    else:
        form = SkillsForm()
    #else: 
     #   raise Http404("У вас нет прав!")
    return render(request, 'cmp/post_edit_zun.html', {'form': form})


@login_required
def post_edit_p(request, pk):
    proficiency = get_object_or_404(Proficiency, pk=pk)
    if request.method == "POST":
        form = ProficiencyForm(request.POST, instance=proficiency)
        if form.is_valid():
            proficiency = form.save(commit=False)
            form.save()
            return redirect('/competences/')
    else:
        form = ProficiencyForm(instance = proficiency)
    return render(request, 'cmp/post_edit_zun.html', {'form': form})
@login_required
def post_edit_s(request, pk):
    skills = get_object_or_404(Skills, pk=pk)
    if request.method == "POST":
        form = SkillsForm(request.POST, instance=skills)
        if form.is_valid():
            skills = form.save(commit=False)
            form.save()
            return redirect('/competences/')
    else:
        form = ProficiencyForm(instance = skills)
    return render(request, 'cmp/post_edit_zun.html', {'form': form})
@login_required
def post_edit_k(request, pk):
    knowledge = get_object_or_404(Knowledge, pk=pk)
    if request.method == "POST":
        form = KnowledgeForm(request.POST, instance=knowledge)
        if form.is_valid():
            knowledge = form.save(commit=False)
            form.save()
            return redirect('/competences/')
    else:
        form = KnowledgeForm(instance = knowledge)
    return render(request, 'cmp/post_edit_zun.html', {'form': form})


#@login_required
#@permission_required('cmp.can_change_employee')
class EmployeesListView(generic.ListView):
    model = Employee
    def get_queryset(self):
        return Employee.objects.all()

#@login_required
#@permission_required('is_staff')
class JobsListView(generic.ListView):
    model = Job
    
    def get_queryset(self):
        return Job.objects.all()



