from fastapi import HTTPException, status


wrong_login_password_ex = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid login or password.",
    headers={"WWW-Authenticate": "Basic"}
)
