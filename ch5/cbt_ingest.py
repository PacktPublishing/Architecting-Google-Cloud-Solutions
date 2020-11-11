import datetime

from google.cloud import bigtable


def write_simple(project_id, instance_id, table_id):
    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)
    table = instance.table(table_id)

    timestamp = datetime.datetime.utcnow()
    column_family_id = "sensors_summary"

    row_key = "iotdevice#10401"

    row = table.direct_row(row_key)
    row.set_cell(column_family_id,
                 "temperature",
                 100,
                 timestamp)
    row.set_cell(column_family_id,
                 "humidity",
                 82,
                 timestamp)
    row.set_cell(column_family_id,
                 "location",
                 "warehouse1",
                 timestamp)

    row.commit()

    print('Successfully wrote row {}.'.format(row_key))

write_simple("PROJECT_ID","cbt-instance1","iot-table")