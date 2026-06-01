from datetime import datetime

class ActivityLogger:
    logs = []

    @classmethod
    def log_activity(
        cls,
        username: str,
        activity: str
    ):

        log = {
            "username": username,
            "activity": activity,
            "timestamp":
                str(datetime.utcnow())
        }
        cls.logs.append(log)
        return {
            "message":
                "Activity logged successfully"
        }
    
    @classmethod
    def get_logs(cls):
        return {
            "total_logs":
                len(cls.logs),
            "logs":
                cls.logs
        }

    @classmethod
    def clear_logs(cls):
        cls.logs.clear()
        return {
            "message":
                "Logs cleared successfully"
        }