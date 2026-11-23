# 00bfdca0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfd878`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd878.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0041.md#compare-7cddab659c7c13d86dbee737f7e5b936)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0042.md#compare-0162eee0da6513944a43de132579704e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfdca0",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5ad19d36ac03fc6dacd11d2b0f0d953df77c81c6465359db2821dd90fb4bca36",
  "source_text_sha256": "5ad19d36ac03fc6dacd11d2b0f0d953df77c81c6465359db2821dd90fb4bca36"
}
~~~

## 呼び出し元

- [00c5e390](../00c5e/00c5e390.md)

## 呼び出し先

- [00c582a0](../00c58/00c582a0.md)
- [00c59dd0](../00c59/00c59dd0.md)

## 疑似コード / UTF-8 2043 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc
                 (long *param_1,undefined1 *param_2,long param_3,uint param_4)

{
  uint uVar1;
  long *plVar2;
  uint uVar3;
  long lVar4;
  undefined1 *puVar5;
  byte local_54 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_54,param_1,1);
  uVar3 = (uint)local_54[0];
  if (local_54[0] != 0) {
    while( true ) {
      plVar2 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
      if ((byte *)plVar2[3] == (byte *)plVar2[4]) {
        uVar3 = (**(code **)(*plVar2 + 0x48))();
        if (uVar3 == 0xffffffff) {
          uVar3 = 2;
          goto joined_r0x00bfde0c;
        }
      }
      else {
        uVar3 = (uint)*(byte *)plVar2[3];
      }
      if ((uVar3 & 0xff) == (param_4 & 0xff)) {
        plVar2 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
        if (plVar2[3] == plVar2[4]) {
          (**(code **)(*plVar2 + 0x50))();
        }
        else {
          plVar2[3] = plVar2[3] + 1;
        }
        if (param_1[1] == 0x7fffffffffffffff) {
          uVar3 = 0;
        }
        else {
          uVar3 = 0;
          param_1[1] = param_1[1] + 1;
        }
        goto joined_r0x00bfde0c;
      }
      if (param_3 + -1 <= param_1[1]) break;
      lVar4 = *param_1;
      puVar5 = param_2 + 1;
      *param_2 = (char)uVar3;
      plVar2 = *(long **)((long)param_1 + *(long *)(lVar4 + -0x18) + 0x28);
      if (plVar2[3] == plVar2[4]) {
        (**(code **)(*plVar2 + 0x50))();
      }
      else {
        plVar2[3] = plVar2[3] + 1;
      }
      param_2 = puVar5;
      if (param_1[1] != 0x7fffffffffffffff) {
        param_1[1] = param_1[1] + 1;
      }
    }
    uVar3 = 4;
  }
joined_r0x00bfde0c:
  if (0 < param_3) {
    *param_2 = 0;
  }
  lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
  uVar1 = uVar3 | 4;
  if (param_1[1] != 0) {
    uVar1 = uVar3;
  }
  _ZNSt6__ndk18ios_base5clearEj(lVar4,*(uint *)(lVar4 + 0x20) | uVar1);
  return param_1;
}

~~~
