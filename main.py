
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

uri = "mongodb+srv://UserPupik:User1@cluster0.f751nmx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.cats_collection
collection = db.cats


db.cats.insert_many([
    {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    },

    {
    "name": "mursik",
    'age':3,
    "features":['normal','allows to pet','red color'],
}]
)


def read_all_records():
    records = collection.find({})
    for record in records:
        print(record)

def read_cat_by_name(name):
    """Функція, яка дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота."""
    cat = collection.find_one({'name': name})
    if cat:
        print(cat)
    else:
        print("Кіт з таким ім'ям не знайдений.")

def update_age_by_name(name, new_age):
    """Функція, яка дозволяє користувачеві оновити вік кота за ім'ям."""
    cat = collection.find_one({'name': name})
    if cat:
        collection.update_one({'name': name}, {'$set': {'age': new_age}})
        print("Вік кота оновлено.")
    else:
        print("Кіт з таким ім'ям не знайдений.")

def add_feature_by_name(name, new_feature):
    """Функція, яка дозволяє додати нову характеристику до списку features кота за ім'ям."""
    cat = collection.find_one({'name': name})
    if cat:
        collection.update_one({'name': name}, {'$push': {'features': new_feature}})
        print("Характеристику додано.")
    else:
        print("Кіт з таким ім'ям не знайдений.")

def delete_record_by_name(name):
    cat = collection.find_one({'name': name})   
    if cat:
        collection.delete_one({'name': name})
        print("Запис про кота видалено.")
    else:
        print("Кіт з таким ім'ям не знайдений.")

def delete_all_records():
    """Функція для видалення всіх записів із колекції."""
    collection.delete_many({})
    print("Всі записи в колекції видалено.")



read_all_records()
read_cat_by_name('barsik')
update_age_by_name('barsik', 2)
add_feature_by_name('barsik', 'farting')
delete_record_by_name('barsik')
delete_all_records()





try:
    client.admin.command('ping')





except Exception as e:
    print(e)