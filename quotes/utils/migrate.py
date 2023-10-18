import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")

import django
django.setup()

from pymongo import MongoClient

from quotesapp.models import Author, Quote, Tag

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')




client = MongoClient(f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/")

db = client.hw2_09db


authors = db.authors.find()
for author in authors:
    Author.objects.get_or_create(
        fullname=author["fullname"],
        born_date=author["born_date"],
        born_location=author["born_location"],
        bio=author["description"]
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = list()
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exists_quote = bool(len(Quote.objects.filter(quote=quote["quote"])))

    if not exists_quote:
        author = db.authors.find_one({"_id": quote["author"]})
        a = Author.objects.get(fullname=author["fullname"])
        q = Quote.objects.create(quote=quote["quote"], author=a)

        for tag in tags:
            q.tags.add(tag)
