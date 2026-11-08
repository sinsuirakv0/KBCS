# 00afbd1c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afbd1c",
  "name": "_ZN8firebase8callback14RemoveCallbackEPv",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d7bc422c8e954cd7832d95a5e3ac20b449ef8a24440be41a4ee1023921744bc",
  "source_text_sha256": "5d7bc422c8e954cd7832d95a5e3ac20b449ef8a24440be41a4ee1023921744bc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00afb944](../00afb/00afb944.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bdddd0](../00bdd/00bdddd0.md)

## 疑似コード / UTF-8 1920 bytes

~~~c

void _ZN8firebase8callback14RemoveCallbackEPv(undefined8 *param_1)

{
  undefined8 uVar1;
  long lVar2;
  undefined8 uVar3;
  long *plVar4;
  
  uVar3 = DAT_010a0ce0;
                    /* try { // try from 00afbd40 to 00bfbd57 has its CatchHandler @ 00aff40c */
  _ZN8firebase5Mutex7AcquireEv(DAT_010a0ce0);
  uVar1 = DAT_010a0ce0;
  if (0 < DAT_010a0ce8) {
    _ZN8firebase5Mutex7AcquireEv(DAT_010a0ce0);
    if (DAT_010a0ce8 == 0) {
      lVar2 = _Znwm(0x68);
      *(long *)lVar2 = lVar2;
      *(long *)(lVar2 + 8) = lVar2;
      *(undefined8 *)(lVar2 + 0x10) = 0;
      _ZN8firebase5MutexC2ENS0_4ModeE(lVar2 + 0x18,1);
                    /* try { // try from 00afbd90 to 00bfbda7 has its CatchHandler @ 00aff408 */
      _ZN8firebase5MutexC2ENS0_4ModeE(lVar2 + 0x40,1);
      DAT_010a0cf0 = lVar2;
    }
    DAT_010a0ce8 = DAT_010a0ce8 + 1;
                    /* try { // try from 00afbda8 to 00bfbdd7 has its CatchHandler @ 00af560c */
    _ZN8firebase5Mutex7ReleaseEv(uVar1);
    _ZN8firebase5Mutex7ReleaseEv(uVar3);
    lVar2 = DAT_010a0cf0 + 0x18;
    _ZN8firebase5Mutex7AcquireEv(lVar2);
    uVar3 = param_1[1];
    _ZN8firebase5Mutex7AcquireEv(uVar3);
                    /* try { // try from 00afbdd8 to 00bfbdef has its CatchHandler @ 00aff3f8 */
                    /* try { // try from 00afbdf0 to 00bfbe1f has its CatchHandler @ 00af560c */
    if ((*(char *)(param_1 + 2) == '\0') && (plVar4 = (long *)*param_1, plVar4 != (long *)0x0)) {
      *param_1 = 0;
      _ZN8firebase5Mutex7ReleaseEv(uVar3);
      (**(code **)(*plVar4 + 8))(plVar4);
    }
    else {
      _ZN8firebase5Mutex7ReleaseEv(uVar3);
    }
    _ZN8firebase5Mutex7ReleaseEv(lVar2);
    uVar3 = DAT_010a0ce0;
                    /* try { // try from 00afbe20 to 00bfbe37 has its CatchHandler @ 00b0037c */
    _ZN8firebase5Mutex7AcquireEv(DAT_010a0ce0);
    FUN_00afb944(1);
  }
  _ZN8firebase5Mutex7ReleaseEv(uVar3);
  return;
}

~~~
