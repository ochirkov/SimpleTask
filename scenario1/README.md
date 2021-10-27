# First scenario
Simpliest way to implement this script and make it executable on both of Linux/MacOs - use Python 2.7.
Python 2.7 is obsolete one but it is included to distros by default as system language. 
In addition newer versions of python are compatible with 2.7, it means that this script will be executed on newer versions as well.

We use system Python, that's why we don't use custom/third-party libs, just system one.

Execute this script simply by command:

```bash
chmod +x my_cool_script.py
my_cool_script.py
``` 

If we use custom libs we could use **virtualenv** for that, but it is out of scope of this task.

In cases when we don't have Python installed but have **docker** we could use it like this:

```bash
docker build script .
docker run script
```