from flask import Flask
from database_setup import create_db_session, Restaurant, MenuItem

app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/<int:rest_id>/')
def print_menu_items(rest_id):
    session = create_db_session()

    menu_items = session.query(MenuItem).filter_by(restaurant_id = rest_id)

    session.close()

    output = ''
    for item in menu_items:
        output += '{}'.format(item.name)
        output += '</br>'
        output += '{}'.format(item.description)
        output += '</br>'
        output += '{}'.format(item.price)
        output += '</br>'
        output += '</br>'

    return output

# Task 1: Create route for newMenuItem function here

@app.route('/restaurants/new_menu_item/<int:restaurant_id>')
def new_menu_item(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"

# Task 2: Create route for editMenuItem function here
@app.route('/restaurants/edit_menu_item/<int:restaurant_id>/<int:menu_id>')
def edit_menu_item(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurants/delete_menu_item/<int:restaurant_id>/<int:menu_id>')
def delete_menu_item(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
