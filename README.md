thomasmanley.org
================

This is the source code for my personal website [thomasmanley.org](http://thomasmanley.org) which is currently hosted at
[Heroku](http://heroku.com). It's based on the awesome static site generator
[Pelican](http://docs.getpelican.com/en/3.5.0/). All the dependencies can be installed in a virtualenv with the
command:

    pip install -r requirements.txt

**Note:** If running on Windows you may run into problems compiling PyCrypto. If that happens, remove the line that
starts with `pycrypto` from requirements.txt and then run the following command before the `pip install` (adjust
for Python version and architecture as appropriate):

    easy_install http://www.voidspace.org.uk/downloads/pycrypto26/pycrypto-2.6.win32-py2.7.exe

The site can be built and served on [http://localhost:8000](http://localhost:8000) with the command:

    fab reserve

Download and install the [Heroku client](https://toolbelt.heroku.com/). Then the site can be deployed to Heroku with the 
command:

    git push heroku master
