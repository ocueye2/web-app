import cherrypy
import time
import os
import sys

cm = []
for i in range(9):
    cm.append("-")

def load(html,css="",note=""):
    path = os.path.dirname(sys.argv[0])
    f = open(f"{path}/web/{html}")
    c = open(f"{path}/web/{css}")
    out = f"""
    <html>
    <style>
    {c.read()}
    </style>
    {f.read()}
    """
    out = out.replace("<replacemehere>",f"{cmd(note)}")
    return out

def listcues():
    path = os.path.dirname(sys.argv[0])
    out = ""
    for i in os.listdir(f"{path}/cues"):
        out = out + f"\n {i}"
    return out



def cmd(text):
    global cm
    if not text == "":
        cm.append(text)
    out = ""

    if len(cm) > 5:
        ls = cm[len(cm) - 5: len(cm)]
    else:
        ls = cm
    
    for i in ls:
        out = f"{out} <p> {i} </p>"
    return out


class HelloWorldApp:

    @cherrypy.expose
    def index(self,cue="",safety=False):
        print(f"{cue}, {safety}")
        out = ""
        if cue == "clear":
                global cm
                cm = []
                for i in range(9):
                    cm.append("-")
        elif cue == "refresh":
            print("refresh")
        elif cue == "list":
            listcues()
            out = ""
        
        elif not safety == False:
            
            if cue == "stop":
                print("stopping")
                exit()
            else:
                out = f"error, cue '{cue}' does not exist"

        elif cue == "":
            out = "new connection"
        else:
            out = f"could not run '{cue}', safety not on"
            

           
        return load("main.html","main.css",out)
    

   
            

if __name__ == '__main__':
    # Set up the server configuration to listen on port 1111
    cherrypy.config.update({
        'server.socket_port': 8080,
        'log.screen': False  # Disable console logging
    })
    cherrypy.quickstart(HelloWorldApp())



