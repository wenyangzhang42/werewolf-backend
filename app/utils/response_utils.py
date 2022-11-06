from fastapi import HTTPException


def api_response(response=None, status_code=200):
    formatted_response = {
        'status_code': status_code,
        'result': response
    }
    return formatted_response


def api_exception(status_code=500, message=None, error=None):
    error_code_map = {
        400: 'BAD_REQUEST',
        401: 'UNAUTHORIZED',
        403: 'FORBIDDEN',
        404: 'NOT_FOUND',
        409: 'DATA_CONFLICT',
        500: 'TECHNICAL_EXCEPTION'
    }

    formatted_response = {
        'status_code': status_code,
        'error_code': error_code_map[status_code],
        'message': message,
        'error': error
    }

    return formatted_response

    # raise HTTPException(status_code=status_code, detail=formatted_response)