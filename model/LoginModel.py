import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='python_code',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
class LoginModel:
    def check_user(self, data):

        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `username` FROM `users` WHERE `username`=%s"
                cursor.execute(sql, (data.username))
                user = cursor.fetchone()
                print(user)

            if user:
                if (user, data.password):
                    return user
                else:
                    return False
            else:
                return False

        except:
            connection.close()