# 0x1A. Application server
# Tasks
## Task 0. Set up development with Python
mandatory

Let’s serve what you built for <strong>AirBnB clone v2 - Web framework</strong>
on web-01. This task is an exercise in setting up your development environment,
which is used for testing and debugging your code before deploying it to
production.

Requirements:
-	Make sure that task #3 of your SSH project is completed for
<code>web-01</code>. The checker will connect to your servers.
-	Install the net-tools package on your server:
<code>sudo apt install -y net-tools</code>
-	Git clone your <code>AirBnB_clone_v2</code> on your <code>web-01</code>
server.
-	Configure the file <code>web_flask/0-hello_route.py</code> to serve its
content from the route <code>/airbnb-onepage/</code> on <code>port 5000</code>.
-	Your Flask application object must be named app (This will allow us to run
and check your code).

### Notes:
-	<code>0-hello_route.py</code> route updated to <code>/airbnb-onepage/</code>
inside <code>web-01</code>
-	installed:
	-	net tools using <code>sudo apt install -y net-tools</code>
	-	python environment using <code>

## Task 
## Task 1. Set up production with Gunicorn
mandatory

Now that you have your development environment set up, let’s get your
production application server set up with Gunicorn on <code>web-01</code>,
<code>port 5000</code>. You’ll need to install Gunicorn and any libraries
required by your application. Your Flask application object will serve as a
<code>WSGI</code> entry point into your application. This will be your
production environment. As you can see we want the production and development
of your application to use the same port, so the conditions for serving your
dynamic content are the same in both environments.

Requirements:
-	Install <strong>Gunicorn</strong> and any other libraries required by your application.
-	The Flask application object should be called app. (This will allow us to run
and check your code)
-	You will serve the same content from the same route as in the previous task.
-	You can verify that it’s working by binding a Gunicorn instance to
localhost listening on <code>port 5000</code> with your application object as
the entry point.
-	In order to check your code, the checker will bind a <strong>Gunicorn</strong>
instance to <code>port 6000</code>, so make sure nothing is listening on that port.

