#!/usr/bin/python

from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from model.logic_gate_model_deployment import Logic

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins
logic = Logic()

api = Api(
    app, 
    version='1.0', 
    title='Logic Gates Predictor',
    description='Logic Gates Predictor')

ns = api.namespace('logic')
   
parser = api.parser()

parser.add_argument(
    'a', 
    type=int, 
    required=True, 
    help='a operand', 
    location='args')

parser.add_argument(
    'b', 
    type=int, 
    required=True, 
    help='b operand', 
    location='args')

parser.add_argument(
    'gate', 
    type=str, 
    required=True, 
    help='operator: or, and, nor, nand, xor', 
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.Integer,
})

@ns.route('/gates')
class LogicGategApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()

        return {
         "result": logic.logic_gate(args['a'], args['b'], args['gate'])
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
