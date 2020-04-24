import falcon
import json
from sqlalchemy.orm import sessionmaker
from API.Booking.Data.source import SqlDB
from API.Booking.Service.impl.passenger_impl import execute


class Passenger(object):

    def __init__(self):
        Session = sessionmaker(bind=SqlDB().engine)
        self.session = Session()

    def on_post(self, req, resp):
        """Handles POST requests"""
        try:
            # add methods

            data = req.media
            doc = execute(self, resp, data)
            resp.body = json.dumps(doc)
            resp.status = falcon.HTTP_OK


        except Exception as ex:

            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

