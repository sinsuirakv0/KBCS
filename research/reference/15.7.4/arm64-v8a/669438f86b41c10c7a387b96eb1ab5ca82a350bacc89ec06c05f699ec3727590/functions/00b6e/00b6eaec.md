# 00b6eaec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00b6e9e0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e9e0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00b6eaec",
  "name": "_ZNK8firebase4auth4User12display_nameEv",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e50e39f7eeafc07b476f1c07f16fb0bb3cd7e4aa490b4918c9af80fc356f3e81",
  "source_text_sha256": "e50e39f7eeafc07b476f1c07f16fb0bb3cd7e4aa490b4918c9af80fc356f3e81"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bde0e0](../00bde/00bde0e0.md)
- [00bde200](../00bde/00bde200.md)
- [00bde510](../00bde/00bde510.md)
- [00bde740](../00bde/00bde740.md)

## 疑似コード / UTF-8 991 bytes

~~~c

void _ZNK8firebase4auth4User12display_nameEv(undefined8 *param_1,long param_2)

{
  undefined8 uVar1;
  ulong uVar2;
  undefined8 *puVar3;
  long lVar4;
  
  puVar3 = *(undefined8 **)(param_2 + 0x98);
  if ((puVar3 == (undefined8 *)0x0) || (lVar4 = puVar3[0x40], lVar4 == 0)) {
                    /* try { // try from 00b6eb70 to 00c6eb87 has its CatchHandler @ 00b7076c */
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
              (param_1,&DAT_002967d9);
    return;
  }
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*puVar3);
  lVar4 = FUN_0047495c(uVar1,lVar4,DAT_010a1ac8);
  uVar2 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
  if ((lVar4 != 0) && ((uVar2 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar1,lVar4);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
                    /* try { // try from 00b6eb88 to 00c6ec3b has its CatchHandler @ 00b6e440 */
  return;
}

~~~
