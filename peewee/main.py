import datetime
import peewee

db = peewee.MySQLDatabase('tsoc', host='10.11.3.92', user='tsoc', passwd='V3.Cupid.Tsoc@Venustech', port=3308, charset='utf8mb4')

class Note(peewee.Model):
    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = 'notes'

def test_note():
    Note.create_table()
    note1 = Note.create(text='Went to the cinema')
    note1.save()

if __name__ == '__main__':
    test_note()