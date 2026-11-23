# 004ababc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `004ababc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ab/004ababc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0009.md#compare-d4074e580377183d95966030a58b60d6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004ababc",
  "name": "_ZNK5Botan3MD510copy_stateEv",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97e9dd0b3a9e7045b2d6c4f95cfe76a836d5e4b10970080e503a70b39fb0a146",
  "source_text_sha256": "97e9dd0b3a9e7045b2d6c4f95cfe76a836d5e4b10970080e503a70b39fb0a146"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [005132d4](../00513/005132d4.md)
- [0051d3cc](../0051d/0051d3cc.md)
- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード / UTF-8 991 bytes

~~~c

void _ZNK5Botan3MD510copy_stateEv(undefined8 *param_1,long param_2)

{
  long lVar1;
  long lVar2;
  undefined *puVar3;
  long *plVar4;
  long lVar5;
  long lVar6;
  long lVar7;
  long lVar8;
  
  plVar4 = (long *)_Znwm(0x70);
  puVar3 = PTR__ZTVN5Botan16MDx_HashFunctionE_00c1b148;
  plVar4[2] = 0;
  plVar4[3] = 0;
  *plVar4 = (long)(puVar3 + 0x10);
  plVar4[1] = 0;
  FUN_0051d3cc();
  puVar3 = PTR__ZTVN5Botan3MD5E_00c1b168;
  lVar6 = *(long *)(param_2 + 0x28);
  lVar5 = *(long *)(param_2 + 0x20);
  lVar8 = *(long *)(param_2 + 0x38);
  lVar7 = *(long *)(param_2 + 0x30);
  lVar1 = *(long *)(param_2 + 0x40);
  lVar2 = *(long *)(param_2 + 0x48);
  plVar4[9] = 0;
  plVar4[10] = 0;
  plVar4[5] = lVar6;
  plVar4[4] = lVar5;
  plVar4[7] = lVar8;
  plVar4[6] = lVar7;
  *plVar4 = (long)(puVar3 + 0x10);
  plVar4[8] = 0;
  FUN_005132d4(plVar4 + 8,lVar1,lVar2,lVar2 - lVar1 >> 2);
  plVar4[0xb] = 0;
  plVar4[0xc] = 0;
  plVar4[0xd] = 0;
  FUN_005132d4();
  *param_1 = plVar4;
  return;
}

~~~
