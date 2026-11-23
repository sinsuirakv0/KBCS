# 00bff3bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b82974`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82974.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0072.md#compare-944134fced05ccdf19575960fdc754ff)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bff3bc",
  "name": "_ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56096bb493ee35ec396e865a055d0393d523d44e25b98ac74dcc88b2ee8b13d4",
  "source_text_sha256": "56096bb493ee35ec396e865a055d0393d523d44e25b98ac74dcc88b2ee8b13d4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57de0](../00c57/00c57de0.md)

## 疑似コード / UTF-8 687 bytes

~~~c

void _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE
               (long *param_1)

{
  undefined *puVar1;
  
  puVar1 = 
  PTR__ZTCNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEE0_NS_13basic_istreamIcS2_EE_00c9b720;
  param_1[9] = 0;
  param_1[3] = (long)(puVar1 + 0x40);
  *param_1 = (long)(puVar1 + 0x18);
  param_1[1] = 0;
  _ZNSt6__ndk18ios_base4initEPv(param_1 + 3);
  puVar1 = PTR__ZTVNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEE_00c9b728;
  *(undefined4 *)(param_1 + 0x15) = 0xffffffff;
  param_1[0x14] = 0;
  *param_1 = (long)(puVar1 + 0x18);
  param_1[2] = (long)(puVar1 + 0x40);
  param_1[3] = (long)(puVar1 + 0x68);
  return;
}

~~~
