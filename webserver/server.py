"""
Columbia W4111 Intro to databases
Example webserver
To run locally
    python server.py
Go to http://localhost:8111 in your browser
A debugger such as "pdb" may be helpful for debugging.
Read about it online.
eugene wu 2015
"""

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

def validate1(recipe):
  """
  @param recipe is a list from the list of lists (PBJSammies, GCSammies)
  @return whether this recipe is a SuperSammie
  """
  # we don't want plain sandwiches!
  if len(recipe) <= 2:
    return False

  else:
    return True

def validate2(recipe, bread, vegetable, other, protein, condiment):
  """
  @param recipe is a list from the list of lists (CSammies, SSammies, HSammies),
  bread, vegetable, and protein are lists specific to these sandwiches
  @return whether this recipe is a SuperSammie
  """
  # you need to have at least bread, protein, vegetable, and condiment
  if len(recipe) <= 3:
    return False

  if (len(set(vegetable) - set(recipe)) == 0) or (len(set(protein) - set(recipe)) == 0):
    return False

  if (len(set(protein) & set(recipe)) != 1):
    return False

  if (len(set(bread) & set(recipe)) != 1):
    return False

  if (len(set(other) & set(recipe)) > 1):
    return False

  if (len(set(condiment) & set(recipe)) != 1):
    return False

  else:
    return True

#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a POST or GET request
#
# If you wanted the user to go to e.g., localhost:8111/foobar/ with POST or GET then you could use
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
#
# see for routing: http://flask.pocoo.org/docs/0.10/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#
@app.route('/', methods=["POST", "GET"])
def index():
  """
  request is a special object that Flask provides to access web request information:
  request.method:   "GET" or "POST"
  request.form:     if the browser submitted a form, this contains the data in the form
  request.args:     dictionary of URL arguments e.g., {a:1, b:2} for http://localhost?a=1&b=2
  See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
  """
  # DEBUG: this is debugging code to see what request looks like
  print request.args


  return render_template("results.html", **context)

@app.route('/error/', methods=["POST","GET"])
def error():
  return render_template("error.html")

@app.route('/results/', methods=["POST","GET"])
def add_entry():
  g.conn.execute("INSERT INTO Bread (type) VALUES (%s)", [request.form['slicedbread']])
  g.conn.execute("INSERT INTO Bread (type) VALUES (%s)", [request.form['roll']])
  g.conn.execute("INSERT INTO Bread (type) VALUES (%s)", [request.form['baguette']])
  g.conn.execute("INSERT INTO Bread (type) VALUES (%s)", [request.form['flatbread']])
  g.conn.execute("INSERT INTO Protein (type) VALUES (%s)", [request.form['coldcut']])
  g.conn.execute("INSERT INTO Protein (type) VALUES (%s)", [request.form['hardboiledegg']])
  g.conn.execute("INSERT INTO Protein (type) VALUES (%s)", [request.form['steak']])
  g.conn.execute("INSERT INTO Protein (type) VALUES (%s)", [request.form['tuna']])
  g.conn.execute("INSERT INTO Protein (type) VALUES (%s)", [request.form['bacon']])
  g.conn.execute("INSERT INTO Protein (type) VALUES (%s)", [request.form['chicken']])
  g.conn.execute("INSERT INTO Protein (type) VALUES (%s)", [request.form['friedegg']])
  g.conn.execute("INSERT INTO Protein (type) VALUES (%s)", [request.form['pork']])
  g.conn.execute("INSERT INTO Protein (type) VALUES (%s)", [request.form['portobello']])
  g.conn.execute("INSERT INTO Protein (type) VALUES (%s)", [request.form['meatball']])
  g.conn.execute("INSERT INTO Cheese(type) VALUES (%s)", [request.form['cheddar']])
  g.conn.execute("INSERT INTO Cheese(type) VALUES (%s)", [request.form['pepperjack']])
  g.conn.execute("INSERT INTO Cheese(type) VALUES (%s)", [request.form['brie']])
  g.conn.execute("INSERT INTO Cheese(type) VALUES (%s)", [request.form['swiss']])
  g.conn.execute("INSERT INTO Cheese(type) VALUES (%s)", [request.form['mozzarella']])
  g.conn.execute("INSERT INTO Cheese(type) VALUES (%s)", [request.form['gouda']])
  g.conn.execute("INSERT INTO Cheese(type) VALUES (%s)", [request.form['montereyjack']])
  g.conn.execute("INSERT INTO Cheese(type) VALUES (%s)", [request.form['goat']])
  g.conn.execute("INSERT INTO Cheese(type) VALUES (%s)", [request.form['feta']])
  g.conn.execute("INSERT INTO Cheese(type) VALUES (%s)", [request.form['parmesan']])
  g.conn.execute("INSERT INTO Vegetable(type) VALUES (%s)", [request.form['lettuce']])
  g.conn.execute("INSERT INTO Vegetable(type) VALUES (%s)", [request.form['spinach']])
  g.conn.execute("INSERT INTO Vegetable(type) VALUES (%s)", [request.form['redonion']])
  g.conn.execute("INSERT INTO Vegetable(type) VALUES (%s)", [request.form['mushroom']])
  g.conn.execute("INSERT INTO Vegetable(type) VALUES (%s)", [request.form['cucumber']])
  g.conn.execute("INSERT INTO Vegetable(type) VALUES (%s)", [request.form['avocado']])
  g.conn.execute("INSERT INTO Vegetable(type) VALUES (%s)", [request.form['tomato']])
  g.conn.execute("INSERT INTO Vegetable(type) VALUES (%s)", [request.form['sprouts']])
  g.conn.execute("INSERT INTO Vegetable(type) VALUES (%s)", [request.form['olive']])
  g.conn.execute("INSERT INTO Vegetable(type) VALUES (%s)", [request.form['bellpepper']])
  g.conn.execute("INSERT INTO Fruit(type) VALUES (%s)", [request.form['strawberry']])
  g.conn.execute("INSERT INTO Fruit(type) VALUES (%s)", [request.form['banana']])
  g.conn.execute("INSERT INTO Fruit(type) VALUES (%s)", [request.form['apple']])
  g.conn.execute("INSERT INTO Fruit(type) VALUES (%s)", [request.form['blueberry']])
  g.conn.execute("INSERT INTO Fruit(type) VALUES (%s)", [request.form['raspberry']])
  g.conn.execute("INSERT INTO Fruit(type) VALUES (%s)", [request.form['pear']])
  g.conn.execute("INSERT INTO Condiment (type) VALUES (%s)", [request.form['ketchup']])
  g.conn.execute("INSERT INTO Condiment (type) VALUES (%s)", [request.form['mustard']])
  g.conn.execute("INSERT INTO Condiment (type) VALUES (%s)", [request.form['mayonnaise']])
  g.conn.execute("INSERT INTO Condiment (type) VALUES (%s)", [request.form['pesto'])
  g.conn.execute("INSERT INTO Condiment (type) VALUES (%s)", [request.form['jelly']])
  g.conn.execute("INSERT INTO Condiment (type) VALUES (%s)", [request.form['peanutbutter']])
  g.conn.execute("INSERT INTO Condiment (type) VALUES (%s)", [request.form['hummus']])
  g.conn.execute("INSERT INTO Condiment (type) VALUES (%s)", [request.form['sriracha']])
  g.conn.execute("INSERT INTO Condiment (type) VALUES (%s)", [request.form['barbecue']])
  g.conn.execute("INSERT INTO Condiment (type) VALUES (%s)", [request.form['oliveoil']])
  g.conn.execute("INSERT INTO Other (type) VALUES (%s)", [request.form['chips']])
  g.conn.execute("INSERT INTO Other (type) VALUES (%s)", [request.form['pickle']])
  g.conn.execute("INSERT INTO Other (type) VALUES (%s)", [request.form['jalapeno']])
  g.conn.execute("INSERT INTO Other (type) VALUES (%s)", [request.form['fries']])

  import itertools # we will use this to find all the combinations of possible sandwiches

  # check if a sandwich is even possible!
  if not bread:
    # make the app redirect to some sort of error page
    return render_template("error.html")

  # tells us if sandwiches are even possible
  PBJ = True
  GrilledCheese = True
  ColdSammie = True
  SaladSammie = True
  HotSammie = True

  SuperSammies = {} # dictionary of SuperSammies

  # lists of lists of all possible sandwiches (that may not necessarily be SuperSammies)
  PBJSammies = []
  GCSammies = []
  CSammies = []
  SSammies = []
  HSammies = []

  # implementing check constraints for PBJ
  # note to self: g.conn.execute automatically guards against SQL injection YAY
  cursor = g.conn.execute("SELECT type FROM Bread WHERE type = 'slicedbread'")
  slicedbread = []
  for result in cursor:
    slicedbread.append(str(result['type']))
  cursor.close()

  cursor = g.conn.execute("SELECT type FROM Condiment WHERE type = 'peanutbutter' or type = 'jelly'")
  PBJcondiment = []
  for result in cursor:
    PBJcondiment.append(str(result['type']))
  cursor.close()

  cursor = g.conn.execute("SELECT type FROM Fruit")
  fruit = []
  for result in cursor:
    fruit.append(str(result['type']))
  cursor.close()

  # let's see if PBJ is a possible sammie
  if len(slicedbread) == 0 or len(PBJcondiment) == 0:
    PBJ = False

  # sort into PBJ sandwiches
  while PBJ == True:
    n = 1
    i = 0 #index
    inside = fruit
    for x in xrange(1,len(inside)+1):
      tempsammies = list(itertools.combinations(inside,x))
      k = 0
      for j in tempsammies:
        value = list(tempsammies[k])
        PBJSammies.append(value)
        k += 1
        n += 1
    while i < len(PBJSammies):
      PBJSammies[i].append('slicedbread')
      i += 1

    # insert only SuperSammies into SuperSammies dictionary
    i = 0 #reset the value of the index
    while i < len(PBJSammies):
      if validate1(PBJSammies[i]) is False:
        PBJSammies.pop(i)
      else:
        i += 1

    # now insert the SuperSammies into the SuperSammies dictionary
    for j in PBJSammies:
      key = 'PBJ'
      SuperSammies.update({key:PBJSammies})

  print SuperSammies

  # implementing check constraints for GrilledCheese
  cursor = g.conn.execute("SELECT type FROM Cheese")
  cheese = []
  for result in cursor:
    cheese.append(str(result['type']))
  cursor.close()

  # you don't HAVE to fulfill this constraint to make a grilled cheese
  cursor = g.conn.execute("SELECT type FROM Vegetable WHERE type = 'mushroom' or type = 'avocado' or type = 'tomato'")
  GrilledCheesevegetable = []
  for result in cursor:
    GrilledCheesevegetable.append(str(result['type']))
  cursor.close()

  cursor = g.conn.execute("SELECT type FROM Condiment WHERE type = 'butter' or type = 'pesto'")
  GrilledCheesecondiment = []
  for result in cursor:
    GrilledCheesecondiment.append(str(result['type']))
  cursor.close()

  if len(slicedbread) == 0 or len(cheese) == 0:
    GrilledCheese = False

  if 'butter' not in GrilledCheesecondiment:
    GrilledCheese = False

  # sort into GrilledCheese
  while GrilledCheese == True:
    n = 1
    i = 0 #index
    inside = GrilledCheesevegetable + GrilledCheesecondiment + cheese
    for i in xrange(1,len(inside)+1):
      tempsammies = list(itertools.combinations(inside,i))
      k = 0
      for j in tempsammies:
        value = list(tempsammies[k])
        GCSammies.append(value)
        k += 1
        n += 1
    while i < len(GCSammies):
      GCSammies[i].append('slicedbread')
      i += 1

    # insert only SuperSammies into SuperSammies dictionary
    i = 0 #reset the value of the index
    while i < len(GCSammies):
      if validate1(GCSammies[i]) is False:
        GCSammies.pop(i)
      else:
        i += 1

    # now insert the SuperSammies into the SuperSammies dictionary
    for j in PBJSammies:
      key = 'GC'
      SuperSammies.update({key:GCSammies})

  # implementing check constraints for ColdSammie
  cursor = g.conn.execute("SELECT type FROM Protein WHERE type = 'tuna' or type = 'hardboiledegg' or type = 'coldcut' or type = 'portobello'")
  ColdSammieprotein = []
  for result in cursor:
    ColdSammieprotein.append(str(result['type']))
  cursor.close()

  cursor = g.conn.execute("SELECT type FROM Condiment WHERE type = 'mustard' or type = 'mayonnaise' or type = 'pesto' or type = 'ketchup' or type = ‘hummus’ or type = ‘sriracha’ or type = ‘oliveoil’")
  ColdSammiecondiment = []
  for result in cursor:
    ColdSammiecondiment.append(str(result['type']))
  cursor.close()

  cursor = g.conn.execute("SELECT type FROM Bread")
  bread = []
  for result in cursor:
    bread.append(str(result['type']))
  cursor.close()

  cursor = g.conn.execute("SELECT type FROM Vegetable")
  vegetable = []
  for result in cursor:
    vegetable.append(str(result['type']))
  cursor.close()

  cursor = g.conn.execute("SELECT type FROM Other")
  other = []
  for result in cursor:
    other.append(str(result['type']))
  cursor.close()

  if len(ColdSammieprotein) == 0:
    ColdSammie = False

  # sort into ColdSammie
  while ColdSammie == True:
    n = 1
    i = 0 #index
    inside = bread + vegetable + other + ColdSammieprotein + ColdSammiecondiment
    for i in xrange(1,len(inside)+1):
      tempsammies = list(itertools.combinations(inside,i))
      k = 0
      for j in tempsammies:
        value = list(tempsammies[k])
        CSammies.append(value)
        k += 1
        n += 1

    # insert only SuperSammies into SuperSammies dictionary value
    i = 0 #reset the value of the index
    while i < len(CSammies):
      if validate2(CSammies[i],bread,vegetable,other,ColdSammieprotein,ColdSammiecondiment) is False:
        CSammies.pop(i)
      else:
        i += 1

    # now insert the SuperSammies into the SuperSammies dictionary
    for j in CSammies:
      key = 'CS'
      SuperSammies.update({key:CSammies})

  # implementing check constraints for SaladSammie
  cursor = g.conn.execute("SELECT type FROM Protein WHERE type = 'chicken' or type = 'hardboiledegg' or type = 'tuna'")
  SaladSammieprotein = []
  for result in cursor:
    SaladSammieprotein.append(str(result['type']))
  cursor.close()

  cursor = g.conn.execute("SELECT type FROM Condiment WHERE type = 'mustard' or type = 'mayonnaise'")
  SaladSammiecondiment = []
  for result in cursor:
    SaladSammiecondiment.append(str(result['type']))
  cursor.close()

  if len(SaladSammieprotein) == 0:
    SaladSammie = False

  # sort into SaladSammie
  while SaladSammie == True:
    n = 1
    i = 0 #index
    inside = bread + vegetable + other + SaladSammieprotein + SaladSammiecondiment
    for i in xrange(1,len(inside)+1):
      tempsammies = list(itertools.combinations(inside,i))
      k = 0
      for j in tempsammies:
        value = list(tempsammies[k])
        SSammies.append(value)
        k += 1
        n += 1

    # insert only SuperSammies into SuperSammies dictionary value
    i = 0 #reset the value of the index
    while i < len(SSammies):
      if validate2(SSammies[i],bread,vegetable,other,SaladSammieprotein,SaladSammiecondiment) is False:
        SSammies.pop(i)
      else:
        i += 1

    # now insert the SuperSammies into the SuperSammies dictionary
    for j in SSammies:
      key = 'SS'
      SuperSammies.update({key:SSammies})

  # implementing check constraints for HotSammie
  cursor = g.conn.execute("SELECT type FROM Protein WHERE type = 'bacon' or type = 'steak' or type = 'chicken' or type = 'friedegg' or type = 'pork' or type = 'meatball'")
  HotSammieprotein = []
  for result in cursor:
    HotSammieprotein.append(str(result['type']))
  cursor.close()

  cursor = g.conn.execute("SELECT type FROM Vegetable WHERE type = 'mushroom' or type = 'avocado' or type = 'tomato' or type = 'redonion' or type = 'olive' or type = 'bellpepper'")
  HotSammievegetable = []
  for result in cursor:
    HotSammievegetable.append(str(result['type']))
  cursor.close()

  cursor = g.conn.execute("SELECT type FROM Condiment WHERE type = 'mustard' or type = 'ketchup' or type = 'mayonnaise' or type = 'pesto' or type = 'hummus' or type = 'sriracha' or type = 'barbecue' or type = 'oliveoil'")
  HotSammiecondiment = []
  for result in cursor:
    HotSammiecondiment.append(str(result['type']))
  cursor.close()

  if len(HotSammieprotein) == 0:
    HotSammie = False

  # sort into HotSammie
  while HotSammie == True:
    n = 1
    i = 0 #index
    inside = bread + HotSammievegetable + other + HotSammieprotein + HotSammiecondiment
    for i in xrange(1,len(inside)+1):
      tempsammies = list(itertools.combinations(inside,i))
      k = 0
      for j in tempsammies:
        value = list(tempsammies[k])
        HSammies.append(value)
        k += 1
        n += 1

    # insert only SuperSammies into SuperSammies dictionary value
    i = 0 #reset the value of the index
    while i < len(HSammies):
      if validate2(HSammies[i],bread,HotSammievegetable,other,HotSammieprotein,HotSammiecondiment) is False:
        HSammies.pop(i)
      else:
        i += 1

    # now insert the SuperSammies into the SuperSammies dictionary
    for j in HSammies:
      key = 'SS'
      SuperSammies.update({key:HSammies})

  context = dict( data = SuperSammies)

  #
  # render_template looks in the templates/ folder for files.
  # for example, the below file reads template/index.html
  #

  return render_template("results.html",**context)

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
