from flask import Flask, render_template, request, jsonify

from etl_api_assignment.db_models import location

app = Flask(__name__)


@app.route('/api/location/<int:id>', methods=['GET'])
def get_location_by_id(id=None):
    """API to fetch location data"""
    error_message = {"error_message": ""}
    error_flag = False
    if request.method == 'GET':

        if not id :
            error_message[
                'error_message'] = 'id needs to be passed in url as `/api/location/id`'
            error_flag = True

        if error_flag:
            return jsonify(error_message)

        results = location.get_loc(id=id)


        return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # for running on local machine
