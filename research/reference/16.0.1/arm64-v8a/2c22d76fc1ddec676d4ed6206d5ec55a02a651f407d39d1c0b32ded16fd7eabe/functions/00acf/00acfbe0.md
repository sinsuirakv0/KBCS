# 00acfbe0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acf9e4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf9e4.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0064.md#compare-a4e512e2f1b0497e6109259d57b0f7c2)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0069.md#compare-6ba3e8da4e9acad263901a8be78500ec)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acfbe0",
  "name": "FUN_00acfbe0",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e36702f0cc624eafcfcb49211d5ad2d1008ff6bcd4db08ce8471aac63fd540d2",
  "source_text_sha256": "e36702f0cc624eafcfcb49211d5ad2d1008ff6bcd4db08ce8471aac63fd540d2"
}
~~~

## 呼び出し元

- [00ad6f4c](../00ad6/00ad6f4c.md)

## 呼び出し先

- [00695bac](../00695/00695bac.md)
- [009a2b34](../009a2/009a2b34.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 1110 bytes

~~~c

void FUN_00acfbe0(long param_1,undefined4 param_2,long *param_3)

{
  long lVar1;
  long lVar2;
  long lVar3;
  long lVar4;
  long *plVar5;
  undefined4 local_58;
  undefined1 uStack_51;
  undefined4 *local_50;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  local_58 = param_2;
  if (*param_3 == 0) {
    FUN_009a2b34(param_1 + 0x318,&local_58);
  }
  else {
    local_50 = &local_58;
    lVar3 = FUN_00695bac(param_1 + 0x318,&local_58,&DAT_002c86f5,&local_50,&uStack_51);
    lVar4 = *param_3;
    lVar1 = param_3[1];
    if (lVar1 != 0) {
      FUN_00c53cd0(1,lVar1 + 8);
    }
    plVar5 = *(long **)(lVar3 + 0x20);
    *(long *)(lVar3 + 0x18) = lVar4;
    *(long *)(lVar3 + 0x20) = lVar1;
    if ((plVar5 != (long *)0x0) && (lVar4 = FUN_00c53d00(0xffffffffffffffff,plVar5 + 1), lVar4 == 0)
       ) {
      (**(code **)(*plVar5 + 0x10))(plVar5);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
    }
  }
  if (*(long *)(lVar2 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
