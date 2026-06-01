from datetime import datetime

class APIMonitor:
    api_logs = []

    @classmethod
    def track_request(
        cls,
        endpoint: str,
        method: str,
        status_code: int,
        response_time: float
    ):

        log = {

            "endpoint": endpoint,
            "method": method,
            "status_code": status_code,
            "response_time":
                f"{response_time} ms",
            "timestamp":
                str(datetime.utcnow())
        }

        cls.api_logs.append(log)

        return {
            "message":
                "API request tracked"
        }

    
    @classmethod
    def get_api_logs(cls):

        return {
            "total_requests":
                len(cls.api_logs),
            "logs":
                cls.api_logs
        }

    
    @classmethod
    def performance_summary(cls):
        total_requests = len(
            cls.api_logs
        )

        success_requests = len([
            log for log in cls.api_logs
            if log["status_code"] < 400
        ])

        failed_requests = (
            total_requests -
            success_requests
        )

        return {
            "total_requests":
                total_requests,
            "successful_requests":
                success_requests,
            "failed_requests":
                failed_requests
        }