#Imports
from fbchat import Client
from fbchat.models import *

#Bot Class
class MessageBot(Client):

    #Read Messages, See Messages from other users
    def onMessage(self, mid=None, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        try:
            msg = str(message_object).split(',')[15][14:-1]
            print(msg)

            #If user sent video or sent text
            if('//video.xx.fbcdn' in msg):
                msg = msg
            else:
                msg = str(message_object).split(',')[19][20:-1]
        except:
            try:
                msg = (message_object.text).lower()
                print(msg)
            except:
                pass

    #Reply to User
        def sendMsg():
            if(author_id != self.uid):
                self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

        #Send Message
        if(author_id != self.uid):
            if("hi" in msg):
                reply = "Hello!"
                sendMsg()
            elif("Crazy" or "crazy" in msg):
                reply = "Crazy? I was Crazy Once. They Locked me in a room. A rubber room. A rubber room with rats. And rats make me crazy."
                sendMsg()
            else:
                pass


session_cookies = {
    "sb" : "",
    "fr" : "",
    "c_user" : "",
    "datr" : "",
    "xs" : "",
}

bot = MessageBot('EMAIL', 'PASSWORD', session_cookies=session_cookies)
print(bot.isLoggedIn())

try:
    bot.listen()
except:
    bot.listen()