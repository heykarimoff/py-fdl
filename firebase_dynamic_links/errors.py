
class FirebaseDynamicLinksError(Exception):
    """
    Base Error for Python Firebase Dynamic Links
    """


class ApiKeyError(FirebaseDynamicLinksError):
    """
    Firebase API Key hasn't been set
    """


class FirebaseServerError(FirebaseDynamicLinksError):
    """
    Server error on Firebase server
    """
