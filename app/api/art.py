from flask_restful import  Resource
from app import Art,db
from flask import request

class GetArt(Resource):
    def get(self):
        """
        Fetch Art
        ---        
        responses:
          200:
            description: Returns available art
            content:
              application/json:
                example: {
                  "art": [
                    {
                      "id": "art_category",
                      "name": "Art Name",
                      "description": "Sample description for sample category one",
                      "price":"Ksh 45637.00",
                      "url": "http://",
                      "category": "Sample category",
                      "created_at":"21-03-2023",
                    }
                  ]
                }
        """
        try:
            art = Art.get_available_art()            
            return {'art': art}
        except Exception as e:
            return {'message': f'Error: {str(e)}'}, 500
          
class MakeReservation(Resource):
    def post(self):
        """
        Place Request
        ---
        parameters:
          - in: body
            name: RequestOrder
            description: Create New Request
            required: true
            schema:
              type: object
              properties:
                buyer_name:
                  type: string
                  description: Reserver's name
                  example: John Doe
                  required: true
                buyer_email:
                  type: string
                  description: Reserver's Email Address
                  example: sample@mail.com
                  required: true
                buyer_phone:
                  type: string
                  description: Reserver's Phone number
                  example: +245788890989
                  required: true
                art_id:
                  type: string
                  description: Art ID
                  example: u34uish-wenii39f-34fvv34
                  required: true
                price:
                  type: float
                  description: Agreed Upon Price
                  example: 3500.00
                  required: true   
                narration:
                  type: string
                  description: More information on the reservation/sale
                  example: Delivery will be done on the seventh of the month
                  required: true               
                # Add other properties as needed

        responses:
          200:
            description: Reservation made successfully
            content:
              application/json:
                example: {"message": "Reservation Made successfully"}
        """
        try:
            art = Art.get_available_art()            
            return {'art': art}
        except Exception as e:
            return {'message': f'Error: {str(e)}'}, 500
          
class CustomOrder(Resource):
    def post(self):
        """
        Place Request
        ---
        parameters:
          - in: body
            name: RequestOrder
            description: Create New Request
            required: true
            schema:
              type: object
              properties:
                buyer_name:
                  type: string
                  description: Customer name
                  example: John Doe
                  required: true
                buyer_email:
                  type: string
                  description: Customer's Email Address
                  example: sample@mail.com
                  required: true
                buyer_phone:
                  type: string
                  description: Customer's Phone number
                  example: +245788890989
                  required: true
                photo:
                  type: file
                  description: Photo
                  required: true  
                narration:
                  type: string
                  description: More information on the order
                  example: Make the frame customisable easily
                  required: true               
                # Add other properties as needed

        responses:
          200:
            description: Order Placed successfully
            content:
              application/json:
                example: {"message": "Order Placed successfully"}
        """
        try:
            art = Art.get_available_art()            
            return {'art': art}
        except Exception as e:
            return {'message': f'Error: {str(e)}'}, 500