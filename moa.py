import web, sys
import threading
import json
import platform

#if platform.system() == "Windows":
#SIMULATOR_IP = "127.0.0.1"

SIMULATOR_IP = "192.168.1.2"

# else:
#     SIMULATOR_IP = "10.42.0.1"

print "Set SIMULATOR_IP to " + SIMULATOR_IP



#
# Specify IP adress of your computer here
# to be able to access from another computer
# otherwise, localhost is fine (127.0.0.1)
#
sys.argv[1:] = [SIMULATOR_IP]
#sys.argv[1:] = ["192.168.2.3"] 


current_color = "black"#set start color

class MyWebserver(threading.Thread):



    def run(self):

        urls = ('/(.*)', 'MyWebserver'

                )

        app = web.application(urls, globals())
        print "gnu"
        app.run()



    def GET(self, dirr):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')

        global current_color


        if dirr == 'view':
            #return json.dumps(current_color)

            return current_color


        if dirr == 'tag/magenta':

            current_color = "magenta"

            return "<html><body bgcolor='magenta'></body></html>"

        if dirr == 'tag/yellow':

            current_color = "#E4E6AE"

            return "<html><body bgcolor='#E4E6AE'></body></html>"
        if dirr == 'tag/green':

            current_color = "#99DB9F"

            return "<html><body bgcolor='#99DB9F'></body></html>"

        if dirr == 'tag/blue':

            current_color = "#A6D3DD"

            return "<html><body bgcolor='#A6D3DD'></body></html>"

        if dirr == 'tag/pink':

            current_color = "#EDC8CE"

            return "<html><body bgcolor='#EDC8CE'></body></html>"


        elif dirr =='tag/katt':
            print "hej ehej "

            obj = {
               'figur': 'katt'
            }
            return json.dumps(obj)



MyWebserver().start()


'''if dirr == 'tag/katt':
            print "Katt!"

            obj = {
               'figur': 'katt'
            };
            str = json.dumps(obj)

            #str = '<html><body><img src="http://testing.jonae.nu/wp-content/uploads/2014/06/katt-orange.jpg"></body></html>';
'''