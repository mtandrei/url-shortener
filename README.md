URL-Shortener Flask App

To get set up on the project:

1. Set up virtualenv
    - run "virtualenv venv"
    - to activate run "source venv/bin/activate"
    - to deactivate run "deactivate"
2. Use pip to install dependencies (in the virtualenv)
    - run "pip install -r pip.req". Try skipping next two commands.
3. Run "python run.py"

Database stuff:

Ubuntu: sudo apt-get install mysql-server libmysqlclient-dev python-dev
Fedora: yum install python-migrate

Run the following commands:
- "sudo mysql"
- "create database url;"
- "create user 'url'@'localhost' identified by 'url';"
- "grant all privileges on url.* to 'url'@'localhost';"
- "flush privileges;"
Quit out of mysql with "quit". Then run:
- "./migrate.py db init"
- "./migrate.py db migrate"
- "./migrate.py db upgrade"

To check the database subsequently, run "mysql -uurl -purl"
To change database structure, edit url/models.py, then run migrate and upgrade again.
If you happen to remove the migrations folder, then run init, migrate, then upgrade.
# HackHers
