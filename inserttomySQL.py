import mysql.connector

def convertToBinary(filename):
    #Convert digitial data to binary format
    with open(filename, 'rb') as file:
        binaryData - file.read()
    return binaryData

def insertBLOB(emp_id, name, photo, biodatafile):
    print('inserting BLOB into py_emp table')
    try:
        connection = mysql.connector.connect(host = 'localhost',
                database = 'py_db',
                user='jerin',
                password='jerin123')
        cursor = connection.cursor()
        sql_ins_qry = """INSERT INTO py_emp
        (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""
        empPic = convertToBinary(photo)
        file = convertToBonary(biodatafile)

        #Convert to tuple
        insert_blob_tuple = (emp_id, name, empPic, file)
        result = cursor.execute(sql_ins_qry, insert_blob_tuple)
        connection.commit()
        print('BLOB inserted')
    except mysql.connector.Error as error:
        print('Failed inserting BLOB {}'.format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Mysql connection is closed")

if __name__=='__main__':
    insertBLOB(1, "Eric", '/home/skycam/basics/mysql_basics/MySQL_BLOB/indata/IMG-20190814-WA0003.jpg', '/home/skycam/basics/mysql_basics/MySQL_BLOB/indata/bio1.txt')

    
