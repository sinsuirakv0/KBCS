# 00bf4bbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf4b20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4b20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0041.md#compare-6a1b55a67e6284cdc9c703e4a95df668)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0038.md#compare-72a09f9e4a48604d7e71c8b4cc1161fa)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf4bbc",
  "name": "_ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmRKS5_mm",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ccc5786ed455bd26e9f98ba6a5d4d7794dfcffe160e20b99f05d952a810f5732",
  "source_text_sha256": "ccc5786ed455bd26e9f98ba6a5d4d7794dfcffe160e20b99f05d952a810f5732"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bf2974](../00bf2/00bf2974.md)
- [00c5e0f0](../00c5e/00c5e0f0.md)

## 疑似コード / UTF-8 838 bytes

~~~c

void _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmRKS5_mm
               (undefined8 param_1,undefined8 param_2,byte *param_3,ulong param_4,ulong param_5)

{
  ulong uVar1;
  byte *pbVar2;
  ulong uVar3;
  byte bVar4;
  
  bVar4 = *param_3;
  uVar1 = (ulong)(bVar4 >> 1);
  if ((bVar4 & 1) != 0) {
    uVar1 = *(ulong *)(param_3 + 8);
  }
  if (param_4 <= uVar1) {
    pbVar2 = param_3 + 4;
    if ((bVar4 & 1) != 0) {
      pbVar2 = *(byte **)(param_3 + 0x10);
    }
    uVar3 = uVar1 - param_4;
    if (param_5 <= uVar1 - param_4) {
      uVar3 = param_5;
    }
    _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKwm
              (param_1,param_2,pbVar2 + param_4 * 4,uVar3);
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00bf2974();
}

~~~
