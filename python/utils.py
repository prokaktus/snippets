def getenv(var, default=None):
    """
    Extract configs from .env
    """
    var = os.getenv(var)
    if var is None:
        return default
    if var:
        var_lower = var.lower()
        if var_lower == 'false':
            return False
        if var_lower == 'true':
            return True
    return var
