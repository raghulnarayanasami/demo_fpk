from django.shortcuts import render
from myapp.myapp.functions.functions import handle_uploaded_file
from myapp.forms import StudentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import boto3
import os
# Create your views here.

user2=''
def user_login(request):
    global user2
    global user1
    context = {}
    if request.method =="POST":
        username = request.POST['username']
        password=request.POST['password']
        user1=authenticate(request,username=username,password=password)
        if user1:
           login(request, user1)
           return HttpResponseRedirect(reverse('storage'))
        else:
            context['error']="Please provide valid credentials!!!"
            return render(request, 'myapp/index.html', context)

    else:
        return render(request, 'myapp/index.html', context)
            
def get_hostname():
    out = os.popen('hostname').read()
    return str(out)
       
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def storagedata(request):
    data = get_hostname()
    return  render(request, 'myapp/landing.html', {"data":data})

@csrf_exempt
def s3bucket(request):
  
    if request.method == 'POST':
        context = {}
        student = StudentForm(request.POST, request.FILES)
        bucketname = request.POST['bucketname']
        file_obj = request.FILES['file']
        filename = str(file_obj.name)
        if student.is_valid():
            bucket_list = bucketlist()
            for bucket in bucket_list:
                if bucket.name == str(bucketname):
                   context['error']="The Bucket Name already exists.  Choose other Buket Name"
                   return render(request, 'myapp/message.html', context)

            handle_uploaded_file(request.FILES['file'])
            uploadfile = "/root/myapp/static/upload/"+filename
            boto3connection(bucketname, filename, uploadfile)
            context['error']="The New Container is created : " + bucketname + " and The File is Uploaded Successfully in that Bucket"
            return render(request, 'myapp/message.html', context)
    else:
        student = StudentForm()
        return render(request, "myapp/s3.html", {'form': student})

def boto3connection(bucketname, filename, uploadfile):

    host = "https://172.25.200.67"
    access = "14641d0aa03b4998bedf8c39b72c2e62"
    secret = "895cb3ee98b84c919e4362e2082c5f69"
    cert_path = "/root/tcs_ecp_cert/tcsecp.pem"

    s3 = boto3.resource('s3',endpoint_url=host,verify=cert_path,aws_access_key_id=access,aws_secret_access_key=secret)

    s3.create_bucket(Bucket=bucketname)
    s3.Object(bucketname,filename).upload_file(Filename=uploadfile)

def bucketlist():
    host = "https://172.25.200.67"
    access = "14641d0aa03b4998bedf8c39b72c2e62"
    secret = "895cb3ee98b84c919e4362e2082c5f69"
    
    cert_path = "/root/tcs_ecp_cert/tcsecp.pem"

    s3 = boto3.resource('s3',endpoint_url=host,verify=cert_path,aws_access_key_id=access,aws_secret_access_key=secret)
    bucket_list = s3.buckets.all()
    return bucket_list
