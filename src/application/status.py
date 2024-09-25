from src.response import ResponseTypes

STATUS_CODES = {
    ResponseTypes.SUCCESS: 200,
    ResponseTypes.CREATE: 201,
    ResponseTypes.DELETE: 204,
    ResponseTypes.RESOURCE_ERROR: 404,
    ResponseTypes.NOT_FOUND_ERROR: 404,
    ResponseTypes.PARAMETERS_ERROR: 400,
    ResponseTypes.SYSTEM_ERROR: 500,
}
