# 00b0ddbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b0ddbc",
  "name": "_ZN20google_play_services17CallMakeAvailableEPv",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ee4322456d2cb960c5b47c2ccd997e1a1c8e90126b76ba72cefce69d4eb2623f",
  "source_text_sha256": "ee4322456d2cb960c5b47c2ccd997e1a1c8e90126b76ba72cefce69d4eb2623f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bddbf0](../00bdd/00bddbf0.md)
- [00bddf30](../00bdd/00bddf30.md)
- [00bde090](../00bde/00bde090.md)
- [00bde4f0](../00bde/00bde4f0.md)
- [00bdedb0](../00bde/00bdedb0.md)
- [00bdf040](../00bdf/00bdf040.md)

## 関連文字列（未確認候補）

~~~text
"Call to makeGooglePlayServicesAvailable failed."
~~~

## 疑似コード / UTF-8 1463 bytes

~~~c

void _ZN20google_play_services17CallMakeAvailableEPv(undefined8 *param_1)

{
  long lVar1;
  long lVar2;
  char cVar3;
  long *plVar4;
  undefined1 auStack_50 [16];
  undefined1 auStack_40 [8];
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  plVar4 = (long *)_ZN8firebase4util19GetThreadsafeJNIEnvEP7_JavaVM(*param_1);
  if (plVar4 != (long *)0x0) {
    cVar3 = _ZN7_JNIEnv23CallStaticBooleanMethodEP7_jclassP10_jmethodIDz
                      (plVar4,DAT_010a0eb8,DAT_010a0ec8,param_1[1]);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar4);
    (**(code **)(*plVar4 + 0xb0))(plVar4,param_1[1]);
    lVar2 = DAT_010a0e98;
    if (cVar3 == '\0') {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_50,DAT_010a0e98 + 0x130);
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (lVar2,auStack_50,0xffffffff,"Call to makeGooglePlayServicesAvailable failed.",
                 auStack_40);
      _ZN8firebase12FutureHandleD1Ev(auStack_50);
    }
  }
                    /* try { // try from 00b0de64 to 00c0de6b has its CatchHandler @ 00b0dfec */
  _ZdlPv(param_1);
                    /* try { // try from 00b0de6c to 00c0df63 has its CatchHandler @ 00b0d964 */
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
