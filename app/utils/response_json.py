

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
JSON_200_1 = {
    "success": [
        {"message": "Successfully logged in", 'secret_key': '', "code": 11001}],
        "meta": {"http_status": 200}
}

JSON_409_2 = {
    "errors": [
        {"message": "An account already exists with this email", "code": 12002}],
        "meta": {"http_status": 409}
}
JSON_409_3 = {"errors": [{"message": "Email or Password is incorrect", "code": 12003}],"meta": {"http_status": 409}}