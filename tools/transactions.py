class IPayment:
    """ Payment interface. """

    def __init__():
        """ Not implemented method. """
        pass

    def __send_request(self, payload: IPayload) -> None:
        """ Not implemented method. """
        pass

    def send_payment(self, payload: IPayload) -> dict:
        """ Not implemented method. """
        pass


class IPayload:
    """ Payload interface. """

    def __init__(self):
        """ Not implemented method. """
        pass

    def status(self) -> None:
        """ Not implemented method. """


class RESTPayload(IPayload):
    """ Set data in object and use object in REST Payments. """

    def __init__(self, data_to_send: dict):
        self.request  = data_to_send
        self.response = None

    def status(self) -> int:
        response = self.response
        if response:
            return response['status']


class PaymentMobbex(IPayment):
    """ Payment using Mobbex service. """

    def __init__(self, payload: RESTPayload):
        self.__payload  = payload
        self.__response = self.__payload.response

    def __send_request(self, payload: RESTPayload) -> None:
        """ Send payload using Requests and set response on Payload. """

        result = {
            'status': 200,
            'message': 'Mock',
            'sended': self.__payload
        }

        self.__payload.response = result

    def send_payment(self) -> dict:
        """ Receive payload and return Payload with response data. """
        self.__send_request(self.__payload)
        return self.__response


# EXAMPLE
# data = {...}
# payload = RESTPayload(data)
# payload = RESTPayload(payload=payload)
# result = payment.send_payment()
# if result.status == 200

