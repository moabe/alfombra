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


current_color = "#000000"
old_current_color = current_color;

data = ""

new_bug = False


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

        global current_color
        global old_current_color
        global show_tag_scanned
        global phoneList
        global phones

        global new_bug


        global data








        #phones = {"phones": phoneList}





        #print json.dumps(phones, sort_keys=True, indent=4, separators=(',', ': '))
        if dirr[:3] == 'tag':
            #r = random.randint(1,3)

            #c = random.randint(1,5)

            #pos = str(r)+str(c)

            ip = web.ctx['ip']

            ip= str(ip[-1])



        if dirr == 'view':


            print (new_bug)
            if new_bug == False:
                print "no"
                return "no"


            if new_bug == True:
                #old_current_color = current_color;
                #color = {"color":current_color}

                print "eeeelsee"

                bug = data #{ "insect": "greenBeetle", "position": 11, 'behaviours': ["upDown", "rightLeft"]}

                new_bug = False

                print json.dumps(bug)

                return json.dumps(bug)






    def POST(self,dirr):


        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')


        global new_bug
        global data

        if dirr == "tag/greenbeetle":#gonna be if dirr[:3] == 'pos':
            data = web.data() # you can get data use this method

            new_bug = True

            print new_bug

            return "hej brevbarare"




MyWebserver().start()





'''         if not phoneList:
                print "phone list empty"
                phoneList.append(phoneDict)
            elif self.ipNotInList(ip, phoneList) == True:
                phoneList.appens(phoneDict)
            else:'''

