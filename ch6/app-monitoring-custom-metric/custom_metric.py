import os
import time
import uuid
import threading

from google.api import metric_pb2 as ga_metric
from google.cloud import monitoring_v3

PROJECT_ID = os.environ["PROJECT_ID"]
#UNIQUE_ID = str(uuid.uuid4())
CUSTOM_METRIC_NAME_PREFIX = "pets_requests_"
CUSTOM_METRIC_DISPLAY_NAME = "PETS_REQUESTS"

def create_metric_descriptor(project_id):
    try:
        client = monitoring_v3.MetricServiceClient()
        #list_metric_descriptors(project_id)
        project_name = f"projects/{project_id}"
        descriptor = ga_metric.MetricDescriptor()
        descriptor.type = "custom.googleapis.com/" + CUSTOM_METRIC_NAME_PREFIX + PROJECT_ID
        descriptor.display_name = CUSTOM_METRIC_DISPLAY_NAME
        descriptor.metric_kind = ga_metric.MetricDescriptor.MetricKind.GAUGE
        descriptor.value_type = ga_metric.MetricDescriptor.ValueType.INT64
        descriptor.unit = "1"
        descriptor.description = "This measures the amount of pets requested so far."
        descriptor = client.create_metric_descriptor(
            name=project_name, metric_descriptor=descriptor
        )
        print("Created", descriptor.type)
    except Exception as e:
        print(e)
    
def list_metric_descriptors(project_id):
    # [START monitoring_list_descriptors]
    client = monitoring_v3.MetricServiceClient()
    project_name = f"projects/{project_id}"
    for descriptor in client.list_metric_descriptors(name=project_name):
        if "custom" in str(descriptor.type):
            print(descriptor.type)
            client.delete_metric_descriptor(name=descriptor.name)
    # [END monitoring_list_descriptors]

def write_time_series(project_id,requested_pets):
    client = monitoring_v3.MetricServiceClient()
    project_name = f"projects/{project_id}"

    series = monitoring_v3.TimeSeries()
    series.metric.type = "custom.googleapis.com/" + CUSTOM_METRIC_NAME_PREFIX + PROJECT_ID
    series.resource.type = "gae_instance"
    series.resource.labels["instance_id"] = os.environ["GAE_INSTANCE"]
    series.resource.labels["location"] = "us-east1"
    series.resource.labels["module_id"] = os.environ["GAE_APPLICATION"]
    series.resource.labels["version_id"] = os.environ["GAE_VERSION"]
    
    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10 ** 9)
    interval = monitoring_v3.TimeInterval(
        {"end_time": {"seconds": seconds, "nanos": nanos}}
    )
    point = monitoring_v3.Point({"interval": interval, "value": {"int64_value": requested_pets}})
    series.points = [point]
    client.create_time_series(name=project_name, time_series=[series])



class MetricsWriter(threading.Thread):

    def __init__(self, value):
        threading.Thread.__init__(self)
        self.time_series_writer = write_time_series
        self.daemon = True
        self.value = value
        self.project_id = PROJECT_ID
        

    def run(self):
        while True:
            try:
                if self.value != 0:
                    self.time_series_writer(self.project_id, self.value)
                    print("Wrote current value:", self.value)
                time.sleep(10)
            except Exception as e:
                print("Unable to update metric", e)
                pass
        
    def update_value(self, val):
        self.value = val

