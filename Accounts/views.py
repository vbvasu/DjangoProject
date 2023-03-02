from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Accounts.models import Education, Skill, UserProfile, Project

# Create your views here.
def register(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=Username):
                messages.error(request,"Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.error(request,"Email already in Use")
                return redirect('register')
            else:    
                myuser = User.objects.create_user(Username,email,password1)
                myuser.first_name=f_name
                myuser.last_name=l_name
                myuser.save()
                messages.success(request,"Your Account has been successfully created.")
                return redirect('signin')
        else:
            messages.error(request,"Password Mismatch")
            return redirect('register')
    else:
        return render(request,'login.html')


def signin(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password1 = request.POST['pass1']
        user = authenticate(username=Username,password=password1)
        if user is not None:
            login(request, user)
            x=User.objects.get(username=Username)
            return render(request,'Useraccount.html',{'name': x.first_name+" "+x.last_name })
        else:
            messages.error(request,"Wrong Username or Password")
            return redirect('signin')
    else:
        return render(request,'login.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return render(request,'login.html')

@login_required
def UserDetails(request):
    if request.method == 'POST':
        country = request.POST['country']
        profession = request.POST['profession']
        about = request.POST['about']
        gitlink = request.POST['gitlink']
        linkedin = request.POST['linkedin']
        insta = request.POST['instalink']
        phno  = request.POST['phno']
        cloud = request.POST['cloud']
        cloud_skills = request.POST['cskills']
        programming = request.POST['programming']
        programming_skills = request.POST['pskills']
        os = request.POST['os']
        os_skills = request.POST['osskills']
        database = request.POST['database']
        database_skills = request.POST['dbskills']
        tools = request.POST['tools']
        tools_skills = request.POST['toolsskills']
        highest_edu = request.POST['highest-edu']
        if highest_edu == 'pg':
            pg_field = request.POST['pg-field']
            pg_univ = request.POST['pg-univ']
            pg_city = request.POST['pg-city']
            pg_year = request.POST['pg-year']
            pg_percent = request.POST['pg-percent']

            ug_field = request.POST['ug-field']
            ug_univ = request.POST['ug-univ']
            ug_city = request.POST['ug-city']
            ug_year = request.POST['ug-year']
            ug_percent = request.POST['ug-percent']

            tlv_field = request.POST['12th-field']
            tlv_univ = request.POST['12th-school']
            tlv_city = request.POST['12th-city']
            tlv_year = request.POST['12th-year']
            tlv_percent = request.POST['12th-percent']

            ten_univ = request.POST['10th-school']
            ten_city = request.POST['10th-city']
            ten_year = request.POST['10th-year']
            ten_percent = request.POST['10th-percent']
            try:
                edu = Education.objects.get(user=request.user)
                edu.highest_edu=highest_edu
                edu.pg_field=pg_field 
                edu.pg_univ=pg_univ 
                edu.pg_city=pg_city
                edu.pg_year=pg_year
                edu.pg_percent=pg_percent
                edu.ug_field=ug_field
                edu.ug_univ=ug_univ
                edu.ug_city=ug_city
                edu.ug_year=ug_year
                edu.ug_percent=ug_percent
                edu.tlv_field=tlv_field
                edu.tlv_univ=tlv_univ
                edu.tlv_city=tlv_city
                edu.tlv_year=tlv_year
                edu.tlv_percent=tlv_percent
                edu.ten_univ=ten_univ
                edu.ten_city=ten_city
                edu.ten_year=ten_year
                edu.ten_percent=ten_percent
                edu.save()
            except Education.DoesNotExist:
                edu = Education.objects.create(user=request.user ,highest_edu=highest_edu, pg_field=pg_field, pg_univ=pg_univ, pg_city=pg_city, pg_year=pg_year, pg_percent=pg_percent,
                            ug_field=ug_field,ug_univ=ug_univ,ug_city=ug_city,ug_year=ug_year,ug_percent=ug_percent,
                            tlv_field=tlv_field,tlv_univ=tlv_univ,tlv_city=tlv_city,tlv_year=tlv_year,tlv_percent=tlv_percent,
                            ten_univ=ten_univ,ten_city=ten_city,ten_year=ten_year,ten_percent=ten_percent)
                edu.save()

        elif highest_edu == 'ug':
            # Retrieve data for Undergraduate education
            ug_field = request.POST['ug-field']
            ug_univ = request.POST['ug-univ']
            ug_city = request.POST['ug-city']
            ug_year = request.POST['ug-year']
            ug_percent = request.POST['ug-percent']

            tlv_field = request.POST['12th-field']
            tlv_univ = request.POST['12th-school']
            tlv_city = request.POST['12th-city']
            tlv_year = request.POST['12th-year']
            tlv_percent = request.POST['12th-percent']

            ten_univ = request.POST['10th-school']
            ten_city = request.POST['10th-city']
            ten_year = request.POST['10th-year']
            ten_percent = request.POST['10th-percent']
            try:
                edu = Education.objects.get(user=request.user)
                edu.highest_edu=highest_edu
                edu.ug_field=ug_field
                edu.ug_univ=ug_univ
                edu.ug_city=ug_city
                edu.ug_year=ug_year
                edu.ug_percent=ug_percent
                edu.tlv_field=tlv_field
                edu.tlv_univ=tlv_univ
                edu.tlv_city=tlv_city
                edu.tlv_year=tlv_year
                edu.tlv_percent=tlv_percent
                edu.ten_univ=ten_univ
                edu.ten_city=ten_city
                edu.ten_year=ten_year
                edu.ten_percent=ten_percent
                edu.save()
            except Education.DoesNotExist:
                edu = Education.objects.create(user=request.user ,highest_edu=highest_edu,
                                               ug_field=ug_field,ug_univ=ug_univ,ug_city=ug_city,ug_year=ug_year,ug_percent=ug_percent,
                                               tlv_field=tlv_field,tlv_univ=tlv_univ,tlv_city=tlv_city,tlv_year=tlv_year,tlv_percent=tlv_percent,
                                               ten_univ=ten_univ,ten_city=ten_city,ten_year=ten_year,ten_percent=ten_percent)
                edu.save()

        elif highest_edu == '12th':
            # Retrieve data for Intermediate education
            tlv_field = request.POST['12th-field']
            tlv_univ = request.POST['12th-school']
            tlv_city = request.POST['12th-city']
            tlv_year = request.POST['12th-year']
            tlv_percent = request.POST['12th-percent']

            ten_univ = request.POST['10th-school']
            ten_city = request.POST['10th-city']
            ten_year = request.POST['10th-year']
            ten_percent = request.POST['10th-percent']
            try:
                edu = Education.objects.get(user=request.user)
                edu.highest_edu=highest_edu
                edu.tlv_field=tlv_field
                edu.tlv_univ=tlv_univ
                edu.tlv_city=tlv_city
                edu.tlv_year=tlv_year
                edu.tlv_percent=tlv_percent
                edu.ten_univ=ten_univ
                edu.ten_city=ten_city
                edu.ten_year=ten_year
                edu.ten_percent=ten_percent
                edu.save()
            except Education.DoesNotExist:
                edu = Education.objects.create(user=request.user ,highest_edu=highest_edu,
                                               tlv_field=tlv_field,tlv_univ=tlv_univ,tlv_city=tlv_city,tlv_year=tlv_year,tlv_percent=tlv_percent,
                                               ten_univ=ten_univ,ten_city=ten_city,ten_year=ten_year,ten_percent=ten_percent)
                edu.save()


        elif highest_edu == '10th':
            # Retrieve data for 10th class education
            ten_univ = request.POST['10th-school']
            ten_city = request.POST['10th-city']
            ten_year = request.POST['10th-year']
            ten_percent = request.POST['10th-percent']
            try:
                edu = Education.objects.get(user=request.user)
                edu.highest_edu=highest_edu
                edu.ten_univ=ten_univ
                edu.ten_city=ten_city
                edu.ten_year=ten_year
                edu.ten_percent=ten_percent
                edu.save()
            except Education.DoesNotExist:
                edu = Education.objects.create(user=request.user ,highest_edu=highest_edu,
                                               ten_univ=ten_univ,ten_city=ten_city,ten_year=ten_year,ten_percent=ten_percent)
                edu.save()
           
        else:   
            pass
        num_projects = 0
        for key in request.POST:
            if key.startswith('Category'):
                num_projects += 1
        for i in range(num_projects):
            project_category =  request.POST.get("Category" + str(i+1))
            project_name = request.POST.get("projectName" + str(i+1))
            project_description = request.POST.get("projectDescription" + str(i+1))
            project_picture = request.FILES.get("projectPicture" + str(i+1))
            project_link = request.POST.get("projectLink" + str(i+1))
            project = Project.objects.create(user = request.user,
                                         project_category=project_category,
                                         project_name=project_name,
                                         project_description=project_description,
                                         project_picture=project_picture,
                                         project_link=project_link)
            project.save()
        cofee = request.POST['cofee']
        certificationno = request.POST['certificationno']
        skillsno = request.POST['skillsno']
        Resume = request.FILES.get('Resume')
        profilepic = request.FILES.get('Profilepic')
        logopic = request.FILES.get('logopic')
        backpic = request.FILES.get('backpic')
        try:
            # Try to get an existing user profile object for this user
            user_profile = UserProfile.objects.get(user=request.user)
            # If a user profile exists for this user, update it with new values
            user_profile.Country = country
            user_profile.Profession = profession
            user_profile.Description = about
            user_profile.Github_link = gitlink
            user_profile.Linkedin_link = linkedin
            user_profile.Instagram_link = insta
            user_profile.Phone_number = phno
            user_profile.Skill_no = skillsno
            user_profile.Certification_no = certificationno
            user_profile.Cofee_no = cofee
            user_profile.Resume = Resume
            user_profile.profile_picture = profilepic
            user_profile.logo_picture = logopic
            user_profile.background_picture = backpic
            user_profile.save()
        except UserProfile.DoesNotExist:
            user_profile = UserProfile.objects.create(
            user=request.user,
            Country= country,
            Profession= profession,
            Description= about,
            Github_link= gitlink,
            Linkedin_link=linkedin,
            Instagram_link=insta,
            Phone_number=phno,
            Skill_no=skillsno,
            Certification_no=certificationno,
            Cofee_no=cofee,
            Resume = Resume,
            profile_picture = profilepic,
            logo_picture = logopic,
            background_picture = backpic,
            )
            user_profile.save()
        if cloud == 'yes':
            Skill.objects.create(
                    user=request.user,
                    skill_type='cloud',
                    skill_name=cloud_skills.strip()
                )
        if programming == 'yes':
            Skill.objects.create(
                    user=request.user,
                    skill_type='programming',
                    skill_name=programming_skills.strip()
                )
        if os == 'yes':
            Skill.objects.create(
                    user=request.user,
                    skill_type='os',
                    skill_name=os_skills.strip()
                )
        if database == 'yes':
            Skill.objects.create(
                    user=request.user,
                    skill_type='database',
                    skill_name=database_skills.strip()
                )
        if tools == 'yes':
            Skill.objects.create(
                    user=request.user,
                    skill_type='tools',
                    skill_name=tools_skills.strip()
                )
        return redirect('Final')

@login_required
def Final(request):
    profile = UserProfile.objects.get(user=request.user)
    user = request.user
    education = Education.objects.get(user=request.user)
    project = Project.objects.filter(user=request.user)
    skills = Skill.objects.filter(user=request.user)
    a = {}
    for skill in skills:
        skill_name_list = skill.skill_name.split(',')
        if skill.skill_type not in a:
            a[skill.skill_type] = []
        a[skill.skill_type].extend(skill_name_list)
    contents = {'profile':profile,'user':user,'education':education,'project':project,'skill':skills,'a':a}
    return render(request,'Profile.html',context=contents)


        
                

            
           
    

   