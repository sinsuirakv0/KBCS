# 00acaad4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aca8d8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca8d8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/high-0007.md#compare-5267d275c78eebbb54eb834ed916875b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/high-0009.md#compare-7c5c4a5f9caabbf0831b2b6837986f64)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acaad4",
  "name": "FUN_00acaad4",
  "size": 256,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "814ae293cf440dfe843aadf31be53d921e5b20df0a46b610608b94ea818f6337",
  "source_text_sha256": "814ae293cf440dfe843aadf31be53d921e5b20df0a46b610608b94ea818f6337"
}
~~~

## 呼び出し元

- [00788cac](../00788/00788cac.md)
- [0082ee20](../0082e/0082ee20.md)
- [008cabc0](../008ca/008cabc0.md)
- [008d1c40](../008d1/008d1c40.md)
- [008fe9e4](../008fe/008fe9e4.md)
- [00a3de58](../00a3d/00a3de58.md)
- [00a73530](../00a73/00a73530.md)
- [00ac0454](../00ac0/00ac0454.md)

## 呼び出し先

- [0057bea8](../0057b/0057bea8.md)
- [008514f8](../00851/008514f8.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 1127 bytes

~~~c

void FUN_00acaad4(long param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  long *plVar3;
  long *plVar4;
  long local_70 [4];
  long *local_50;
  long local_38;
  
  plVar4 = local_70;
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  lVar2 = FUN_008514f8();
  *(undefined1 *)((long)&fde_table_entry_00332a20.data_loc + lVar2) = 1;
  lVar2 = FUN_008514f8();
  plVar3 = (long *)param_2[4];
  *(undefined4 *)((long)&fde_table_entry_00334170.data_loc + lVar2) = 0x129;
  if (plVar3 == (long *)0x0) {
    local_50 = (long *)0x0;
  }
  else if (plVar3 == param_2) {
    local_50 = local_70;
    (**(code **)(*param_2 + 0x18))(param_2,local_70);
  }
  else {
    local_50 = (long *)(**(code **)(*plVar3 + 0x10))();
  }
  FUN_0057bea8(local_70,param_1 + 0x110);
  if (local_50 == local_70) {
    lVar2 = 0x20;
  }
  else {
    if (local_50 == (long *)0x0) goto LAB_00acabac;
    lVar2 = 0x28;
    plVar4 = local_50;
  }
  (**(code **)(*plVar4 + lVar2))();
LAB_00acabac:
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
