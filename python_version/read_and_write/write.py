#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sqlite3
import sys

mf_inst = SimpleMFRC522()

def get_data(): # get personal data
    data = []
    while True:
        reg_num = input("Reg No: ")
        if (check(0, reg_num)):
            print('Reg_No already exist')
            continue
        else:
            break

    while True:
        serial_no  = input("Serial No: ")
        if (check(0, serial_no)):
            print('Serial_No already exist')
            continue
        else:
            break

    while True:
        phone_no = input("Mobile Phone No: ")
        if (check(0, phone_no)):
            print('Mobile_No already exist')
            continue
        else:
            break

    while True:
        secret_code = input("Secret Code: ")
        if (check(0, secret_code)):
            print('Secret Code already exist')
            continue
        else:
            break

    while True:
        uid_tag1 = read_tag(1)
        if(check(4, uid_tag1)):
            print('Tag1 already in use')
            continue
        else:
            break

    while True:
        uid_tag2 = read_tag(2)
        if (check(5, uid_tag2)):
            print('Tag2 already in use')
            continue
        else:
            break

    data.extend([reg_num,serial_no,phone_no,secret_code,uid_tag1,uid_tag2])
    return data

def write(text):
    try:
        mf_inst.write(text)
        print("Written")
    finally:
        GPIO.cleanup()

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

def read_tag(num):
    print(f'Place your card {num} to get uid...')
    val = mf_inst.read()
    return val

def insert(data):
    global con
    try:
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.executemany('INSERT INTO t_data VALUES (?,?,?,?,?,?)',data)
        con.commit()
    except sqlite3.Error as e:
        if con:
            con.rollback()
        print ("Error {}:".format(e.args[0]))
        sys.exit(1)
    finally:
        if con:
            con.close()


data = get_data()
insert(data)