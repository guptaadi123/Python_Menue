#!/usr/bin/env python
# coding: utf-8

# In[2]:





# In[3]:





# In[5]:


import os
import pyttsx3
pyttsx3.speak("hello how may i help you")
while True:
  pyttsx3.speak("Enter command u want me to open or type quite for quite")
  a=input("Enter command u want me to run:")
  print(a)
  b=a.lower()
  if ("run" in b) and("aws" in b):
    print("To make key press1\nTo make security group press 2\nTo get information of your security group press 3\nTo Add ingress rule to you security group press 4\nTo launch the EBS volume press 5\nTo attach Ebs volume to your instance press 6\nTo Launch instance press7")
    pyttsx3.speak("Enter option u want me to configure")
    option=input("Select the option you want\n")
    if option == '1':
            key_name=input("your_key_name\n")
            a="aws ec2 create-key-pair --key-name {0} --query KeyMaterial --output text > {0}.pem".format(key_name)
            os.system(a)
    elif option == '2':
            sgname=input("Secrity group name\n")
            description=input("Descript (optiona)")
            b= "aws ec2 create-security-group --group-name {0} --description {1}".format(sgname,description)
            os.system(b)
    elif option == '3':
            sgname=input("Secrity group name\n")
            c="aws ec2 describe-security-groups --groups-name {0}".format(sgname)
            os.system(c)
    elif option == '4':
            grpid=input("Enter group id\n")
            protocol=input("Enter protocol\n")
            port=input("Enter port number\n")
            cidr=input("Cidr value\n")  
            d="aws ec2 authorize-security-group-ingress --group-id {0} --protocol    {1} --port {2} --cidr {3}".format(grpid,protocol,port,cidr)
            os.system(d)
    elif option == '5':
            volumetype=input("Volume type you want\n")
            size=input("Size you want\n")
            Avalzone=input("Avaiblity zone\n")
            e="aws ec2 create-volume --volume-type {} --size {} --availability-zone  {}".format(volumetype,size,Avalzone)
            os.system(e)
    elif option == '6':
            volumename=input("Volume id\n")
            instid=input("Instance id\n")
            devname=input("devicename eg(/dev/sdf)\n")
            f="aws ec2 attach-volume --volume-id {} --instance-id {} --device {}".format(volumename,instid,devname)
            os.system(f)
    elif option == '7':
            sgname=input("Secrity group id\n")
            instance_type=input("instance type(egt2micro)\n")
            amiid=input("ami id\n")
            key=input("key name\n")
            count=input("No of instances you want to launch\n")
            subnetid=input("subnetid\n")
            g="aws ec2 run-instances --security-group-ids   {0}   --instance-type {1} --image-id {2}  --key-name {3}  --count {4} --subnet-id {5}".format(sgname,instance_type,amiid,key,count,subnetid)
            os.system(g)  
  elif ("configure" in b) and("lvm" in b):
        i=0
        e=[]
        remove_content = ["'", "[", "]",","]
        while True:
            s=i=1+i
            pyttsx3.speak("Please insert the Physical disk name or q to exit")
            a=input("Please insert the Physical disk name or q to exit\n")
            print(s)
            if (a=='q'):
                break;
            else:
                e.append(a)
        n=input("Enter volume name\n")
        my_str = repr(e)
        for content in remove_content:
            my_str = my_str.replace(content, '')
        vg=("vgcreate  {1} {0}".format(my_str,n))
        os.system(vg)
        a=input("lv name you want to give\n")
        b=input("size\n")
        lv=("lvcreate --name {0} --size {1} {2}".format(a,b,n))
        os.system(lv)
  elif ("configure" in b) and("yum" in b):
        pyttsx3.speak("YUM CONFIGURATION IS UNDER PROCESS")
        yum_status=sp.getstatusoutput("yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
        if yum_status[0] == 0 :
            pyttsx3.speak("configured yum")
        else:
            pyttsx3.speak("error in configureation")
  elif ("configure" in b) and ("docker"in b) :
        pyttsx3.speak("WELCOME TO DOCKER SERVICES")
        present_docker=sp.getstatusoutput("docker --version")
        if (present_docker[0] != 0):
            pyttsx3.speak("DOWNLOADING DOCKER SERVICES")
            s=download_docker=sp.getstatusoutput("yum install docker-ce --nobest")
            if(s[0] == 0):
                pyttsx3.speak("successfullly installed docker")
            else:
                print(s[1])
                exit()
        status_docker=sp.getstatusoutput("systemctl is-active docker.services")
        if(status_docker[1] == 'inactive'):
            s=input(" do u want to start docker : ")
            if ('yes' in s) or ('start' in s) :
                sp.getstatusoutput("systemctl start docker.services")
            else:
                exit()
        pyttsx3.speak("do u want to run an instance in docker")
        checker=input("enter your choice")
        if("yes" in checker):
            cmd=""
            enter=input("Enter os name and tag")
            if ("centos" in enter):
                sp.getstatusoutput("docker run -it centos:latest")
            elif ("fedora" in enter):
                sp.getstatusoutput("docker run -it fedora:latest")
            else:
                print("{} is not available ".format(enter))
                print("pulling image from docker hub")
                sp.getstatusoutput("docker pull {}".format(enter))
                sp.getstatusoutput("docker run -it {}".format(enter))
  elif ("quit" in b) :
    pyttsx3.speak("Hope you like the service byy")
    break;
    

    


# In[10]:





# In[ ]:




