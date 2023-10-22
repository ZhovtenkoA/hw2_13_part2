'''
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")

import django
django.setup()

from pymongo import MongoClient

from quotesapp.models import Author, Quote, Tag

import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

mongo_user = env('USER')
mongodb_pass = env('PASS')
db_name = env('db_name')
domain = env('domain')

print(db_name)


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

'''
