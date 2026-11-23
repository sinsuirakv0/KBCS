# 00adb3ac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00adb2e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb2e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0001.md#compare-5962fb40c05d743cca68eecf14bc2778)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00adb3f0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb3f0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-54f83913834aa592fce6e9b3e6afe12e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adb3ac",
  "name": "FUN_00adb3ac",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4931f63f43fbcf6d1c0edee33669db254c39338bbe550fad688022d84ab0096d",
  "source_text_sha256": "4931f63f43fbcf6d1c0edee33669db254c39338bbe550fad688022d84ab0096d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adb3ac",
        "00adb4af"
      ]
    ],
    "bytes_sha256": "5c9e37e4f46812eb2864307db6022ddc977c2a088d588b494d74a0de07e20bf4",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00adb268](../00adb/00adb268.md)

## 呼び出し先

- [00bdb1b0](../00bdb/00bdb1b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1502 bytes

~~~c

long * FUN_00adb3ac(long param_1,undefined8 *param_2,byte *param_3)

{
  void *__s2;
  size_t __n;
  ulong uVar1;
  byte *__s1;
  bool bVar2;
  ulong uVar3;
  int iVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  
  plVar6 = (long *)(param_1 + 8);
  plVar5 = (long *)*plVar6;
  plVar7 = plVar6;
  if (plVar5 != (long *)0x0) {
    uVar1 = *(ulong *)(param_3 + 8);
    __s1 = *(byte **)(param_3 + 0x10);
    if ((*param_3 & 1) == 0) {
      __s1 = param_3 + 1;
      uVar1 = (ulong)(*param_3 >> 1);
    }
    do {
      while( true ) {
        plVar7 = plVar5;
        __s2 = (void *)((long)plVar7 + 0x21);
        uVar3 = (ulong)(*(byte *)(plVar7 + 4) >> 1);
        if ((*(byte *)(plVar7 + 4) & 1) != 0) {
          __s2 = (void *)plVar7[6];
          uVar3 = plVar7[5];
        }
        __n = uVar3;
        if (uVar1 <= uVar3) {
          __n = uVar1;
        }
        iVar4 = memcmp(__s1,__s2,__n);
        bVar2 = uVar1 < uVar3;
        if (iVar4 != 0) {
          bVar2 = iVar4 < 0;
        }
        if (bVar2) break;
        iVar4 = memcmp(__s2,__s1,__n);
        bVar2 = uVar3 < uVar1;
        if (iVar4 != 0) {
          bVar2 = iVar4 < 0;
        }
        if (!bVar2) goto LAB_00adb490;
        plVar6 = plVar7 + 1;
        plVar5 = (long *)*plVar6;
        if ((long *)*plVar6 == (long *)0x0) goto LAB_00adb490;
      }
      plVar5 = (long *)*plVar7;
      plVar6 = plVar7;
    } while ((long *)*plVar7 != (long *)0x0);
  }
LAB_00adb490:
  *param_2 = plVar7;
  return plVar6;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adb3ac"></a> `00adb3ac` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00adb3b0"></a> `00adb3b0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adb3b4"></a> `00adb3b4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adb3b8"></a> `00adb3b8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adb3bc"></a> `00adb3bc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adb3c0"></a> `00adb3c0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00adb3c4"></a> `00adb3c4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00adb3c8"></a> `00adb3c8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00adb3cc"></a> `00adb3cc` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00adb3d0"></a> `00adb3d0` | `e8 05 00 b4` | cbz x8,0x00adb48c | `CONDITIONAL_JUMP`
<a id="insn-00adb3d4"></a> `00adb3d4` | `49 00 40 39` | ldrb w9,[x2] | `FALL_THROUGH`
<a id="insn-00adb3d8"></a> `00adb3d8` | `4b b0 40 a9` | ldp x11,x12,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00adb3dc"></a> `00adb3dc` | `2a fd 41 d3` | lsr x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00adb3e0"></a> `00adb3e0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00adb3e4"></a> `00adb3e4` | `95 15 82 9a` | csinc x21,x12,x2,ne | `FALL_THROUGH`
<a id="insn-00adb3e8"></a> `00adb3e8` | `59 01 8b 9a` | csel x25,x10,x11,eq | `FALL_THROUGH`
<a id="insn-00adb3ec"></a> `00adb3ec` | `04 00 00 14` | b 0x00adb3fc | `UNCONDITIONAL_JUMP`
<a id="insn-00adb3f0"></a> `00adb3f0` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00adb3f4"></a> `00adb3f4` | `f4 03 18 aa` | mov x20,x24 | `FALL_THROUGH`
<a id="insn-00adb3f8"></a> `00adb3f8` | `c8 04 00 b4` | cbz x8,0x00adb490 | `CONDITIONAL_JUMP`
<a id="insn-00adb3fc"></a> `00adb3fc` | `f8 03 08 aa` | mov x24,x8 | `FALL_THROUGH`
<a id="insn-00adb400"></a> `00adb400` | `08 81 40 39` | ldrb w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00adb404"></a> `00adb404` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00adb408"></a> `00adb408` | `09 af 42 a9` | ldp x9,x11,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00adb40c"></a> `00adb40c` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00adb410"></a> `00adb410` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00adb414"></a> `00adb414` | `08 87 00 91` | add x8,x24,#0x21 | `FALL_THROUGH`
<a id="insn-00adb418"></a> `00adb418` | `5a 01 89 9a` | csel x26,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00adb41c"></a> `00adb41c` | `16 01 8b 9a` | csel x22,x8,x11,eq | `FALL_THROUGH`
<a id="insn-00adb420"></a> `00adb420` | `5f 03 19 eb` | cmp x26,x25 | `FALL_THROUGH`
<a id="insn-00adb424"></a> `00adb424` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00adb428"></a> `00adb428` | `57 33 99 9a` | csel x23,x26,x25,cc | `FALL_THROUGH`
<a id="insn-00adb42c"></a> `00adb42c` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00adb430"></a> `00adb430` | `60 ff 03 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00adb434"></a> `00adb434` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-00adb438"></a> `00adb438` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00adb43c"></a> `00adb43c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00adb440"></a> `00adb440` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00adb444"></a> `00adb444` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00adb448"></a> `00adb448` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00adb44c"></a> `00adb44c` | `20 fd ff 54` | b.eq 0x00adb3f0 | `CONDITIONAL_JUMP`
<a id="insn-00adb450"></a> `00adb450` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00adb454"></a> `00adb454` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00adb458"></a> `00adb458` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00adb45c"></a> `00adb45c` | `55 ff 03 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00adb460"></a> `00adb460` | `5f 03 19 eb` | cmp x26,x25 | `FALL_THROUGH`
<a id="insn-00adb464"></a> `00adb464` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00adb468"></a> `00adb468` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00adb46c"></a> `00adb46c` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00adb470"></a> `00adb470` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00adb474"></a> `00adb474` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00adb478"></a> `00adb478` | `c1 00 00 54` | b.ne 0x00adb490 | `CONDITIONAL_JUMP`
<a id="insn-00adb47c"></a> `00adb47c` | `f4 03 18 aa` | mov x20,x24 | `FALL_THROUGH`
<a id="insn-00adb480"></a> `00adb480` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00adb484"></a> `00adb484` | `c8 fb ff b5` | cbnz x8,0x00adb3fc | `CONDITIONAL_JUMP`
<a id="insn-00adb488"></a> `00adb488` | `02 00 00 14` | b 0x00adb490 | `UNCONDITIONAL_JUMP`
<a id="insn-00adb48c"></a> `00adb48c` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00adb490"></a> `00adb490` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adb494"></a> `00adb494` | `78 02 00 f9` | str x24,[x19] | `FALL_THROUGH`
<a id="insn-00adb498"></a> `00adb498` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adb49c"></a> `00adb49c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adb4a0"></a> `00adb4a0` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adb4a4"></a> `00adb4a4` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adb4a8"></a> `00adb4a8` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00adb4ac"></a> `00adb4ac` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adb3ac`](#insn-00adb3ac) 範囲 `[['00adb3ac', '00adb3d3']]`
  - `CONDITIONAL_JUMP` [`00adb3d0`](#insn-00adb3d0) → [`00adb48c`](#insn-00adb48c)
  - `FALL_THROUGH` [`00adb3d0`](#insn-00adb3d0) → [`00adb3d4`](#insn-00adb3d4)
- ブロック [`00adb3d4`](#insn-00adb3d4) 範囲 `[['00adb3d4', '00adb3ef']]`
  - `UNCONDITIONAL_JUMP` [`00adb3ec`](#insn-00adb3ec) → [`00adb3fc`](#insn-00adb3fc)
- ブロック [`00adb3f0`](#insn-00adb3f0) 範囲 `[['00adb3f0', '00adb3fb']]`
  - `CONDITIONAL_JUMP` [`00adb3f8`](#insn-00adb3f8) → [`00adb490`](#insn-00adb490)
  - `FALL_THROUGH` [`00adb3f8`](#insn-00adb3f8) → [`00adb3fc`](#insn-00adb3fc)
- ブロック [`00adb3fc`](#insn-00adb3fc) 範囲 `[['00adb3fc', '00adb44f']]`
  - `CONDITIONAL_JUMP` [`00adb44c`](#insn-00adb44c) → [`00adb3f0`](#insn-00adb3f0)
  - `FALL_THROUGH` [`00adb44c`](#insn-00adb44c) → [`00adb450`](#insn-00adb450)
- ブロック [`00adb450`](#insn-00adb450) 範囲 `[['00adb450', '00adb47b']]`
  - `CONDITIONAL_JUMP` [`00adb478`](#insn-00adb478) → [`00adb490`](#insn-00adb490)
  - `FALL_THROUGH` [`00adb478`](#insn-00adb478) → [`00adb47c`](#insn-00adb47c)
- ブロック [`00adb47c`](#insn-00adb47c) 範囲 `[['00adb47c', '00adb487']]`
  - `CONDITIONAL_JUMP` [`00adb484`](#insn-00adb484) → [`00adb3fc`](#insn-00adb3fc)
  - `FALL_THROUGH` [`00adb484`](#insn-00adb484) → [`00adb488`](#insn-00adb488)
- ブロック [`00adb488`](#insn-00adb488) 範囲 `[['00adb488', '00adb48b']]`
  - `UNCONDITIONAL_JUMP` [`00adb488`](#insn-00adb488) → [`00adb490`](#insn-00adb490)
- ブロック [`00adb48c`](#insn-00adb48c) 範囲 `[['00adb48c', '00adb48f']]`
  - `FALL_THROUGH` [`00adb48c`](#insn-00adb48c) → [`00adb490`](#insn-00adb490)
- ブロック [`00adb490`](#insn-00adb490) 範囲 `[['00adb490', '00adb4af']]`

## 命令位置別の参照

- [`00adb3ac`](#insn-00adb3ac) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb3b0`](#insn-00adb3b0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb3b4`](#insn-00adb3b4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb3b8`](#insn-00adb3b8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb3bc`](#insn-00adb3bc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb3d0`](#insn-00adb3d0) → [`00adb48c`](#insn-00adb48c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb3ec`](#insn-00adb3ec) → [`00adb3fc`](#insn-00adb3fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb3f8`](#insn-00adb3f8) → [`00adb490`](#insn-00adb490) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb430`](#insn-00adb430) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00adb44c`](#insn-00adb44c) → [`00adb3f0`](#insn-00adb3f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb45c`](#insn-00adb45c) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00adb478`](#insn-00adb478) → [`00adb490`](#insn-00adb490) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb484`](#insn-00adb484) → [`00adb3fc`](#insn-00adb3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb488`](#insn-00adb488) → [`00adb490`](#insn-00adb490) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb498`](#insn-00adb498) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb49c`](#insn-00adb49c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb4a0`](#insn-00adb4a0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb4a4`](#insn-00adb4a4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb4a8`](#insn-00adb4a8) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adb3ac`](#insn-00adb3ac)

~~~json
{
  "source": "00adb3ac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb3b0`](#insn-00adb3b0)

~~~json
{
  "source": "00adb3b0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb3b4`](#insn-00adb3b4)

~~~json
{
  "source": "00adb3b4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb3b8`](#insn-00adb3b8)

~~~json
{
  "source": "00adb3b8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb3bc`](#insn-00adb3bc)

~~~json
{
  "source": "00adb3bc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb3d0`](#insn-00adb3d0)

~~~json
{
  "source": "00adb3d0",
  "target": "00adb48c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb3ec`](#insn-00adb3ec)

~~~json
{
  "source": "00adb3ec",
  "target": "00adb3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb3f8`](#insn-00adb3f8)

~~~json
{
  "source": "00adb3f8",
  "target": "00adb490",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb430`](#insn-00adb430)

~~~json
{
  "source": "00adb430",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adb44c`](#insn-00adb44c)

~~~json
{
  "source": "00adb44c",
  "target": "00adb3f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb45c`](#insn-00adb45c)

~~~json
{
  "source": "00adb45c",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adb478`](#insn-00adb478)

~~~json
{
  "source": "00adb478",
  "target": "00adb490",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb484`](#insn-00adb484)

~~~json
{
  "source": "00adb484",
  "target": "00adb3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb488`](#insn-00adb488)

~~~json
{
  "source": "00adb488",
  "target": "00adb490",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb498`](#insn-00adb498)

~~~json
{
  "source": "00adb498",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb49c`](#insn-00adb49c)

~~~json
{
  "source": "00adb49c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb4a0`](#insn-00adb4a0)

~~~json
{
  "source": "00adb4a0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb4a4`](#insn-00adb4a4)

~~~json
{
  "source": "00adb4a4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb4a8`](#insn-00adb4a8)

~~~json
{
  "source": "00adb4a8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
