# 00bf8cfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bf8cfc",
  "name": "_ZNSt6__ndk112system_errorC2EiRKNS_14error_categoryERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1a16dcb903fd0fdf89f08b2e9376d1b64bc006e58117febc1e3ad56aa39cf662",
  "source_text_sha256": "1a16dcb903fd0fdf89f08b2e9376d1b64bc006e58117febc1e3ad56aa39cf662"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0043bb20](../0043b/0043bb20.md)
- [00bf8a14](../00bf8/00bf8a14.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c5dfa0](../00c5d/00c5dfa0.md)

## 疑似コード / UTF-8 1050 bytes

~~~c

void _ZNSt6__ndk112system_errorC2EiRKNS_14error_categoryERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
               (long *param_1,undefined4 param_2,long param_3,ulong *param_4)

{
  undefined *puVar1;
  ulong local_70;
  ulong uStack_68;
  void *local_60;
  undefined4 local_58 [2];
  long local_50;
  byte local_48 [16];
  void *local_38;
  
  local_58[0] = param_2;
  local_50 = param_3;
  if ((*param_4 & 1) == 0) {
    uStack_68 = param_4[1];
    local_70 = *param_4;
    local_60 = (void *)param_4[2];
  }
  else {
    FUN_0043bb20(&local_70,param_4[2],param_4[1]);
  }
  FUN_00bf8a14(local_48,local_58,&local_70);
  _ZNSt13runtime_errorC1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
            (param_1,local_48);
  if ((local_48[0] & 1) != 0) {
    _ZdlPv(local_38);
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv(local_60);
  }
  puVar1 = PTR__ZTVNSt6__ndk112system_errorE_00c9bad0;
  *(undefined4 *)(param_1 + 2) = param_2;
  *param_1 = (long)(puVar1 + 0x10);
  param_1[3] = param_3;
  return;
}

~~~
