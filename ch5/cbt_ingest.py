import datetime

from google.cloud import bigtable


def write_simple(project_id, instance_id, table_id):
    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)
    table = instance.table(table_id)

    timestamp = datetime.datetime.utcnow()
    # Create a column family with GC policy : most recent N versions
    # Define the GC policy to retain only the most recent 2 versions
    max_versions_rule = column_family.MaxVersionsGCRule(2)
    column_family_id = "sensors_summary"
    column_families = {column_family_id: max_versions_rule}
    if not table.exists():
        table.create(column_families=column_families)

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

write_simple("chapter-5-295010","cbt-instance1","iot-table")