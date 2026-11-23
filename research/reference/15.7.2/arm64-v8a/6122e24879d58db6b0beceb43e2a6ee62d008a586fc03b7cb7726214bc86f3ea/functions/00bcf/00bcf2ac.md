# 00bcf2ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcf374`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf374.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-9cefd09cea009e553ffdf36913d96681)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcf2ac",
  "name": "FUN_00bcf2ac",
  "size": 272,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b3ba88e081626942a4f3a466bc945d5d60bac6162b08a9ac9bffcf378b7f0919",
  "source_text_sha256": "b3ba88e081626942a4f3a466bc945d5d60bac6162b08a9ac9bffcf378b7f0919",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcf2ac",
        "00bcf3bb"
      ]
    ],
    "bytes_sha256": "dbbdaa7f96dfd4f9599e9065bb7eb2a895c812c18532743d0eb1a893fe33bbad",
    "instruction_count": 68,
    "instruction_bytes": 272,
    "body_bytes": 272,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bc20b8](../00bc2/00bc20b8.md)
- [00bc2394](../00bc2/00bc2394.md)

## 呼び出し先

- [00bcf8c4](../00bcf/00bcf8c4.md)
- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2324 bytes

~~~c

undefined8 * FUN_00bcf2ac(long *param_1,undefined8 *param_2)

{
  ushort uVar1;
  undefined8 *puVar2;
  char *pcVar3;
  long lVar4;
  undefined8 *puVar5;
  void *pvVar6;
  undefined1 auVar7 [16];
  
                    /* catch() { ... } // from try @ 00bce6f8 with catch @ 00bcf2c0 */
  pcVar3 = (char *)*param_1;
  puVar5 = param_2;
  if (pcVar3 != (char *)param_1[1]) {
    do {
      if (*pcVar3 != 'B') {
        return puVar5;
      }
      *param_1 = (long)(pcVar3 + 1);
      auVar7 = FUN_00bcf8c4(param_1);
      if (auVar7._8_8_ == 0) {
        return (undefined8 *)0x0;
      }
      pvVar6 = (void *)param_1[0x266];
      lVar4 = *(long *)((long)pvVar6 + 8);
      puVar2 = pvVar6;
      if (lVar4 - 0xfc0U < 0xfffffffffffff010) {
        puVar2 = malloc(0x1000);
        if (puVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
          _ZSt9terminatev();
        }
        lVar4 = 0;
        *puVar2 = pvVar6;
        puVar2[1] = 0;
        param_1[0x266] = (long)puVar2;
      }
      *(long *)((long)puVar2 + 8) = lVar4 + 0x30;
                    /* catch() { ... } // from try @ 00bce930 with catch @ 00bcf2f8 */
      uVar1 = *(ushort *)((long)puVar5 + 9);
                    /* catch() { ... } // from try @ 00bced48 with catch @ 00bcf2fc */
      param_2 = (undefined8 *)((long)puVar2 + lVar4 + 0x10);
      *param_2 = &PTR_FUN_00c192a8;
                    /* catch() { ... } // from try @ 00bcea18 with catch @ 00bcf300 */
                    /* catch() { ... } // from try @ 00bce678 with catch @ 00bcf304 */
      *(long *)((long)puVar2 + lVar4 + 0x28) = auVar7._0_8_;
      *(undefined8 **)((long)puVar2 + lVar4 + 0x20) = puVar5;
                    /* catch() { ... } // from try @ 00bce9a0 with catch @ 00bcf318 */
      *(undefined1 *)((long)puVar2 + lVar4 + 0x18) = 9;
                    /* catch() { ... } // from try @ 00bce590 with catch @ 00bcf31c */
                    /* catch() { ... } // from try @ 00bce888 with catch @ 00bcf320 */
      *(long *)((long)puVar2 + lVar4 + 0x30) = auVar7._8_8_;
      *(ushort *)((long)puVar2 + lVar4 + 0x19) =
           *(ushort *)((long)puVar2 + lVar4 + 0x19) & 0xf000 | uVar1 & 0xfc0;
      pcVar3 = (char *)*param_1;
      puVar5 = param_2;
    } while (pcVar3 != (char *)param_1[1]);
  }
  return param_2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcf2ac"></a> `00bcf2ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcf2b0"></a> `00bcf2b0` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bcf2b4"></a> `00bcf2b4` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf2b8"></a> `00bcf2b8` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcf2bc"></a> `00bcf2bc` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcf2c0"></a> `00bcf2c0` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcf2c4"></a> `00bcf2c4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcf2c8"></a> `00bcf2c8` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bcf2cc"></a> `00bcf2cc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bcf2d0"></a> `00bcf2d0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcf2d4"></a> `00bcf2d4` | `e0 05 00 54` | b.eq 0x00bcf390 | `CONDITIONAL_JUMP`
<a id="insn-00bcf2d8"></a> `00bcf2d8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcf2dc"></a> `00bcf2dc` | `57 02 00 d0` | adrp x23,0xc19000 | `FALL_THROUGH`
<a id="insn-00bcf2e0"></a> `00bcf2e0` | `f7 a2 0a 91` | add x23,x23,#0x2a8 | `FALL_THROUGH`
<a id="insn-00bcf2e4"></a> `00bcf2e4` | `38 01 80 52` | mov w24,#0x9 | `FALL_THROUGH`
<a id="insn-00bcf2e8"></a> `00bcf2e8` | `13 00 00 14` | b 0x00bcf334 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf2ec"></a> `00bcf2ec` | `09 c1 00 91` | add x9,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00bcf2f0"></a> `00bcf2f0` | `20 03 08 8b` | add x0,x25,x8 | `FALL_THROUGH`
<a id="insn-00bcf2f4"></a> `00bcf2f4` | `29 07 00 f9` | str x9,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf2f8"></a> `00bcf2f8` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bcf2fc"></a> `00bcf2fc` | `17 0c 01 f8` | str x23,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcf300"></a> `00bcf300` | `09 90 40 78` | ldurh w9,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcf304"></a> `00bcf304` | `16 0c 00 f9` | str x22,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bcf308"></a> `00bcf308` | `08 15 1a 12` | and w8,w8,#0xfc0 | `FALL_THROUGH`
<a id="insn-00bcf30c"></a> `00bcf30c` | `14 08 00 f9` | str x20,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf310"></a> `00bcf310` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcf314"></a> `00bcf314` | `29 0d 14 12` | and w9,w9,#0xf000 | `FALL_THROUGH`
<a id="insn-00bcf318"></a> `00bcf318` | `18 20 00 39` | strb w24,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf31c"></a> `00bcf31c` | `28 01 08 2a` | orr w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00bcf320"></a> `00bcf320` | `15 10 00 f9` | str x21,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bcf324"></a> `00bcf324` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcf328"></a> `00bcf328` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bcf32c"></a> `00bcf32c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcf330"></a> `00bcf330` | `60 03 00 54` | b.eq 0x00bcf39c | `CONDITIONAL_JUMP`
<a id="insn-00bcf334"></a> `00bcf334` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bcf338"></a> `00bcf338` | `3f 09 01 71` | cmp w9,#0x42 | `FALL_THROUGH`
<a id="insn-00bcf33c"></a> `00bcf33c` | `a1 02 00 54` | b.ne 0x00bcf390 | `CONDITIONAL_JUMP`
<a id="insn-00bcf340"></a> `00bcf340` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcf344"></a> `00bcf344` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf348"></a> `00bcf348` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcf34c"></a> `00bcf34c` | `5e 01 00 94` | bl 0x00bcf8c4 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf350"></a> `00bcf350` | `41 02 00 b4` | cbz x1,0x00bcf398 | `CONDITIONAL_JUMP`
<a id="insn-00bcf354"></a> `00bcf354` | `79 9a 49 f9` | ldr x25,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcf358"></a> `00bcf358` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bcf35c"></a> `00bcf35c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcf360"></a> `00bcf360` | `28 07 40 f9` | ldr x8,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf364"></a> `00bcf364` | `09 01 3f d1` | sub x9,x8,#0xfc0 | `FALL_THROUGH`
<a id="insn-00bcf368"></a> `00bcf368` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bcf36c"></a> `00bcf36c` | `08 fc ff 54` | b.hi 0x00bcf2ec | `CONDITIONAL_JUMP`
<a id="insn-00bcf370"></a> `00bcf370` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bcf374"></a> `00bcf374` | `57 37 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf378"></a> `00bcf378` | `00 02 00 b4` | cbz x0,0x00bcf3b8 | `CONDITIONAL_JUMP`
<a id="insn-00bcf37c"></a> `00bcf37c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bcf380"></a> `00bcf380` | `19 7c 00 a9` | stp x25,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcf384"></a> `00bcf384` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bcf388"></a> `00bcf388` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcf38c"></a> `00bcf38c` | `d8 ff ff 17` | b 0x00bcf2ec | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf390"></a> `00bcf390` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcf394"></a> `00bcf394` | `02 00 00 14` | b 0x00bcf39c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf398"></a> `00bcf398` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bcf39c"></a> `00bcf39c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcf3a0"></a> `00bcf3a0` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf3a4"></a> `00bcf3a4` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcf3a8"></a> `00bcf3a8` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcf3ac"></a> `00bcf3ac` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcf3b0"></a> `00bcf3b0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcf3b4"></a> `00bcf3b4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcf3b8"></a> `00bcf3b8` | `46 2f 00 94` | bl 0x00bdb0d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcf2ac`](#insn-00bcf2ac) 範囲 `[['00bcf2ac', '00bcf2bf']]`
  - `FALL_THROUGH` [`00bcf2bc`](#insn-00bcf2bc) → [`00bcf2c0`](#insn-00bcf2c0)
- ブロック [`00bcf2c0`](#insn-00bcf2c0) 範囲 `[['00bcf2c0', '00bcf2d7']]`
  - `CONDITIONAL_JUMP` [`00bcf2d4`](#insn-00bcf2d4) → [`00bcf390`](#insn-00bcf390)
  - `FALL_THROUGH` [`00bcf2d4`](#insn-00bcf2d4) → [`00bcf2d8`](#insn-00bcf2d8)
- ブロック [`00bcf2d8`](#insn-00bcf2d8) 範囲 `[['00bcf2d8', '00bcf2df']]`
  - `FALL_THROUGH` [`00bcf2dc`](#insn-00bcf2dc) → [`00bcf2e0`](#insn-00bcf2e0)
- ブロック [`00bcf2e0`](#insn-00bcf2e0) 範囲 `[['00bcf2e0', '00bcf2eb']]`
  - `UNCONDITIONAL_JUMP` [`00bcf2e8`](#insn-00bcf2e8) → [`00bcf334`](#insn-00bcf334)
- ブロック [`00bcf2ec`](#insn-00bcf2ec) 範囲 `[['00bcf2ec', '00bcf2f7']]`
  - `FALL_THROUGH` [`00bcf2f4`](#insn-00bcf2f4) → [`00bcf2f8`](#insn-00bcf2f8)
- ブロック [`00bcf2f8`](#insn-00bcf2f8) 範囲 `[['00bcf2f8', '00bcf2fb']]`
  - `FALL_THROUGH` [`00bcf2f8`](#insn-00bcf2f8) → [`00bcf2fc`](#insn-00bcf2fc)
- ブロック [`00bcf2fc`](#insn-00bcf2fc) 範囲 `[['00bcf2fc', '00bcf2ff']]`
  - `FALL_THROUGH` [`00bcf2fc`](#insn-00bcf2fc) → [`00bcf300`](#insn-00bcf300)
- ブロック [`00bcf300`](#insn-00bcf300) 範囲 `[['00bcf300', '00bcf303']]`
  - `FALL_THROUGH` [`00bcf300`](#insn-00bcf300) → [`00bcf304`](#insn-00bcf304)
- ブロック [`00bcf304`](#insn-00bcf304) 範囲 `[['00bcf304', '00bcf317']]`
  - `FALL_THROUGH` [`00bcf314`](#insn-00bcf314) → [`00bcf318`](#insn-00bcf318)
- ブロック [`00bcf318`](#insn-00bcf318) 範囲 `[['00bcf318', '00bcf31b']]`
  - `FALL_THROUGH` [`00bcf318`](#insn-00bcf318) → [`00bcf31c`](#insn-00bcf31c)
- ブロック [`00bcf31c`](#insn-00bcf31c) 範囲 `[['00bcf31c', '00bcf31f']]`
  - `FALL_THROUGH` [`00bcf31c`](#insn-00bcf31c) → [`00bcf320`](#insn-00bcf320)
- ブロック [`00bcf320`](#insn-00bcf320) 範囲 `[['00bcf320', '00bcf333']]`
  - `CONDITIONAL_JUMP` [`00bcf330`](#insn-00bcf330) → [`00bcf39c`](#insn-00bcf39c)
  - `FALL_THROUGH` [`00bcf330`](#insn-00bcf330) → [`00bcf334`](#insn-00bcf334)
- ブロック [`00bcf334`](#insn-00bcf334) 範囲 `[['00bcf334', '00bcf33f']]`
  - `CONDITIONAL_JUMP` [`00bcf33c`](#insn-00bcf33c) → [`00bcf390`](#insn-00bcf390)
  - `FALL_THROUGH` [`00bcf33c`](#insn-00bcf33c) → [`00bcf340`](#insn-00bcf340)
- ブロック [`00bcf340`](#insn-00bcf340) 範囲 `[['00bcf340', '00bcf353']]`
  - `CONDITIONAL_JUMP` [`00bcf350`](#insn-00bcf350) → [`00bcf398`](#insn-00bcf398)
  - `FALL_THROUGH` [`00bcf350`](#insn-00bcf350) → [`00bcf354`](#insn-00bcf354)
- ブロック [`00bcf354`](#insn-00bcf354) 範囲 `[['00bcf354', '00bcf36f']]`
  - `CONDITIONAL_JUMP` [`00bcf36c`](#insn-00bcf36c) → [`00bcf2ec`](#insn-00bcf2ec)
  - `FALL_THROUGH` [`00bcf36c`](#insn-00bcf36c) → [`00bcf370`](#insn-00bcf370)
- ブロック [`00bcf370`](#insn-00bcf370) 範囲 `[['00bcf370', '00bcf37b']]`
  - `CONDITIONAL_JUMP` [`00bcf378`](#insn-00bcf378) → [`00bcf3b8`](#insn-00bcf3b8)
  - `FALL_THROUGH` [`00bcf378`](#insn-00bcf378) → [`00bcf37c`](#insn-00bcf37c)
- ブロック [`00bcf37c`](#insn-00bcf37c) 範囲 `[['00bcf37c', '00bcf38f']]`
  - `UNCONDITIONAL_JUMP` [`00bcf38c`](#insn-00bcf38c) → [`00bcf2ec`](#insn-00bcf2ec)
- ブロック [`00bcf390`](#insn-00bcf390) 範囲 `[['00bcf390', '00bcf397']]`
  - `UNCONDITIONAL_JUMP` [`00bcf394`](#insn-00bcf394) → [`00bcf39c`](#insn-00bcf39c)
- ブロック [`00bcf398`](#insn-00bcf398) 範囲 `[['00bcf398', '00bcf39b']]`
  - `FALL_THROUGH` [`00bcf398`](#insn-00bcf398) → [`00bcf39c`](#insn-00bcf39c)
- ブロック [`00bcf39c`](#insn-00bcf39c) 範囲 `[['00bcf39c', '00bcf3b7']]`
- ブロック [`00bcf3b8`](#insn-00bcf3b8) 範囲 `[['00bcf3b8', '00bcf3bb']]`

## 命令位置別の参照

- [`00bcf2b0`](#insn-00bcf2b0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf2b4`](#insn-00bcf2b4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf2b8`](#insn-00bcf2b8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf2bc`](#insn-00bcf2bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf2c0`](#insn-00bcf2c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf2d4`](#insn-00bcf2d4) → [`00bcf390`](#insn-00bcf390) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf2e8`](#insn-00bcf2e8) → [`00bcf334`](#insn-00bcf334) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf2fc`](#insn-00bcf2fc) → `00c192a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcf330`](#insn-00bcf330) → [`00bcf39c`](#insn-00bcf39c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf33c`](#insn-00bcf33c) → [`00bcf390`](#insn-00bcf390) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf34c`](#insn-00bcf34c) → [`00bcf8c4`](00bcf8c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bcf8c4` · 推定シンボル `None` · 推定型 `None`
- [`00bcf350`](#insn-00bcf350) → [`00bcf398`](#insn-00bcf398) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf36c`](#insn-00bcf36c) → [`00bcf2ec`](#insn-00bcf2ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf374`](#insn-00bcf374) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcf378`](#insn-00bcf378) → [`00bcf3b8`](#insn-00bcf3b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf38c`](#insn-00bcf38c) → [`00bcf2ec`](#insn-00bcf2ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf394`](#insn-00bcf394) → [`00bcf39c`](#insn-00bcf39c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf39c`](#insn-00bcf39c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf3a0`](#insn-00bcf3a0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf3a4`](#insn-00bcf3a4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf3a8`](#insn-00bcf3a8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf3ac`](#insn-00bcf3ac) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf3b8`](#insn-00bcf3b8) → [`00bdb0d0`](../00bdb/00bdb0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcf2b0`](#insn-00bcf2b0)

~~~json
{
  "source": "00bcf2b0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf2b4`](#insn-00bcf2b4)

~~~json
{
  "source": "00bcf2b4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf2b8`](#insn-00bcf2b8)

~~~json
{
  "source": "00bcf2b8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf2bc`](#insn-00bcf2bc)

~~~json
{
  "source": "00bcf2bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf2c0`](#insn-00bcf2c0)

~~~json
{
  "source": "00bcf2c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf2d4`](#insn-00bcf2d4)

~~~json
{
  "source": "00bcf2d4",
  "target": "00bcf390",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf2e8`](#insn-00bcf2e8)

~~~json
{
  "source": "00bcf2e8",
  "target": "00bcf334",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf2fc`](#insn-00bcf2fc)

~~~json
{
  "source": "00bcf2fc",
  "target": "00c192a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c192a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcf330`](#insn-00bcf330)

~~~json
{
  "source": "00bcf330",
  "target": "00bcf39c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf33c`](#insn-00bcf33c)

~~~json
{
  "source": "00bcf33c",
  "target": "00bcf390",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf34c`](#insn-00bcf34c)

~~~json
{
  "source": "00bcf34c",
  "target": "00bcf8c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf350`](#insn-00bcf350)

~~~json
{
  "source": "00bcf350",
  "target": "00bcf398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf36c`](#insn-00bcf36c)

~~~json
{
  "source": "00bcf36c",
  "target": "00bcf2ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf374`](#insn-00bcf374)

~~~json
{
  "source": "00bcf374",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf378`](#insn-00bcf378)

~~~json
{
  "source": "00bcf378",
  "target": "00bcf3b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf38c`](#insn-00bcf38c)

~~~json
{
  "source": "00bcf38c",
  "target": "00bcf2ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf394`](#insn-00bcf394)

~~~json
{
  "source": "00bcf394",
  "target": "00bcf39c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf39c`](#insn-00bcf39c)

~~~json
{
  "source": "00bcf39c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf3a0`](#insn-00bcf3a0)

~~~json
{
  "source": "00bcf3a0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf3a4`](#insn-00bcf3a4)

~~~json
{
  "source": "00bcf3a4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf3a8`](#insn-00bcf3a8)

~~~json
{
  "source": "00bcf3a8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf3ac`](#insn-00bcf3ac)

~~~json
{
  "source": "00bcf3ac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf3b8`](#insn-00bcf3b8)

~~~json
{
  "source": "00bcf3b8",
  "target": "00bdb0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
