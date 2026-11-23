# 00bda6cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bda78c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda78c.md) · 移動量 `+0xc0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0080.md#compare-2d5b0c4f596256509b18e091d59a2c71)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bda6cc",
  "name": "FUN_00bda6cc",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6ddedb8f720a0af180b62e47abc9e8f248791171f59afc6422ff77f68effe923",
  "source_text_sha256": "6ddedb8f720a0af180b62e47abc9e8f248791171f59afc6422ff77f68effe923",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bda6cc",
        "00bda7eb"
      ]
    ],
    "bytes_sha256": "8de76bb5843aa3e93e702b29b49441fc7e8ebead1d0a4c548b4dc9a1a181107c",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bda59c](../00bda/00bda59c.md)
- [00bda9b4](../00bda/00bda9b4.md)

## 呼び出し先

- [00bd93b0](../00bd9/00bd93b0.md)
- [00bdd260](../00bdd/00bdd260.md)
- [00be1e80](../00be1/00be1e80.md)

## 関連文字列（未確認候補）

~~~text
"libunwind: unsupported .eh_frame_hdr at %lx: need at least 4 bytes of data but only got %zd\n"
"libunwind: unsupported .eh_frame_hdr version: %u at %lx\n"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1394 bytes

~~~c

undefined8 FUN_00bda6cc(undefined8 param_1,byte *param_2,byte *param_3,undefined8 *param_4)

{
  byte bVar1;
  byte bVar2;
  undefined *puVar3;
  undefined8 uVar4;
  byte *local_28;
  
  puVar3 = PTR___sF_00c1bc48;
  if ((ulong)((long)param_3 - (long)param_2) < 4) {
    if (param_3 == param_2) {
      return 0;
    }
    fprintf((FILE *)(PTR___sF_00c1bc48 + 0x130),
            "libunwind: unsupported .eh_frame_hdr at %lx: need at least 4 bytes of data but only got %zd\n"
            ,param_2);
  }
  else {
                    /* try { // try from 00bda720 to 00cda72f has its CatchHandler @ 00bda82c */
    if (*param_2 == 1) {
      local_28 = param_2 + 4;
                    /* try { // try from 00bda730 to 00cda86b has its CatchHandler @ 00bda6ac */
      bVar1 = param_2[2];
      bVar2 = param_2[1];
      *(byte *)(param_4 + 3) = param_2[3];
      uVar4 = FUN_00bd93b0(param_1,&local_28,param_3,bVar2,param_2);
      *param_4 = uVar4;
      if (bVar1 == 0xff) {
        uVar4 = 0;
      }
      else {
        uVar4 = FUN_00bd93b0(param_1,&local_28,param_3,bVar1,param_2);
      }
      param_4[1] = uVar4;
      param_4[2] = local_28;
      return 1;
    }
    fprintf((FILE *)(PTR___sF_00c1bc48 + 0x130),
            "libunwind: unsupported .eh_frame_hdr version: %u at %lx\n",(ulong)(uint)*param_2,
            param_2);
  }
  fflush((FILE *)(puVar3 + 0x130));
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bda6cc"></a> `00bda6cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bda6d0"></a> `00bda6d0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bda6d4"></a> `00bda6d4` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda6d8"></a> `00bda6d8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bda6dc"></a> `00bda6dc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bda6e0"></a> `00bda6e0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bda6e4"></a> `00bda6e4` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bda6e8"></a> `00bda6e8` | `43 00 01 cb` | sub x3,x2,x1 | `FALL_THROUGH`
<a id="insn-00bda6ec"></a> `00bda6ec` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bda6f0"></a> `00bda6f0` | `7f 0c 00 f1` | cmp x3,#0x3 | `FALL_THROUGH`
<a id="insn-00bda6f4"></a> `00bda6f4` | `68 01 00 54` | b.hi 0x00bda720 | `CONDITIONAL_JUMP`
<a id="insn-00bda6f8"></a> `00bda6f8` | `5f 00 13 eb` | cmp x2,x19 | `FALL_THROUGH`
<a id="insn-00bda6fc"></a> `00bda6fc` | `60 05 00 54` | b.eq 0x00bda7a8 | `CONDITIONAL_JUMP`
<a id="insn-00bda700"></a> `00bda700` | `14 02 00 b0` | adrp x20,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bda704"></a> `00bda704` | `41 b6 ff d0` | adrp x1,0x2a4000 | `FALL_THROUGH`
<a id="insn-00bda708"></a> `00bda708` | `21 00 08 91` | add x1,x1,#0x200 | `FALL_THROUGH`
<a id="insn-00bda70c"></a> `00bda70c` | `94 26 46 f9` | ldr x20,[x20, #0xc48] | `FALL_THROUGH`
<a id="insn-00bda710"></a> `00bda710` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bda714"></a> `00bda714` | `80 c2 04 91` | add x0,x20,#0x130 | `FALL_THROUGH`
<a id="insn-00bda718"></a> `00bda718` | `da 1d 00 94` | bl 0x00be1e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bda71c"></a> `00bda71c` | `21 00 00 14` | b 0x00bda7a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bda720"></a> `00bda720` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bda724"></a> `00bda724` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bda728"></a> `00bda728` | `c1 02 00 54` | b.ne 0x00bda780 | `CONDITIONAL_JUMP`
<a id="insn-00bda72c"></a> `00bda72c` | `68 12 00 91` | add x8,x19,#0x4 | `FALL_THROUGH`
<a id="insn-00bda730"></a> `00bda730` | `75 0a 40 39` | ldrb w21,[x19, #0x2] | `FALL_THROUGH`
<a id="insn-00bda734"></a> `00bda734` | `63 06 40 39` | ldrb w3,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00bda738"></a> `00bda738` | `a8 0f 00 f9` | str x8,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bda73c"></a> `00bda73c` | `a1 63 00 91` | add x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bda740"></a> `00bda740` | `e4 03 13 aa` | mov x4,x19 | `FALL_THROUGH`
<a id="insn-00bda744"></a> `00bda744` | `68 0e 40 39` | ldrb w8,[x19, #0x3] | `FALL_THROUGH`
<a id="insn-00bda748"></a> `00bda748` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bda74c"></a> `00bda74c` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00bda750"></a> `00bda750` | `88 62 00 39` | strb w8,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bda754"></a> `00bda754` | `17 fb ff 97` | bl 0x00bd93b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda758"></a> `00bda758` | `bf fe 03 71` | cmp w21,#0xff | `FALL_THROUGH`
<a id="insn-00bda75c"></a> `00bda75c` | `80 02 00 f9` | str x0,[x20] | `FALL_THROUGH`
<a id="insn-00bda760"></a> `00bda760` | `20 03 00 54` | b.eq 0x00bda7c4 | `CONDITIONAL_JUMP`
<a id="insn-00bda764"></a> `00bda764` | `a1 63 00 91` | add x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bda768"></a> `00bda768` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bda76c"></a> `00bda76c` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bda770"></a> `00bda770` | `e3 03 15 2a` | mov w3,w21 | `FALL_THROUGH`
<a id="insn-00bda774"></a> `00bda774` | `e4 03 13 aa` | mov x4,x19 | `FALL_THROUGH`
<a id="insn-00bda778"></a> `00bda778` | `0e fb ff 97` | bl 0x00bd93b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda77c"></a> `00bda77c` | `13 00 00 14` | b 0x00bda7c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bda780"></a> `00bda780` | `14 02 00 b0` | adrp x20,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bda784"></a> `00bda784` | `e1 b5 ff d0` | adrp x1,0x298000 | `FALL_THROUGH`
<a id="insn-00bda788"></a> `00bda788` | `21 28 2e 91` | add x1,x1,#0xb8a | `FALL_THROUGH`
<a id="insn-00bda78c"></a> `00bda78c` | `94 26 46 f9` | ldr x20,[x20, #0xc48] | `FALL_THROUGH`
<a id="insn-00bda790"></a> `00bda790` | `e2 03 08 2a` | mov w2,w8 | `FALL_THROUGH`
<a id="insn-00bda794"></a> `00bda794` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00bda798"></a> `00bda798` | `80 c2 04 91` | add x0,x20,#0x130 | `FALL_THROUGH`
<a id="insn-00bda79c"></a> `00bda79c` | `b9 1d 00 94` | bl 0x00be1e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bda7a0"></a> `00bda7a0` | `80 c2 04 91` | add x0,x20,#0x130 | `FALL_THROUGH`
<a id="insn-00bda7a4"></a> `00bda7a4` | `af 0a 00 94` | bl 0x00bdd260 | `UNCONDITIONAL_CALL`
<a id="insn-00bda7a8"></a> `00bda7a8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bda7ac"></a> `00bda7ac` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bda7b0"></a> `00bda7b0` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda7b4"></a> `00bda7b4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bda7b8"></a> `00bda7b8` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bda7bc"></a> `00bda7bc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bda7c0"></a> `00bda7c0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bda7c4"></a> `00bda7c4` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bda7c8"></a> `00bda7c8` | `a8 0f 40 f9` | ldr x8,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bda7cc"></a> `00bda7cc` | `80 a2 00 a9` | stp x0,x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bda7d0"></a> `00bda7d0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bda7d4"></a> `00bda7d4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bda7d8"></a> `00bda7d8` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda7dc"></a> `00bda7dc` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bda7e0"></a> `00bda7e0` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bda7e4"></a> `00bda7e4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bda7e8"></a> `00bda7e8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bda6cc`](#insn-00bda6cc) 範囲 `[['00bda6cc', '00bda6f7']]`
  - `CONDITIONAL_JUMP` [`00bda6f4`](#insn-00bda6f4) → [`00bda720`](#insn-00bda720)
  - `FALL_THROUGH` [`00bda6f4`](#insn-00bda6f4) → [`00bda6f8`](#insn-00bda6f8)
- ブロック [`00bda6f8`](#insn-00bda6f8) 範囲 `[['00bda6f8', '00bda6ff']]`
  - `CONDITIONAL_JUMP` [`00bda6fc`](#insn-00bda6fc) → [`00bda7a8`](#insn-00bda7a8)
  - `FALL_THROUGH` [`00bda6fc`](#insn-00bda6fc) → [`00bda700`](#insn-00bda700)
- ブロック [`00bda700`](#insn-00bda700) 範囲 `[['00bda700', '00bda71f']]`
  - `UNCONDITIONAL_JUMP` [`00bda71c`](#insn-00bda71c) → [`00bda7a0`](#insn-00bda7a0)
- ブロック [`00bda720`](#insn-00bda720) 範囲 `[['00bda720', '00bda72b']]`
  - `CONDITIONAL_JUMP` [`00bda728`](#insn-00bda728) → [`00bda780`](#insn-00bda780)
  - `FALL_THROUGH` [`00bda728`](#insn-00bda728) → [`00bda72c`](#insn-00bda72c)
- ブロック [`00bda72c`](#insn-00bda72c) 範囲 `[['00bda72c', '00bda72f']]`
  - `FALL_THROUGH` [`00bda72c`](#insn-00bda72c) → [`00bda730`](#insn-00bda730)
- ブロック [`00bda730`](#insn-00bda730) 範囲 `[['00bda730', '00bda763']]`
  - `CONDITIONAL_JUMP` [`00bda760`](#insn-00bda760) → [`00bda7c4`](#insn-00bda7c4)
  - `FALL_THROUGH` [`00bda760`](#insn-00bda760) → [`00bda764`](#insn-00bda764)
- ブロック [`00bda764`](#insn-00bda764) 範囲 `[['00bda764', '00bda77f']]`
  - `UNCONDITIONAL_JUMP` [`00bda77c`](#insn-00bda77c) → [`00bda7c8`](#insn-00bda7c8)
- ブロック [`00bda780`](#insn-00bda780) 範囲 `[['00bda780', '00bda79f']]`
  - `FALL_THROUGH` [`00bda79c`](#insn-00bda79c) → [`00bda7a0`](#insn-00bda7a0)
- ブロック [`00bda7a0`](#insn-00bda7a0) 範囲 `[['00bda7a0', '00bda7a7']]`
  - `FALL_THROUGH` [`00bda7a4`](#insn-00bda7a4) → [`00bda7a8`](#insn-00bda7a8)
- ブロック [`00bda7a8`](#insn-00bda7a8) 範囲 `[['00bda7a8', '00bda7c3']]`
- ブロック [`00bda7c4`](#insn-00bda7c4) 範囲 `[['00bda7c4', '00bda7c7']]`
  - `FALL_THROUGH` [`00bda7c4`](#insn-00bda7c4) → [`00bda7c8`](#insn-00bda7c8)
- ブロック [`00bda7c8`](#insn-00bda7c8) 範囲 `[['00bda7c8', '00bda7eb']]`

## 命令位置別の参照

- [`00bda6d0`](#insn-00bda6d0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda6d4`](#insn-00bda6d4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda6d8`](#insn-00bda6d8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda6dc`](#insn-00bda6dc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda6f4`](#insn-00bda6f4) → [`00bda720`](#insn-00bda720) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda6fc`](#insn-00bda6fc) → [`00bda7a8`](#insn-00bda7a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda708`](#insn-00bda708) → `002a4200`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bda70c`](#insn-00bda70c) → `00c1bc48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bda714`](#insn-00bda714) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bda718`](#insn-00bda718) → [`00be1e80`](../00be1/00be1e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1e80` · 推定シンボル `None` · 推定型 `None`
- [`00bda71c`](#insn-00bda71c) → [`00bda7a0`](#insn-00bda7a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda728`](#insn-00bda728) → [`00bda780`](#insn-00bda780) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda738`](#insn-00bda738) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda754`](#insn-00bda754) → [`00bd93b0`](../00bd9/00bd93b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd93b0` · 推定シンボル `None` · 推定型 `None`
- [`00bda760`](#insn-00bda760) → [`00bda7c4`](#insn-00bda7c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda778`](#insn-00bda778) → [`00bd93b0`](../00bd9/00bd93b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd93b0` · 推定シンボル `None` · 推定型 `None`
- [`00bda77c`](#insn-00bda77c) → [`00bda7c8`](#insn-00bda7c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda788`](#insn-00bda788) → `00298b8a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bda78c`](#insn-00bda78c) → `00c1bc48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bda798`](#insn-00bda798) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bda79c`](#insn-00bda79c) → [`00be1e80`](../00be1/00be1e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1e80` · 推定シンボル `None` · 推定型 `None`
- [`00bda7a0`](#insn-00bda7a0) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bda7a4`](#insn-00bda7a4) → [`00bdd260`](../00bdd/00bdd260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd260` · 推定シンボル `None` · 推定型 `None`
- [`00bda7ac`](#insn-00bda7ac) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7b0`](#insn-00bda7b0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7b4`](#insn-00bda7b4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7b8`](#insn-00bda7b8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7c8`](#insn-00bda7c8) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7d4`](#insn-00bda7d4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7d8`](#insn-00bda7d8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7dc`](#insn-00bda7dc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7e0`](#insn-00bda7e0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bda6d0`](#insn-00bda6d0)

~~~json
{
  "source": "00bda6d0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda6d4`](#insn-00bda6d4)

~~~json
{
  "source": "00bda6d4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda6d8`](#insn-00bda6d8)

~~~json
{
  "source": "00bda6d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda6dc`](#insn-00bda6dc)

~~~json
{
  "source": "00bda6dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda6f4`](#insn-00bda6f4)

~~~json
{
  "source": "00bda6f4",
  "target": "00bda720",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda6fc`](#insn-00bda6fc)

~~~json
{
  "source": "00bda6fc",
  "target": "00bda7a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda708`](#insn-00bda708)

~~~json
{
  "source": "00bda708",
  "target": "002a4200",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4200",
  "offset": 0,
  "size": 93,
  "datatype": "string",
  "bytes": "6c6962756e77696e643a20756e737570706f72746564202e65685f6672616d65",
  "capture_start": "002a4200",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bda70c`](#insn-00bda70c)

~~~json
{
  "source": "00bda70c",
  "target": "00c1bc48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bc48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bda714`](#insn-00bda714)

~~~json
{
  "source": "00bda714",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda718`](#insn-00bda718)

~~~json
{
  "source": "00bda718",
  "target": "00be1e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda71c`](#insn-00bda71c)

~~~json
{
  "source": "00bda71c",
  "target": "00bda7a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda728`](#insn-00bda728)

~~~json
{
  "source": "00bda728",
  "target": "00bda780",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda738`](#insn-00bda738)

~~~json
{
  "source": "00bda738",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda754`](#insn-00bda754)

~~~json
{
  "source": "00bda754",
  "target": "00bd93b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda760`](#insn-00bda760)

~~~json
{
  "source": "00bda760",
  "target": "00bda7c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda778`](#insn-00bda778)

~~~json
{
  "source": "00bda778",
  "target": "00bd93b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda77c`](#insn-00bda77c)

~~~json
{
  "source": "00bda77c",
  "target": "00bda7c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda788`](#insn-00bda788)

~~~json
{
  "source": "00bda788",
  "target": "00298b8a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00298b8a",
  "offset": 0,
  "size": 57,
  "datatype": "string",
  "bytes": "6c6962756e77696e643a20756e737570706f72746564202e65685f6672616d65",
  "capture_start": "00298b8a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bda78c`](#insn-00bda78c)

~~~json
{
  "source": "00bda78c",
  "target": "00c1bc48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bc48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bda798`](#insn-00bda798)

~~~json
{
  "source": "00bda798",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda79c`](#insn-00bda79c)

~~~json
{
  "source": "00bda79c",
  "target": "00be1e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda7a0`](#insn-00bda7a0)

~~~json
{
  "source": "00bda7a0",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda7a4`](#insn-00bda7a4)

~~~json
{
  "source": "00bda7a4",
  "target": "00bdd260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda7ac`](#insn-00bda7ac)

~~~json
{
  "source": "00bda7ac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7b0`](#insn-00bda7b0)

~~~json
{
  "source": "00bda7b0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7b4`](#insn-00bda7b4)

~~~json
{
  "source": "00bda7b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7b8`](#insn-00bda7b8)

~~~json
{
  "source": "00bda7b8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7c8`](#insn-00bda7c8)

~~~json
{
  "source": "00bda7c8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7d4`](#insn-00bda7d4)

~~~json
{
  "source": "00bda7d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7d8`](#insn-00bda7d8)

~~~json
{
  "source": "00bda7d8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7dc`](#insn-00bda7dc)

~~~json
{
  "source": "00bda7dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7e0`](#insn-00bda7e0)

~~~json
{
  "source": "00bda7e0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
