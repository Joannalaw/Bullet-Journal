import csv
import operator
import pandas as pd

task_path = "journal.csv"


def new_task():
    item = input("Please input the task name:")
    print("Please input the date:")
    year = input("Year: ")
    month = input("Month: ")
    day = input ("Day: ")
    status = "Not Completed"
    category = input("Please input the category: ")
    try: 
        f = open(task_path)
        add_in_old(item, year, month, day, status, category)
    except IOError:
        add_in_new(item, year, month, day, status, category)


    
def add_in_new(item, year, month, day, status, category):
    with open(task_path,"w") as task_file:
        field_name_list = ["Item","Year","Month","Day","Status","category"]
        writer = csv.DictWriter(task_file, fieldnames = field_name_list)
        writer.writeheader()
        writer.writerow({"Item":item,"Year":year,"Month":month,"Day":day,"Status":status,"category":category})
        print("-------------new task is added!------------")
def add_in_old(item, year, month, day, status, category):
    with open(task_path,"a") as task_file:
        field_name_list = ["Item","Year","Month","Day","Status","category"]
        writer = csv.DictWriter(task_file, fieldnames = field_name_list)
        writer.writerow({"Item":item,"Year":year,"Month":month,"Day":day,"Status":status,"category":category})
        print("-------------------new task is added!-------------------")

def show_task():
    with open(task_path) as task_file:
        reader = csv.DictReader(task_file)
        for row in reader:
            item = row.get("Item")
            year = row.get("Year")
            month = row.get("Month")
            day = row.get("Day")
            status = row.get("Status")
            category = row.get("category")


            print("{0:<4} - {1:^2} - {2:^2}{3:^20}{4:<20}{5:<10}".format(year,month,day,item,status,category))




while True:
    print("-----------------------------------")
    print("'A': add item \n'S': show item \nexit': close journal  ")
    print("-----------------------------------")
    cmd = input("Action:")
    if cmd == "exit":
        print("-------------------closed the journal!--------------------")
        break
    if cmd =="A":
        new_task()
        show_task()
    if cmd =="S":
        show_task()



