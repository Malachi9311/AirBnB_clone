#!/usr/bin/python3

from models.__init__ import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("----------------------")
print("-- Reloaded objects --")
print("----------------------")

for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("----------------------")
print("-- Create a new object --")
print("----------------------")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
