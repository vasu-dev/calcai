import urllib.request
import base64

def faceplusplus(name):

	img_base_url = "https://storage.googleapis.com/faceapp-media/"
	img_url = img_base_url + name
	http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
	key = "Ymznfr45A92cHhEp71JnhN5Bg-4in8i0"
	secret = "nMvxII8gY2FWRGq1myLGqHGiuKKD8lAC"

	#with open(filepath, "rb") as image_file:
	#    encoded_image = base64.b64encode(image_file.read())
	#raw_params = {"api_key": key, "api_secret": secret, "image_base64": encoded_image}
	raw_params = {"api_key": key, "api_secret": secret, "image_url": img_url}
	params = urllib.parse.urlencode(raw_params)
	data = params.encode( "ascii" ) 

	request = urllib.request.Request(http_url, data)
	request.add_header("Content-type", "application/x-www-form-urlencoded; charset=UTF-8")
	resp = urllib.request.urlopen(request)
	qrcont=resp.read()
	return qrcont
