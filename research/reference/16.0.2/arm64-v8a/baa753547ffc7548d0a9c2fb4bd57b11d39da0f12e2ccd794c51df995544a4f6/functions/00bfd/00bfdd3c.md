# 00bfdd3c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfdca0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdca0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0041.md#compare-0162eee0da6513944a43de132579704e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0039.md#compare-bf0d26b4f0776e547803ad8439c34551)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfdd3c",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "464be215ec48d6ccddf2f177ff6b7cf28733e1b80b3a4beea365c57d0c762f7e",
  "source_text_sha256": "464be215ec48d6ccddf2f177ff6b7cf28733e1b80b3a4beea365c57d0c762f7e"
}
~~~

## 呼び出し元

- [00c5e460](../00c5e/00c5e460.md)

## 呼び出し先

- [00c58370](../00c58/00c58370.md)
- [00c59ea0](../00c59/00c59ea0.md)

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
          goto joined_r0x00bfdea8;
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
        goto joined_r0x00bfdea8;
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
joined_r0x00bfdea8:
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
