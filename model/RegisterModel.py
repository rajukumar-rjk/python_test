import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='python_code',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

class RegisterModel:
    def insert_user(self,data):

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `users` (`name`, `email`, `username`, `password`, `confirmpassword`) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (data.name, data.email, data.username, data.password, data.confirm))

            connection.commit()
            print('data is ',sql)

        finally:
            connection.close()
