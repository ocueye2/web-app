import cherrypy
import time
import os
import sys

def load(html,css=""):
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
    return out

class HelloWorldApp:

    @cherrypy.expose
    def index(self):
        # HTML for the webpage
        return load("main.html","main.css")

    @cherrypy.expose
    def dropa(self):

        print("Dropped")


        return ("<h1> done </h1> <a href='/proxy/8000/'>test </a>")
        raise cherrypy.HTTPRedirect('/proxy/1111/')

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

