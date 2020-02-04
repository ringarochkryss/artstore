# Code Institute

Welcome Petra  Mellbrand,

We have preinstalled all of the tools you need to get started.

To run a frontend application in GitPod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Expose*,

Another blue button should appear to click: *Open Browser*.

To run a backend python file, type `python3 app.py`, if your python file is named `app.py` of course.

A blue button should appear to click: *Expose*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons. 

Happy coding!


For Flask and Django, to add environment variables locally in editor, you'll want to do the following:
•	Create an env.py file and add it to your .gitignore file with the following commands:
touch env.py 
             echo env.py > .gitignore

•	Add the following to your new env.py file:
import os
os.environ.setdefault("MONGO_URI", "your_URI_here")
•	Then, in your app.py file, you'll want to include:
import os
import env
app.config['MONGO_URI'] = os.getenv('MONGO_URI', "Env value not loaded")
You can follow this example to assign the rest of your environment variables now!
