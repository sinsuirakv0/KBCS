# 00a9afbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/review-0082.md#review-4b287365d9b01ea200ffa4766a70938b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/review-0039.md#review-4b287365d9b01ea200ffa4766a70938b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9afbc",
  "name": "FUN_00a9afbc",
  "size": 196,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42b77fe8218090744dbe07ebe561fb9c83af9d2fe03b330366580f8579ec45a7",
  "source_text_sha256": "42b77fe8218090744dbe07ebe561fb9c83af9d2fe03b330366580f8579ec45a7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0048ccf8](../0048c/0048ccf8.md)
- [0048e7e0](../0048e/0048e7e0.md)
- [0066d0dc](../0066d/0066d0dc.md)
- [00a605b4](../00a60/00a605b4.md)

## 疑似コード / UTF-8 925 bytes

~~~c

void FUN_00a9afbc(long param_1,byte *param_2)

{
  ulong uVar1;
  long lVar2;
  
  lVar2 = *(long *)(param_1 + 8);
  if ((*param_2 & 1) == 0) {
    *(undefined1 *)(*(long *)(lVar2 + 0x2268) + 0x20) = 0;
  }
  *(undefined1 *)((long)&DWORD_0039b1d8 + lVar2) = 0;
  FUN_0048ccf8();
  FUN_0048e7e0();
  FUN_0066d0dc(0xe);
  *(undefined4 *)((long)&fde_table_entry_00333970.data_loc + lVar2) = 3;
  *(undefined4 *)((long)&fde_0038f284 + lVar2) = 3;
  *(undefined1 *)(lVar2 + 0x33d9) = 1;
  *(undefined4 *)((long)&fde_table_entry_00332068.initial_loc + lVar2) = 0;
  uVar1 = FUN_00a605b4(lVar2 + 0x23a0);
  if ((uVar1 & 1) != 0) {
    *(undefined4 *)((long)&fde_table_entry_00332068.initial_loc + lVar2) = 1;
    *(undefined1 *)((long)&fde_table_entry_003372c8.data_loc + lVar2) = 1;
  }
  *(undefined1 *)((long)&fde_table_entry_00332060.initial_loc + lVar2) = 1;
  *(undefined4 *)((long)&DWORD_003c7c6c + lVar2) = 0;
  return;
}

~~~
