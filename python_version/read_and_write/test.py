import sqlite3

def get_data():  # get personal data
    data = []
    while True:
        reg_num = input("Reg No: ")
        if (check(0, reg_num)):
            print('Reg_No already exist')
            continue
        else:
            break

    while True:
        serial_no = input("Serial No: ")
        if (check(1, serial_no)):
            print('Serial_No already exist')
            continue
        else:
            break

    while True:
        phone_no = input("Mobile Phone No: ")
        if (check(2, phone_no)):
            print('Mobile_No already exist')
            continue
        else:
            break

    while True:
        secret_code = input("Secret Code: ")
        if (check(3, secret_code)):
            print('Reg_No already exist')
            continue
        else:
            break

    data.extend([reg_num, serial_no, phone_no, secret_code])
    return data


#param : num : 0(reg_no), 1(serial_no), 2(phone_no) ,3(secret_code),4(uid_tag1),5(uid_tag2)
def check(num , item):
    flag = False
    conn = sqlite3.connect('data.db')
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM t_data')
        while True:
            row = cur.fetchone()
            if row == None:
                break
            elif row[num] == item:
                flag = True

    conn.close()
    return flag

data = get_data()
print(data)