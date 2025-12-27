from prometheus_client import Counter

class Metrics:
    def __init__(self):
        self.request_count = Counter('inference_requests_total', 'Total inference requests')

    def increment_request_count(self):
        self.request_count.inc()
