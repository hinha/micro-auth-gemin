from secure import SecureHeaders

secure_headers = SecureHeaders()

def setup_middleware(app):
    @app.middleware('response')
    async def set_secure_headers(request, response):
        secure_headers.sanic(response)
        response.headers["Server"] = "Linoed"
        response.headers["x-xss-protection"] = "1; mode=block"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "Deny"
        response.headers["Access-Control-Allow-Headers"] = "X-Real-IP"
        response.headers["Content-Type"] = "application/json"