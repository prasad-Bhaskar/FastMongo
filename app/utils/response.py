from typing import Any, Optional, Dict


class APIResponse:
    """
    Central response contract for the entire application.
    Used by middleware and exception handlers.
    """

    @staticmethod
    def success(
        data: Optional[Any] = None,
        message: str = "Request successful"
    ) -> Dict[str, Any]:
        return {
            "success": True,
            "message": message,
            "data": data
        }

    @staticmethod
    def error(
        message: str,
        error_code: Optional[str] = None,
        errors: Optional[Any] = None
    ) -> Dict[str, Any]:
        response = {
            "success": False,
            "message": message
        }

        if error_code:
            response["error_code"] = error_code

        if errors:
            response["errors"] = errors

        return response
