from flask import Flask
from database_setup import create_db_session, Restaurant, MenuItem

app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/')
def print_restaurants():
    session = create_db_session()

    restaurant = session.query(Restaurant).first()
    menu_items = session.query(MenuItem).filter_by(restaurant_id = restaurant.Id)

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


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
