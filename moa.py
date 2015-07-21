import web, sys
import threading
import json
import platform
import random

# if platform.system() == "Windows":
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

behaveList = []

bugDict = {}


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
        global new_bug
        global data
        global bugDict
        global behaveList




        #print json.dumps(phones, sort_keys=True, indent=4, separators=(',', ': '))
        if dirr[:3] == 'tag':
            #r = random.randint(1,3)

            #c = random.randint(1,5)

            #pos = str(r)+str(c)

            ip = web.ctx['ip']

            ip = str(ip[-1])

        if dirr[:3] == 'pos':
            pos = dirr[4:6]

            posInt = int(pos)

            data = web.input()
            bug = str(data.bug)
            #{ "insect": "greenBeetle", "position": 11}

            bugDict = {"insect": bug, "position": posInt}

            #take data.behaviour split on commas and make it into a list.

            print data.behaviour

            behaveList = data.behaviour.split(",")
            del behaveList[-1]

            print behaveList

            if bug != "":
                new_bug = True

            return "hej android"

        if dirr == 'view':


            if new_bug == False:
                return "no"

            if new_bug == True:
                #bug = data #{ "insect": "greenBeetle", "position": 11, 'behaviours': ["upDown", "rightLeft"]}

                new_bug = False

                bugDict['behaviours'] = behaveList


                #print json.dumps(bugDict)

                return json.dumps(bugDict)


MyWebserver().start()

''' def POST(self,dirr):


        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')


        global new_bug
        global data

        if dirr == "tag/greenbeetle":#gonna be if dirr[:3] == 'pos':
            data = web.data() # you can get data use this method

            new_bug = True

            print new_bug

            return "hej brevbarare"'''

'''         if not phoneList:
                print "phone list empty"
                phoneList.append(phoneDict)
            elif self.ipNotInList(ip, phoneList) == True:
                phoneList.appens(phoneDict)
            else:'''

