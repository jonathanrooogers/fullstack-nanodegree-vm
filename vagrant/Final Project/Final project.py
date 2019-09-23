from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}

#engine = create_engine('sqlite:///restaurantmenu.db')
#Base.metadata.bind = engine

#DBSession = sessionmaker(bind=engine)
#session = DBSession()

#show all restaurants
@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    return render_template('allrestaurants.html', restaurants = restaurants)

#create new restaurant
@app.route('/restaurant/new')
def newRestaurant():
    return render_template('newrestaurant.html')

#edit a restaurant
@app.route('/restaurant/restaurant_id/edit')
def editRestaurant():
    return render_template('editrestaurant.html')

#delete a restaurant
@app.route('/restaurant/restaurant_id/delete')
def deleteRestaurant():
    return render_template('deleterestaurant.html')

#show menu for restaurant
@app.route('/restaurant/restaurant_id')
@app.route('/restaurant/restaurant_id/menu')
def showMenu():
    return render_template('menu.html')

#add item to menu
@app.route('/restaurant/restaurant_id/menu/new')
def addItemMenu():
    return render_template('additemmenu.html')

#edit item in menu
@app.route('/restaurant/restaurants_id/menu/menu_id/edit')
def editItemMenu():
    return render_template('edititemmenu.html')

#delete a item in menu
@app.route('/restaurant/restaurant_id/menu/menu_id/delete')
def deleteItemMenu():
    return render_template('deleteitemmenu.html')


if __name__ == '__main__':
    #app.secret_key= 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)