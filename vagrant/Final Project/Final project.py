from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#show all restaurants
@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    restaurantlist = session.query(Restaurant).all()
    return render_template('allrestaurants.html', restaurants = restaurantlist)

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
@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id).all()

    return render_template('menu.html', restaurant =restaurant, items = items )

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