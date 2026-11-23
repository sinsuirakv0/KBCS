# 00bfa2bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7d874`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d874.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/inspection-0020.md#compare-a5b60ffbe170ba9dff013543ae9bf93f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa2bc",
  "name": "_ZNSt6__ndk16threadD2Ev",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f4a0dbf2c6ca2e59794e120809d6f08ac0e148e1fbe43a79561a00908594a160",
  "source_text_sha256": "f4a0dbf2c6ca2e59794e120809d6f08ac0e148e1fbe43a79561a00908594a160"
}
~~~

## 呼び出し元

- [00c57d80](../00c57/00c57d80.md)

## 呼び出し先

- [00c57c20](../00c57/00c57c20.md)

## 疑似コード / UTF-8 173 bytes

~~~c

void _ZNSt6__ndk16threadD2Ev(long *param_1)

{
  if (*param_1 == 0) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  _ZSt9terminatev();
}

~~~
