import eel
from array import array

lightStr = "0000000000000000"

@eel.expose
def lightPress(light):
	global lightStr
	ind = int(light)

	if lightStr[ind] == "0":
		lightStr = f"{lightStr[:ind]}1{lightStr[ind+1:]}"
	else:
		lightStr = f"{lightStr[:ind]}0{lightStr[ind+1:]}"

	print(lightStr)
	
	# Everything above can be replaced by the return value from what we get from the
	# microcontroller
	return lightStr
	



eel.init('index')
eel.start("index.html"
		  , size=(800, 600)
		)