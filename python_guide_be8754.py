# Python Web Server Tutorial: A Simple HTTP Server

# Learning Objective:
# This tutorial will teach you how to create a very basic web server in Python.
# We'll focus on understanding the fundamental concepts of how a server
# listens for requests and sends back responses, using Python's built-in
# http.server module. This is a great starting point for anyone interested
# in web development or network programming with Python.

# We will be using Python's built-in `http.server` module.
# This module provides a simple way to create an HTTP server without needing
# to install any external libraries. It's perfect for learning the basics.

# Import the necessary modules from the http.server library.
# `HTTPServer` is the class that represents our server. It needs an address
# (host and port) and a request handler class.
# `SimpleHTTPRequestHandler` is a pre-built handler that serves files from
# the current directory. This is the easiest way to get started.
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os # We'll use `os` to get the current directory, which SimpleHTTPRequestHandler will serve from.

# --- Configuration ---
# Define the host and port for our server.
# 'localhost' means the server will only be accessible from your own computer.
# '8000' is a common port number for development servers. You can choose another
# available port if 8000 is already in use (e.g., 8080, 8888).
HOST = 'localhost'
PORT = 8000

# --- The Web Server Class ---
# We can inherit from SimpleHTTPRequestHandler to customize behavior if needed,
# but for this basic example, we'll just use it directly.
# The `HTTPServer` class is what manages the listening socket and dispatches
# incoming requests to the handler.

# --- Starting the Server ---
def run_server(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host=HOST, port=PORT):
    """
    This function sets up and runs our simple HTTP server.

    Args:
        server_class (class): The server class to use (defaults to HTTPServer).
        handler_class (class): The request handler class to use (defaults to SimpleHTTPRequestHandler).
        host (str): The hostname or IP address to bind the server to.
        port (int): The port number to listen on.
    """
    # Create an instance of the server.
    # `server_address` is a tuple containing the host and port.
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)

    # Print a message to the console indicating that the server is running
    # and where it can be accessed.
    # `os.getcwd()` gets the current working directory, which `SimpleHTTPRequestHandler`
    # will serve files from by default.
    print(f"Serving HTTP on {host} port {port} from directory {os.getcwd()}...")
    print("Press Ctrl+C to stop the server.")

    try:
        # `serve_forever()` starts the server and keeps it running indefinitely.
        # It will listen for incoming HTTP requests on the specified host and port.
        # When a request comes in, it will be handled by our `handler_class`.
        httpd.serve_forever()
    except KeyboardInterrupt:
        # This block handles the case when the user presses Ctrl+C.
        # It allows us to gracefully shut down the server.
        print("\nServer stopped.")
        # `server_close()` cleans up the server's resources.
        httpd.server_close()

# --- Main Execution Block ---
# This is a standard Python construct. The code inside this block will only
# run when the script is executed directly (not when it's imported as a module).
if __name__ == "__main__":
    # Call our function to start the server.
    run_server()

# --- Example Usage ---
# 1. Save this code as a Python file (e.g., `simple_server.py`).
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Create a simple HTML file in the same directory, for example, `index.html`, with the following content:
#    <!DOCTYPE html>
#    <html>
#    <head>
#        <title>My Simple Page</title>
#    </head>
#    <body>
#        <h1>Hello from my Python server!</h1>
#        <p>This is a basic HTML page served by Python.</p>
#    </body>
#    </html>
# 5. Run the server from your terminal:
#    python simple_server.py
# 6. Open your web browser and go to:
#    http://localhost:8000/
#    You should see your "index.html" page displayed.
# 7. If you don't have an `index.html` file, `SimpleHTTPRequestHandler` will show you a directory listing of the current folder.
# 8. To stop the server, go back to your terminal and press `Ctrl+C`.

# This simple server is great for:
# - Testing static HTML/CSS/JavaScript files locally.
# - Sharing files on your local network (if you change HOST to '0.0.0.0').
# - Understanding the very basic request/response cycle of the web.

# For more complex web applications, you would typically use a web framework
# like Flask or Django, which build upon these fundamental concepts but
# provide many more features for routing, templating, database integration, etc.