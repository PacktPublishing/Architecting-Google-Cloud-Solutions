from google.cloud import bigtable
import google.cloud.bigtable.row_filters as row_filters
from google.cloud.bigtable.row_set import RowSet

def read_row(project_id, instance_id, table_id, row_key):
    print("read_row() ****************************")
    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)
    table = instance.table(table_id)

    row_key = b"iotdevice#10401"
    row = table.read_row(row_key)
    print(row)
    print_row(row)


def print_row(row):
    print("Reading data for {}:".format(row.row_key.decode('utf-8')))
    for cf, cols in sorted(row.cells.items()):
        print("Column Family {}".format(cf))
        for col, cells in sorted(cols.items()):
            for cell in cells:
                labels = " [{}]".format(",".join(cell.labels)) \
                    if len(cell.labels) else ""
                print(
                    "\t{}: {} @{}{}".format(col.decode('utf-8'),
                                            cell.value.decode('utf-8'),
                                            cell.timestamp, labels))
    print("")


read_row("chapter-5-295010","cbt-instance1","iot-table", "iotdevice#10401")