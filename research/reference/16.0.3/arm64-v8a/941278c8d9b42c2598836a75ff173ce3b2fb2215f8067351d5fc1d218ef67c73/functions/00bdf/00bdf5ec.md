# 00bdf5ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bdf5ec",
  "name": "_ZNK8firebase4auth4User9photo_urlEv",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6fd9dbebbaab874f8c7faf0f69adf00b62f70c256dc652a54492d4d759c25b12",
  "source_text_sha256": "6fd9dbebbaab874f8c7faf0f69adf00b62f70c256dc652a54492d4d759c25b12"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497b94](../00497/00497b94.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c390](../00c5c/00c5c390.md)
- [00c5c660](../00c5c/00c5c660.md)

## 疑似コード / UTF-8 790 bytes

~~~c

void _ZNK8firebase4auth4User9photo_urlEv(undefined8 *param_1,long param_2)

{
  undefined8 uVar1;
  ulong uVar2;
  undefined8 *puVar3;
  long lVar4;
  
  puVar3 = *(undefined8 **)(param_2 + 0x98);
  if ((puVar3 == (undefined8 *)0x0) || (lVar4 = puVar3[0x40], lVar4 == 0)) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
              (param_1,&DAT_002a64e6);
    return;
  }
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*puVar3);
  lVar4 = FUN_00497b94(uVar1,lVar4,DAT_01127ea0);
  uVar2 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
  if ((lVar4 != 0) && ((uVar2 & 1) == 0)) {
    _ZN8firebase4util14JniUriToStringEP7_JNIEnvP8_jobject(param_1,uVar1,lVar4);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  return;
}

~~~
