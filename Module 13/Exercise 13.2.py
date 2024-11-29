from flask import Flask, jsonify
import mysql.connector

connection = mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                database='flight_game',
                user='root',
                password='unaismetropolia',
    )

app = Flask(__name__)
@app.route('/airport/<icao>')
def airport(icao):
    cursor = connection.cursor()
    sql = "SELECT name,municipality FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    response = {
        "ICAO" : icao,
        "Name" : result[0],
        "Location" : result[1],
    }
    return jsonify(response)
if __name__ == '__main__':
    app.run(port=5000)