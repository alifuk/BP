import numpy as np


class Alvalidator:


    def __init__(self, params):
        print('ooobj')
        self.filters_description = []
        self.invalid_fields = []

        # If test data are in params, make note that we need to return informations about validators
        if len(params) > 0 and params[0] == 'get_validation_params':
            self.getting_description = True
        else:
            self.getting_description = False

    def evaluate(self):
        if self.getting_description is True:
            return False
        elif len(self.invalid_fields) is not 0:
            self.filters_description = np.zeros((10, 10, 3), np.uint8)
            return False
        else:
            return True

    def string_validate(self, input_string, description):
        if input_string is 'get_validation_params':
            string_description = {
                'type': 'select',
                'label': description,
            }
            self.filters_description.append(string_description)
            return 'test_string'
        else:
            return input_string

    def range_validate(self, input_value, description, options_list):
        if input_value is 'get_validation_params':
            range_description = {
                'type': 'select',
                'label': description,
                'options_list': options_list
            }
            self.filters_description.append(range_description)
            return 'test_list'
        else:
            if input_value in options_list:
                return input_value
            else:
                self.invalid_fields.append(description)
                return ''
