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
            self.send(Message(text=reply))