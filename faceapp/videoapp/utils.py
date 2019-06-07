import urllib.request
import base64

def faceplusplus(filepath):

	http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
	key = "c6gsubtpVs-Mat5Q62VKYCQt1E2mV-ky"
	secret = "fXHckaD7yf1l0xwQOOzwKb58W1-dFOvX"

	with open(filepath, "rb") as image_file:
	    encoded_image = base64.b64encode(image_file.read())
	raw_params = {"api_key": key, "api_secret": secret, "image_base64": encoded_image}
	params = urllib.parse.urlencode(raw_params)
	data = params.encode( "ascii" ) 

	request = urllib.request.Request(http_url, data)
	request.add_header("Content-type", "application/x-www-form-urlencoded; charset=UTF-8")
	resp = urllib.request.urlopen(request)
	qrcont=resp.read()
	return qrcont