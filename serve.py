import os, sys
os.chdir("/Users/nickagostino/Library/CloudStorage/OneDrive-AGH/AGH Shared Claude/Sienna Wood App")
from http.server import HTTPServer, SimpleHTTPRequestHandler
HTTPServer(("", 3456), SimpleHTTPRequestHandler).serve_forever()
