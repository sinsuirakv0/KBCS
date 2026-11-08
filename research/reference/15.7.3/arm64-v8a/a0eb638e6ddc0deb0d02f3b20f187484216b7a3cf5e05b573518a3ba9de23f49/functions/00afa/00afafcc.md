# 00afafcc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afafcc",
  "name": "_INIT_271",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "99ca1c56ae997c87c1621e448ad027399344cd97eee07db8c093eb81d060ba92",
  "source_text_sha256": "99ca1c56ae997c87c1621e448ad027399344cd97eee07db8c093eb81d060ba92"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdddd0](../00bdd/00bdddd0.md)

## 疑似コード / UTF-8 491 bytes

~~~c

void _INIT_271(void)

{
  undefined8 uVar1;
  
                    /* try { // try from 00afafd4 to 00bfafdb has its CatchHandler @ 00aff4d4 */
  __cxa_atexit(PTR__ZN8firebase6LoggerD2Ev_00c1b8a0,
               PTR__ZN8firebase10app_common15g_system_loggerE_00c1b908,&PTR_LOOP_00be5f80);
  uVar1 = _Znwm(0x28);
                    /* try { // try from 00afb004 to 00bfb017 has its CatchHandler @ 00aff4d0 */
  _ZN8firebase5MutexC2ENS0_4ModeE(uVar1,1);
  DAT_010a0cc0 = uVar1;
  return;
}

~~~
