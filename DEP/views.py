from django.conf import settings
from django.contrib import messages
from django.http import *
from django.http import FileResponse
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from django.views.static import serve
from django.views.generic import View
from django.core.paginator import Paginator
from django.core.files import File
from django.utils.encoding import smart_str
from pathlib import Path
from utils.utils import *
from codegen.codegen import *
from sendfile import sendfile
from django.core.files.storage import FileSystemStorage
import urllib.request
import requests
import json
import os
import re
import subprocess
import mimetypes


RUN_AS_youraccount = settings.RUN_AS_youraccount
MDMCTL_JSON = settings.MDMCTL_JSON
EU_JSON = settings.EU_JSON
TW_JSON = settings.TW_JSON
JP_JSON = settings.JP_JSON
PH_JSON = settings.PH_JSON
US_JSON = settings.US_JSON
AU_JSON = settings.AU_JSON
SG_JSON = settings.SG_JSON
IOS_JSON = settings.IOS_JSON
EU_TXT = settings.EU_TXT
SYNC_FLEET_DEVICES = settings.SYNC_FLEET_DEVICES
SYNC_DEP_DEVICES = settings.SYNC_DEP_DEVICES
RESTART_DEVICE = settings.RESTART_DEVICE
PUSH_APP = settings.PUSH_APP
PUSH_UPDATE = settings.PUSH_UPDATE
INSTALL_PROFILE = settings.INSTALL_PROFILE
MOBILECONF = settings.MOBILECONF
ERASE_DEVICE = settings.ERASE_DEVICE
LOCK_DEVICE = settings.LOCK_DEVICE
REMOVE_APP = settings.REMOVE_APP
UPDATE_ENROLL_PROFILE = settings.UPDATE_ENROLL_PROFILE
REMOVE_PROFILE = settings.REMOVE_PROFILE
DOWNLOADONLY_UPDATE = settings.DOWNLOADONLY_UPDATE
DEFAULT = settings.DEFAULT
PUSH_NOTIFICATION = settings.PUSH_NOTIFICATION
GENERATE_CSR = settings.GENERATE_CSR

SSO_EU = settings.SSO_EU
SSO_JP = settings.SSO_JP
SSO_TW = settings.SSO_TW
SSO_PH = settings.SSO_PH
SSO_US = settings.SSO_US
TCC_ZOOM = settings.TCC_ZOOM
REMOVE_TCC_ZOOM = settings.REMOVE_TCC_ZOOM

#testing path default commited
HTTP_POST_DATA = settings.HTTP_POST_DATA
TRAFIC_DATA = settings.TRAFIC_DATA

@never_cache
def login_method(request):
	# If user is already authenticated, user is redirected to root page.
	if request.user.is_authenticated:
		return HttpResponseRedirect('/')
	if request.POST:
		# We use next parameter to redirect when user login is successful.
		try:
			next_page = request.POST['next']
		except:
			next_page = ''
		# Username & password parameters has to be present.
		try:
			username = request.POST['username']
			password = request.POST['password']
		except:
			return render(request, 'DEP/login.html')
		# Authenticating user.
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				if next_page:
					return HttpResponseRedirect(next_page)
				else:
					return HttpResponseRedirect('/')
		else:
			context = {'first_attempt': False, 'next': next_page}
			return render(request, 'DEP/login.html', context)
	else:
		next = ''
		try:
			next = request.GET['next']
		except:
			pass
		context = {'first_attempt': True, 'next': next}
		return render(request, 'DEP/login.html', context)


@never_cache
@login_required(login_url='/login')
def main_method(request):
# e.g. mdmctl get devices | wc -l
	try:
		output = subprocess.check_output("{} \"{}\"".format(RUN_AS_youraccount, "mdmctl get devices"), stderr=subprocess.STDOUT, shell=True, timeout=10, universal_newlines=True)
		search = re.findall("\n[\w-]+\x20+\w+\x20+false\x20+", output, re.IGNORECASE) #search number only
		if search:
			ios_number = len(search) #take whole match
		else:
			ios_number = 0
	except subprocess.CalledProcessError as exc:
			ios_number = str(exc.output)


	try:
		output = subprocess.check_output("{} \"{}\"".format(RUN_AS_youraccount, "mdmctl get devices"), stderr=subprocess.STDOUT, shell=True, timeout=10, universal_newlines=True)
		search = re.findall("\n[\w-]+\x20+\w+\x20+true\x20+", output, re.IGNORECASE) #search number only
		if search:
			macos_number = len(search) #take whole match
		else:
			macos_number = 0
		
	except subprocess.CalledProcessError as exc:
			macos_number = str(exc)
	try:
		output = subprocess.check_output("echo | openssl x509 -inform pem  -in /home/youraccount/mdm-certificates/MDM_YOURSERVERIncorporatedEnt_Certificate.pem | openssl x509 -noout -dates", stderr=subprocess.STDOUT, shell=True, timeout=10, universal_newlines=True)
		search = re.search("notAfter\=(\w+\x20+\d+\x20+\d{2}:\d{2}:\d{2}\x20+\d{4})", output, re.IGNORECASE) #search number only
		if search:
			date_now = search.group(1)
		else:
			date_now = 0
		
	except subprocess.CalledProcessError as exc:
			date_now = str(exc)

	try:
		output = subprocess.check_output("echo | openssl s_client -servername yourdomain.com -connect yourdomain.com:443 2>/dev/null | openssl x509 -noout -dates", stderr=subprocess.STDOUT, shell=True, timeout=10, universal_newlines=True)
		search = re.search("notAfter\=(\w+\x20+\d+\x20+\d{2}:\d{2}:\d{2}\x20+\d{4})", output, re.IGNORECASE) #search number only
		if search:
			blocked = search.group(1)
		else:
			blocked = 0
		
	except subprocess.CalledProcessError as exc:
			blocked = str(exc)
	
	try:
		output = subprocess.check_output("echo | openssl s_client -servername yourdomain.com -connect yourdomain.com:443 2>/dev/null | openssl x509 -noout -dates", stderr=subprocess.STDOUT, shell=True, timeout=10, universal_newlines=True)
		search = re.search("notAfter\=(\w+\x20+\d+\x20+\d{2}:\d{2}:\d{2}\x20+\d{4})", output, re.IGNORECASE) #search number only
		if search:
			blocked2 = search.group(1)
		else:
			blocked2 = 0
		
	except subprocess.CalledProcessError as exc:
			blocked2 = str(exc)

	try:
		output = subprocess.check_output("{} \"{}\"".format(RUN_AS_youraccount, "mdmctl get profiles"), stderr=subprocess.STDOUT, shell=True, timeout=10, universal_newlines=True)
		search = re.findall("\n(\w+\.[^\x20]+)\x20+\d+", output, re.IGNORECASE) #search number only
		if search:
			profiles = search
		else:
			profiles = []
		print("profiles: {}".format(profiles))
	except subprocess.CalledProcessError as exc:
		profiles = [str(exc)]

	try:
		output = subprocess.check_output("{} \"{}\"".format(RUN_AS_youraccount, "mdmctl get apps"), stderr=subprocess.STDOUT, shell=True, timeout=10, universal_newlines=True)
		search = re.findall("\n([^\x20]+)", output, re.IGNORECASE) #search number only
		if search:
			mdmstrap = search
		else:
			mdmstrap = []
		print("mdmstrap: {}".format(profiles))
	except subprocess.CalledProcessError as exc:
		mdmstrap = [str(exc)]
	
	try:
		output = subprocess.check_output("{} \"{}\"".format(RUN_AS_youraccount, "micromdm version"), stderr=subprocess.STDOUT, shell=True, timeout=10, universal_newlines=True)
		search = re.findall("\w+\d.\d.\d", output, re.IGNORECASE) #search number only
		if search:
			mdmver = search
		else:
			mdmver = []
		print("mdmver: {}".format(profiles))
	except subprocess.CalledProcessError as exc:
		mdmver = [str(exc)]

	try:
		output = subprocess.check_output("{} \"{}\"".format(RUN_AS_youraccount, "systemctl status micromdm.service --no-pager"), stderr=subprocess.STDOUT, shell=True, timeout=10, universal_newlines=True)
		search = re.findall("Active:\x20\w+", output, re.IGNORECASE) #search number only
		if search:
			status = search
		else:
			status = []
		print("status: {}".format(status))
	except subprocess.CalledProcessError as exc:
		status = [str(exc)]


	context = {'status': status, 'ios_number': ios_number, 'macos_number': macos_number, 'blocked': blocked, 'blocked2': blocked2, "date_now": date_now, "profiles": profiles, "mdmver": mdmver, "mdmstrap": mdmstrap}

	return render(request, 'DEP/dashboard.html', context)


@never_cache
@login_required(login_url='/login')
def add_device_method(request):
	if request.POST:
		print(request.POST)

	return render(request, 'DEP/adddevice.html')

@never_cache
@login_required(login_url='/login')
def regional_fleet_method(request):
	return render(request, 'DEP/regional_fleet.html')

@never_cache
@login_required(login_url='/login')
def managed_profiles_method(request):
	return render(request, 'DEP/managed_profiles.html')



@never_cache
@login_required(login_url='/login')
def remove_device_method(request):
	if not request.user.is_superuser:
		return HttpResponseRedirect('/no_perm')
	
	return render(request, 'DEP/removedevice.html')

@never_cache
@login_required(login_url='/login')
def enroll_method(request):
	return render(request, 'DEP/enroll.html')

@never_cache
@login_required(login_url='/login')
def munkireport_method(request):
	return render(request, 'DEP/munkireport.html')

@never_cache
@login_required(login_url='/login')
def munkimanifest_method(request):
	return render(request, 'DEP/munkimanifest.html')

@never_cache
@login_required(login_url='/login')
def munkipkginfo_method(request):
	return render(request, 'DEP/munkipkginfo.html')

@never_cache
@login_required(login_url='/login')
def howto_method(request):
	return render(request, 'DEP/howto.html')

@never_cache
@login_required(login_url='/login')
def renewmdm_method(request):
	if request.method == 'POST' and request.POST.get("gen_csr") == 'ven_csr':
		print(request.POST)
		gen_csr = request.POST.get('ven_csr')
		output = subprocess.check_call([GENERATE_CSR])
		messages.success(request, 'VendorCSR successfully generated')
		print(GENERATE_CSR)
		return JsonResponse({'result': 'Success'})

	elif request.method == 'POST' and request.POST.get("dwn_csr") == 'get_csr':
		print(request.POST)
		dwn_csr = request.POST.get('get_csr')
		
		file_path = os.path.join(settings.MEDIA_ROOT, "/home/youraccount/DEP_tool/upload/VendorCertificateRequest.csr")
		filename = 'VendorCertificateRequest.csr'
		with open(file_path, 'r') as fl:
			csr_file = fl.read()
			
			mime_type, _ = mimetypes.guess_type(file_path)
			try:
				response = HttpResponse(csr_file, content_type=mime_type)
				response['Content-Disposition'] = "attachment; filename=%s" % filename
			except:
				pass
			#messages.success(request, print(csr_file))
			return response

	elif request.method =='POST':
		try:
			uploaded_file = request.FILES['document']
			fs = FileSystemStorage()
			name = fs.save(uploaded_file.name, uploaded_file)
			messages.success(request, 'File successfully uploaded')
			print(uploaded_file)
		except:
			pass
		return HttpResponseRedirect('/renewmdm')
	else:
		return render(request, 'DEP/renewmdm.html')


@never_cache
@login_required(login_url='/login')
def setupdep_method(request):
	if request.method =='POST':
		print(request.POST)
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		messages.success(request, 'File successfully uploaded')
		
		return HttpResponseRedirect('/setupdep')
	else:
		return render(request, 'DEP/setupdep.html')

@never_cache
@login_required(login_url='/login')
def asus_method(request):
	return render(request, 'DEP/asus.html')

@never_cache
@login_required(login_url='/login')
def no_perm_method(request):
	return render(request, 'DEP/no_perm.html')



@never_cache
@login_required(login_url='/login')
def system_journal_method(request):

	# context = {'rows': [{'server_name':1, 'service_status':534988,'last_restart':'A'},
	#                     {'server_name': 1, 'service_status': 534988, 'last_restart': 'A'},
	#                     {'server_name': 1, 'service_status': 534988, 'last_restart': 'A'}]}

	try:
		output = subprocess.check_output(
			"{} \"{}\"".format(RUN_AS_youraccount, "journalctl -u micromdm.service -n 200 --no-pager"),
			stderr=subprocess.STDOUT,
			shell=True,
			timeout=15,
			universal_newlines=True)
		search = re.findall('[^\n]+', output, re.IGNORECASE)
		# search = re.findall('level=([^\x20]+)[^\n]+msg="([^"]+)"[^\n]+op_type=([^\x20]+)[^\n]+previously_known=([^\x20\n]+)', output, re.IGNORECASE)
		if search:
			records = search
			#server_name = "YOURSERVER02"
			#records = [{"level":i[0], "msg": i[1], "op_type": i[2], "previously_known": i[3]} for i in search]
		else:
			records = []
			#server_name = "YOURSERVER02"
			#records = [{"level": "", "msg": "", "op_type": "", "previously_known": ""}]
	except subprocess.CalledProcessError as exc:
		records = []
		#server_name = "YOURSERVER02"
		#records = [{"level": "", "msg": "", "op_type": "", "previously_known": ""}]

	context = {'records': records}


	print(context)
	return render(request, 'DEP/systemjournal.html', context)

@never_cache
@login_required(login_url='/login')
def webhook_method(request):

	# context = {'rows': [{'server_name':1, 'service_status':534988,'last_restart':'A'},
	#                     {'server_name': 1, 'service_status': 534988, 'last_restart': 'A'},
	#                     {'server_name': 1, 'service_status': 534988, 'last_restart': 'A'}]}

	try:
		output = subprocess.check_output(
			"{} \"{}\"".format(RUN_AS_youraccount, "journalctl -u webhook.service -n 200 --no-pager"),
			stderr=subprocess.STDOUT,
			shell=True,
			timeout=15,
			universal_newlines=True)
		search = re.findall('[^\n]+', output, re.IGNORECASE)
		# search = re.findall('level=([^\x20]+)[^\n]+msg="([^"]+)"[^\n]+op_type=([^\x20]+)[^\n]+previously_known=([^\x20\n]+)', output, re.IGNORECASE)
		if search:
			records = search
			#server_name = "YOURSERVER02"
			#records = [{"level":i[0], "msg": i[1], "op_type": i[2], "previously_known": i[3]} for i in search]
		else:
			records = []
			#server_name = "YOURSERVER02"
			#records = [{"level": "", "msg": "", "op_type": "", "previously_known": ""}]
	except subprocess.CalledProcessError as exc:
		records = []
		#server_name = "YOURSERVER02"
		#records = [{"level": "", "msg": "", "op_type": "", "previously_known": ""}]

	context = {'records': records}


	print(context)
	return render(request, 'DEP/webhook.html', context)



@never_cache
@login_required(login_url='/login')
def vpp_method(request):
	#if not request.user.is_superuser:
	#	return HttpResponseRedirect('/no_perm')

#Install Application
	if request.method == 'POST' and request.POST.get("action") == 'push':
		print(request.POST)
		action = request.POST.get('action')
		device = request.POST.get('device')
		#output = subprocess.Popen([PUSH_APP, "device", "900259081"], stdout=subprocess.PIPE).communicate()[0]
		output = subprocess.check_call([PUSH_APP, device, '900259081'], stdin=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None) 
		#output = subprocess.Popen([PUSH_APP, device], stdout=subprocess.PIPE).communicate()[0] #installapplication don't like Popen method
		#output = output.decode('utf-8')
		#output = output.replace('\n', '')
		print(PUSH_APP, device, '900259081')
		print(output)
		# json_string = json.dumps(output)
		# with open(HTTP_POST_DATA, 'a+') as f:

		# 	json_string = json.dumps(output)
		# 	f.write(output)
		# 	f.close()

		# if GOLDEN_UUID in TESTING_UUID.keys():
		# 	print('Approved Command UUID: ', GOLDEN_UUID)
		# 	print('Approved Status: ', TESTING_UUID[GOLDEN_UUID])

		# 	return JsonResponse ({'result': 'Acknowledged', 'details': GOLDEN_UUID})
		# else:
		return JsonResponse({'result': 'Acknowledged', 'details': "Application has been pushed and will be install ASAP."})

#Remove Application	
	elif request.method == 'POST' and request.POST.get("remove_app") == 'remove_application':
		remove_app = request.POST.get('remove_app')
		device = request.POST.get('device')
		#output = subprocess.Popen([PUSH_APP, "device", "900259081"], stdout=subprocess.PIPE).communicate()[0]
		output = subprocess.check_call([REMOVE_APP, device], stdin=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None) 
		#output = subprocess.Popen([PUSH_APP, device], stdout=subprocess.PIPE).communicate()[0] #installapplication don't like Popen method
		#output = output.decode('utf-8')
		#output = output.replace('\n', '')
		print(REMOVE_APP, device)
		# json_string = json.dumps(output)
		# with open(HTTP_POST_DATA.JSON, 'w') as f:
		#  	f.write(output)
		#  	f.close()
	
		return JsonResponse({'result': 'Remove', 'details': "Application will be remove from remote device."})

#Restart device
	elif request.method == 'POST' and request.POST.get("action_re") == 'restart':
		action_re = request.POST.get('action_re')
		device = request.POST.get('device')
		#output = subprocess.check_call([RESTART_DEVICE, device])
		output = subprocess.Popen([RESTART_DEVICE, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(RESTART_DEVICE, device)
	#	json_string = json.dumps(output)
	#	with open(HTTP_POST_DATA, 'w+') as f:
	#	 	f.write(output)
	#	 	f.close()
	#if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "Restart request sent."})

#Install Profile
	elif request.method == 'POST' and request.POST.get("action_pro") == 'profile':
		action_pro = request.POST.get('action_pro')
		device = request.POST.get('device')
		#output = subprocess.check_call([INSTALL_PROFILE, device])
		output = subprocess.Popen([INSTALL_PROFILE, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(INSTALL_PROFILE, device)
	#	json_string = json.dumps(output)
	#	with open(HTTP_POST_DATA, 'w+') as f:
	#	 	f.write(output)
	#	 	f.close()
	#if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "Profile has been pushed."})

#Update Enroll Profile
	elif request.method == 'POST' and request.POST.get("action_en_pro") == 'enroll_profile':
		action_en_pro = request.POST.get('action_en_pro')
		device = request.POST.get('device')
		#output = subprocess.check_call([INSTALL_PROFILE, device])
		output = subprocess.Popen([UPDATE_ENROLL_PROFILE, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(UPDATE_ENROLL_PROFILE, device)
	#	json_string = json.dumps(output)
	#	with open(HTTP_POST_DATA, 'w+') as f:
	#	 	f.write(output)
	#	 	f.close()
	#if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "Profiles has been pushed and will be install ASAP."})

#Remove Profile
	elif request.method == 'POST' and request.POST.get("action_rempro") == 'remove-profile':
		action_rempro = request.POST.get('action_rempro')
		device = request.POST.get('device')
		#output = subprocess.check_call([INSTALL_PROFILE, device])
		output = subprocess.Popen([REMOVE_PROFILE, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(REMOVE_PROFILE, device)
	# 	json_string = json.dumps(output)
	# 	with open(HTTP_POST_DATA, 'w+') as f:
	# 	 	f.write(output)
	# 	 	f.close()
	# if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "Profile will be remove from device."})

#Remove TCC Zoom Profile
	elif request.method == 'POST' and request.POST.get("remove_tcc_zoom") == 'remo_tcc_zoom':
		remove_tcc_zoom = request.POST.get('remove_tcc_zoom')
		device = request.POST.get('device')
		#output = subprocess.check_call([INSTALL_PROFILE, device])
		output = subprocess.Popen([REMOVE_TCC_ZOOM, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(REMOVE_TCC_ZOOM, device)
	# 	json_string = json.dumps(output)
	# 	with open(HTTP_POST_DATA, 'w+') as f:
	# 	 	f.write(output)
	# 	 	f.close()
	# if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "TCC Profile will be remove from device."})

#Push TCC Zoom
	elif request.method == 'POST' and request.POST.get("push_tcc_zoom") == 'tcc_zoom':
		push_tcc_zoom = request.POST.get('push_tcc_zoom')
		device = request.POST.get('device')
		#output = subprocess.check_call([ERASE_DEVICE, device])
		output = subprocess.Popen([TCC_ZOOM, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(TCC_ZOOM, device)
	# 	json_string = json.dumps(output)
	# 	with open(HTTP_POST_DATA, 'w+') as f:
	# 	 	f.write(output)
	# 	 	f.close()
	# if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "TCC Configuration pushed."})

#Install iOS update	
	elif request.method == 'POST' and request.POST.get("action_up") == 'update':
		action_up = request.POST.get('action_up')
		device = request.POST.get('device')
		#output = subprocess.check_call([PUSH_UPDATE, device])
		output = subprocess.Popen([PUSH_UPDATE, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(PUSH_UPDATE, device)
	# 	json_string = json.dumps(output)
	# 	with open(HTTP_POST_DATA, 'w+') as f:
	# 	 	f.write(output)
	# 	 	f.close()
	# if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "Install an already downloaded softwareupdate."})

#PUSH_NOTIFICATION	
	elif request.method == 'POST' and request.POST.get("action_not") == 'notify':
		action_not = request.POST.get('action_not')
		device = request.POST.get('device')
		#output = subprocess.check_call([PUSH_UPDATE, device])
		output = subprocess.Popen([PUSH_NOTIFICATION, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(PUSH_NOTIFICATION, device)
	# 	json_string = json.dumps(output)
	# 	with open(HTTP_POST_DATA, 'w+') as f:
	# 	 	f.write(output)
	# 	 	f.close()
	# if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': TRAFIC_STATUS})

#DownloadONly iOS update	
	elif request.method == 'POST' and request.POST.get("download") == 'ios':
		download = request.POST.get('download')
		device = request.POST.get('device')
		#output = subprocess.check_call([PUSH_UPDATE, device])
		output = subprocess.Popen([DOWNLOADONLY_UPDATE, device], stdout=subprocess.PIPE).communicate()[0]
		#output = subprocess.check_call([DOWNLOADONLY_UPDATE, device], stdin=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None) 
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(DOWNLOADONLY_UPDATE, device)
	# 	json_string = json.dumps(output)
	# 	with open(HTTP_POST_DATA, 'w+') as f:
	# 	 	f.write(output)
	# 	 	f.close()
	# if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "Download the softwareupdate without installing it."})

#Default iOS update	
	elif request.method == 'POST' and request.POST.get("default") == 'default2':
		default = request.POST.get('default')
		device = request.POST.get('device')
		#output = subprocess.check_call([PUSH_UPDATE, device])
		output = subprocess.Popen([DEFAULT, device], stdout=subprocess.PIPE).communicate()[0]
		#output = subprocess.check_call([DOWNLOADONLY_UPDATE, device], stdin=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None) 
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(DEFAULT, device)
	# 	json_string = json.dumps(output)
	# 	with open(HTTP_POST_DATA, 'w+') as f:
	# 	 	f.write(output)
	# 	 	f.close()
	# if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "Download  or install the softwareupdate."})


#Wipe Device
	elif request.method == 'POST' and request.POST.get("action_del") == 'erase':
		action_del = request.POST.get('action_del')
		device = request.POST.get('device')
		#output = subprocess.check_call([ERASE_DEVICE, device])
		output = subprocess.Popen([ERASE_DEVICE, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(ERASE_DEVICE, device)
	# 	json_string = json.dumps(output)
	# 	with open(HTTP_POST_DATA, 'w+') as f:
	# 	 	f.write(output)
	# 	 	f.close()
	# if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "!!!Wipe request sent!!!"})
#SSO EU
	elif request.method == 'POST' and request.POST.get("sso_eu_push") == 'eu_push':
		sso_eu_push = request.POST.get('sso_eu_push')
		device = request.POST.get('device')
		#output = subprocess.check_call([ERASE_DEVICE, device])
		output = subprocess.Popen([SSO_EU, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(SSO_EU, device)
	# 	json_string = json.dumps(output)
	# 	with open(HTTP_POST_DATA, 'w+') as f:
	# 	 	f.write(output)
	# 	 	f.close()
	# if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "Configuration pushed."})
#SSO TW
	elif request.method == 'POST' and request.POST.get("sso_tw_push") == 'tw_push':
		sso_tw_push = request.POST.get('sso_tw_push')
		device = request.POST.get('device')
		#output = subprocess.check_call([ERASE_DEVICE, device])
		output = subprocess.Popen([SSO_TW, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(SSO_TW, device)
	# 	json_string = json.dumps(output)
	# 	with open(HTTP_POST_DATA, 'w+') as f:
	# 	 	f.write(output)
	# 	 	f.close()
	# if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "Configuration pushed."})
#SSO US
	elif request.method == 'POST' and request.POST.get("sso_us_push") == 'us_push':
		sso_us_push = request.POST.get('sso_us_push')
		device = request.POST.get('device')
		#output = subprocess.check_call([ERASE_DEVICE, device])
		output = subprocess.Popen([SSO_US, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(SSO_US, device)
	# 	json_string = json.dumps(output)
	# 	with open(HTTP_POST_DATA, 'w+') as f:
	# 	 	f.write(output)
	# 	 	f.close()
	# if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "Configuration pushed."})
#SSO PH
	elif request.method == 'POST' and request.POST.get("sso_ph_push") == 'ph_push':
		sso_ph_push = request.POST.get('sso_ph_push')
		device = request.POST.get('device')
		#output = subprocess.check_call([ERASE_DEVICE, device])
		output = subprocess.Popen([SSO_PH, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(SSO_PH, device)
	# 	json_string = json.dumps(output)
	# 	with open(HTTP_POST_DATA, 'w+') as f:
	# 	 	f.write(output)
	# 	 	f.close()
	# if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "Configuration pushed."})
#SSO JP
	elif request.method == 'POST' and request.POST.get("sso_jp_push") == 'jp_push':
		sso_jp_push = request.POST.get('sso_jp_push')
		device = request.POST.get('device')
		#output = subprocess.check_call([ERASE_DEVICE, device])
		output = subprocess.Popen([SSO_JP, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(SSO_JP, device)
	# 	json_string = json.dumps(output)
	# 	with open(HTTP_POST_DATA, 'w+') as f:
	# 	 	f.write(output)
	# 	 	f.close()
	# if GOLDEN_UUID in TESTING_UUID.keys():
		return JsonResponse({'result': 'Acknowledged', 'details': "Configuration pushed."})
#Lock Device
	elif request.method == 'POST' and request.POST.get("action_lck") == 'lock':
		
		action_lck = request.POST.get('action_lck')
		device = request.POST.get('device')
		#output = str(subprocess.check_call([LOCK_DEVICE, device]))
		#output = str(subprocess.Popen([LOCK_DEVICE, device], stdout=subprocess.PIPE).communicate()[0])
		#output = subprocess.check_call([LOCK_DEVICE, device], stdin=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None)
		output = subprocess.Popen([LOCK_DEVICE, device], stdout=subprocess.PIPE).communicate()[0]
		output = output.decode('utf-8')
		output = output.replace('\n', '')
		print(LOCK_DEVICE, device)
	# 	json_string = json.dumps(output)
	# 	with open(HTTP_POST_DATA, 'w+') as f:
	# 	 	f.write(output)
	# 	 	f.close()

	# if GOLDEN_UUID in TESTING_UUID.keys():				
		return JsonResponse({'result': 'Acknowledged', 'details': "Lock request sent : PIN:847284"})

	# if not GOLDEN_UUID in TESTING_UUID.keys():
	# 	return JsonResponse({'result': 'Error', 'details': 'Error - contact your system admin'})

	else:
		try:
			with open(MDMCTL_JSON, 'r') as json_file:
				dep_json = json.load(json_file)
		except:
			return JsonResponse({'result': 'Error', 'details': 'Cannot open local json file'})
		context = {'devices': dep_json["devices"]}

		try:
			serial_numbers = []
			with open(MDMCTL_JSON, 'r') as json_file:
				dep_json = json.load(json_file)
			if dep_json.get('devices', ''):
				for i in dep_json.get('devices', ''):
					serial_numbers.append({"serial_number": i})
			context = {'rows': serial_numbers}
		except:
			context = {'rows': []}




		return render(request, 'DEP/vpp.html', context)



@never_cache
@login_required(login_url='/login')
def show_devices_method(request):
	try:
		serial_numbers = []
		with open(MDMCTL_JSON, 'r') as json_file:
			dep_json = json.load(json_file)
		if dep_json.get('devices', ''):
			for i in dep_json.get('devices', ''):
				serial_numbers.append({"serial_number": i})
		context = {'rows': serial_numbers}
	except:
		context = {'rows': []}

	return render(request, 'DEP/showdevices.html', context)

@never_cache
@login_required(login_url='/login')
def regional_fleet_method(request):
    # if request.POST:
    #     output = subprocess.check_output(SYNC_DEP_DEVICES,
    #                     stderr=subprocess.STDOUT,
    #                     shell=True,
    #                     timeout=3,
    #                     universal_newlines=True)
    #     return JsonResponse({'result': 'Success'})
    # else:
    #     return render(request, 'DEP/api.html')

	if request.method == 'POST' and request.POST.get("action_fleet_sync") == 'sync_fleet_dev':
		action = request.POST.get('action_fleet_sync')
		
		#output = subprocess.Popen([PUSH_APP, "device", "900259081"], stdout=subprocess.PIPE).communicate()[0]
		output = subprocess.check_call([SYNC_FLEET_DEVICES])
		print(SYNC_FLEET_DEVICES)
		return JsonResponse({'result': 'Success'})
	else:
		return render(request, 'DEP/regional_fleet.html')

@never_cache
@login_required(login_url='/login')
def api_command_method(request):
    # if request.POST:
    #     output = subprocess.check_output(SYNC_DEP_DEVICES,
    #                     stderr=subprocess.STDOUT,
    #                     shell=True,
    #                     timeout=3,
    #                     universal_newlines=True)
    #     return JsonResponse({'result': 'Success'})
    # else:
    #     return render(request, 'DEP/api.html')

	if request.method == 'POST' and request.POST.get("action_sync") == 'sync_dev':
		action = request.POST.get('action_sync')
		
		#output = subprocess.Popen([PUSH_APP, "device", "900259081"], stdout=subprocess.PIPE).communicate()[0]
		output = subprocess.check_call([SYNC_DEP_DEVICES])
		print(SYNC_DEP_DEVICES)
		return JsonResponse({'result': 'Success'})
	else:
		return render(request, 'DEP/api.html')



@never_cache
@login_required(login_url='/login')
def manifest_method(request):
	return render(request, 'DEP/manifest.html')


@never_cache
@login_required(login_url='/login')
def service_status_method(request):
	# context = {'rows': [{'server_name':1, 'service_status':534988,'last_restart':'A'},
	#                     {'server_name': 1, 'service_status': 534988, 'last_restart': 'A'},
	#                     {'server_name': 1, 'service_status': 534988, 'last_restart': 'A'}]}

	try:
		output = subprocess.check_output(
			"{} \"{}\"".format(RUN_AS_youraccount, "systemctl status micromdm.service --no-pager"),
			stderr=subprocess.STDOUT,
			shell=True,
			timeout=3,
			universal_newlines=True)
		search = re.search('Active: (active|inactive) \((?:dead|running)\) since [^;]*; (.+) ago', output, re.IGNORECASE)
		if search:
			server_name = "YOURSERVER01"
			service_status = search.group(1)
			last_restart = search.group(2)
		else:
			server_name = "YOURSERVER01"
			service_status = "error"
			last_restart = "error"
	except subprocess.CalledProcessError as exc:
		server_name = "YOURSERVER01"
		service_status = "error"
		last_restart = "error"

	context = {'rows': [{'server_name':server_name, 'service_status':service_status,'last_restart':last_restart}]}

	return render(request, 'DEP/servicestatus.html', context)



@never_cache
@login_required(login_url='/login')
def add_method(request):
	if request.POST:
		print(request.POST)
		try:
			with open(MDMCTL_JSON, 'r') as json_file:
				dep_json = json.load(json_file)
			with open(EU_JSON, 'r') as json_file2:
				dep_json2 = json.load(json_file2)
			with open(TW_JSON, 'r') as json_file3:
				dep_json3 = json.load(json_file3)
			with open(JP_JSON, 'r') as json_file4:
				dep_json4 = json.load(json_file4)
			with open(PH_JSON, 'r') as json_file5:
				dep_json5 = json.load(json_file5)
			with open(US_JSON, 'r') as json_file6:
				dep_json6 = json.load(json_file6)
			with open(AU_JSON, 'r') as json_file7:
				dep_json7 = json.load(json_file7)
			with open(SG_JSON, 'r') as json_file8:
				dep_json8 = json.load(json_file8)
			with open(IOS_JSON, 'r') as json_file9:
				dep_json9 = json.load(json_file9)
			

			
		except:
			return JsonResponse({'result': 'Error', 'details': 'Cannot open local json file'})

		try:
			device_id = ''
			device_id = request.POST['id']

			device_region = ''
			device_region = request.POST['posilamvybranyregion']
			
			
		except:
			pass

		if not device_id:
			return JsonResponse({'result': 'Error', 'details': 'Blank Device ID filled in'})

		if not dep_json.get('devices', ''):
			return JsonResponse({'result': 'Error', 'details': 'No devices list in json file'})

		if device_id in dep_json['devices']:
			return JsonResponse({'result': 'Error', 'details': 'Already in'})
		else:
			dep_json['devices'].append(device_id)
			dep_json2['devices'].append(device_id)
			dep_json3['devices'].append(device_id)
			dep_json4['devices'].append(device_id)
			dep_json5['devices'].append(device_id)
			dep_json6['devices'].append(device_id)
			dep_json7['devices'].append(device_id)
			dep_json8['devices'].append(device_id)
			dep_json9['devices'].append(device_id)
			
			
			try:
				with open(MDMCTL_JSON, 'w') as json_file:
					json.dump(dep_json, json_file)
				
				if request.method == 'POST' and request.POST.get("posilamvybranyregion") == 'EU':
					with open(EU_JSON, 'w') as json_file2:
						json.dump(dep_json2, json_file2)
				if request.method == 'POST' and request.POST.get("posilamvybranyregion") == 'TW':
					with open(TW_JSON, 'w') as json_file3:
						json.dump(dep_json3, json_file3)			
				if request.method == 'POST' and request.POST.get("posilamvybranyregion") == 'JP':
					with open(JP_JSON, 'w') as json_file4:
						json.dump(dep_json4, json_file4)
				if request.method == 'POST' and request.POST.get("posilamvybranyregion") == 'PH':
					with open(PH_JSON, 'w') as json_file5:
						json.dump(dep_json5, json_file5)
				if request.method == 'POST' and request.POST.get("posilamvybranyregion") == 'US':
					with open(US_JSON, 'w') as json_file6:
						json.dump(dep_json6, json_file6)
				if request.method == 'POST' and request.POST.get("posilamvybranyregion") == 'AU':
					with open(AU_JSON, 'w') as json_file7:
						json.dump(dep_json7, json_file7)
				if request.method == 'POST' and request.POST.get("posilamvybranyregion") == 'SG':
					with open(SG_JSON, 'w') as json_file8:
						json.dump(dep_json8, json_file8)
				if request.method == 'POST' and request.POST.get("posilamvybranyregion") == 'iOS':
					with open(IOS_JSON, 'w') as json_file9:
						json.dump(dep_json9, json_file9)
				
				
				
			except:
				return JsonResponse({'result': 'Error', 'details': 'Error dumping updated json'})
			return JsonResponse({'result': 'Success', 'details': 'Newly added. Please apply.'})
	else:
		return JsonResponse({'result': 'Error', 'details': 'Use POST method'})



@never_cache
@login_required(login_url='/login')
def remove_method(request):
	if not request.user.is_superuser:
		return JsonResponse({'result': 'Questionable', 'details': 'Permission denied - you have to be superuser'})

	if request.POST:
		try:
			with open(MDMCTL_JSON, 'r') as json_file:
				dep_json = json.load(json_file)
			
		except:
			return JsonResponse({'result': 'Error', 'details': 'Cannot open local json file'})

		try:
			device_id = ''
			device_id = request.POST['id']
		
		except:
			pass

		if not device_id:
			return JsonResponse({'result': 'Error', 'details': 'Blank Device ID filled in'})

		if not dep_json.get('devices', ''):
			return JsonResponse({'result': 'Error', 'details': 'No devices list in json file'})

		if device_id not in dep_json['devices']:
			return JsonResponse({'result': 'Empty', 'details': 'Not present in devices'})
		else:
			dep_json['devices'].remove(device_id)
			try:
				with open(MDMCTL_JSON, 'w') as json_file:
					json.dump(dep_json, json_file)
				
			except:
				return JsonResponse({'result': 'Error', 'details': 'Error dumping updated json to local file'})
			return JsonResponse({'result': 'Success', 'details': 'Removed selected Device ID'})
	else:
		return JsonResponse({'result': 'Error', 'details': 'Use POST method'})


@never_cache
@login_required(login_url='/login')
def apply_method(request):
	if request.POST:
		try:
			output = subprocess.check_output("{} \"mdmctl apply dep-profiles -f {}\"".format(RUN_AS_youraccount, MDMCTL_JSON),
											 stderr=subprocess.STDOUT,
											 shell=True,
											 timeout=15,
											 universal_newlines=True)
		except subprocess.CalledProcessError as exc:
			output = exc.output

		if re.search('Defined DEP Profile with UUID [\dA-Za-z]+', output, re.IGNORECASE):
			return JsonResponse({'result': 'Success', 'details': output, 'additional': 'Output looks fine based on '
																					   'standard behaviour'})
		else:
			return JsonResponse({'result': 'Questionable', 'details': output, 'additional': 'Output doesn\'t look '
																							'standard'})
	else:
		return JsonResponse({'result': 'Error', 'details': 'Use POST method'})


@never_cache
@login_required(login_url='/login')
def modular_method(request):
	modular_list = [
		{"method": "journalctl_micromdm_service",
		 "command": "journalctl -u micromdm.service -n 100 --no-pager",
		 "expected_result": "Logs begin at"},
		{"method": "systemctl_status_micromdm_service",
		 "command": "systemctl status micromdm.service --no-pager",
		 "expected_result": "micromdm.service - MicroMDM MDM Server"},
		{"method": "GET APPS",
		 "command": "mdmctl get apps",
		 "expected_result": ""},
		{"method": "restart_micromdm",
		 "command": "sudo service micromdm restart --no-pager",
		 "expected_result": ""},
		 {"method": "sync_dep_devices",
		 "command": "sudo ./sync_dep_devices.sh --no-pager",
		 "expected_result": ""},
		 {"method": "restart_device",
		 "command": "sudo ./restart_device.sh --no-pager",
		 "expected_result": ""},
		 {"method": "push_app",
		 "command": "sudo ./push_app.sh --no-pager",
		 "expected_result": ""},
		 {"method": "push_update",
		 "command": "sudo ./push_update.sh --no-pager",
		 "expected_result": ""}
	]

	if not request.user.is_superuser:
		return JsonResponse({'result': 'Error', 'details': 'Permission denied - you have to be superuser'})

	if request.POST:
		try:
			method_param = request.POST['method']
		except:
			return JsonResponse({'result': 'Error', 'details': 'Undefined method.'})

		for elem in modular_list:
			if elem['method'] == method_param:
				command, expected_result = elem['command'], elem['expected_result']
				break
		else:
			return JsonResponse({'result': 'Error', 'details': 'Couldn\'t find selected method.'})

		try:
			output = subprocess.check_output("{} \"{}\"".format(RUN_AS_youraccount, command),
											 stderr=subprocess.STDOUT,
											 shell=True,
											 timeout=15,
											 universal_newlines=True)
		except subprocess.CalledProcessError as exc:
			output = exc.output

		if re.search(expected_result, output, re.IGNORECASE):
			return JsonResponse({'result': 'Success', 'output': output})
		else:
			return JsonResponse({'result': 'Error', 'details': output})
	else:
		return JsonResponse({'result': 'Error', 'details': 'Use POST method'})


@never_cache
@login_required(login_url='/login')
def get_json_method(request):
	return serve(request, os.path.basename(MDMCTL_JSON), os.path.dirname(MDMCTL_JSON))


@never_cache
@login_required(login_url='/login')
def logout_method(request):
	logout(request)
	return HttpResponseRedirect('/login')


@never_cache
def not_present_method(request):
	return HttpResponse("Not present on the server!", status=404)

