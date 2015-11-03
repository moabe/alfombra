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


data = ""

new_bug = False


behaveList = []

bugDict = {}


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

        global new_bug
        global data
        global bugDict
        global behaveList

        if dirr[:3] == 'pos':
            pos = dirr[4:6]

            posInt = int(pos)

            data = web.input()
            bug = str(data.bug)
            exp = str(data.exp)


            bugDict = {"insect": bug, "position": posInt, "explode": exp}

            print "explode: " + exp
            print bug

            # take data.behaviour split on commas and make it into a list.

            # print data.behaviour

            behaveList = data.behaviour.split(",")
            del behaveList[-1]

            print behaveList

            # check so I didn't just send position without bug
            if bug != "":
                new_bug = True

            return "hej android"

        if dirr == 'view':

            if not new_bug:
                return "no"

            if new_bug:
                # bug = data #{ "insect": "greenBeetle", "position": 11, 'behaviours': ["upDown", "rightLeft"]}

                new_bug = False

                bugDict['behaviours'] = behaveList

                # print json.dumps(bugDict)

                return json.dumps(bugDict)


MyWebserver().start()