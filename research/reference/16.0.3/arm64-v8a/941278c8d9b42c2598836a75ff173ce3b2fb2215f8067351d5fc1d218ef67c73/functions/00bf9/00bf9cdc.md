# 00bf9cdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bf9cdc",
  "name": "_ZNSt6__ndk112system_errorC1ENS_10error_codeE",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "230c1816d240347e7d01b2834d9626cfcbf135d74f799808ec652f29542c5f87",
  "source_text_sha256": "230c1816d240347e7d01b2834d9626cfcbf135d74f799808ec652f29542c5f87"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)
- [00c5f040](../00c5f/00c5f040.md)

## 疑似コード / UTF-8 654 bytes

~~~c

void _ZNSt6__ndk112system_errorC1ENS_10error_codeE(long *param_1,ulong param_2,long *param_3)

{
  ulong local_48 [2];
  void *local_38;
  
  if ((int)param_2 == 0) {
    local_48[0] = 0;
    local_48[1] = 0;
    local_38 = (void *)0x0;
  }
  else {
    (**(code **)(*param_3 + 0x30))(local_48,param_3,param_2 & 0xffffffff);
  }
  _ZNSt13runtime_errorC1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
            (param_1,local_48);
  if ((local_48[0] & 1) != 0) {
    _ZdlPv(local_38);
  }
  *param_1 = (long)(PTR__ZTVNSt6__ndk112system_errorE_00c9cb70 + 0x10);
  param_1[2] = param_2;
  param_1[3] = (long)param_3;
  return;
}

~~~
