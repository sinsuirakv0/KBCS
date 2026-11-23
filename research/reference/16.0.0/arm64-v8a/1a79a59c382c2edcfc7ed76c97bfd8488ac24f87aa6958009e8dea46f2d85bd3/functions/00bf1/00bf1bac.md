# 00bf1bac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b75164`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75164.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/inspection-0019.md#compare-09d8fc89fe3784c311c7f0340b8dd614)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf1bac",
  "name": "_ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEPKcmm",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "acd845f5b67359a24cecad3f0f8a76c227148df935f0170de9b8b2a2809c18de",
  "source_text_sha256": "acd845f5b67359a24cecad3f0f8a76c227148df935f0170de9b8b2a2809c18de"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57bd0](../00c57/00c57bd0.md)
- [00c57c50](../00c57/00c57c50.md)

## 疑似コード / UTF-8 1288 bytes

~~~c

ulong _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEPKcmm
                (byte *param_1,byte *param_2,ulong param_3,size_t param_4)

{
  byte *pbVar1;
  ulong uVar2;
  byte *pbVar3;
  byte bVar4;
  int iVar5;
  byte *pbVar6;
  long lVar7;
  byte *pbVar8;
  
  uVar2 = *(ulong *)(param_1 + 8);
  pbVar3 = *(byte **)(param_1 + 0x10);
  if ((*param_1 & 1) == 0) {
    pbVar3 = param_1 + 1;
    uVar2 = (ulong)(*param_1 >> 1);
  }
  if (uVar2 < param_3) {
    param_3 = 0xffffffffffffffff;
  }
  else if (param_4 != 0) {
    pbVar6 = pbVar3 + param_3;
    pbVar1 = pbVar3 + uVar2;
    lVar7 = (long)pbVar1 - (long)pbVar6;
    pbVar8 = pbVar1;
    if ((long)param_4 <= lVar7) {
      bVar4 = *param_2;
      do {
        pbVar8 = pbVar1;
        if (((0xfffffffffffffffe < lVar7 - param_4) ||
            (pbVar6 = memchr(pbVar6,(uint)bVar4,(lVar7 - param_4) + 1), pbVar6 == (byte *)0x0)) ||
           (iVar5 = memcmp(pbVar6,param_2,param_4), pbVar8 = pbVar6, iVar5 == 0)) break;
        pbVar6 = pbVar6 + 1;
        lVar7 = (long)pbVar1 - (long)pbVar6;
        pbVar8 = pbVar1;
      } while ((long)param_4 <= lVar7);
    }
    param_3 = (long)pbVar8 - (long)pbVar3;
    if (pbVar8 == pbVar1) {
      param_3 = 0xffffffffffffffff;
    }
  }
  return param_3;
}

~~~
