import cherrypy
import time
import os
import sys

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
    <div class="note">
    <h2> {note} </h2>
    """
    return out

def eventa():
    print("dropa")
def eventb():
    print("dropb")

class HelloWorldApp:

    @cherrypy.expose
    def index(self):
        # HTML for the webpage
        return load("main.html","main.css")

    @cherrypy.expose
    def eventa(self):
        eventa()
        return load("main.html","main.css","drop a active")

    @cherrypy.expose
    def eventb(self):
        eventb()
        return load("main.html","main.css","drop b active")
    @cherrypy.expose
    def stop(self):
        exit()
            

if __name__ == '__main__':
    # Set up the server configuration to listen on port 1111
    cherrypy.config.update({
        'server.socket_port': 1111,
        'log.screen': False  # Disable console logging
    })
    cherrypy.quickstart(HelloWorldApp())



