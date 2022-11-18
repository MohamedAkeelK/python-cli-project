from peewee import *

db = PostgresqlDatabase('notes_app', user='mohamedkhan', password='', host='localhost', port=5432)

def Connect():
    db.connect()
    print("Connecting to postgresql database")
    return 0

Connect()

class BaseModel(Model):
    class Meta:
        database = db


class Notes(BaseModel):
    title = CharField()
    content = CharField()

db.create_tables([Notes])

def inputNote(title_input, content_input):
    newNote = Notes(title=title_input, content=content_input)
    newNote.save()
    print('Added to Notes')
    return 0

running = True

while running:
  isAddingNote = input('add a new Note? Y or N : ').lower()
  if isAddingNote == "n":
   print("Goodbye!")
   running = False
  elif isAddingNote == "y":
    note_title = input("Add a Title to This Note!")
    note_content = input("Write your note ...")
    inputNote(note_title, note_content)
  else: 
    print("invalid input, enter y or n: ")
    running = False