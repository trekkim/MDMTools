DEP Tool
=================

This Django project provides a custom webapp interface to micromd service (https://github.com/micromdm/micromdm). It handles adding and removing records in .json record file, applying configuration and generally running a couple of defined commands.

This project is still under development and not everything works


!!!Sorry for all mistakes done in codes, this was mostly my training project !!! Please feel free to rewrite in any aspects.

Requirements
=================

* Linux host (preffered)
* Python 3.0+ and its Django library
* Micromdm json located in /home/youraccount/DEP-Config/DEP-Profile.json
* Database file located in /var/db/deptool/database.sqllite3


Setting up
=================

# Important  : check in all location for YOURDOMAIN text and replace with your, before you start :

view.py
HTML in DEP/templates/
Scripts/

/home/youraccount/DEP_tool/upload/ = you can use your on path just make changes in code.

1. Clone the `DEP_tool` Git repository:
   ```bash
   $ cd DEP_tool
   ```
2. Make sure you have .json record file in /home/youraccount/DEP-Config/DEP-Profile.json.
3. Create a Python virtual environment for `DEP_tool`.
   ```bash
   $ python3 -m venv venv
   ```
4. Install Django library.
   ```bash
   $ source venv/bin/activate
   $ pip3 install django
   ```
5. Create database. Make sure path /var/db/deptool exists.
   ```bash
   $ python3 manage.py makemigrations
   $ python3 manage.py migrate
   ```
6. You should be able to run the tool.
   ```bash
   $ python3 manage.py runserver 0.0.0.0:8080
   ``` 
7. If you need to deploy it on Apache server you can follow:
   * https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-16-04
   * https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04


Adding new "button functionality" to main view
=================

Currently it is implemented in way that api calls are directed to /modular url. There is an "method" POST paramd which defines method which will be run on the server. If you need to add new button running command similiar to systemctl or journactl you just need to following actions:

1. Add new form to DEP/templates/DEP/main.html.
   ```html
   <form action="/modular" method="POST" class="modular_form" id='NEW_METHOD_NAME'>
       <input type="submit" value="anything" class="login100-form-btn">
   </form>
   ```
2. Add new record to modular_list in DEP/views.py.
   ```python
   modular_list = [
           {"method": "journalctl_micromdm_service",
            "command": "journalctl -u micromdm.service -n 100 --no-pager",
            "expected_result": "Logs begin at"},
           {"method": "systemctl_status_micromdm_service",
            "command": "systemctl status micromdm.service --no-pager",
            "expected_result": "micromdm.service - MicroMDM MDM Server"},
           {"method": "NEW_METHOD_NAME",
            "command": "ls -la /home/youraccount",
            "expected_result": ".bashrc"},
       ]
   ```

Permissions
=================

There are two levels of users. If you are superuser (set in Django admin site), you can see and do everything. If you are just regular staff user (set in Django admin site), you have limited view and actions you can do.

Images:
=================

please import your desired Images for icons and pictures , i removed all related internal stuff

Credits
=================

Fonts:
Font AweSome
Montserrat
Poppins

HTML Tools:

BootStrap 4 - SB Admin2
Jquery
Pace
Login
