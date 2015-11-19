""""
Columbia W4111 Intro to Databases
Christina Nguyen (chn2109)
Faith Yu (fjy2101)
"""
from pprint import pprint
import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

#
# The following uses the sqlite3 database test.db -- you can use this for debugging purposes
# However for the project you will need to connect to your Part 2 database in order to use the
# data
#
# XXX: The URI should be in the format of:
#
#     postgresql://USER:PASSWORD@w4111db1.cloudapp.net:5432/proj1part2
#
# For example, if you had username ewu2493, password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://ewu2493:foobar@w4111db1.cloudapp.net:5432/proj1part2"
#

DATABASEURI = "postgresql://chn2109:680@w4111db1.cloudapp.net:5432/proj1part2"

#
# This line creates a database engine that knows how to connect to the URI above
#
engine = create_engine(DATABASEURI)

@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request
  The variable g is globally accessible
  """
  try:
    g.conn = engine.connect()
  except:
    print "uh oh, problem connecting to database"
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass

"""
try:
  g.conn = engine.connect()
except:
  print "uh oh, problem connecting to database"
  import traceback; traceback.print_exc()
  g.conn = None

try:
  g.conn.close()
except Exception as e:
  pass
"""

@app.route('/', methods=["POST", "GET"])
def index():
  """
  request is a special object that Flask provides to access web request information:
  request.method:   "GET" or "POST"
  request.form:     if the browser submitted a form, this contains the data in the form
  request.args:     dictionary of URL arguments e.g., {a:1, b:2} for http://localhost?a=1&b=2
  See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
  """
  print 'There are 24 magical SuperSammies.'
  print 'Let\'s test out SuperSammie with all the ingredients. Will it produce all 24 possible Sammies?'
  g.conn.execute("DELETE FROM Ingredients")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('slicedbread','bread')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('roll','bread')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('baguette','bread')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('flatbread','bread')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('hardboiledegg','protein')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('coldcut','protein')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('steak','protein')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('tuna','protein')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('bacon','protein')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('chicken','protein')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('friedegg','protein')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('pork','protein')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('portobello','protein')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('meatball','protein')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('cheddar','cheese')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('pepperjack','cheese')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('brie','cheese')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('swiss','cheese')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('mozzarella','cheese')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('gouda','cheese')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('montereyjack','cheese')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('goat','cheese')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('feta','cheese')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('parmesan','cheese')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('lettuce','vegetable')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('spinach','vegetable')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('redonion','vegetable')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('mushroom','vegetable')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('cucumber','vegetable')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('avocado','vegetable')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('tomato','vegetable')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('sprouts','vegetable')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('olive','vegetable')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('bellpepper','vegetable')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('strawberry','fruit')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('banana','fruit')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('apple','fruit')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('blueberry','fruit')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('raspberry','fruit')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('pear','fruit')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('ketchup','condiment')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('mustard','condiment')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('mayonnaise','condiment')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('pesto','condiment')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('jelly','condiment')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('peanutbutter','condiment')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('hummus','condiment')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('sriracha','condiment')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('barbecue','condiment')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('oliveoil','condiment')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('chips','other')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('pickle','other')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('jalapeno','other')")
  g.conn.execute("INSERT INTO Ingredients (name, type) VALUES ('fries','other')")

  possibleSammies = ['FancyGC','ChickenSammie','ColdSammie','MeltSammie','FunSammie','SpicyGC','ReallyFancyGC','ChickenParm','BaconFlatbread','EggSammie','BreakfastSammie','GreekFlatbread','WeirdGC','FatSammie','PorkSammie','MeatballSub','FetaSammie','TunaGC','FruitPB','RaspberrySammie','RaspberryPB','BBQPork','AvocadoSammie','MushroomGC']

#This code should work. For some reason, it doesn't. :( 
# And... this is why we have to use the brute force method. 
# If you could tell us why, and how to fix it, that would be amazing. We're dying to know. 
#
#  foundSammies = []
#  recipelength = [3,6,6,5,5,5,3,4,6,4,4,5,3,6,5,6,6,9,5,5,4,4,5,6]
#
#  for recipe in possibleSammies:
#    cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT SELECT name FROM (SELECT name FROM Recipes WHERE name = (%s))", recipe)
#    for result in cursor:
#      foundSammies.append(str(result['name']))
#    cursor.close()
#
#  i = 0
#  for f in foundSammies: 
#    if foundSammies[i] != 'NO':
#      SuperSammies.update({possibleSammies[i]:foundSammies[i]})
#    i += 1

  SuperSammies = {}

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from FancyGC") 
  temp = []
  for result in cursor:  
    temp.append(str(result['name']))
  if len(temp) == 3: 
    SuperSammies.update({'FancyGC':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from ChickenSammie")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 6:
    SuperSammies.update({'ChickenSammie':temp})
  cursor.close()  

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from ColdSammie")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 6:
    SuperSammies.update({'ColdSammie':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from MeltSammie")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 5:
    SuperSammies.update({'MeltSammie':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from FunSammie")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 5:
    SuperSammies.update({'FunSammie':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from SpicyGC")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 5:
    SuperSammies.update({'SpicyGC':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from ReallyFancyGC")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 3:
    SuperSammies.update({'ReallyFancyGC':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from ChickenParm")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 4:
    SuperSammies.update({'ChickenParm':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from BaconFlatbread")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 6:
    SuperSammies.update({'BaconFlatbread':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from EggSammie")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 4:
    SuperSammies.update({'EggSammie':temp})
  cursor.close()  

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from BreakfastSammie")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 4:
    SuperSammies.update({'BreakfastSammie':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from GreekFlatbread")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 5:
    SuperSammies.update({'GreekFlatbread':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from WeirdGC")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 3:
    SuperSammies.update({'WeirdGC':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from FatSammie")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 6:
    SuperSammies.update({'FatSammie':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from PorkSammie")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 5:
    SuperSammies.update({'PorkSammie':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from MeatballSub")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 6:
    SuperSammies.update({'MeatballSub':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from FetaSammie")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 6:
    SuperSammies.update({'FetaSammie':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from TunaGC")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 9:
    SuperSammies.update({'TunaGC':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from FruitPB")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 5:
    SuperSammies.update({'FruitPB':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from RaspberrySammie")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 5:
    SuperSammies.update({'RaspberrySammie':temp})
  cursor.close()  

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from RaspberryPB")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 4:
    SuperSammies.update({'RaspberryPB':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from BBQPork")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 4:
    SuperSammies.update({'BBQPork':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from AvocadoSammie")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 5:
    SuperSammies.update({'AvocadoSammie':temp})
  cursor.close()

  cursor = g.conn.execute("SELECT name FROM Ingredients INTERSECT Select name from MushroomGC")
  temp = []
  for result in cursor:
    temp.append(str(result['name']))
  if len(temp) == 6:
    SuperSammies.update({'MushroomGC':temp})
  cursor.close()

  pprint(SuperSammies)

  context = dict( data = SuperSammies)

  return render_template("index.html",**context)

if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using
        python server.py
    Show the help text using
        python server.py --help
    """

    HOST, PORT = host, port
    print "running on %s:%d" % (HOST, PORT)
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

  run()
