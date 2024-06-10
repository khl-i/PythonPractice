import peewee
from peewee import *

db = MySQLDatabase('tsoc', host='10.11.3.92', user='tsoc', passwd='V3.Cupid.Tsoc@Venustech', port=3308, charset='utf8mb4')
class Price(peewee.Model):
    timestamp = peewee.DateTimeField(primary_key=True)
    BTCUSD = peewee.FloatField()

    class Meta:
        database = db
def test_peewee():
    Price.create_table()
    price = Price(timestamp='2019-06-07 13:17:18', BTCUSD='12345.67')
    price.save()

if __name__ == '__main__':
    test_peewee()