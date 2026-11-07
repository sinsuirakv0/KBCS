# 00b6ebcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00b6ecd8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ecd8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00b6ebcc",
  "name": "_ZNK8firebase4auth4User11provider_idEv",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0c0e1e46b81714489e898a346c0ec408146364f5ea4108f20b008e23c84005d2",
  "source_text_sha256": "0c0e1e46b81714489e898a346c0ec408146364f5ea4108f20b008e23c84005d2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bddfe0](../00bdd/00bddfe0.md)
- [00bde100](../00bde/00bde100.md)
- [00bde410](../00bde/00bde410.md)
- [00bde640](../00bde/00bde640.md)

## 疑似コード / UTF-8 990 bytes

~~~c

void _ZNK8firebase4auth4User11provider_idEv(undefined8 *param_1,long param_2)

{
  undefined8 uVar1;
  ulong uVar2;
  undefined8 *puVar3;
  long lVar4;
  
  puVar3 = *(undefined8 **)(param_2 + 0x98);
  if ((puVar3 == (undefined8 *)0x0) || (lVar4 = puVar3[0x40], lVar4 == 0)) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
              (param_1,&DAT_002967d9);
    return;
  }
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*puVar3);
                    /* try { // try from 00b6ebf8 to 00c6ec0f has its CatchHandler @ 00b70724 */
  lVar4 = FUN_0047495c(uVar1,lVar4,DAT_010a19c0);
                    /* try { // try from 00b6ec10 to 00c6ecbb has its CatchHandler @ 00b6e3fc */
  uVar2 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
  if ((lVar4 != 0) && ((uVar2 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar1,lVar4);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  return;
}

~~~
