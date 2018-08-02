import ibm_db
conn = ibm_db.connect("DATABASE=sample;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=db2inst1;", "", "")
sql = "SELECT * FROM STAFF"
stmt = ibm_db.exec_immediate(conn, sql)
#result = ibm_db.fetch_both(stmt)
result = ibm_db.fetch_assoc(stmt)
while result:
    print(result)
    result = ibm_db.fetch_assoc(stmt)
