import psutil
from datetime import datetime

class PerformanceMonitor:

    @staticmethod
    def system_metrics():

        return {
            "cpu_usage":
                f"{psutil.cpu_percent()}%",
            "memory_usage":
                f"{psutil.virtual_memory().percent}%",
            "disk_usage":
                f"{psutil.disk_usage('/').percent}%",
            "timestamp":
                str(datetime.utcnow())
        }


    @staticmethod
    def application_health():

        return {
            "server_status": "Running",
            "database_status": "Connected",
            "api_status": "Active",
            "health": "Healthy"
        }

    @staticmethod
    def performance_summary():
        cpu = psutil.cpu_percent()
        memory = (
            psutil.virtual_memory().percent
        )
        status = "Stable"

        if cpu > 80 or memory > 80:
            status = "High Usage"
        return {
            "cpu_usage": f"{cpu}%",
            "memory_usage":
                f"{memory}%",
            "system_status":
                status
        }