
class Alvalidator:

    message = ''

    def evaluate(self):
        if self.message is '':
            return True
        else:
            return False

    def string_validate(self, input_string):
        if input_string is 'get_validation_params':
            self.message = 'ojjj'
            return 'string'
        else:
            return input_string

