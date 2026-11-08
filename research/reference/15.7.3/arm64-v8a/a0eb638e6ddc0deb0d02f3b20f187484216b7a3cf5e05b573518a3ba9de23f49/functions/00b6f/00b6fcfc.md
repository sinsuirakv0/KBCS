# 00b6fcfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b6fcfc",
  "name": "_ZNK8firebase4auth22AndroidWrappedUserInfo12phone_numberEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2e35f66cef5980b1d926de96e00258c3ba01185b9ec12908f6ec5de78b48e504",
  "source_text_sha256": "2e35f66cef5980b1d926de96e00258c3ba01185b9ec12908f6ec5de78b48e504"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bde090](../00bde/00bde090.md)
- [00bde1b0](../00bde/00bde1b0.md)
- [00bde4c0](../00bde/00bde4c0.md)

## 疑似コード / UTF-8 749 bytes

~~~c

void _ZNK8firebase4auth22AndroidWrappedUserInfo12phone_numberEv(undefined8 *param_1,long param_2)

{
  long lVar1;
  undefined8 uVar2;
  long lVar3;
  ulong uVar4;
  
  lVar1 = *(long *)(param_2 + 0xa0);
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
  lVar3 = 0;
  if (lVar1 != 0) {
    lVar3 = FUN_0047495c(uVar2,lVar1,DAT_010a1a90);
  }
  uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar2);
  if ((lVar3 != 0) && ((uVar4 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar2,lVar3);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
                    /* try { // try from 00b6fd74 to 00c6fd7b has its CatchHandler @ 00b706dc */
  return;
}

~~~
