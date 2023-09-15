from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex

class CarFactory:
    def create_calliope(
            current_date,
            last_service_date,
            current_mileage,
            last_service_mileage):
        return Calliope(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_glissade(
            current_date,
            last_service_date,
            current_mileage,
            last_service_mileage):
        return Glissade(current_date, last_service_date, current_mileage, last_service_mileage)
    def create_palindrome(
            current_date,
            last_service_date,
            current_mileage,
            last_service_mileage):
        return Palindrome(current_date, last_service_date, current_mileage, last_service_mileage)
    def create_rorschach(
            current_date,
            last_service_date,
            current_mileage,
            last_service_mileage):
        return Rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
    def create_thovex(
            current_date,
            last_service_date,
            current_mileage,
            last_service_mileage):
        return Thovex(current_date, last_service_date, current_mileage, last_service_mileage)
