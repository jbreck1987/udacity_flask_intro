from flask import Flask, render_template
from database_setup import create_db_session, Restaurant, MenuItem

app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/<int:rest_id>/')
def print_menu_items(rest_id):
    session = create_db_session()

    restaurant = session.query(Restaurant.name).filter_by(Id=rest_id).first()
    menu_items = session.query(MenuItem).filter_by(restaurant_id=rest_id)

    session.close()

    return render_template('template.html', restaurant=restaurant, menu_items=menu_items)


@app.route('/restaurants/new_menu_item/<int:restaurant_id>')
def new_menu_item(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"

@app.route('/restaurants/edit_menu_item/<int:restaurant_id>/<int:menu_id>')
def edit_menu_item(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"


@app.route('/restaurants/delete_menu_item/<int:restaurant_id>/<int:menu_id>')
def delete_menu_item(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
