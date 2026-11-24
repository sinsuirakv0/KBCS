# 00befcc4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00befc28`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc28.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0086.md#compare-1c0fe76272fdbc0365792cb3c068fc4a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0098.md#compare-8e9474813f9d78025519784d0930db59)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befcc4",
  "name": "_ZNSt6__ndk112__next_primeEm",
  "size": 1824,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3a7063c3cd3e51532f4b175263fde61a7b8cb9a56c1a01a83ae966e7777e8854",
  "source_text_sha256": "3a7063c3cd3e51532f4b175263fde61a7b8cb9a56c1a01a83ae966e7777e8854"
}
~~~

## 呼び出し元

- [00c5a8f0](../00c5a/00c5a8f0.md)

## 呼び出し先

- [00bf03e4](../00bf0/00bf03e4.md)

## 関連文字列（未確認候補）

~~~text
"__next_prime overflow"
~~~

## 疑似コード / UTF-8 12503 bytes

~~~c

ulong _ZNSt6__ndk112__next_primeEm(ulong param_1)

{
  uint *puVar1;
  uint *puVar2;
  ulong uVar3;
  ulong uVar4;
  long lVar5;
  long lVar6;
  ulong uVar7;
  ulong uVar8;
  ulong uVar9;
  
  if (param_1 < 0xd4) {
    uVar3 = 0x30;
    puVar2 = &DAT_00310308;
    do {
      uVar4 = uVar3 >> 1;
      puVar1 = puVar2 + uVar4 + 1;
      uVar3 = uVar3 + ~uVar4;
      if (param_1 <= puVar2[uVar4]) {
        puVar1 = puVar2;
        uVar3 = uVar4;
      }
      puVar2 = puVar1;
    } while (uVar3 != 0);
    return (ulong)*puVar1;
  }
  if (0xffffffffffffffc5 < param_1) {
                    /* WARNING: Subroutine does not return */
    FUN_00bf03e4("__next_prime overflow");
  }
  uVar4 = 0x30;
  uVar3 = param_1 / 0xd2;
  puVar2 = &DAT_003103c8;
  do {
    uVar7 = uVar4 >> 1;
    puVar1 = puVar2 + uVar7 + 1;
    uVar4 = uVar4 + ~uVar7;
    if (param_1 % 0xd2 <= (ulong)puVar2[uVar7]) {
      puVar1 = puVar2;
      uVar4 = uVar7;
    }
    puVar2 = puVar1;
  } while (uVar4 != 0);
  lVar6 = (long)(puVar1 + -0xc40f2) >> 2;
  do {
    lVar5 = lVar6;
    uVar4 = uVar3 * 0xd2 + (ulong)(uint)(&DAT_003103c8)[lVar5];
    lVar6 = 0x14;
    do {
      uVar8 = (ulong)*(uint *)((long)&DAT_00310308 + lVar6);
      uVar7 = 0;
      if (uVar8 != 0) {
        uVar7 = uVar4 / uVar8;
      }
      if (uVar7 < uVar8) {
        return uVar4;
      }
      if (uVar4 == uVar7 * uVar8) goto LAB_00bf03c0;
      lVar6 = lVar6 + 4;
    } while (lVar6 != 0xbc);
    uVar7 = 0x1a3;
    do {
      uVar9 = uVar7 - 0xd0;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar9) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0xc6;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0xc6) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0xc4;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0xc4) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0xc0;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0xc0) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0xbe;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0xbe) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0xba;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0xba) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0xb4;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0xb4) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0xb2;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0xb2) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0xac;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0xac) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0xa8;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0xa8) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0xa6;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0xa6) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0xa2;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0xa2) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x9c;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x9c) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x96;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x96) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x94;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x94) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x8e;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x8e) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x8a;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x8a) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x88;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x88) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x82;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x82) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x7e;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x7e) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x78;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x78) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x70;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x70) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x6c;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x6c) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x6a;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x6a) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x66;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x66) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 100;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 100) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x60;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x60) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x58;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x58) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x52;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x52) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x4e;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x4e) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x48;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x48) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x46;
                    /* try { // try from 00bf01a4 to 00cf039b has its CatchHandler @ 00bf01a4
                       catch() { ... } // from try @ 00bf01a4 with catch @ 00bf01a4
                       catch() { ... } // from try @ 00bf03e4 with catch @ 00bf01a4
                       catch() { ... } // from try @ 00bf04a0 with catch @ 00bf01a4 */
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x46) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x42;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x42) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x3c;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x3c) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x3a;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x3a) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x34;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x34) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x2e;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x2e) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x2a;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x2a) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x28;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x28) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x24;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x24) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x1e;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x1e) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x1c;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x1c) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x16;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x16) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x12;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x12) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0x10;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0x10) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 0xc;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 0xc) {
        return uVar4;
      }
      if (uVar4 == uVar8 * uVar9) break;
      uVar9 = uVar7 - 10;
      uVar8 = 0;
      if (uVar9 != 0) {
        uVar8 = uVar4 / uVar9;
      }
      if (uVar8 < uVar7 - 10) {
        return uVar4;
      }
                    /* try { // try from 00bf039c to 00cf03a3 has its CatchHandler @ 00bf0600 */
      if (uVar4 == uVar8 * uVar9) break;
      uVar8 = 0;
      if (uVar7 != 0) {
        uVar8 = uVar4 / uVar7;
      }
                    /* try { // try from 00bf03a4 to 00cf03af has its CatchHandler @ 00bf05fc */
      if (uVar8 < uVar7) {
        return uVar4;
      }
      uVar8 = uVar8 * uVar7;
      uVar7 = uVar7 + 0xd2;
    } while (uVar4 != uVar8);
LAB_00bf03c0:
                    /* try { // try from 00bf03c8 to 00cf03e3 has its CatchHandler @ 00bf0598 */
    if (lVar5 == 0x2f) {
      uVar3 = uVar3 + 1;
    }
    lVar6 = 0;
    if (lVar5 != 0x2f) {
      lVar6 = lVar5 + 1;
    }
  } while( true );
}

~~~
