# Toys

## Install

In db create user:
<pre> 
db_name:   test3
user_name: moni3
password:  Mertelya2
</pre> 

Upload dump to database:
```bash
psql -h localhost -d test3 -U moni3 -f sqll.sql 
```
Expected output:
<pre>
Password for user moni3: 
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
</pre>


Use in venv: 
```bash
source ./build_files.sh
```

Make migrations:
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```