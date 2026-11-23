# 00bced7c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5f87c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f87c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/high-0004.md#compare-005477b6d1a593740109b6a58a4e45c4)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bced7c",
  "name": "_ZN8firebase4auth4Auth12current_userEv",
  "size": 220,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d363c7793845079a474c3a3aa265281b804cdf3c2c5436ad2c5d16709e57f8c7",
  "source_text_sha256": "d363c7793845079a474c3a3aa265281b804cdf3c2c5436ad2c5d16709e57f8c7"
}
~~~

## 呼び出し元

- [00c5a630](../00c5a/00c5a630.md)

## 呼び出し先

- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5a640](../00c5a/00c5a640.md)

## 疑似コード / UTF-8 1436 bytes

~~~c

void _ZN8firebase4auth4Auth12current_userEv(long *param_1,long *param_2)

{
  long lVar1;
  undefined *puVar2;
  
  puVar2 = PTR__ZTVN8firebase4auth4UserE_00c9b5c0;
  if (*param_2 == 0) {
    param_1[0x12] = 0;
    param_1[0x11] = 0;
    param_1[0x10] = 0;
    param_1[0xf] = 0;
    param_1[0xe] = 0;
    param_1[0xd] = 0;
    param_1[0xc] = 0;
    param_1[0xb] = 0;
    param_1[10] = 0;
    param_1[9] = 0;
    param_1[8] = 0;
    param_1[7] = 0;
    param_1[6] = 0;
    param_1[5] = 0;
    param_1[4] = 0;
    param_1[3] = 0;
    param_1[2] = 0;
    param_1[1] = 0;
    *param_1 = (long)(puVar2 + 0x10);
    param_1[0x13] = 0;
  }
  else {
    lVar1 = *param_2 + 0x18;
    _ZN8firebase5Mutex7AcquireEv(lVar1);
    puVar2 = PTR__ZTVN8firebase4auth4UserE_00c9b5c0;
    if (*(long *)(*param_2 + 0x200) == 0) {
      param_1[0x12] = 0;
      param_1[0x11] = 0;
      param_1[0x10] = 0;
      param_1[0xf] = 0;
      param_1[0xe] = 0;
      param_1[0xd] = 0;
      param_1[0xc] = 0;
      param_1[0xb] = 0;
      param_1[10] = 0;
      param_1[9] = 0;
      param_1[8] = 0;
      param_1[7] = 0;
      param_1[6] = 0;
      param_1[5] = 0;
      param_1[4] = 0;
      param_1[3] = 0;
      param_1[2] = 0;
      param_1[1] = 0;
      *param_1 = (long)(puVar2 + 0x10);
      param_1[0x13] = 0;
    }
    else {
      _ZN8firebase4auth4UserC1ERKS1_(param_1,*param_2 + 0x158);
    }
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  return;
}

~~~
