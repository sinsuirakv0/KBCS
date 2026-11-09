# 00bdefac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bdefac",
  "name": "_ZNK8firebase4auth22AndroidWrappedUserInfo3uidEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ce09066525025cec485d27dd2da9dfc8a3ff2f0aaea386735eac552552976bc",
  "source_text_sha256": "0ce09066525025cec485d27dd2da9dfc8a3ff2f0aaea386735eac552552976bc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004977f4](../00497/004977f4.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5af90](../00c5a/00c5af90.md)

## 疑似コード / UTF-8 991 bytes

~~~c

void _ZNK8firebase4auth22AndroidWrappedUserInfo3uidEv(undefined8 *param_1,long param_2)

{
  long lVar1;
  undefined8 uVar2;
  long lVar3;
  ulong uVar4;
  
  lVar1 = *(long *)(param_2 + 0xa0);
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
  lVar3 = 0;
  if (lVar1 != 0) {
    lVar3 = FUN_004977f4(uVar2,lVar1,DAT_011269c0);
  }
  uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar2);
  if ((lVar3 != 0) && ((uVar4 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar2,lVar3);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
                    /* try { // try from 00bdf01c to 00cdf0ab has its CatchHandler @ 00bdf01c
                       catch() { ... } // from try @ 00bdf01c with catch @ 00bdf01c
                       catch() { ... } // from try @ 00bdfeb0 with catch @ 00bdf01c
                       catch() { ... } // from try @ 00be0198 with catch @ 00bdf01c */
  param_1[2] = 0;
  return;
}

~~~
