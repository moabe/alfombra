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


current_color = "black"

show_tag_scanned = False

#set start color

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
        global show_tag_scanned
        global phoneList
        global phones



        phoneList = []
        print phoneList
        phoneList.append("hej")


        phones = {"phones": phoneList}



        #print json.dumps(phones, sort_keys=True, indent=4, separators=(',', ': '))

        if dirr == 'view':

            return json.dumps(phones)

        if dirr == 'tag/yellow':


            show_tag_scanned = False

            current_color = "#E4E6AE"

            yel = "#E4E6AE"

            ip = web.ctx['ip']

            ip= str(ip[-1])


            pearlsList = []

            pearlDict = {"color":yel, "position": "32"}

            pearlsList.append(pearlDict)

            phoneDict = { "ip" : ip, "pearls" : pearlsList }

            phoneList.append("hrj")




            return "<html><body bgcolor='#E4E6AE'></body></html>"









        if dirr == 'tag/green':
            show_tag_scanned = False

            current_color = "#99DB9F"

            return "<html><body bgcolor='#99DB9F'></body></html>"

        if dirr == 'tag/blue':
            show_tag_scanned = False

            current_color = "#A6D3DD"

            return "<html><body bgcolor='#A6D3DD'></body></html>"

        if dirr == 'tag/pink':
            show_tag_scanned = False

            current_color = "#EDC8CE"

            return "<html><body bgcolor='#EDC8CE'></body></html>"

        if dirr == 'tag/dump':

            show_tag_scanned = True

            return "<html><body bgcolor='"+ current_color +"'></body></html>"



MyWebserver().start()

