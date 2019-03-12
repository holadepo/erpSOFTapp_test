#!/usr/bin/env python3

import sqlite3
from jenkinsapi.jenkins import Jenkins

# Jenkins instance details
URL = "http://jenkins_host:8080"
USERNAME = ""
PASSWORD = ""

# database details
DB_NAME = "jobs.db"
JOBS_TABLE = "jobs_table"

def get_server_instance():
    """
    Get jenkins server instance
    """
    server = Jenkins(URL, username=USERNAME, password=PASSWORD)
    return server
    
if __name__ == "__main__":
    # get jenkins server instance
    server = get_server_instance()
    
    # connect to output database
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    # create sqlite database table for jobs it does not exist yet
    cur.execute("""CREATE TABLE IF NOT EXISTS {0} 
                (job_name text, status text, time text) """.format(JOBS_TABLE))
    
    # get job info
    for job in server.get_jobs():
        job_name = job['name']
        print('Job Name:'.format(job_name))
        job_status = None
        if job['color'] == 'blue':
            job_status = 'SUCCESS'
        elif job['color'] == 'grey':
            job_status = 'PENDING'
        elif job['color'] == 'red':
            job_status = 'FAILED'
        elif job['color'] == 'yellow':
            job_status = 'UNSTABLE'
        else:
            job_status = 'OTHER'
        
        # write job info into database
        cur.execute("INSERT INTO {0} VALUES ('{1}', '{2}', CURRENT_TIMESTAMP)".format(JOBS_TABLE, job_name, job_status))
        conn.commit()

    # close database
    conn.close()
    
    
