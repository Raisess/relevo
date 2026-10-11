# Constant for the access token header name
ACCESS_TOKEN_HEADER = "x-access-token"
# Constant for the access token header value
ACCESS_TOKEN_VALUE = "secret"

def validate_access_token(headers: dict):
  """Validate that the x-access-token header is present and valid.

  Raises ValueError if the header is missing or invalid.
  """
  token = headers.get(ACCESS_TOKEN_HEADER)
  if not token:
    raise ValueError(f"Missing {ACCESS_TOKEN_HEADER} header")

  if token != ACCESS_TOKEN_VALUE:
    raise ValueError("Invalid token")
