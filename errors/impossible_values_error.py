class ImpossibleValuesError(Exception):
    def __str__(self):
        return "Possible values: '1', '2' or '3'"
