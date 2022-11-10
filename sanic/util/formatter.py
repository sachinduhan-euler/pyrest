def http_formatter(body, message = "ok", success = True):
    return {
        "body": body,
        "message": message,
        "success": success
    }