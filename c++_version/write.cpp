#include <iostream>
#include <string>
#include <sstream>
#include "MFRC522.h"

std::string get_details()
{
    std::string reg_no, serial_no, phone_no;
    std::cout << "Enter REG NO: ";
    std::getline(std::cin, reg_no);
    std::cout << "Enter serial_no: ";
    std::getline(std::cin, serial_no);
    std::cout << "Enter phone_no: ";
    std::getline(std::cin , phone_no);
    // concatenate all the strings
    std::stringstream ss;
    ss << reg_no << '\n' << serial_no << '\n' << phone_no;
    return ss.str();
}
int main() {
    MFRC522 mfrc;
    mfrc.PCD_Init();// initialize   the PCD
    unsigned char status;
    while (true) {
        // Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle.
        if (!mfrc.PICC_IsNewCardPresent()) {
            continue;
        }

        // Select one of the cards
        if (!mfrc.PICC_ReadCardSerial()) {
            continue;
        }

        byte blockaddr = 1;
        // request for the data  to write
        std::string data = get_details();
        char const *w_data = data.c_str();
        status = (MFRC522::StatusCode) mfrc.MIFARE_Write(blockaddr, (byte *) w_data, sizeof(w_data));
        if (status != MFRC522::STATUS_OK) {
            std::cerr << "Writing Data failed: " << '\n';
            std::cout << mfrc.GetStatusCodeName(status) << '\n';
        }
    }
  return 0;
}
