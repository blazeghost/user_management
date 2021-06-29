from typing import ContextManager
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .models import *

# Create your views here.


def LoginPage(request):
    return render(request, 'app/login.html')


def RegisterPage(request):
    return render(request, 'app/register.html')


def Register(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    password = request.POST['password']
    cpass = request.POST['cpassword']
    role = request.POST['role']

    testuser = Master_Table.objects.filter(Email=email)
    if testuser:
        message = "User is already exist"
        return render(request, "app/register.html", {'msg': message})
    else:
        if password == cpass:
            masteruser = Master_Table.objects.create(
                Email=email, Password=password, Role=role)
            user = User.objects.create(
                m_id=masteruser, Firstname=fname, Lastname=lname)

            message = "User Successfully Registered"
            return render(request, "app/register.html", {'msg': message})
        else:
            message = "Password and Confirm Password doesnot match"
            return render(request, "app/register.html", {'msg': message})


def Login(request):
    if request.POST['role'] == "Admin":
        email = request.POST['email']
        password = request.POST['password']

        testuser = Master_Table.objects.get(Email=email)

        if testuser:
            if testuser.Password == password and testuser.Role == "Admin":
                user = User.objects.get(m_id=testuser)

                request.session['Role'] = testuser.Role
                request.session['id'] = testuser.id
                request.session['is_verified'] = testuser.is_verified
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Email'] = testuser.Email

                return render(request, "app/index.html")

            else:
                message = "User Password or Role Doesnot match"
                return render(request, "app/login.html", {'msg': message})

        else:
            message = "User not Found"
            return render(request, "app/login.html", {'msg': message})

    else:
        if request.POST['role'] == "Security":
            email = request.POST['email']
            password = request.POST['password']

            testuser = Master_Table.objects.get(Email=email)

            if testuser:
                if testuser.Password == password and testuser.Role == "Security":
                    user = User.objects.get(m_id=testuser)

                    request.session['Role'] = testuser.Role
                    request.session['id'] = testuser.id
                    request.session['is_verified'] = testuser.is_verified
                    request.session['Firstname'] = user.Firstname
                    request.session['Lastname'] = user.Lastname
                    request.session['Email'] = testuser.Email

                    return render(request, "app/index.html")

                else:
                    message = "User Password or Role Doesnot match"
                    return render(request, "app/login.html", {'msg': message})

            else:
                message = "User not Found"
                return render(request, "app/login.html", {'msg': message})


def IndexPage(request):
    return render(request, 'app/index.html')


def Logout(request):

    del request.session['Role']
    del request.session['id']
    del request.session['Firstname']
    del request.session['Lastname']
    del request.session['Email']
    del request.session['is_verified']

    return render(request, "app/login.html")


def Blank(request):
    return render(request, 'app/blank_copy.html')


def Profile(request, pk):
    m_data = Master_Table.objects.get(id=pk)
    u_data = User.objects.get(m_id=m_data)

    context = {
        'key1': u_data
    }
    return render(request, 'app/profile.html', context)


def VisitorDetails(request):
    return render(request, 'app/visitor_details.html')


def VisitorList(request):
    data_one = Table_one.objects.all()
    data_two = Table_two.objects.all()

    context = {
        'key1': data_one,
        'key2': data_two

    }
    return render(request, 'app/visitor_list.html', context)


def AddVisitor(request, pk):
    m_data = Master_Table.objects.get(id=pk)
    user = User.objects.get(m_id=m_data)

    role = request.POST['role']

    if role == 'Admin':
        vname = request.POST['v_name']
        vpurpose = request.POST['v_purpose']
        vcontact = request.POST['v_contact']
        concern_person = request.POST['concerned_p']
        datetime = request.POST['date_time']

        data_one = Table_one.objects.create(a_id=user, visitor_name=vname, visitor_purpose=vpurpose,
                                            visitor_contact=vcontact, concerned_person=concern_person, date_time=datetime)

        msg = "Success"
        return render(request, 'app/visitor_details.html', {'keymsg': msg})

    elif role == 'Security':
        vname = request.POST['v_name']
        vpurpose = request.POST['v_purpose']
        vcontact = request.POST['v_contact']
        concern_person = request.POST['concerned_p']
        datetime = request.POST['date_time']

        vaddress = request.POST['v_address']
        v_vechicle = request.POST['v_vechicle']

        data_two = Table_two.objects.create(s_id=user, visitor_name=vname, visitor_purpose=vpurpose,
                                            visitor_contact=vcontact, visitor_address=vaddress, visitor_vehicle_number=v_vechicle, concerned_person=concern_person, date_time=datetime)

        msg = "Success"
        return render(request, 'app/visitor_details.html', {'keymsg': msg})


def AdminEditPage(request, pk):
    data_one = Table_one.objects.get(id=pk)
    # data_two = Table_two.objects.get(id=pk)

    context = {
        'key1': data_one,
        # 'key2': data_two,
    }

    return render(request, 'app/visitor_edit.html', context)


def SecurityEditPage(request, pk):
    # data_one = Table_one.objects.get(id=pk)
    data_two = Table_two.objects.get(id=pk)

    context = {
        # 'key1': data_one,
        'key2': data_two,
    }

    return render(request, 'app/visitor_edit.html', context)


def AdminEditVisitor(request, pk):
    # m_data = Master_Table.objects.get(id=pk)
    # user = User.objects.get(m_id=m_data)
    data = Table_one.objects.get(id=pk)
    data.visitor_name = request.POST['v_name']
    data.visitor_purpose = request.POST['v_purpose']
    data.visitor_contact = request.POST['v_contact']
    data.concerned_person = request.POST['concerned_p']
    data.date_time = request.POST['date_time']

    print("-------------->>", data.visitor_name)

    data.save()
    url = f'/admineditpage/{pk}'

    return redirect(url)


def SecurityEditVisitor(request, pk):
    # m_data = Master_Table.objects.get(id=pk)
    # user = User.objects.get(m_id=m_data)
    data = Table_two.objects.get(id=pk)
    data.visitor_name = request.POST['v_name']
    data.visitor_purpose = request.POST['v_purpose']
    data.visitor_contact = request.POST['v_contact']
    data.concerned_person = request.POST['concerned_p']
    data.date_time = request.POST['date_time']
    data.visitor_address = request.POST['v_address']
    data.visitor_vehicle_number = request.POST['v_vechicle']

    data.save()

    url = f'/securityeditpage/{pk}'

    return redirect(url)


def AdminDelete(request, pk):
    data = Table_one.objects.get(id=pk)
    data.delete()
    return HttpResponseRedirect(reverse('visitorlist'))


def SecurityDelete(request, pk):
    data = Table_two.objects.get(id=pk)
    data.delete()
    return HttpResponseRedirect(reverse('visitorlist'))
