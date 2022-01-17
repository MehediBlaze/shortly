from pymongo import MongoClient
from .config import mongo_url

client = MongoClient(mongo_url)
database = client.shortly["shorten"]
