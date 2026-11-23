# 00afaba4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00afa77c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afa/00afa77c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0066.md#compare-82e5fdbabb38a06d0127c4a63cd5d4f6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0072.md#compare-29bc00a25f368a5b8344b9de4a07b545)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaba4",
  "name": "FUN_00afaba4",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "89feba2e282f0e7f67f1ef5c5a4856b336479560e278e0434deaa67ec0bb8f81",
  "source_text_sha256": "89feba2e282f0e7f67f1ef5c5a4856b336479560e278e0434deaa67ec0bb8f81"
}
~~~

## 呼び出し元

- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 978 bytes

~~~c

void FUN_00afaba4(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
                    /* try { // try from 00afabcc to 00bfac67 has its CatchHandler @ 00afabcc
                       catch() { ... } // from try @ 00afabcc with catch @ 00afabcc
                       catch() { ... } // from try @ 00afac80 with catch @ 00afabcc
                       catch() { ... } // from try @ 00afad40 with catch @ 00afabcc
                       catch() { ... } // from try @ 00afae0c with catch @ 00afabcc
                       catch() { ... } // from try @ 00afafa8 with catch @ 00afabcc
                       catch() { ... } // from try @ 00afaff8 with catch @ 00afabcc
                       catch() { ... } // from try @ 00afb0a4 with catch @ 00afabcc
                       catch() { ... } // from try @ 00afb180 with catch @ 00afabcc */
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a28) = param_3 & 1;
  return;
}

~~~
