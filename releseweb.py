import cherrypy
import time
import os
import sys

cm = []
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
    out.replace("<replacemehere>",f"{note}")
    return out

def eventa():
    print("dropa")
def eventb():
    print("dropb")

def cmd(text):
    global cm
    for i in cm[cm.len() - 10:cm.len()]


class HelloWorldApp:

    @cherrypy.expose
    def index(self,cue="",safety=False):
        print(f"{cue}, {safety}")
        if safety:
            print(cue)
        return load("main.html","main.css")

   
            

if __name__ == '__main__':
    # Set up the server configuration to listen on port 1111
    cherrypy.config.update({
        'server.socket_port': 1111,
        'log.screen': False  # Disable console logging
    })
    cherrypy.quickstart(HelloWorldApp())



