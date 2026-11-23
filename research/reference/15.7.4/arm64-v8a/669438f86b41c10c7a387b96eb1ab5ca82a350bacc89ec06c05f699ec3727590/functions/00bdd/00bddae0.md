# 00bddae0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdda90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda90.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0017.md#compare-e9d53c691d3cab06f38f79de4c18045b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddae0",
  "name": "<EXTERNAL>::atoi",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "501d8539eefe3e735eabf2255a9ffc5fb9e84ac9e10e75bd38157f3546ca59cf",
  "source_text_sha256": "501d8539eefe3e735eabf2255a9ffc5fb9e84ac9e10e75bd38157f3546ca59cf"
}
~~~

## 呼び出し元

- [007e5fa4](../007e5/007e5fa4.md)
- [00b12820](../00b12/00b12820.md)
- [00b17160](../00b17/00b17160.md)
- [00b18d1c](../00b18/00b18d1c.md)
- [00b195a8](../00b19/00b195a8.md)
- [00b218b0](../00b21/00b218b0.md)
- [00b22320](../00b22/00b22320.md)

## 呼び出し先

- [010a5560](../010a5/010a5560.md)

## 疑似コード / UTF-8 193 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int atoi(char *__nptr)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_atoi_00c1d628)((int)__nptr);
  return iVar1;
}

~~~
