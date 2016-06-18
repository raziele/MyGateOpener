#define PIN_RF_DATA                     12
#define PIN_LED                         13

#define SYMBOL_SIZE                     3
#define CODE_LENGTH                     52
#define PREAMBLE_LENGTH                 5

#define TX_SLOT_SIZE_US                 510 //ampiric result. theoretical is 520
#define TIME_BETWEEN_RETRANSMISSIONS_US 20000

#define RETRANSMISSIONS                 5

byte preamble[PREAMBLE_LENGTH] = {1, 1, 1, 1, 1};
byte A[SYMBOL_SIZE] = {0, 0, 1};
byte B[SYMBOL_SIZE] = {0, 1, 1};
char code[CODE_LENGTH]= {'A','A','A','A','A','B','A','A','B','A','A','B','A','A','B','B',\
                'A','B','A','B','B','B','B','B','A','B','A','A','A','A','A','A',\
                'A','B','A','A','A','A','B','A','A','A','B','B','A','B','A','A','A'};

void transmit(byte buff[], byte sz_buff, byte continuous); //only a declaration

 void setup(){
   pinMode(PIN_RF_DATA, OUTPUT);
   pinMode(PIN_LED, OUTPUT);
   //Serial.begin(9600);
 }

 void loop(){
   transmit(preamble, PREAMBLE_LENGTH, 1); //'1' is for continuous tranmission
   for(int m = 0; m < CODE_LENGTH; m++){
     if(code[m] == 'A'){      transmit(A, SYMBOL_SIZE, 0); }
     else if(code[m] == 'B'){ transmit(B, SYMBOL_SIZE, 0); }
   }
   delayMicroseconds(TIME_BETWEEN_RETRANSMISSIONS_US);
   //Serial.println(' ');
 }

void transmit(byte buff[], byte sz_buff, byte continuous = 0){
   for(byte i = 0; i < sz_buff; i++){
     if(buff[i] == 1){ //transmit for tx time slot
       digitalWrite(PIN_RF_DATA, HIGH);
       //Serial.print('1');
       delayMicroseconds(TX_SLOT_SIZE_US);
      /* if(continuous == 0){ //preamble is a continuous signal
         digitalWrite(PIN_RF_DATA, LOW);
       }*/
     }
     else{
       digitalWrite(PIN_RF_DATA, LOW);
       delayMicroseconds(TX_SLOT_SIZE_US); //if symbol is zero don't transmit, just wait tx time slot
       //Serial.print('0');
     }
   }
   digitalWrite(PIN_RF_DATA, LOW);
   return;
 }
