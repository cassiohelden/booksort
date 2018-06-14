# Booksort

This project consists in an application that sort based in user choices

### Installing
In case you want to use a virtualenv to run this projetct.
```
virtualenv -p python3 envname
```

Install the requirements file, you can use pip for that:

```
pip install -r requirements.txt
```

## Commands
First of all, you need to run the migration to create default django and book models into your database. Django create an db.sqlite3 file for you no worry about it! 

```
python manage.py migrate
```

With your database and model created, you need to run this command to populate with data:
```

python manage.py populate_db
```

You can check of success message in shell.

If you want to see admin part you need to create a superuser, like this:

```
python manage.py createsuperuser
```

To run the application use:
```
python manage.py runserver
```

## Usage
To access admin page:
```
localhost:8000/admin
```

Access books list page:
```
localhost:8000/books
```
Now you can sort your data using any condition you want.

## Authors

* **Cassio Van Helden Gameiro** 
