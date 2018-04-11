from flask import Flask, render_template, url_for, request, redirect, flash
from database_setup import create_db_session, Restaurant, MenuItem

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def print_menu_items(restaurant_id):
    session = create_db_session()
    restaurant = session.query(Restaurant).filter_by(Id=restaurant_id).first()
    menu_items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    session.close()

    return render_template(
        'template.html',
        restaurant=restaurant,
        menu_items=menu_items)


@app.route('/restaurants/new_menu_item/<int:restaurant_id>', methods=['GET', 'POST'])
def new_menu_item(restaurant_id):

    if request.method == 'GET':
        # Return template for entering a new menu item
        return render_template('tp_new_menu_item.html', restaurant_id=restaurant_id)

    # If request is NOT GET (must be POST), take the new menu item
    # that was input by user and add to database
    session = create_db_session()
    new_item = MenuItem(name=request.form['new_item'], restaurant_id=restaurant_id)
    session.add(new_item)
    session.commit()

    # Create a flash message to indicate that a new item was added
    flash('New item created!')

    # Redirect user back to the menu page for the restaurant that
    # was just modified
    return redirect(url_for('print_menu_items', restaurant_id=restaurant_id))



@app.route('/restaurants/edit_menu_item/<int:restaurant_id>/<int:menu_id>', methods=['GET', 'POST'])
def edit_menu_item(restaurant_id, menu_id):
    if request.method == 'GET':
        session = create_db_session()
        menu_item = session.query(MenuItem).filter_by(Id=menu_id, restaurant_id=restaurant_id).one()

        # Return template for editing a menu item
        return render_template('tp_edit_menu_item.html', restaurant_id=restaurant_id, menu_id=menu_id, menu_item=menu_item)

    # If request is NOT GET (must be POST), take the edited menu item name
    # that was input by user and add to database
    session = create_db_session()
    session.query(MenuItem).filter(
        MenuItem.Id == menu_id,
        MenuItem.restaurant_id == restaurant_id).update(
        {MenuItem.name: request.form['new_item_name']},
        synchronize_session=False)
    session.commit()

    # Create a flash message to indicate that an item was edited
    flash('Item was edited!')

    # Redirect user back to the menu page for the restaurant that
    # was just modified
    return redirect(url_for('print_menu_items', restaurant_id=restaurant_id))


@app.route('/restaurants/delete_menu_item/<int:restaurant_id>/<int:menu_id>', methods=['GET', 'POST'])
def delete_menu_item(restaurant_id, menu_id):
    if request.method == 'GET':
        session = create_db_session()
        menu_item = session.query(MenuItem).filter_by(Id=menu_id).one()
        return render_template('tp_delete_menu_item.html', item=menu_item)

    session = create_db_session()
    session.query(MenuItem).filter(
        MenuItem.Id == menu_id).delete(
        synchronize_session=False)
    session.commit()

    # Create a flash message to indicate that an item was deleted
    flash('Item was deleted!')

    return redirect(url_for('print_menu_items', restaurant_id=restaurant_id))


if __name__ == '__main__':
    app.secret_key = 'test_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
