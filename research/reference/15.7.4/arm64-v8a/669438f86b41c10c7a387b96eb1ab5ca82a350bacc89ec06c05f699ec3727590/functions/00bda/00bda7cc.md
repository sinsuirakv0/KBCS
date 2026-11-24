# 00bda7cc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bda78c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda78c.md) · 移動量 `+0x40`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-caa223135fc52a1dc5557d162e14eb4c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5721c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5721c.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0079.md#compare-87430ec9c42cbe6d335a8dad7add0e9b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bda7cc",
  "name": "FUN_00bda7cc",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fb537be12c93e6f6005184c61fcbb88f9102fa346cf5f4bfe6a4f9f74fa2d20e",
  "source_text_sha256": "fb537be12c93e6f6005184c61fcbb88f9102fa346cf5f4bfe6a4f9f74fa2d20e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bda7cc",
        "00bda8eb"
      ]
    ],
    "bytes_sha256": "0bb07a0cc361c0f939f703c1ddfa7909ff8049fe2316c81ea74da3ccee8fec46",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bda69c](../00bda/00bda69c.md)
- [00bdaab4](../00bda/00bdaab4.md)

## 呼び出し先

- [00bd94b0](../00bd9/00bd94b0.md)
- [00bdd360](../00bdd/00bdd360.md)
- [00be1f80](../00be1/00be1f80.md)

## 関連文字列（未確認候補）

~~~text
"libunwind: unsupported .eh_frame_hdr at %lx: need at least 4 bytes of data but only got %zd\n"
"libunwind: unsupported .eh_frame_hdr version: %u at %lx\n"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1394 bytes

~~~c

undefined8 FUN_00bda7cc(undefined8 param_1,byte *param_2,byte *param_3,undefined8 *param_4)

{
  byte bVar1;
  byte bVar2;
  undefined *puVar3;
  undefined8 uVar4;
  byte *local_28;
  
  puVar3 = PTR___sF_00c1bd48;
  if ((ulong)((long)param_3 - (long)param_2) < 4) {
    if (param_3 == param_2) {
      return 0;
    }
    fprintf((FILE *)(PTR___sF_00c1bd48 + 0x130),
            "libunwind: unsupported .eh_frame_hdr at %lx: need at least 4 bytes of data but only got %zd\n"
            ,param_2);
  }
  else {
    if (*param_2 == 1) {
                    /* try { // try from 00bda82c to 00cda83b has its CatchHandler @ 00bda938 */
      local_28 = param_2 + 4;
      bVar1 = param_2[2];
      bVar2 = param_2[1];
                    /* try { // try from 00bda83c to 00cda977 has its CatchHandler @ 00bda7b8 */
      *(byte *)(param_4 + 3) = param_2[3];
      uVar4 = FUN_00bd94b0(param_1,&local_28,param_3,bVar2,param_2);
      *param_4 = uVar4;
      if (bVar1 == 0xff) {
        uVar4 = 0;
      }
      else {
        uVar4 = FUN_00bd94b0(param_1,&local_28,param_3,bVar1,param_2);
      }
      param_4[1] = uVar4;
      param_4[2] = local_28;
      return 1;
    }
    fprintf((FILE *)(PTR___sF_00c1bd48 + 0x130),
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
<a id="insn-00bda7cc"></a> `00bda7cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bda7d0"></a> `00bda7d0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bda7d4"></a> `00bda7d4` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda7d8"></a> `00bda7d8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bda7dc"></a> `00bda7dc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bda7e0"></a> `00bda7e0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bda7e4"></a> `00bda7e4` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bda7e8"></a> `00bda7e8` | `43 00 01 cb` | sub x3,x2,x1 | `FALL_THROUGH`
<a id="insn-00bda7ec"></a> `00bda7ec` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bda7f0"></a> `00bda7f0` | `7f 0c 00 f1` | cmp x3,#0x3 | `FALL_THROUGH`
<a id="insn-00bda7f4"></a> `00bda7f4` | `68 01 00 54` | b.hi 0x00bda820 | `CONDITIONAL_JUMP`
<a id="insn-00bda7f8"></a> `00bda7f8` | `5f 00 13 eb` | cmp x2,x19 | `FALL_THROUGH`
<a id="insn-00bda7fc"></a> `00bda7fc` | `60 05 00 54` | b.eq 0x00bda8a8 | `CONDITIONAL_JUMP`
<a id="insn-00bda800"></a> `00bda800` | `14 02 00 b0` | adrp x20,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bda804"></a> `00bda804` | `41 b6 ff d0` | adrp x1,0x2a4000 | `FALL_THROUGH`
<a id="insn-00bda808"></a> `00bda808` | `21 10 0a 91` | add x1,x1,#0x284 | `FALL_THROUGH`
<a id="insn-00bda80c"></a> `00bda80c` | `94 a6 46 f9` | ldr x20,[x20, #0xd48] | `FALL_THROUGH`
<a id="insn-00bda810"></a> `00bda810` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bda814"></a> `00bda814` | `80 c2 04 91` | add x0,x20,#0x130 | `FALL_THROUGH`
<a id="insn-00bda818"></a> `00bda818` | `da 1d 00 94` | bl 0x00be1f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bda81c"></a> `00bda81c` | `21 00 00 14` | b 0x00bda8a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bda820"></a> `00bda820` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bda824"></a> `00bda824` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bda828"></a> `00bda828` | `c1 02 00 54` | b.ne 0x00bda880 | `CONDITIONAL_JUMP`
<a id="insn-00bda82c"></a> `00bda82c` | `68 12 00 91` | add x8,x19,#0x4 | `FALL_THROUGH`
<a id="insn-00bda830"></a> `00bda830` | `75 0a 40 39` | ldrb w21,[x19, #0x2] | `FALL_THROUGH`
<a id="insn-00bda834"></a> `00bda834` | `63 06 40 39` | ldrb w3,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00bda838"></a> `00bda838` | `a8 0f 00 f9` | str x8,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bda83c"></a> `00bda83c` | `a1 63 00 91` | add x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bda840"></a> `00bda840` | `e4 03 13 aa` | mov x4,x19 | `FALL_THROUGH`
<a id="insn-00bda844"></a> `00bda844` | `68 0e 40 39` | ldrb w8,[x19, #0x3] | `FALL_THROUGH`
<a id="insn-00bda848"></a> `00bda848` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bda84c"></a> `00bda84c` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00bda850"></a> `00bda850` | `88 62 00 39` | strb w8,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bda854"></a> `00bda854` | `17 fb ff 97` | bl 0x00bd94b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda858"></a> `00bda858` | `bf fe 03 71` | cmp w21,#0xff | `FALL_THROUGH`
<a id="insn-00bda85c"></a> `00bda85c` | `80 02 00 f9` | str x0,[x20] | `FALL_THROUGH`
<a id="insn-00bda860"></a> `00bda860` | `20 03 00 54` | b.eq 0x00bda8c4 | `CONDITIONAL_JUMP`
<a id="insn-00bda864"></a> `00bda864` | `a1 63 00 91` | add x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bda868"></a> `00bda868` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bda86c"></a> `00bda86c` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bda870"></a> `00bda870` | `e3 03 15 2a` | mov w3,w21 | `FALL_THROUGH`
<a id="insn-00bda874"></a> `00bda874` | `e4 03 13 aa` | mov x4,x19 | `FALL_THROUGH`
<a id="insn-00bda878"></a> `00bda878` | `0e fb ff 97` | bl 0x00bd94b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda87c"></a> `00bda87c` | `13 00 00 14` | b 0x00bda8c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bda880"></a> `00bda880` | `14 02 00 b0` | adrp x20,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bda884"></a> `00bda884` | `e1 b5 ff d0` | adrp x1,0x298000 | `FALL_THROUGH`
<a id="insn-00bda888"></a> `00bda888` | `21 28 2e 91` | add x1,x1,#0xb8a | `FALL_THROUGH`
<a id="insn-00bda88c"></a> `00bda88c` | `94 a6 46 f9` | ldr x20,[x20, #0xd48] | `FALL_THROUGH`
<a id="insn-00bda890"></a> `00bda890` | `e2 03 08 2a` | mov w2,w8 | `FALL_THROUGH`
<a id="insn-00bda894"></a> `00bda894` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00bda898"></a> `00bda898` | `80 c2 04 91` | add x0,x20,#0x130 | `FALL_THROUGH`
<a id="insn-00bda89c"></a> `00bda89c` | `b9 1d 00 94` | bl 0x00be1f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bda8a0"></a> `00bda8a0` | `80 c2 04 91` | add x0,x20,#0x130 | `FALL_THROUGH`
<a id="insn-00bda8a4"></a> `00bda8a4` | `af 0a 00 94` | bl 0x00bdd360 | `UNCONDITIONAL_CALL`
<a id="insn-00bda8a8"></a> `00bda8a8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bda8ac"></a> `00bda8ac` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bda8b0"></a> `00bda8b0` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda8b4"></a> `00bda8b4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bda8b8"></a> `00bda8b8` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bda8bc"></a> `00bda8bc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bda8c0"></a> `00bda8c0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bda8c4"></a> `00bda8c4` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bda8c8"></a> `00bda8c8` | `a8 0f 40 f9` | ldr x8,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bda8cc"></a> `00bda8cc` | `80 a2 00 a9` | stp x0,x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bda8d0"></a> `00bda8d0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bda8d4"></a> `00bda8d4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bda8d8"></a> `00bda8d8` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda8dc"></a> `00bda8dc` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bda8e0"></a> `00bda8e0` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bda8e4"></a> `00bda8e4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bda8e8"></a> `00bda8e8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bda7cc`](#insn-00bda7cc) 範囲 `[['00bda7cc', '00bda7f7']]`
  - `CONDITIONAL_JUMP` [`00bda7f4`](#insn-00bda7f4) → [`00bda820`](#insn-00bda820)
  - `FALL_THROUGH` [`00bda7f4`](#insn-00bda7f4) → [`00bda7f8`](#insn-00bda7f8)
- ブロック [`00bda7f8`](#insn-00bda7f8) 範囲 `[['00bda7f8', '00bda7ff']]`
  - `CONDITIONAL_JUMP` [`00bda7fc`](#insn-00bda7fc) → [`00bda8a8`](#insn-00bda8a8)
  - `FALL_THROUGH` [`00bda7fc`](#insn-00bda7fc) → [`00bda800`](#insn-00bda800)
- ブロック [`00bda800`](#insn-00bda800) 範囲 `[['00bda800', '00bda81f']]`
  - `UNCONDITIONAL_JUMP` [`00bda81c`](#insn-00bda81c) → [`00bda8a0`](#insn-00bda8a0)
- ブロック [`00bda820`](#insn-00bda820) 範囲 `[['00bda820', '00bda82b']]`
  - `CONDITIONAL_JUMP` [`00bda828`](#insn-00bda828) → [`00bda880`](#insn-00bda880)
  - `FALL_THROUGH` [`00bda828`](#insn-00bda828) → [`00bda82c`](#insn-00bda82c)
- ブロック [`00bda82c`](#insn-00bda82c) 範囲 `[['00bda82c', '00bda83b']]`
  - `FALL_THROUGH` [`00bda838`](#insn-00bda838) → [`00bda83c`](#insn-00bda83c)
- ブロック [`00bda83c`](#insn-00bda83c) 範囲 `[['00bda83c', '00bda863']]`
  - `CONDITIONAL_JUMP` [`00bda860`](#insn-00bda860) → [`00bda8c4`](#insn-00bda8c4)
  - `FALL_THROUGH` [`00bda860`](#insn-00bda860) → [`00bda864`](#insn-00bda864)
- ブロック [`00bda864`](#insn-00bda864) 範囲 `[['00bda864', '00bda87f']]`
  - `UNCONDITIONAL_JUMP` [`00bda87c`](#insn-00bda87c) → [`00bda8c8`](#insn-00bda8c8)
- ブロック [`00bda880`](#insn-00bda880) 範囲 `[['00bda880', '00bda89f']]`
  - `FALL_THROUGH` [`00bda89c`](#insn-00bda89c) → [`00bda8a0`](#insn-00bda8a0)
- ブロック [`00bda8a0`](#insn-00bda8a0) 範囲 `[['00bda8a0', '00bda8a7']]`
  - `FALL_THROUGH` [`00bda8a4`](#insn-00bda8a4) → [`00bda8a8`](#insn-00bda8a8)
- ブロック [`00bda8a8`](#insn-00bda8a8) 範囲 `[['00bda8a8', '00bda8c3']]`
- ブロック [`00bda8c4`](#insn-00bda8c4) 範囲 `[['00bda8c4', '00bda8c7']]`
  - `FALL_THROUGH` [`00bda8c4`](#insn-00bda8c4) → [`00bda8c8`](#insn-00bda8c8)
- ブロック [`00bda8c8`](#insn-00bda8c8) 範囲 `[['00bda8c8', '00bda8eb']]`

## 命令位置別の参照

- [`00bda7d0`](#insn-00bda7d0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7d4`](#insn-00bda7d4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7d8`](#insn-00bda7d8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7dc`](#insn-00bda7dc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7f4`](#insn-00bda7f4) → [`00bda820`](#insn-00bda820) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7fc`](#insn-00bda7fc) → [`00bda8a8`](#insn-00bda8a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda808`](#insn-00bda808) → `002a4284`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bda80c`](#insn-00bda80c) → `00c1bd48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bda814`](#insn-00bda814) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bda818`](#insn-00bda818) → [`00be1f80`](../00be1/00be1f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1f80` · 推定シンボル `None` · 推定型 `None`
- [`00bda81c`](#insn-00bda81c) → [`00bda8a0`](#insn-00bda8a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda828`](#insn-00bda828) → [`00bda880`](#insn-00bda880) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda838`](#insn-00bda838) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda854`](#insn-00bda854) → [`00bd94b0`](../00bd9/00bd94b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd94b0` · 推定シンボル `None` · 推定型 `None`
- [`00bda860`](#insn-00bda860) → [`00bda8c4`](#insn-00bda8c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda878`](#insn-00bda878) → [`00bd94b0`](../00bd9/00bd94b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd94b0` · 推定シンボル `None` · 推定型 `None`
- [`00bda87c`](#insn-00bda87c) → [`00bda8c8`](#insn-00bda8c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda888`](#insn-00bda888) → `00298b8a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bda88c`](#insn-00bda88c) → `00c1bd48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bda898`](#insn-00bda898) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bda89c`](#insn-00bda89c) → [`00be1f80`](../00be1/00be1f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1f80` · 推定シンボル `None` · 推定型 `None`
- [`00bda8a0`](#insn-00bda8a0) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bda8a4`](#insn-00bda8a4) → [`00bdd360`](../00bdd/00bdd360.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd360` · 推定シンボル `None` · 推定型 `None`
- [`00bda8ac`](#insn-00bda8ac) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8b0`](#insn-00bda8b0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8b4`](#insn-00bda8b4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8b8`](#insn-00bda8b8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8c8`](#insn-00bda8c8) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8d4`](#insn-00bda8d4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8d8`](#insn-00bda8d8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8dc`](#insn-00bda8dc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8e0`](#insn-00bda8e0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bda7d0`](#insn-00bda7d0)

~~~json
{
  "source": "00bda7d0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7d4`](#insn-00bda7d4)

~~~json
{
  "source": "00bda7d4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7d8`](#insn-00bda7d8)

~~~json
{
  "source": "00bda7d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7dc`](#insn-00bda7dc)

~~~json
{
  "source": "00bda7dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7f4`](#insn-00bda7f4)

~~~json
{
  "source": "00bda7f4",
  "target": "00bda820",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7fc`](#insn-00bda7fc)

~~~json
{
  "source": "00bda7fc",
  "target": "00bda8a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda808`](#insn-00bda808)

~~~json
{
  "source": "00bda808",
  "target": "002a4284",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4284",
  "offset": 0,
  "size": 93,
  "datatype": "string",
  "bytes": "6c6962756e77696e643a20756e737570706f72746564202e65685f6672616d65",
  "capture_start": "002a4284",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bda80c`](#insn-00bda80c)

~~~json
{
  "source": "00bda80c",
  "target": "00c1bd48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bd48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bda814`](#insn-00bda814)

~~~json
{
  "source": "00bda814",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda818`](#insn-00bda818)

~~~json
{
  "source": "00bda818",
  "target": "00be1f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda81c`](#insn-00bda81c)

~~~json
{
  "source": "00bda81c",
  "target": "00bda8a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda828`](#insn-00bda828)

~~~json
{
  "source": "00bda828",
  "target": "00bda880",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda838`](#insn-00bda838)

~~~json
{
  "source": "00bda838",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda854`](#insn-00bda854)

~~~json
{
  "source": "00bda854",
  "target": "00bd94b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda860`](#insn-00bda860)

~~~json
{
  "source": "00bda860",
  "target": "00bda8c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda878`](#insn-00bda878)

~~~json
{
  "source": "00bda878",
  "target": "00bd94b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda87c`](#insn-00bda87c)

~~~json
{
  "source": "00bda87c",
  "target": "00bda8c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda888`](#insn-00bda888)

~~~json
{
  "source": "00bda888",
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
- 参照命令 [`00bda88c`](#insn-00bda88c)

~~~json
{
  "source": "00bda88c",
  "target": "00c1bd48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bd48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bda898`](#insn-00bda898)

~~~json
{
  "source": "00bda898",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda89c`](#insn-00bda89c)

~~~json
{
  "source": "00bda89c",
  "target": "00be1f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda8a0`](#insn-00bda8a0)

~~~json
{
  "source": "00bda8a0",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda8a4`](#insn-00bda8a4)

~~~json
{
  "source": "00bda8a4",
  "target": "00bdd360",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda8ac`](#insn-00bda8ac)

~~~json
{
  "source": "00bda8ac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8b0`](#insn-00bda8b0)

~~~json
{
  "source": "00bda8b0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8b4`](#insn-00bda8b4)

~~~json
{
  "source": "00bda8b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8b8`](#insn-00bda8b8)

~~~json
{
  "source": "00bda8b8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8c8`](#insn-00bda8c8)

~~~json
{
  "source": "00bda8c8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8d4`](#insn-00bda8d4)

~~~json
{
  "source": "00bda8d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8d8`](#insn-00bda8d8)

~~~json
{
  "source": "00bda8d8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8dc`](#insn-00bda8dc)

~~~json
{
  "source": "00bda8dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8e0`](#insn-00bda8e0)

~~~json
{
  "source": "00bda8e0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
