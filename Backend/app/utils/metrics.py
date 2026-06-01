import psutil

class Metrics:

    @staticmethod
    def system_metrics():

        return {
            "cpu_usage":
                f"{psutil.cpu_percent()}%",
            "memory_usage":
                f"{psutil.virtual_memory().percent}%",
            "disk_usage":
                f"{psutil.disk_usage('/').percent}%"
        }

    @staticmethod
    def forecast_metrics(
        total_forecasts,
        accuracy
    ):

        return {
            "total_forecasts":
                total_forecasts,
            "forecast_accuracy":
                f"{accuracy}%"
        }