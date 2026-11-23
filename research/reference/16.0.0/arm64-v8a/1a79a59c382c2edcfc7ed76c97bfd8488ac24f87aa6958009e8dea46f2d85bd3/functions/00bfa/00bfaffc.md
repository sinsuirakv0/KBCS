# 00bfaffc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7e5b4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e5b4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0072.md#compare-034d67c6e895d627b5fbf005c169f8c0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaffc",
  "name": "_ZNSt6__ndk18ios_baseD1Ev",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c75c54f5477b9b61cdb86d55c1f490bd99cffa6d4bc65a9c6e38b963ec01493a",
  "source_text_sha256": "c75c54f5477b9b61cdb86d55c1f490bd99cffa6d4bc65a9c6e38b963ec01493a"
}
~~~

## 呼び出し元

- [00c5cce0](../00c5c/00c5cce0.md)
- [00c5def0](../00c5d/00c5def0.md)

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c58260](../00c58/00c58260.md)

## 疑似コード / UTF-8 584 bytes

~~~c

void _ZNSt6__ndk18ios_baseD1Ev(long *param_1)

{
  long lVar1;
  
  *param_1 = (long)(PTR__ZTVNSt6__ndk18ios_baseE_00c9b700 + 0x10);
  if (param_1[6] != 0) {
    if (param_1[9] != 0) {
      lVar1 = param_1[9] + -1;
      do {
        (**(code **)(param_1[7] + lVar1 * 8))(0,param_1,*(undefined4 *)(param_1[8] + lVar1 * 4));
        lVar1 = lVar1 + -1;
      } while (lVar1 != -1);
    }
    _ZNSt6__ndk16localeD1Ev(param_1 + 6);
    free((void *)param_1[7]);
    free((void *)param_1[8]);
    free((void *)param_1[0xb]);
    free((void *)param_1[0xe]);
    return;
  }
  return;
}

~~~
