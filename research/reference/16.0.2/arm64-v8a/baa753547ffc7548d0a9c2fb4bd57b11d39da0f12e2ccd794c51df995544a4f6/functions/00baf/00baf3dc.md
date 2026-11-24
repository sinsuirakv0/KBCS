# 00baf3dc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baf340`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf340.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-d58568f37efaaeca73766e8abdbbedc3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bb03d0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb03d0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-f67336d8f7e665523661e6d03f0eeea8)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baf3dc",
  "name": "_ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEjT0_SA_SA_SA_T_",
  "size": 388,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bee6be015250dbfdd050822998bedf2ad463ad1ef9811b6962e738382f57db35",
  "source_text_sha256": "bee6be015250dbfdd050822998bedf2ad463ad1ef9811b6962e738382f57db35",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baf3dc",
        "00baf55f"
      ]
    ],
    "bytes_sha256": "a8123fe1939ec277603a7d85c6107fa95548ddf8f8a1c9b7e10586b6cba9cbca",
    "instruction_count": 97,
    "instruction_bytes": 388,
    "body_bytes": 388,
    "indirect": 7,
    "unresolved": 7
  }
}
~~~

## 呼び出し元

- [00c5d180](../00c5d/00c5d180.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1781 bytes

~~~c

int _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEjT0_SA_SA_SA_T_
              (undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
              undefined8 *param_5)

{
  ulong uVar1;
  ulong uVar2;
  undefined8 uVar3;
  int iVar4;
  
  uVar1 = (*(code *)*param_5)(*param_2,*param_1);
  uVar2 = (*(code *)*param_5)(*param_3,*param_2);
  if ((uVar1 & 1) == 0) {
    if ((uVar2 & 1) == 0) {
      iVar4 = 0;
      goto LAB_00baf4c8;
    }
    uVar3 = *param_2;
    *param_2 = *param_3;
    *param_3 = uVar3;
    uVar1 = (*(code *)*param_5)(*param_2,*param_1);
    if ((uVar1 & 1) == 0) goto LAB_00baf4bc;
    uVar3 = *param_1;
    *param_1 = *param_2;
    *param_2 = uVar3;
  }
  else {
    uVar3 = *param_1;
    if ((uVar2 & 1) != 0) {
      iVar4 = 1;
      *param_1 = *param_3;
      *param_3 = uVar3;
      goto LAB_00baf4c8;
    }
    *param_1 = *param_2;
    *param_2 = uVar3;
    uVar1 = (*(code *)*param_5)(*param_3);
    if ((uVar1 & 1) == 0) {
LAB_00baf4bc:
      iVar4 = 1;
      goto LAB_00baf4c8;
    }
    uVar3 = *param_2;
    *param_2 = *param_3;
    *param_3 = uVar3;
  }
  iVar4 = 2;
LAB_00baf4c8:
  uVar1 = (*(code *)*param_5)(*param_4,*param_3);
  if ((uVar1 & 1) != 0) {
    uVar3 = *param_3;
    *param_3 = *param_4;
    *param_4 = uVar3;
    uVar1 = (*(code *)*param_5)(*param_3,*param_2);
    if ((uVar1 & 1) == 0) {
      iVar4 = iVar4 + 1;
    }
    else {
      uVar3 = *param_2;
      *param_2 = *param_3;
      *param_3 = uVar3;
      uVar1 = (*(code *)*param_5)(*param_2,*param_1);
      if ((uVar1 & 1) == 0) {
        iVar4 = iVar4 + 2;
      }
      else {
        uVar3 = *param_1;
        iVar4 = iVar4 + 3;
        *param_1 = *param_2;
        *param_2 = uVar3;
      }
    }
  }
  return iVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baf3dc"></a> `00baf3dc` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00baf3e0"></a> `00baf3e0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baf3e4"></a> `00baf3e4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baf3e8"></a> `00baf3e8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baf3ec"></a> `00baf3ec` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baf3f0"></a> `00baf3f0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00baf3f4"></a> `00baf3f4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baf3f8"></a> `00baf3f8` | `88 00 40 f9` | ldr x8,[x4] | `FALL_THROUGH`
<a id="insn-00baf3fc"></a> `00baf3fc` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-00baf400"></a> `00baf400` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00baf404"></a> `00baf404` | `f5 03 04 aa` | mov x21,x4 | `FALL_THROUGH`
<a id="insn-00baf408"></a> `00baf408` | `f7 03 03 aa` | mov x23,x3 | `FALL_THROUGH`
<a id="insn-00baf40c"></a> `00baf40c` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00baf410"></a> `00baf410` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf414"></a> `00baf414` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00baf418"></a> `00baf418` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00baf41c"></a> `00baf41c` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00baf420"></a> `00baf420` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-00baf424"></a> `00baf424` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00baf428"></a> `00baf428` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00baf42c"></a> `00baf42c` | `18 01 00 36` | tbz w24,#0x0,0x00baf44c | `CONDITIONAL_JUMP`
<a id="insn-00baf430"></a> `00baf430` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00baf434"></a> `00baf434` | `a0 02 00 36` | tbz w0,#0x0,0x00baf488 | `CONDITIONAL_JUMP`
<a id="insn-00baf438"></a> `00baf438` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00baf43c"></a> `00baf43c` | `38 00 80 52` | mov w24,#0x1 | `FALL_THROUGH`
<a id="insn-00baf440"></a> `00baf440` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00baf444"></a> `00baf444` | `c1 02 00 f9` | str x1,[x22] | `FALL_THROUGH`
<a id="insn-00baf448"></a> `00baf448` | `20 00 00 14` | b 0x00baf4c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf44c"></a> `00baf44c` | `c0 03 00 36` | tbz w0,#0x0,0x00baf4c4 | `CONDITIONAL_JUMP`
<a id="insn-00baf450"></a> `00baf450` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00baf454"></a> `00baf454` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00baf458"></a> `00baf458` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00baf45c"></a> `00baf45c` | `c9 02 00 f9` | str x9,[x22] | `FALL_THROUGH`
<a id="insn-00baf460"></a> `00baf460` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf464"></a> `00baf464` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00baf468"></a> `00baf468` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00baf46c"></a> `00baf46c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf470"></a> `00baf470` | `60 02 00 36` | tbz w0,#0x0,0x00baf4bc | `CONDITIONAL_JUMP`
<a id="insn-00baf474"></a> `00baf474` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00baf478"></a> `00baf478` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00baf47c"></a> `00baf47c` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00baf480"></a> `00baf480` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00baf484"></a> `00baf484` | `0c 00 00 14` | b 0x00baf4b4 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf488"></a> `00baf488` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00baf48c"></a> `00baf48c` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00baf490"></a> `00baf490` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00baf494"></a> `00baf494` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf498"></a> `00baf498` | `c0 02 40 f9` | ldr x0,[x22] | `FALL_THROUGH`
<a id="insn-00baf49c"></a> `00baf49c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf4a0"></a> `00baf4a0` | `e0 00 00 36` | tbz w0,#0x0,0x00baf4bc | `CONDITIONAL_JUMP`
<a id="insn-00baf4a4"></a> `00baf4a4` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00baf4a8"></a> `00baf4a8` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00baf4ac"></a> `00baf4ac` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00baf4b0"></a> `00baf4b0` | `c9 02 00 f9` | str x9,[x22] | `FALL_THROUGH`
<a id="insn-00baf4b4"></a> `00baf4b4` | `58 00 80 52` | mov w24,#0x2 | `FALL_THROUGH`
<a id="insn-00baf4b8"></a> `00baf4b8` | `04 00 00 14` | b 0x00baf4c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf4bc"></a> `00baf4bc` | `38 00 80 52` | mov w24,#0x1 | `FALL_THROUGH`
<a id="insn-00baf4c0"></a> `00baf4c0` | `02 00 00 14` | b 0x00baf4c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf4c4"></a> `00baf4c4` | `f8 03 1f 2a` | mov w24,wzr | `FALL_THROUGH`
<a id="insn-00baf4c8"></a> `00baf4c8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf4cc"></a> `00baf4cc` | `e0 02 40 f9` | ldr x0,[x23] | `FALL_THROUGH`
<a id="insn-00baf4d0"></a> `00baf4d0` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00baf4d4"></a> `00baf4d4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf4d8"></a> `00baf4d8` | `80 03 00 36` | tbz w0,#0x0,0x00baf548 | `CONDITIONAL_JUMP`
<a id="insn-00baf4dc"></a> `00baf4dc` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00baf4e0"></a> `00baf4e0` | `c9 02 40 f9` | ldr x9,[x22] | `FALL_THROUGH`
<a id="insn-00baf4e4"></a> `00baf4e4` | `c8 02 00 f9` | str x8,[x22] | `FALL_THROUGH`
<a id="insn-00baf4e8"></a> `00baf4e8` | `e9 02 00 f9` | str x9,[x23] | `FALL_THROUGH`
<a id="insn-00baf4ec"></a> `00baf4ec` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf4f0"></a> `00baf4f0` | `c0 02 40 f9` | ldr x0,[x22] | `FALL_THROUGH`
<a id="insn-00baf4f4"></a> `00baf4f4` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00baf4f8"></a> `00baf4f8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf4fc"></a> `00baf4fc` | `00 02 00 36` | tbz w0,#0x0,0x00baf53c | `CONDITIONAL_JUMP`
<a id="insn-00baf500"></a> `00baf500` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00baf504"></a> `00baf504` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00baf508"></a> `00baf508` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00baf50c"></a> `00baf50c` | `c9 02 00 f9` | str x9,[x22] | `FALL_THROUGH`
<a id="insn-00baf510"></a> `00baf510` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf514"></a> `00baf514` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00baf518"></a> `00baf518` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00baf51c"></a> `00baf51c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf520"></a> `00baf520` | `20 01 00 36` | tbz w0,#0x0,0x00baf544 | `CONDITIONAL_JUMP`
<a id="insn-00baf524"></a> `00baf524` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00baf528"></a> `00baf528` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00baf52c"></a> `00baf52c` | `18 0f 00 11` | add w24,w24,#0x3 | `FALL_THROUGH`
<a id="insn-00baf530"></a> `00baf530` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00baf534"></a> `00baf534` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00baf538"></a> `00baf538` | `04 00 00 14` | b 0x00baf548 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf53c"></a> `00baf53c` | `18 07 00 11` | add w24,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00baf540"></a> `00baf540` | `02 00 00 14` | b 0x00baf548 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf544"></a> `00baf544` | `18 0b 00 11` | add w24,w24,#0x2 | `FALL_THROUGH`
<a id="insn-00baf548"></a> `00baf548` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baf54c"></a> `00baf54c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baf550"></a> `00baf550` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baf554"></a> `00baf554` | `e0 03 18 2a` | mov w0,w24 | `FALL_THROUGH`
<a id="insn-00baf558"></a> `00baf558` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00baf55c"></a> `00baf55c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baf3dc`](#insn-00baf3dc) 範囲 `[['00baf3dc', '00baf42f']]`
  - `CONDITIONAL_JUMP` [`00baf42c`](#insn-00baf42c) → [`00baf44c`](#insn-00baf44c)
  - `FALL_THROUGH` [`00baf42c`](#insn-00baf42c) → [`00baf430`](#insn-00baf430)
- ブロック [`00baf430`](#insn-00baf430) 範囲 `[['00baf430', '00baf437']]`
  - `CONDITIONAL_JUMP` [`00baf434`](#insn-00baf434) → [`00baf488`](#insn-00baf488)
  - `FALL_THROUGH` [`00baf434`](#insn-00baf434) → [`00baf438`](#insn-00baf438)
- ブロック [`00baf438`](#insn-00baf438) 範囲 `[['00baf438', '00baf44b']]`
  - `UNCONDITIONAL_JUMP` [`00baf448`](#insn-00baf448) → [`00baf4c8`](#insn-00baf4c8)
- ブロック [`00baf44c`](#insn-00baf44c) 範囲 `[['00baf44c', '00baf44f']]`
  - `CONDITIONAL_JUMP` [`00baf44c`](#insn-00baf44c) → [`00baf4c4`](#insn-00baf4c4)
  - `FALL_THROUGH` [`00baf44c`](#insn-00baf44c) → [`00baf450`](#insn-00baf450)
- ブロック [`00baf450`](#insn-00baf450) 範囲 `[['00baf450', '00baf473']]`
  - `CONDITIONAL_JUMP` [`00baf470`](#insn-00baf470) → [`00baf4bc`](#insn-00baf4bc)
  - `FALL_THROUGH` [`00baf470`](#insn-00baf470) → [`00baf474`](#insn-00baf474)
- ブロック [`00baf474`](#insn-00baf474) 範囲 `[['00baf474', '00baf487']]`
  - `UNCONDITIONAL_JUMP` [`00baf484`](#insn-00baf484) → [`00baf4b4`](#insn-00baf4b4)
- ブロック [`00baf488`](#insn-00baf488) 範囲 `[['00baf488', '00baf4a3']]`
  - `CONDITIONAL_JUMP` [`00baf4a0`](#insn-00baf4a0) → [`00baf4bc`](#insn-00baf4bc)
  - `FALL_THROUGH` [`00baf4a0`](#insn-00baf4a0) → [`00baf4a4`](#insn-00baf4a4)
- ブロック [`00baf4a4`](#insn-00baf4a4) 範囲 `[['00baf4a4', '00baf4b3']]`
  - `FALL_THROUGH` [`00baf4b0`](#insn-00baf4b0) → [`00baf4b4`](#insn-00baf4b4)
- ブロック [`00baf4b4`](#insn-00baf4b4) 範囲 `[['00baf4b4', '00baf4bb']]`
  - `UNCONDITIONAL_JUMP` [`00baf4b8`](#insn-00baf4b8) → [`00baf4c8`](#insn-00baf4c8)
- ブロック [`00baf4bc`](#insn-00baf4bc) 範囲 `[['00baf4bc', '00baf4c3']]`
  - `UNCONDITIONAL_JUMP` [`00baf4c0`](#insn-00baf4c0) → [`00baf4c8`](#insn-00baf4c8)
- ブロック [`00baf4c4`](#insn-00baf4c4) 範囲 `[['00baf4c4', '00baf4c7']]`
  - `FALL_THROUGH` [`00baf4c4`](#insn-00baf4c4) → [`00baf4c8`](#insn-00baf4c8)
- ブロック [`00baf4c8`](#insn-00baf4c8) 範囲 `[['00baf4c8', '00baf4db']]`
  - `CONDITIONAL_JUMP` [`00baf4d8`](#insn-00baf4d8) → [`00baf548`](#insn-00baf548)
  - `FALL_THROUGH` [`00baf4d8`](#insn-00baf4d8) → [`00baf4dc`](#insn-00baf4dc)
- ブロック [`00baf4dc`](#insn-00baf4dc) 範囲 `[['00baf4dc', '00baf4ff']]`
  - `CONDITIONAL_JUMP` [`00baf4fc`](#insn-00baf4fc) → [`00baf53c`](#insn-00baf53c)
  - `FALL_THROUGH` [`00baf4fc`](#insn-00baf4fc) → [`00baf500`](#insn-00baf500)
- ブロック [`00baf500`](#insn-00baf500) 範囲 `[['00baf500', '00baf523']]`
  - `CONDITIONAL_JUMP` [`00baf520`](#insn-00baf520) → [`00baf544`](#insn-00baf544)
  - `FALL_THROUGH` [`00baf520`](#insn-00baf520) → [`00baf524`](#insn-00baf524)
- ブロック [`00baf524`](#insn-00baf524) 範囲 `[['00baf524', '00baf53b']]`
  - `UNCONDITIONAL_JUMP` [`00baf538`](#insn-00baf538) → [`00baf548`](#insn-00baf548)
- ブロック [`00baf53c`](#insn-00baf53c) 範囲 `[['00baf53c', '00baf543']]`
  - `UNCONDITIONAL_JUMP` [`00baf540`](#insn-00baf540) → [`00baf548`](#insn-00baf548)
- ブロック [`00baf544`](#insn-00baf544) 範囲 `[['00baf544', '00baf547']]`
  - `FALL_THROUGH` [`00baf544`](#insn-00baf544) → [`00baf548`](#insn-00baf548)
- ブロック [`00baf548`](#insn-00baf548) 範囲 `[['00baf548', '00baf55f']]`

## 命令位置別の参照

- [`00baf3dc`](#insn-00baf3dc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf3e0`](#insn-00baf3e0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf3e4`](#insn-00baf3e4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf3e8`](#insn-00baf3e8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf42c`](#insn-00baf42c) → [`00baf44c`](#insn-00baf44c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf434`](#insn-00baf434) → [`00baf488`](#insn-00baf488) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf448`](#insn-00baf448) → [`00baf4c8`](#insn-00baf4c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf44c`](#insn-00baf44c) → [`00baf4c4`](#insn-00baf4c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf470`](#insn-00baf470) → [`00baf4bc`](#insn-00baf4bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf484`](#insn-00baf484) → [`00baf4b4`](#insn-00baf4b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf4a0`](#insn-00baf4a0) → [`00baf4bc`](#insn-00baf4bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf4b8`](#insn-00baf4b8) → [`00baf4c8`](#insn-00baf4c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf4c0`](#insn-00baf4c0) → [`00baf4c8`](#insn-00baf4c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf4d8`](#insn-00baf4d8) → [`00baf548`](#insn-00baf548) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf4fc`](#insn-00baf4fc) → [`00baf53c`](#insn-00baf53c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf520`](#insn-00baf520) → [`00baf544`](#insn-00baf544) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf538`](#insn-00baf538) → [`00baf548`](#insn-00baf548) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf540`](#insn-00baf540) → [`00baf548`](#insn-00baf548) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf548`](#insn-00baf548) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf54c`](#insn-00baf54c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf550`](#insn-00baf550) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baf3dc`](#insn-00baf3dc)

~~~json
{
  "source": "00baf3dc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf3e0`](#insn-00baf3e0)

~~~json
{
  "source": "00baf3e0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf3e4`](#insn-00baf3e4)

~~~json
{
  "source": "00baf3e4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf3e8`](#insn-00baf3e8)

~~~json
{
  "source": "00baf3e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf42c`](#insn-00baf42c)

~~~json
{
  "source": "00baf42c",
  "target": "00baf44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf434`](#insn-00baf434)

~~~json
{
  "source": "00baf434",
  "target": "00baf488",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf448`](#insn-00baf448)

~~~json
{
  "source": "00baf448",
  "target": "00baf4c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf44c`](#insn-00baf44c)

~~~json
{
  "source": "00baf44c",
  "target": "00baf4c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf470`](#insn-00baf470)

~~~json
{
  "source": "00baf470",
  "target": "00baf4bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf484`](#insn-00baf484)

~~~json
{
  "source": "00baf484",
  "target": "00baf4b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf4a0`](#insn-00baf4a0)

~~~json
{
  "source": "00baf4a0",
  "target": "00baf4bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf4b8`](#insn-00baf4b8)

~~~json
{
  "source": "00baf4b8",
  "target": "00baf4c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf4c0`](#insn-00baf4c0)

~~~json
{
  "source": "00baf4c0",
  "target": "00baf4c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf4d8`](#insn-00baf4d8)

~~~json
{
  "source": "00baf4d8",
  "target": "00baf548",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf4fc`](#insn-00baf4fc)

~~~json
{
  "source": "00baf4fc",
  "target": "00baf53c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf520`](#insn-00baf520)

~~~json
{
  "source": "00baf520",
  "target": "00baf544",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf538`](#insn-00baf538)

~~~json
{
  "source": "00baf538",
  "target": "00baf548",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf540`](#insn-00baf540)

~~~json
{
  "source": "00baf540",
  "target": "00baf548",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf548`](#insn-00baf548)

~~~json
{
  "source": "00baf548",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf54c`](#insn-00baf54c)

~~~json
{
  "source": "00baf54c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf550`](#insn-00baf550)

~~~json
{
  "source": "00baf550",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
