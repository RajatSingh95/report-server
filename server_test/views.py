
from django.http import HttpResponse,JsonResponse
from django.core.files.storage import default_storage
import datetime
import os
#import tarfile
def server(request):
	if request.method == "POST":
		my_file = request.FILES['file']
		file_name = default_storage.save(my_file.name, my_file)
		#file_url = default_storage.url(file_name)
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		media_path = os.path.join(BASE_DIR,'media')
		full_path=os.path.join(media_path,my_file.name)
		
		# my_tar = tarfile.open(full_path,"r:gz")
		# my_tar.extractall('./my_folder') # specify which folder to extract to
		# my_tar.close()
		
		path = request.scheme+'://'+request.META['HTTP_HOST']+'/media/'+my_file.name
		print("$path to server: ",path)
		message = "<span id=\"download_path\">path:"+path+"</span>"

		return HttpResponse(message)
	
