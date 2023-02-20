# adding EIS.csv data into postgre database
import psycopg2
from urllib.parse import urlparse
import csv

conStr = "localhost://postgres:Valentina@eis:5432"
p = urlparse(conStr)

pg_connection_dict = {
    'dbname': p.hostname,
    'user': p.username,
    'password': p.password,
    'port': p.port,
    'host': p.scheme
}

conn = psycopg2.connect(**pg_connection_dict)
cur = conn.cursor()

# Create the table
cur.execute("""
    CREATE TABLE eis_data (
        id SERIAL PRIMARY KEY,
        time_stamp TIMESTAMP,
        step NUMERIC,
        status TEXT,
        prog_time INTERVAL,
        step_time INTERVAL,
        cycle NUMERIC,
        cycle_level NUMERIC,
        procedure TEXT,
        voltage NUMERIC,
        current NUMERIC,
        ah_accu NUMERIC,
        energy TEXT,
        start_freq NUMERIC,
        end_freq NUMERIC,
        set_freq NUMERIC,
        aac_max NUMERIC,
        vac_min NUMERIC,
        vac_max NUMERIC,
        mv_ideal NUMERIC,
        go NUMERIC,
        status_1 NUMERIC,
        u1 NUMERIC,
        zreal1 NUMERIC,
        zimg1 NUMERIC,
        act_freq NUMERIC,
        eis_error NUMERIC,
        aac_start NUMERIC,
        min_interval_time NUMERIC,
        count_of_periods NUMERIC,
        u_ideal NUMERIC,
        a_start NUMERIC,
        min_duration NUMERIC,
        min_periods NUMERIC,
        rem_time NUMERIC,
        v_relativ NUMERIC,
        a_amplitude NUMERIC,
        betrag NUMERIC,
        phase NUMERIC,
        chamber_t NUMERIC,
        chamber_sp NUMERIC,
        temp45 NUMERIC
    );
""")

# Read the data from the CSV file and insert it into the table
with open('EIS.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        cur.execute("""
            INSERT INTO eis_data (
                id,
                time_stamp,
                step,
                status,
                prog_time,
                step_time,
                cycle,
                cycle_level,
                procedure,
                voltage,
                current,
                ah_accu,
                energy,
                start_freq,
                end_freq,
                set_freq,
                aac_max,
                vac_min,
                vac_max,
                mv_ideal,
                go,
                status_1,
                u1,
                zreal1,
                zimg1,
                act_freq,
                eis_error,
                aac_start,
                min_interval_time,
                count_of_periods,
                u_ideal,
                a_start,
                min_duration,
                min_periods,
                rem_time,
                v_relativ,
                a_amplitude,
                betrag,
                phase,
                chamber_t,
                chamber_sp,
                temp45
                
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, row)

# Commit the changes and close the connection
conn.commit()
cur.close()