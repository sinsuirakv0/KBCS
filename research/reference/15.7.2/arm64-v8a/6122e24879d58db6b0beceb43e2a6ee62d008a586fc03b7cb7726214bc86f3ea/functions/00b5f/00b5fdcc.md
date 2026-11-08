# 00b5fdcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00b5fdcc",
  "name": "_ZN8firebase4auth4Auth11UseEmulatorENSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEj",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d5a9317eb64ea714d1a31bd7ce6cf90ea3be025884cf750519cf8c635d8cfe90",
  "source_text_sha256": "d5a9317eb64ea714d1a31bd7ce6cf90ea3be025884cf750519cf8c635d8cfe90"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bddfe0](../00bdd/00bddfe0.md)
- [00bde100](../00bde/00bde100.md)

## 疑似コード / UTF-8 1635 bytes

~~~c

void _ZN8firebase4auth4Auth11UseEmulatorENSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEj
               (undefined8 *param_1,byte *param_2,undefined4 param_3)

{
  long *plVar1;
  undefined8 uVar2;
  
                    /* catch() { ... } // from try @ 00b5f94c with catch @ 00b5fdd0 */
                    /* catch() { ... } // from try @ 00b5fa90 with catch @ 00b5fddc */
                    /* catch() { ... } // from try @ 00b5fc00 with catch @ 00b5fde0 */
  param_1 = (undefined8 *)*param_1;
                    /* catch() { ... } // from try @ 00b5fd50 with catch @ 00b5fde8
                       catch() { ... } // from try @ 00b5fd84 with catch @ 00b5fde8 */
  if ((*param_2 & 1) == 0) {
    param_2 = param_2 + 1;
  }
  else {
    param_2 = *(byte **)(param_2 + 0x10);
  }
  plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_1);
                    /* catch() { ... } // from try @ 00b5fcfc with catch @ 00b5fe08 */
                    /* catch() { ... } // from try @ 00b5f8c0 with catch @ 00b5fe0c */
                    /* catch() { ... } // from try @ 00b5f880 with catch @ 00b5fe10 */
  uVar2 = (**(code **)(*plVar1 + 0x538))(plVar1,param_2);
                    /* catch() { ... } // from try @ 00b5fd18 with catch @ 00b5fe14
                       catch() { ... } // from try @ 00b5fd6c with catch @ 00b5fe14 */
                    /* catch() { ... } // from try @ 00b5f9dc with catch @ 00b5fe1c */
  FUN_00551e14(plVar1,param_1[0x3f],DAT_010a1380,uVar2,param_3);
  (**(code **)(*plVar1 + 0xb8))(plVar1,uVar2);
  _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar1);
  return;
}

~~~
