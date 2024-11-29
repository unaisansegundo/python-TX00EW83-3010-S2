from flask import Flask, jsonify

app = Flask(__name__)

def Prime(n):
    if n < 0:
        return False
    i = 2
    while (i<n): 
        if (n % i) == 0:
            return False
        i += 1
    return True

@app.route('/prime_number/<int:number>')
def check_prime(number):
    result = {
        "Number": number,
        "Prime": Prime(number)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)
