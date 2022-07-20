class NumberError(Exception):
    def __str__(self):
        return 'Too many pencils were taken'
