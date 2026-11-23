# 004edddc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `004edd9c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edd9c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0010.md#compare-03fb37f3d6da0f89d46e4efd5c186610)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0010.md#compare-9e1f05c877635fea91b551bad5e0a219)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004edddc",
  "name": "_ZN5Botan5PKCS88load_keyERNS_10DataSourceE",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "adcd1d9a7ad21fc53a5dcc9e93970791a5e0303dc4d3af1f922acabcbb3d0af5",
  "source_text_sha256": "adcd1d9a7ad21fc53a5dcc9e93970791a5e0303dc4d3af1f922acabcbb3d0af5"
}
~~~

## 呼び出し元

- [00c59640](../00c59/00c59640.md)

## 呼び出し先

- [004ecd10](../004ec/004ecd10.md)
- [00545970](../00545/00545970.md)
- [00545974](../00545/00545974.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 771 bytes

~~~c

void _ZN5Botan5PKCS88load_keyERNS_10DataSourceE(undefined8 param_1)

{
  long lVar1;
  undefined ***pppuVar2;
  long lVar3;
  undefined **local_60 [4];
  long *local_40;
  long local_28;
  
  local_40 = (long *)local_60;
  pppuVar2 = local_60;
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  local_60[0] = &PTR_FUN_00c6a5b0;
  FUN_004ecd10(param_1,local_60,0);
  if ((undefined ***)local_40 == local_60) {
    lVar3 = 0x20;
  }
  else {
    if (local_40 == (long *)0x0) goto LAB_004ede44;
    lVar3 = 0x28;
    pppuVar2 = (undefined ***)local_40;
  }
  (**(code **)((long)*pppuVar2 + lVar3))();
LAB_004ede44:
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
