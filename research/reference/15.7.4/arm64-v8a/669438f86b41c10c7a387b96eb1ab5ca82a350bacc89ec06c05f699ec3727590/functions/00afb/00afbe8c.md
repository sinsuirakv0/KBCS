# 00afbe8c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00afbe8c",
  "name": "_ZN8firebase8callback13PollCallbacksEv",
  "size": 236,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "126834f70ad2beb0e719f92696bed8f1156f2c52f96a1d0d100e08608d071623",
  "source_text_sha256": "126834f70ad2beb0e719f92696bed8f1156f2c52f96a1d0d100e08608d071623"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00afb988](../00afb/00afb988.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb7d0](../00bdb/00bdb7d0.md)
- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)
- [00bdde20](../00bdd/00bdde20.md)
- [00bdec70](../00bde/00bdec70.md)

## 疑似コード / UTF-8 1350 bytes

~~~c

void _ZN8firebase8callback13PollCallbacksEv(void)

{
  undefined8 uVar1;
  undefined8 uVar2;
  int iVar3;
  long lVar4;
  
  uVar1 = DAT_010a0d20;
  _ZN8firebase5Mutex7AcquireEv(DAT_010a0d20);
  uVar2 = DAT_010a0d20;
  if (0 < DAT_010a0d28) {
    _ZN8firebase5Mutex7AcquireEv(DAT_010a0d20);
                    /* try { // try from 00afbecc to 00bfbed7 has its CatchHandler @ 00b00490 */
    if (DAT_010a0d28 == 0) {
                    /* try { // try from 00afbedc to 00bfbee7 has its CatchHandler @ 00b00488 */
      lVar4 = _Znwm(0x68);
      *(long *)lVar4 = lVar4;
      *(long *)(lVar4 + 8) = lVar4;
                    /* try { // try from 00afbee8 to 00bfbef7 has its CatchHandler @ 00b00484 */
      *(undefined8 *)(lVar4 + 0x10) = 0;
      _ZN8firebase5MutexC2ENS0_4ModeE(lVar4 + 0x18,1);
                    /* try { // try from 00afbef8 to 00bfbf0b has its CatchHandler @ 00b0048c */
      _ZN8firebase5MutexC2ENS0_4ModeE(lVar4 + 0x40,1);
      DAT_010a0d30 = lVar4;
    }
    DAT_010a0d28 = DAT_010a0d28 + 1;
    _ZN8firebase5Mutex7ReleaseEv(uVar2);
    _ZN8firebase5Mutex7ReleaseEv(uVar1);
    DAT_010a0d40 = pthread_self();
    DAT_010a0d38 = 1;
    iVar3 = _ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv(DAT_010a0d30);
    FUN_00afb988(iVar3 + 1);
    return;
  }
  _ZN8firebase5Mutex7ReleaseEv(uVar1);
  return;
}

~~~
