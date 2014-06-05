#coding:utf-8
# Author:LuYu
# Date:2013-12-31

colorMap = {
	'black'  :30 ,
	'red'    :31 ,
	'green'  :32 ,
	'yellow' :33 ,
	'blue'   :34 ,
	'purple' :35 ,
	'cyan'   :36 ,
	'white'  :37 ,
}


def colorPrint(string,color='red',style=0):
	if color in colorMap:
		color_code = colorMap[color]
	else:
		print "warning:your color is not support!"
		color_code = 31
	color = "\x1B[%d;%d;%dm" % (style,color_code,40)
	print "%s%s\x1B[0m" % (color,string),

def colorPrintln(string,color='red',style=0):
	if color in colorMap:
		color_code = colorMap[color]
	else:
		print "warning:your color is not support!"
		color_code = 31
	color = "\x1B[%d;%d;%dm" % (style,color_code,40)
	print "%s%s\x1B[0m" % (color,string)
