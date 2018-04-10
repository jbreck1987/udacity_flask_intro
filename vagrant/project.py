from flask import Flask
from database_setup import create_db_session, Restaurant, MenuItem

app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/<int:rest_id>/')
def print_restaurants(rest_id):
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


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
