import web, sys
import threading
import json
import platform
import random

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


#current_color = "black"

show_tag_scanned = False


phoneList = []

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

        #global current_color
        global show_tag_scanned
        global phoneList
        global phones






        phones = {"phones": phoneList}



        #print json.dumps(phones, sort_keys=True, indent=4, separators=(',', ': '))
        if dirr[:3] == 'tag':
            r = random.randint(1,3)

            c = random.randint(1,5)

            pos = str(r)+str(c)

            ip = web.ctx['ip']

            ip= str(ip[-1])

        if dirr == 'view':

            return json.dumps(phones)

        if dirr == 'tag/yellow':

            show_tag_scanned = False

            current_color = "#E4E6AE"


            pearlsList = []


            pearlDict = {"color":current_color, "pos": pos}

            pearlsList.append(pearlDict)

            phoneDict = { "ip" : ip, "pearls" : pearlsList }

            phoneList.append(phoneDict)




            return "<html><body bgcolor='#E4E6AE'></body></html>"









        if dirr == 'tag/green':
            show_tag_scanned = False

            current_color = "#99DB9F"


            pearlsList = []


            pearlDict = {"color":current_color, "pos": pos}

            pearlsList.append(pearlDict)

            phoneDict = { "ip" : ip, "pearls" : pearlsList }


            phoneList.append(phoneDict)



            return "<html><body bgcolor='#99DB9F'></body></html>"

        if dirr == 'tag/blue':
            show_tag_scanned = False

            current_color = "#A6D3DD"


            pearlsList = []


            pearlDict = {"color":current_color, "pos": pos}

            pearlsList.append(pearlDict)

            phoneDict = { "ip" : ip, "pearls" : pearlsList }

            phoneList.append(phoneDict)

            return "<html><body bgcolor='#A6D3DD'></body></html>"

        if dirr == 'tag/pink':
            show_tag_scanned = False

            current_color = "#EDC8CE"


            pearlsList = []


            pearlDict = {"color":current_color, "pos": pos}

            pearlsList.append(pearlDict)

            phoneDict = { "ip" : ip, "pearls" : pearlsList }

            phoneList.append(phoneDict)

            return "<html><body bgcolor='#EDC8CE'></body></html>"

        if dirr == 'tag/dump':

            show_tag_scanned = True

            return "<html><body bgcolor='"+ current_color +"'></body></html>"



MyWebserver().start()

