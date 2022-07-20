class InputError(Exception):
    def __str__(self):
        return 'The number of pencils should be numeric'
