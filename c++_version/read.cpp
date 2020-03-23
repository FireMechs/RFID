#include <unistd.h>
#include "RPi-RFID/MFRC522.h" // contains  a class

using namespace std;

int main()
{
    MFRC522 mfr; /*constructor- bcm2835_init() and spiConfig()
                  *  Boths sets up raspberry
                  *  */
    mfr.PCD_Init(); // Initializes the MFRC522 chip.
    // always look for new cards
    while(1)
    {
        if(!mfr.PICC_IsNewCardPresent()) // checks for a new card
        {
            continue;
        }
        if(!mfr.PICC_ReadCardSerial()) // this reads the card Serial
        {
            continue;
        }
        // loop through uid
        for (byte i = 0; i < mfr.uid.size; i++)
        {
            if(mfr.uid.uidByte[i] < 0x10)
            {
                printf(" 0 ");
                printf("%X",mfr.uid.uidByte[i]);
            }
            else
            {
                printf(" ");
                printf("%X",mfr.uid.uidByte[i]);
            }
        }
        printf("\n");
        usleep(1000 * 1000);
    }

    return 0;
}