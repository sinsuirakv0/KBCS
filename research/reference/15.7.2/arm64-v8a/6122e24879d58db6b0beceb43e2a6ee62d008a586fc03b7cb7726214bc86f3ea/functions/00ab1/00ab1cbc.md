# 00ab1cbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ab1d84`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1d84.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0008.md#compare-71a61a82ce9f60641f5320b0067a2996)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ab1cbc",
  "name": "FUN_00ab1cbc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ae20df65ea6003ae6e564c663d630ec2ac9fff79dc1040fd793388018e745e49",
  "source_text_sha256": "ae20df65ea6003ae6e564c663d630ec2ac9fff79dc1040fd793388018e745e49",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ab1cbc",
        "00ab1dbf"
      ]
    ],
    "bytes_sha256": "7befa147f65331bcfb64308662250bca339b5c6df80b25f5d77e9c09912e8de8",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00596128](../00596/00596128.md)

## 呼び出し先

- [0041be0c](../0041b/0041be0c.md)
- [0041cddc](../0041c/0041cddc.md)
- [0044df7c](../0044d/0044df7c.md)
- [0044e05c](../0044e/0044e05c.md)
- [009d8a60](../009d8/009d8a60.md)
- [009dafc4](../009da/009dafc4.md)
- [009dafd0](../009da/009dafd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1054 bytes

~~~c

void FUN_00ab1cbc(long param_1)

{
  undefined *puVar1;
  ulong uVar2;
  long *plVar3;
  byte bVar4;
  undefined *puVar5;
  undefined8 uVar6;
  undefined4 uVar7;
  long lVar8;
  
  FUN_009dafc4(param_1 + 0x397700);
  FUN_009d8a60();
  FUN_009dafd0();
  FUN_0041be0c();
  FUN_0041cddc();
  puVar5 = PTR_DAT_00c1b710;
  lVar8 = 0;
  do {
    puVar1 = puVar5 + lVar8;
    bVar4 = puVar1[0x18];
    uVar2 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar2 = *(ulong *)(puVar1 + 0x20);
    }
    if (uVar2 == 0x13) {
      plVar3 = (long *)(puVar1 + 0x19);
      if ((bVar4 & 1) != 0) {
        plVar3 = *(long **)(puVar1 + 0x28);
      }
      if ((*plVar3 != 0x7461446567616d49 || plVar3[1] != 0x702e6c61636f4c61) ||
          *(long *)((long)plVar3 + 0xb) != 0x6b6361702e6c6163) goto LAB_00ab1d30;
      uVar7 = 1;
    }
    else {
LAB_00ab1d30:
      uVar7 = 0;
    }
    uVar6 = FUN_0044df7c();
    FUN_0044e05c(uVar6,puVar1,puVar1 + 0x18,uVar7);
    lVar8 = lVar8 + 0x30;
    if (lVar8 == 0x150) {
      return;
    }
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ab1cbc"></a> `00ab1cbc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00ab1cc0"></a> `00ab1cc0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab1cc4"></a> `00ab1cc4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ab1cc8"></a> `00ab1cc8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ab1ccc"></a> `00ab1ccc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ab1cd0"></a> `00ab1cd0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ab1cd4"></a> `00ab1cd4` | `08 5c 4e 91` | add x8,x0,#0x397, LSL #12 | `FALL_THROUGH`
<a id="insn-00ab1cd8"></a> `00ab1cd8` | `00 01 1c 91` | add x0,x8,#0x700 | `FALL_THROUGH`
<a id="insn-00ab1cdc"></a> `00ab1cdc` | `ba a4 fc 97` | bl 0x009dafc4 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1ce0"></a> `00ab1ce0` | `60 9b fc 97` | bl 0x009d8a60 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1ce4"></a> `00ab1ce4` | `bb a4 fc 97` | bl 0x009dafd0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1ce8"></a> `00ab1ce8` | `49 a8 e5 97` | bl 0x0041be0c | `UNCONDITIONAL_CALL`
<a id="insn-00ab1cec"></a> `00ab1cec` | `3c ac e5 97` | bl 0x0041cddc | `UNCONDITIONAL_CALL`
<a id="insn-00ab1cf0"></a> `00ab1cf0` | `38 a9 8d d2` | mov x24,#0x6d49 | `FALL_THROUGH`
<a id="insn-00ab1cf4"></a> `00ab1cf4` | `39 8c 89 d2` | mov x25,#0x4c61 | `FALL_THROUGH`
<a id="insn-00ab1cf8"></a> `00ab1cf8` | `7a 2c 8c d2` | mov x26,#0x6163 | `FALL_THROUGH`
<a id="insn-00ab1cfc"></a> `00ab1cfc` | `57 0b 00 d0` | adrp x23,0xc1b000 | `FALL_THROUGH`
<a id="insn-00ab1d00"></a> `00ab1d00` | `38 ec ac f2` | movk x24,#0x6761, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1d04"></a> `00ab1d04` | `f9 6d ac f2` | movk x25,#0x636f, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1d08"></a> `00ab1d08` | `9a cd a5 f2` | movk x26,#0x2e6c, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1d0c"></a> `00ab1d0c` | `f7 8a 43 f9` | ldr x23,[x23, #0x710] | `FALL_THROUGH`
<a id="insn-00ab1d10"></a> `00ab1d10` | `b8 8c c8 f2` | movk x24,#0x4465, LSL #32 | `FALL_THROUGH`
<a id="insn-00ab1d14"></a> `00ab1d14` | `39 8c cd f2` | movk x25,#0x6c61, LSL #32 | `FALL_THROUGH`
<a id="insn-00ab1d18"></a> `00ab1d18` | `1a 2e cc f2` | movk x26,#0x6170, LSL #32 | `FALL_THROUGH`
<a id="insn-00ab1d1c"></a> `00ab1d1c` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00ab1d20"></a> `00ab1d20` | `38 8c ee f2` | movk x24,#0x7461, LSL #48 | `FALL_THROUGH`
<a id="insn-00ab1d24"></a> `00ab1d24` | `d9 05 ee f2` | movk x25,#0x702e, LSL #48 | `FALL_THROUGH`
<a id="insn-00ab1d28"></a> `00ab1d28` | `7a 6c ed f2` | movk x26,#0x6b63, LSL #48 | `FALL_THROUGH`
<a id="insn-00ab1d2c"></a> `00ab1d2c` | `0a 00 00 14` | b 0x00ab1d54 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab1d30"></a> `00ab1d30` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00ab1d34"></a> `00ab1d34` | `92 70 e6 97` | bl 0x0044df7c | `UNCONDITIONAL_CALL`
<a id="insn-00ab1d38"></a> `00ab1d38` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00ab1d3c"></a> `00ab1d3c` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00ab1d40"></a> `00ab1d40` | `e3 03 15 2a` | mov w3,w21 | `FALL_THROUGH`
<a id="insn-00ab1d44"></a> `00ab1d44` | `c6 70 e6 97` | bl 0x0044e05c | `UNCONDITIONAL_CALL`
<a id="insn-00ab1d48"></a> `00ab1d48` | `d6 c2 00 91` | add x22,x22,#0x30 | `FALL_THROUGH`
<a id="insn-00ab1d4c"></a> `00ab1d4c` | `df 42 05 f1` | cmp x22,#0x150 | `FALL_THROUGH`
<a id="insn-00ab1d50"></a> `00ab1d50` | `c0 02 00 54` | b.eq 0x00ab1da8 | `CONDITIONAL_JUMP`
<a id="insn-00ab1d54"></a> `00ab1d54` | `f3 02 16 8b` | add x19,x23,x22 | `FALL_THROUGH`
<a id="insn-00ab1d58"></a> `00ab1d58` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00ab1d5c"></a> `00ab1d5c` | `69 12 40 f9` | ldr x9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00ab1d60"></a> `00ab1d60` | `88 8e 41 38` | ldrb w8,[x20, #0x18]! | `FALL_THROUGH`
<a id="insn-00ab1d64"></a> `00ab1d64` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1d68"></a> `00ab1d68` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1d6c"></a> `00ab1d6c` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00ab1d70"></a> `00ab1d70` | `3f 4d 00 f1` | cmp x9,#0x13 | `FALL_THROUGH`
<a id="insn-00ab1d74"></a> `00ab1d74` | `e1 fd ff 54` | b.ne 0x00ab1d30 | `CONDITIONAL_JUMP`
<a id="insn-00ab1d78"></a> `00ab1d78` | `69 16 40 f9` | ldr x9,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00ab1d7c"></a> `00ab1d7c` | `6a 66 00 91` | add x10,x19,#0x19 | `FALL_THROUGH`
<a id="insn-00ab1d80"></a> `00ab1d80` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1d84"></a> `00ab1d84` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00ab1d88"></a> `00ab1d88` | `09 29 40 a9` | ldp x9,x10,[x8] | `FALL_THROUGH`
<a id="insn-00ab1d8c"></a> `00ab1d8c` | `08 b1 40 f8` | ldur x8,[x8, #0xb] | `FALL_THROUGH`
<a id="insn-00ab1d90"></a> `00ab1d90` | `3f 01 18 eb` | cmp x9,x24 | `FALL_THROUGH`
<a id="insn-00ab1d94"></a> `00ab1d94` | `40 01 59 fa` | ccmp x10,x25,#0x0,eq | `FALL_THROUGH`
<a id="insn-00ab1d98"></a> `00ab1d98` | `00 01 5a fa` | ccmp x8,x26,#0x0,eq | `FALL_THROUGH`
<a id="insn-00ab1d9c"></a> `00ab1d9c` | `a1 fc ff 54` | b.ne 0x00ab1d30 | `CONDITIONAL_JUMP`
<a id="insn-00ab1da0"></a> `00ab1da0` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1da4"></a> `00ab1da4` | `e4 ff ff 17` | b 0x00ab1d34 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab1da8"></a> `00ab1da8` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ab1dac"></a> `00ab1dac` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ab1db0"></a> `00ab1db0` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ab1db4"></a> `00ab1db4` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab1db8"></a> `00ab1db8` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00ab1dbc"></a> `00ab1dbc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ab1cbc`](#insn-00ab1cbc) 範囲 `[['00ab1cbc', '00ab1d2f']]`
  - `UNCONDITIONAL_JUMP` [`00ab1d2c`](#insn-00ab1d2c) → [`00ab1d54`](#insn-00ab1d54)
- ブロック [`00ab1d30`](#insn-00ab1d30) 範囲 `[['00ab1d30', '00ab1d33']]`
  - `FALL_THROUGH` [`00ab1d30`](#insn-00ab1d30) → [`00ab1d34`](#insn-00ab1d34)
- ブロック [`00ab1d34`](#insn-00ab1d34) 範囲 `[['00ab1d34', '00ab1d53']]`
  - `CONDITIONAL_JUMP` [`00ab1d50`](#insn-00ab1d50) → [`00ab1da8`](#insn-00ab1da8)
  - `FALL_THROUGH` [`00ab1d50`](#insn-00ab1d50) → [`00ab1d54`](#insn-00ab1d54)
- ブロック [`00ab1d54`](#insn-00ab1d54) 範囲 `[['00ab1d54', '00ab1d77']]`
  - `CONDITIONAL_JUMP` [`00ab1d74`](#insn-00ab1d74) → [`00ab1d30`](#insn-00ab1d30)
  - `FALL_THROUGH` [`00ab1d74`](#insn-00ab1d74) → [`00ab1d78`](#insn-00ab1d78)
- ブロック [`00ab1d78`](#insn-00ab1d78) 範囲 `[['00ab1d78', '00ab1d9f']]`
  - `CONDITIONAL_JUMP` [`00ab1d9c`](#insn-00ab1d9c) → [`00ab1d30`](#insn-00ab1d30)
  - `FALL_THROUGH` [`00ab1d9c`](#insn-00ab1d9c) → [`00ab1da0`](#insn-00ab1da0)
- ブロック [`00ab1da0`](#insn-00ab1da0) 範囲 `[['00ab1da0', '00ab1da7']]`
  - `UNCONDITIONAL_JUMP` [`00ab1da4`](#insn-00ab1da4) → [`00ab1d34`](#insn-00ab1d34)
- ブロック [`00ab1da8`](#insn-00ab1da8) 範囲 `[['00ab1da8', '00ab1dbf']]`

## 命令位置別の参照

- [`00ab1cbc`](#insn-00ab1cbc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1cc0`](#insn-00ab1cc0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1cc4`](#insn-00ab1cc4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1cc8`](#insn-00ab1cc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1ccc`](#insn-00ab1ccc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1cdc`](#insn-00ab1cdc) → [`009dafc4`](../009da/009dafc4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009dafc4` · 推定シンボル `None` · 推定型 `None`
- [`00ab1ce0`](#insn-00ab1ce0) → [`009d8a60`](../009d8/009d8a60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009d8a60` · 推定シンボル `None` · 推定型 `None`
- [`00ab1ce4`](#insn-00ab1ce4) → [`009dafd0`](../009da/009dafd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009dafd0` · 推定シンボル `None` · 推定型 `None`
- [`00ab1ce8`](#insn-00ab1ce8) → [`0041be0c`](../0041b/0041be0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041be0c` · 推定シンボル `None` · 推定型 `None`
- [`00ab1cec`](#insn-00ab1cec) → [`0041cddc`](../0041c/0041cddc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041cddc` · 推定シンボル `None` · 推定型 `None`
- [`00ab1d0c`](#insn-00ab1d0c) → `00c1b710`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ab1d2c`](#insn-00ab1d2c) → [`00ab1d54`](#insn-00ab1d54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1d34`](#insn-00ab1d34) → [`0044df7c`](../0044d/0044df7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044df7c` · 推定シンボル `None` · 推定型 `None`
- [`00ab1d38`](#insn-00ab1d38) → `0109c5a8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ab1d3c`](#insn-00ab1d3c) → `0109c5c0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ab1d44`](#insn-00ab1d44) → [`0044e05c`](../0044e/0044e05c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044e05c` · 推定シンボル `None` · 推定型 `None`
- [`00ab1d50`](#insn-00ab1d50) → [`00ab1da8`](#insn-00ab1da8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1d5c`](#insn-00ab1d5c) → `0109c5c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ab1d5c`](#insn-00ab1d5c) → `0109c5f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ab1d60`](#insn-00ab1d60) → `0109c5c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ab1d60`](#insn-00ab1d60) → `0109c5f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ab1d74`](#insn-00ab1d74) → [`00ab1d30`](#insn-00ab1d30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1d78`](#insn-00ab1d78) → `0109c5d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ab1d78`](#insn-00ab1d78) → `0109c600`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ab1d88`](#insn-00ab1d88) → `0109c5f1`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ab1d88`](#insn-00ab1d88) → `0109c5f9`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ab1d8c`](#insn-00ab1d8c) → `0109c5fc`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ab1d9c`](#insn-00ab1d9c) → [`00ab1d30`](#insn-00ab1d30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1da4`](#insn-00ab1da4) → [`00ab1d34`](#insn-00ab1d34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1da8`](#insn-00ab1da8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1dac`](#insn-00ab1dac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1db0`](#insn-00ab1db0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1db4`](#insn-00ab1db4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1db8`](#insn-00ab1db8) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ab1cbc`](#insn-00ab1cbc)

~~~json
{
  "source": "00ab1cbc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1cc0`](#insn-00ab1cc0)

~~~json
{
  "source": "00ab1cc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1cc4`](#insn-00ab1cc4)

~~~json
{
  "source": "00ab1cc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1cc8`](#insn-00ab1cc8)

~~~json
{
  "source": "00ab1cc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1ccc`](#insn-00ab1ccc)

~~~json
{
  "source": "00ab1ccc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1cdc`](#insn-00ab1cdc)

~~~json
{
  "source": "00ab1cdc",
  "target": "009dafc4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1ce0`](#insn-00ab1ce0)

~~~json
{
  "source": "00ab1ce0",
  "target": "009d8a60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1ce4`](#insn-00ab1ce4)

~~~json
{
  "source": "00ab1ce4",
  "target": "009dafd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1ce8`](#insn-00ab1ce8)

~~~json
{
  "source": "00ab1ce8",
  "target": "0041be0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1cec`](#insn-00ab1cec)

~~~json
{
  "source": "00ab1cec",
  "target": "0041cddc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1d0c`](#insn-00ab1d0c)

~~~json
{
  "source": "00ab1d0c",
  "target": "00c1b710",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b710",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ab1d2c`](#insn-00ab1d2c)

~~~json
{
  "source": "00ab1d2c",
  "target": "00ab1d54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1d34`](#insn-00ab1d34)

~~~json
{
  "source": "00ab1d34",
  "target": "0044df7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1d38`](#insn-00ab1d38)

~~~json
{
  "source": "00ab1d38",
  "target": "0109c5a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109c5a8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ab1d3c`](#insn-00ab1d3c)

~~~json
{
  "source": "00ab1d3c",
  "target": "0109c5c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109c5c0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ab1d44`](#insn-00ab1d44)

~~~json
{
  "source": "00ab1d44",
  "target": "0044e05c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1d50`](#insn-00ab1d50)

~~~json
{
  "source": "00ab1d50",
  "target": "00ab1da8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1d5c`](#insn-00ab1d5c)

~~~json
{
  "source": "00ab1d5c",
  "target": "0109c5c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109c5c1",
  "offset": 7,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ab1d5c`](#insn-00ab1d5c)

~~~json
{
  "source": "00ab1d5c",
  "target": "0109c5f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109c5f1",
  "offset": 7,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ab1d60`](#insn-00ab1d60)

~~~json
{
  "source": "00ab1d60",
  "target": "0109c5c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109c5c0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ab1d60`](#insn-00ab1d60)

~~~json
{
  "source": "00ab1d60",
  "target": "0109c5f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109c5f0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ab1d74`](#insn-00ab1d74)

~~~json
{
  "source": "00ab1d74",
  "target": "00ab1d30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1d78`](#insn-00ab1d78)

~~~json
{
  "source": "00ab1d78",
  "target": "0109c5d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109c5d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ab1d78`](#insn-00ab1d78)

~~~json
{
  "source": "00ab1d78",
  "target": "0109c600",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109c5f9",
  "offset": 7,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ab1d88`](#insn-00ab1d88)

~~~json
{
  "source": "00ab1d88",
  "target": "0109c5f1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109c5f1",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ab1d88`](#insn-00ab1d88)

~~~json
{
  "source": "00ab1d88",
  "target": "0109c5f9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109c5f9",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ab1d8c`](#insn-00ab1d8c)

~~~json
{
  "source": "00ab1d8c",
  "target": "0109c5fc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109c5f9",
  "offset": 3,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ab1d9c`](#insn-00ab1d9c)

~~~json
{
  "source": "00ab1d9c",
  "target": "00ab1d30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1da4`](#insn-00ab1da4)

~~~json
{
  "source": "00ab1da4",
  "target": "00ab1d34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1da8`](#insn-00ab1da8)

~~~json
{
  "source": "00ab1da8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1dac`](#insn-00ab1dac)

~~~json
{
  "source": "00ab1dac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1db0`](#insn-00ab1db0)

~~~json
{
  "source": "00ab1db0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1db4`](#insn-00ab1db4)

~~~json
{
  "source": "00ab1db4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1db8`](#insn-00ab1db8)

~~~json
{
  "source": "00ab1db8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
