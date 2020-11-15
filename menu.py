import os
import subprocess
os.system("clear")
print("\n\n")
print("\t Welcome To The Automatic System  Mangement Service(RHEL-8)\t\t\t")
print("\n")
print("\t--------------------------------------------------------------\n\n\t Here is the Menu:\t\t\n")

print("\t Press 1 to check LVM Software\n\t Press 2 to Know Disk Status\n\t Press 3 to Create a Logical Volume\n\t Press 4 to Increase the Size of Logical Volume\n\t Press 5 to Extend Volume Group\n\t Press 6 to Install AWS CLI\n\t Press 7 to register an IAM User\n\t Press 8 to Create Key,Security Group\n\t Press 9 to Create Volume\n\t Press 10 to add inbound Rules to the Security Group\n\t Press 11 to Create the Instance\n\t Press 12 to Attach Volume with the Instance\n\t Press 13 to Install Docker\n\t Press 14 to Run a command on conatiner without visiting it\n\t Press 15 to launch an OS in docker\n\t Press 16 to Launch HTTPD in docker\n\t Press 17 to Launch Python Interpreter in Docker\n\t Press 18 to Install Software through Yum\n\t Press 19 to Create Partition\n\t Press 20 to Mount a folder\n\t Press 21 to Exit the Menu")

def yum():
	i = input("Please Enter the Name of the Software: ")
	s = "yum install " + i
	os.system(s)

def awsinstall():
	cmd = "curl" + "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" + "-o" +  "awscliv2.zip"
	os.system("yum install curl -y")
	os.system("yum install unzip -y")
	os.system(cmd)
	os.system("unzip awscliv2.zip")
	os.system("sudo ./aws/install")
	print(subprocess.check_output("aws --version",shell=True,universal_newlines=True))
	print("The AWS CLI v2 is now Installed")

def iam():
	print(os.system("aws configure"))
	print("Your IAM User is now registered")

def aws():
	k = input("Please Enter the Key Name: ")
	s = input("Please Enter the Security Group Name: ")
	d = input("Please tell the Description for the Security Group: ")
	v = input("Please Tell the VPC-id: ")
	sec = "aws ec2 create-security-group --group-name " + s + " --description " + d + " --vpc-id " + v
	os.system("aws ec2 create-key-pair --key-name {}".format(k))
	os.system(sec)
	print("Your Key and Security Group is now created.")	
	
def inbound():
	g = input("Please Enter the Security Group Id: ")
	p = input("Please Enter the Protocol: ")
	o = input("Please Enter the Port: ")
	c = input("Please Enter the IP to allow: ")
	rule = "aws ec2 authorize-security-group-ingress --group-id " + g + " --protocol " + p + " --port " + o + " --cidr " + c
	os.system(rule)
	print("Your Security Group Rules are now set")

def instance():
	i = input("Please Enter the Image id: ")
	t = input("Please Enter the Instance Type: ")
	u = input("Please Enter the Number of OS: ")
	b = input("Please Enter the Subnet-id: ")
	g = input("Please Enter the Security Group Id: ")
	k = input("Please Enter the Key Name: ")
	ins = "aws ec2 run-instances --image-id " + i + " --instance-type " + t +  " --count " + u + " --subnet-id " + b +" --security-group-ids " + g + " --key-name " + k
	os.system(ins)

def volume():
	t = input("Please Enter the Volume Type: ")
	s = input("Please Enter the Size of Volume: ")
	r = input("Please Enter the Availability Zone: ")
	vol = "aws ec2 create-volume --volume-type " + t  + "  --size " + s + " --availability-zone " + r
	os.system(vol)
	print("Your Volume is now created")

def attach():
	v = input("Please Enter the Volume id: ")
	i = input("Please Enter the Instance id: ")
	d = input("Please Enter the Device Path: ")
	att = "aws ec2 attach-volume --volume-id " + v + " --instance-id " + i + " --device " + d
	os.system(att)
	print("Your Volume is now attached")

def createlv():
	n = input("Please Enter 1st disk name: ")
	d =input("Please Enter 2nd disk name: ")
	v = input("Please Enter the name for Volume Group: ")
	s = input("Please Enter the Size for Volume Group: ")
	g = input("Please Enter the name for Logical Volume: ")
	k = input("Please Enter the Name of Directory: ")
	first = "pvcreate /dev/" + n
	sec = "pvcreate /dev/" + d
	vol = "vgcreate " + v + " /dev/" + n + " /dev/" + d
	lv = "lvcreate --size " + s + "G" + " --name " + g + " " + v
	form = "mkfs.ext4 /dev/" + v + "/" + g
	dir = "mkdir /" + k
	mou = "mount /dev/"+ v + "/" + g + " " + k
	dis = "lvdisplay " + v + "/" + g
	os.system("yum install lvm2 -y")
	os.system(first)
	os.system(sec)
	os.system(vol)
	os.system(lv)
	os.system(form)
	os.system(dir)
	os.system(mou)
	print(os.system("lsblk"))
	print(os.system(dis))
	print("Your LV is now created")

def lvextend():
	s = input("Please Enter the Size to Extend: ")
	g = input("Please Enter the Existing LV Name: ")
	v = input("Please Enter the Existing VG Name: ")
	ext = "lvextend --size " + "+" + s + "G" + " /dev/" + v + "/" + g
	form = "resize2fs /dev/" + v + "/" + g
	dis = "lvdisplay " + v + "/" + g
	os.system(ext)
	os.system(form)
	print(os.system(dis))
	print("LV is Extended")

def vgextend():
	p = input("Please tell the Device Name: ")
	v = input("Please Enter the name of Existing Volume Group Name: ")
	ext = "vgextend " + v + " /dev/" + p
	dis = "vgdisplay " + v
	os.system(ext)
	print(os.system(dis))
	print("Volume Group is Extended")

def docker():
	os.system("yum install git -y")
	os.system("git clone https://github.com/rishabhjain1799/docker.git /abc")
	os.system("cp /abc/docker.repo /etc/yum.repos.d/")
	os.system("cd")
	os.system("rm -rf /abc") 
	os.system("yum install docker-ce --nobest -y")
	print("Your Docker is Installed now.")

def start():
	n = input("Please Enter the Command to Execute: ")
	i = input("Please Enter the Name of the Running Docker OS: ")
	cmd = "docker exec -it " + i + " " + n
	os.system("systemctl start docker")
	os.system(cmd)
	

def pull():
	n = input("Please Enter the Name of the Docker OS: ")
	i = input("Please Enter the Image for the Docker OS: ")
	run = "docker run -it --name " + n + " " + i
	os.system(run)

def httpd():
	n = input("Please Enter the Name of the Docker OS: ")
	i = input("Please Enter the Image for the Docker OS: ")
	run = "docker run -dit --name " + n + " " + i
	os.system("systemctl start docker")
	os.system(run)
	os.system("docker exec -it " + n + " yum install net-tools -y")
	os.system("docker exec -it " + n + " yum install httpd -y")
	os.system("/usr/sbin/httpd")

def python():
	n = input("Please Enter the Name of the Docker OS: ")
	i = input("Please Enter the Image for the Docker OS: ")
	os.system("systemctl start docker")
	run = "docker run -dit --name " + n + " " + i
	os.system(run)
	os.system("docker exec -it " + n + " yum install python3 -y")
	os.system("docker exec -it " + n + " /bin/bash")

def partition():
	print("After Entering in the Device:\n\n\t1. Press n to create New Partition.\n\t2. Press p to Primary Partition.\n\t3. Press e for Extended Partition.\n\t4. Press w to save the Partition created.\n\t5. Press d to delete the Partition.\n\t6. Press q to come out of the Device\n\n")
	n = input("Please tell the Device name: ")
	cmd = "fdisk /dev/" + n
	os.system(cmd)
	os.system("udevadm settle")
	os.system("mkfs.ext4 /dev/{}".format(n))
	print("Your Partition is now Ready!!")

def mount():
	x = input("Please Enter the Device Name: ")
	f = input("Please Enter the Folder Name: ")
	cmd = "mount /dev/" + x + " " + "/" + f
	m = "mkdir " + "/" + f
	os.system(f)
	os.system(cmd)
	print("Your folder is mounted")

while(True):
	x = input("\nPlease Enter Your Choice: ")
	os.system("clear")
	if x == '1':
		print(os.system("rpm -q lvm2"))
	elif x == '2':
		print(os.system("lsblk"))
	elif x == '3':
		createlv()
	elif x == '4':
		lvextend()
	elif x == '5':
		vgextend()	
	elif x == '6':
		awsinstall()
	elif x == '7':
		iam()
	elif x == '8':
		aws()
	elif x == '9':
		volume()
	elif x == '10':
		inbound()
	elif x == '11':
		instance()	
	elif x == '12':
		attach()
	elif x == '13':
		docker()
	elif x == '14':
		start()
	elif x == '15':
		pull()
	elif x == '16':
		httpd()
	elif x == '17':
		python()
	elif x == '18':
		yum()
	elif x == '19':
		partition()
	elif x == '20':
		mount()	
	elif x == '21':
		print("Hope you Enjoyed!! Please Visit Us Again\n")
		exit()
	else:
		print("Oops!! You entered something wrong. Bye!!\n")
		exit()	
