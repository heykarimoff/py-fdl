
class FirebaseDynamicLinksError(Exception):
    """
    Base Error for Python Firebase Dynamic Links
    """


class ValidationError(FirebaseDynamicLinksError):
    """
    Validation error on input values
    """


class APIKeyError(FirebaseDynamicLinksError):
    """
    Firebase API Key hasn't been set
    """


class FirebaseServerError(FirebaseDynamicLinksError):
    """
    Server error on Firebase server
    """
