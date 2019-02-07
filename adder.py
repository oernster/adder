from flask import Flask, request, jsonify, abort

app = Flask(__name__)


@app.route('/total', methods=['GET'])
def total():
    """Calc total and return as json response if GET.
        Assumed hardcoded data; better alternative could
        be passed in as POST data via json or back end
        retrieval"""
    if request.method == 'GET':
        numbers_to_add = list(range(10000001))
        output = {
            "total": numbers_to_add,
        }
        return jsonify(output)
    else:
        return abort(404)


if __name__ == '__main__':
    app.run()
