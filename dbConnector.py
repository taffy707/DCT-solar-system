import mysql.connector
# from Crypto.Cipher import DES3
# from Crypto.Util.Padding import pad, unpad

# def encrypt(data, key):
  #  cipher = DES3.new(key, DES3.MODE_ECB)
   # padded_data = pad(data.encode(), DES3.block_size)
   # encrypted_data = cipher.encrypt(padded_data)
   # return 

def connect_to_database(host, user, password, database):
    try:
        SolarDB = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Joshh2003&",
            database="solar"
        )
        mycursor = SolarDB.cursor()
        return SolarDB, mycursor
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        print(err.errno)
        print(err.msg)
        return None, None

def fetch_data(cursor):
    try:
        cursor.execute("SELECT * FROM customer")
        cursor.execute("SELECT * FROM user")
        myresult = cursor.fetchall()
        return myresult
    except mysql.connector.Error as err:
        print(f"Error fetching data: {err}")
        print(err.errno)
        print(err.msg)
        return None

def main():
    SolarDB, mycursor = connect_to_database("127.0.0.1", "root", "Joshh2003&", "solar")
    if SolarDB and mycursor:
        myresult = fetch_data(mycursor)
        if myresult:
            for x in myresult:
                print(x)
            else:
                print("No results found")
            SolarDB.close()
    
    # Running Main Func
    if __name__ == "__main__":
        main()
