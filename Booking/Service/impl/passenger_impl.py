from API.Booking.Data.Models.Models import Passenger_model as Passenger, Passenger_model


def execute(self, resp, data):
    booking_id = int(data["booking_id"])
    name = data["name"]
    age = int(data["age"])
    gender = data["gender"]



    passenger = Passenger_model(booking_id=booking_id,name=name,age=age,gender=gender,is_active=1)

    self.session.add(passenger)
    self.session.commit()
    self.session.close()
    doc = 'Passenger added'
    return doc