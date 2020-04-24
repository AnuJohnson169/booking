from API.app import app
from API.Booking.Service.Passenger.Passenger import Passenger

app.add_route("/api/passenger", Passenger())


