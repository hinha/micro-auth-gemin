

JSON_422_1 = {
    "errors": [
        {"message": "Invalid parameters: Your request form parameters are incorrect.", "code": 13011}
    ],
    "meta": {"http_status": 422}
}


JSON_200_2 = {
    "success": [
        {"message": "register successfully, please login", "code": 11002}],
        "meta": {"http_status": 200}
}
JSON_409_2 = {
    "errors": [
        {"message": "An account already exists with this email", "code": 12002}],
        "meta": {"http_status": 409}
}