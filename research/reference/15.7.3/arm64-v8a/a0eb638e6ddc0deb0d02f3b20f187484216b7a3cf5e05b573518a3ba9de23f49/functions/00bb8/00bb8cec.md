# 00bb8cec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bb8c24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8c24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-5e68837e8b7b34aea06b7c7729278373)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bb8d30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8d30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-d7e405969791417a200ddf09ccc12c71)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb8cec",
  "name": "FUN_00bb8cec",
  "size": 368,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5a763abbc6370dd054dbdf3fa2c7c945efe8a3cd03ef2ff880fc3f59f0f1fdfd",
  "source_text_sha256": "5a763abbc6370dd054dbdf3fa2c7c945efe8a3cd03ef2ff880fc3f59f0f1fdfd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb8cec",
        "00bb8e5b"
      ]
    ],
    "bytes_sha256": "aab1fde618235049483fcf520d8cf35a39146816e9d545b8d27e2ee66a083956",
    "instruction_count": 92,
    "instruction_bytes": 368,
    "body_bytes": 368,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1127 bytes

~~~c

void FUN_00bb8cec(void)

{
  if ((DAT_010a2d98 & 1) != 0) {
    _ZdlPv(DAT_010a2da8);
  }
  if ((DAT_010a2d80 & 1) != 0) {
    _ZdlPv(DAT_010a2d90);
  }
  if ((DAT_010a2d68 & 1) != 0) {
    _ZdlPv(DAT_010a2d78);
  }
  if ((DAT_010a2d50 & 1) != 0) {
    _ZdlPv(DAT_010a2d60);
  }
  if ((DAT_010a2d38 & 1) != 0) {
    _ZdlPv(DAT_010a2d48);
  }
  if ((DAT_010a2d20 & 1) != 0) {
                    /* try { // try from 00bb8d80 to 00cb8e57 has its CatchHandler @ 00bb3400 */
    _ZdlPv(DAT_010a2d30);
  }
  if ((DAT_010a2d08 & 1) != 0) {
    _ZdlPv(DAT_010a2d18);
  }
  if ((DAT_010a2cf0 & 1) != 0) {
    _ZdlPv(DAT_010a2d00);
  }
  if ((DAT_010a2cd8 & 1) != 0) {
    _ZdlPv(DAT_010a2ce8);
  }
  if ((DAT_010a2cc0 & 1) != 0) {
    _ZdlPv(DAT_010a2cd0);
  }
  if ((DAT_010a2ca8 & 1) != 0) {
    _ZdlPv(DAT_010a2cb8);
  }
  if ((DAT_010a2c90 & 1) != 0) {
    _ZdlPv(DAT_010a2ca0);
  }
  if ((DAT_010a2c78 & 1) != 0) {
    _ZdlPv(DAT_010a2c88);
  }
  if ((DAT_010a2c60 & 1) == 0) {
    return;
  }
                    /* try { // try from 00bb8e58 to 00cb8e5f has its CatchHandler @ 00bbac98 */
  _ZdlPv(DAT_010a2c70);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb8cec"></a> `00bb8cec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bb8cf0"></a> `00bb8cf0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bb8cf4"></a> `00bb8cf4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bb8cf8"></a> `00bb8cf8` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8cfc"></a> `00bb8cfc` | `08 61 76 39` | ldrb w8,[x8, #0xd98] | `FALL_THROUGH`
<a id="insn-00bb8d00"></a> `00bb8d00` | `88 00 00 36` | tbz w8,#0x0,0x00bb8d10 | `CONDITIONAL_JUMP`
<a id="insn-00bb8d04"></a> `00bb8d04` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8d08"></a> `00bb8d08` | `00 d5 46 f9` | ldr x0,[x8, #0xda8] | `FALL_THROUGH`
<a id="insn-00bb8d0c"></a> `00bb8d0c` | `c1 88 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8d10"></a> `00bb8d10` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8d14"></a> `00bb8d14` | `08 01 76 39` | ldrb w8,[x8, #0xd80] | `FALL_THROUGH`
<a id="insn-00bb8d18"></a> `00bb8d18` | `88 00 00 36` | tbz w8,#0x0,0x00bb8d28 | `CONDITIONAL_JUMP`
<a id="insn-00bb8d1c"></a> `00bb8d1c` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8d20"></a> `00bb8d20` | `00 c9 46 f9` | ldr x0,[x8, #0xd90] | `FALL_THROUGH`
<a id="insn-00bb8d24"></a> `00bb8d24` | `bb 88 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8d28"></a> `00bb8d28` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8d2c"></a> `00bb8d2c` | `08 a1 75 39` | ldrb w8,[x8, #0xd68] | `FALL_THROUGH`
<a id="insn-00bb8d30"></a> `00bb8d30` | `88 00 00 36` | tbz w8,#0x0,0x00bb8d40 | `CONDITIONAL_JUMP`
<a id="insn-00bb8d34"></a> `00bb8d34` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8d38"></a> `00bb8d38` | `00 bd 46 f9` | ldr x0,[x8, #0xd78] | `FALL_THROUGH`
<a id="insn-00bb8d3c"></a> `00bb8d3c` | `b5 88 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8d40"></a> `00bb8d40` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8d44"></a> `00bb8d44` | `08 41 75 39` | ldrb w8,[x8, #0xd50] | `FALL_THROUGH`
<a id="insn-00bb8d48"></a> `00bb8d48` | `88 00 00 36` | tbz w8,#0x0,0x00bb8d58 | `CONDITIONAL_JUMP`
<a id="insn-00bb8d4c"></a> `00bb8d4c` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8d50"></a> `00bb8d50` | `00 b1 46 f9` | ldr x0,[x8, #0xd60] | `FALL_THROUGH`
<a id="insn-00bb8d54"></a> `00bb8d54` | `af 88 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8d58"></a> `00bb8d58` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8d5c"></a> `00bb8d5c` | `08 e1 74 39` | ldrb w8,[x8, #0xd38] | `FALL_THROUGH`
<a id="insn-00bb8d60"></a> `00bb8d60` | `88 00 00 36` | tbz w8,#0x0,0x00bb8d70 | `CONDITIONAL_JUMP`
<a id="insn-00bb8d64"></a> `00bb8d64` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8d68"></a> `00bb8d68` | `00 a5 46 f9` | ldr x0,[x8, #0xd48] | `FALL_THROUGH`
<a id="insn-00bb8d6c"></a> `00bb8d6c` | `a9 88 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8d70"></a> `00bb8d70` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8d74"></a> `00bb8d74` | `08 81 74 39` | ldrb w8,[x8, #0xd20] | `FALL_THROUGH`
<a id="insn-00bb8d78"></a> `00bb8d78` | `88 00 00 36` | tbz w8,#0x0,0x00bb8d88 | `CONDITIONAL_JUMP`
<a id="insn-00bb8d7c"></a> `00bb8d7c` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8d80"></a> `00bb8d80` | `00 99 46 f9` | ldr x0,[x8, #0xd30] | `FALL_THROUGH`
<a id="insn-00bb8d84"></a> `00bb8d84` | `a3 88 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8d88"></a> `00bb8d88` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8d8c"></a> `00bb8d8c` | `08 21 74 39` | ldrb w8,[x8, #0xd08] | `FALL_THROUGH`
<a id="insn-00bb8d90"></a> `00bb8d90` | `88 00 00 36` | tbz w8,#0x0,0x00bb8da0 | `CONDITIONAL_JUMP`
<a id="insn-00bb8d94"></a> `00bb8d94` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8d98"></a> `00bb8d98` | `00 8d 46 f9` | ldr x0,[x8, #0xd18] | `FALL_THROUGH`
<a id="insn-00bb8d9c"></a> `00bb8d9c` | `9d 88 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8da0"></a> `00bb8da0` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8da4"></a> `00bb8da4` | `08 c1 73 39` | ldrb w8,[x8, #0xcf0] | `FALL_THROUGH`
<a id="insn-00bb8da8"></a> `00bb8da8` | `88 00 00 36` | tbz w8,#0x0,0x00bb8db8 | `CONDITIONAL_JUMP`
<a id="insn-00bb8dac"></a> `00bb8dac` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8db0"></a> `00bb8db0` | `00 81 46 f9` | ldr x0,[x8, #0xd00] | `FALL_THROUGH`
<a id="insn-00bb8db4"></a> `00bb8db4` | `97 88 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8db8"></a> `00bb8db8` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8dbc"></a> `00bb8dbc` | `08 61 73 39` | ldrb w8,[x8, #0xcd8] | `FALL_THROUGH`
<a id="insn-00bb8dc0"></a> `00bb8dc0` | `88 00 00 36` | tbz w8,#0x0,0x00bb8dd0 | `CONDITIONAL_JUMP`
<a id="insn-00bb8dc4"></a> `00bb8dc4` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8dc8"></a> `00bb8dc8` | `00 75 46 f9` | ldr x0,[x8, #0xce8] | `FALL_THROUGH`
<a id="insn-00bb8dcc"></a> `00bb8dcc` | `91 88 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8dd0"></a> `00bb8dd0` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8dd4"></a> `00bb8dd4` | `08 01 73 39` | ldrb w8,[x8, #0xcc0] | `FALL_THROUGH`
<a id="insn-00bb8dd8"></a> `00bb8dd8` | `88 00 00 36` | tbz w8,#0x0,0x00bb8de8 | `CONDITIONAL_JUMP`
<a id="insn-00bb8ddc"></a> `00bb8ddc` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8de0"></a> `00bb8de0` | `00 69 46 f9` | ldr x0,[x8, #0xcd0] | `FALL_THROUGH`
<a id="insn-00bb8de4"></a> `00bb8de4` | `8b 88 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8de8"></a> `00bb8de8` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8dec"></a> `00bb8dec` | `08 a1 72 39` | ldrb w8,[x8, #0xca8] | `FALL_THROUGH`
<a id="insn-00bb8df0"></a> `00bb8df0` | `88 00 00 36` | tbz w8,#0x0,0x00bb8e00 | `CONDITIONAL_JUMP`
<a id="insn-00bb8df4"></a> `00bb8df4` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8df8"></a> `00bb8df8` | `00 5d 46 f9` | ldr x0,[x8, #0xcb8] | `FALL_THROUGH`
<a id="insn-00bb8dfc"></a> `00bb8dfc` | `85 88 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8e00"></a> `00bb8e00` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8e04"></a> `00bb8e04` | `08 41 72 39` | ldrb w8,[x8, #0xc90] | `FALL_THROUGH`
<a id="insn-00bb8e08"></a> `00bb8e08` | `88 00 00 36` | tbz w8,#0x0,0x00bb8e18 | `CONDITIONAL_JUMP`
<a id="insn-00bb8e0c"></a> `00bb8e0c` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8e10"></a> `00bb8e10` | `00 51 46 f9` | ldr x0,[x8, #0xca0] | `FALL_THROUGH`
<a id="insn-00bb8e14"></a> `00bb8e14` | `7f 88 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8e18"></a> `00bb8e18` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8e1c"></a> `00bb8e1c` | `08 e1 71 39` | ldrb w8,[x8, #0xc78] | `FALL_THROUGH`
<a id="insn-00bb8e20"></a> `00bb8e20` | `88 00 00 36` | tbz w8,#0x0,0x00bb8e30 | `CONDITIONAL_JUMP`
<a id="insn-00bb8e24"></a> `00bb8e24` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8e28"></a> `00bb8e28` | `00 45 46 f9` | ldr x0,[x8, #0xc88] | `FALL_THROUGH`
<a id="insn-00bb8e2c"></a> `00bb8e2c` | `79 88 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8e30"></a> `00bb8e30` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8e34"></a> `00bb8e34` | `08 81 71 39` | ldrb w8,[x8, #0xc60] | `FALL_THROUGH`
<a id="insn-00bb8e38"></a> `00bb8e38` | `88 00 00 37` | tbnz w8,#0x0,0x00bb8e48 | `CONDITIONAL_JUMP`
<a id="insn-00bb8e3c"></a> `00bb8e3c` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bb8e40"></a> `00bb8e40` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bb8e44"></a> `00bb8e44` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bb8e48"></a> `00bb8e48` | `48 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8e4c"></a> `00bb8e4c` | `00 39 46 f9` | ldr x0,[x8, #0xc70] | `FALL_THROUGH`
<a id="insn-00bb8e50"></a> `00bb8e50` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bb8e54"></a> `00bb8e54` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bb8e58"></a> `00bb8e58` | `6e 88 00 14` | b 0x00bdb010 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb8cec`](#insn-00bb8cec) 範囲 `[['00bb8cec', '00bb8d03']]`
  - `CONDITIONAL_JUMP` [`00bb8d00`](#insn-00bb8d00) → [`00bb8d10`](#insn-00bb8d10)
  - `FALL_THROUGH` [`00bb8d00`](#insn-00bb8d00) → [`00bb8d04`](#insn-00bb8d04)
- ブロック [`00bb8d04`](#insn-00bb8d04) 範囲 `[['00bb8d04', '00bb8d0f']]`
  - `FALL_THROUGH` [`00bb8d0c`](#insn-00bb8d0c) → [`00bb8d10`](#insn-00bb8d10)
- ブロック [`00bb8d10`](#insn-00bb8d10) 範囲 `[['00bb8d10', '00bb8d1b']]`
  - `CONDITIONAL_JUMP` [`00bb8d18`](#insn-00bb8d18) → [`00bb8d28`](#insn-00bb8d28)
  - `FALL_THROUGH` [`00bb8d18`](#insn-00bb8d18) → [`00bb8d1c`](#insn-00bb8d1c)
- ブロック [`00bb8d1c`](#insn-00bb8d1c) 範囲 `[['00bb8d1c', '00bb8d27']]`
  - `FALL_THROUGH` [`00bb8d24`](#insn-00bb8d24) → [`00bb8d28`](#insn-00bb8d28)
- ブロック [`00bb8d28`](#insn-00bb8d28) 範囲 `[['00bb8d28', '00bb8d33']]`
  - `CONDITIONAL_JUMP` [`00bb8d30`](#insn-00bb8d30) → [`00bb8d40`](#insn-00bb8d40)
  - `FALL_THROUGH` [`00bb8d30`](#insn-00bb8d30) → [`00bb8d34`](#insn-00bb8d34)
- ブロック [`00bb8d34`](#insn-00bb8d34) 範囲 `[['00bb8d34', '00bb8d3f']]`
  - `FALL_THROUGH` [`00bb8d3c`](#insn-00bb8d3c) → [`00bb8d40`](#insn-00bb8d40)
- ブロック [`00bb8d40`](#insn-00bb8d40) 範囲 `[['00bb8d40', '00bb8d4b']]`
  - `CONDITIONAL_JUMP` [`00bb8d48`](#insn-00bb8d48) → [`00bb8d58`](#insn-00bb8d58)
  - `FALL_THROUGH` [`00bb8d48`](#insn-00bb8d48) → [`00bb8d4c`](#insn-00bb8d4c)
- ブロック [`00bb8d4c`](#insn-00bb8d4c) 範囲 `[['00bb8d4c', '00bb8d57']]`
  - `FALL_THROUGH` [`00bb8d54`](#insn-00bb8d54) → [`00bb8d58`](#insn-00bb8d58)
- ブロック [`00bb8d58`](#insn-00bb8d58) 範囲 `[['00bb8d58', '00bb8d63']]`
  - `CONDITIONAL_JUMP` [`00bb8d60`](#insn-00bb8d60) → [`00bb8d70`](#insn-00bb8d70)
  - `FALL_THROUGH` [`00bb8d60`](#insn-00bb8d60) → [`00bb8d64`](#insn-00bb8d64)
- ブロック [`00bb8d64`](#insn-00bb8d64) 範囲 `[['00bb8d64', '00bb8d6f']]`
  - `FALL_THROUGH` [`00bb8d6c`](#insn-00bb8d6c) → [`00bb8d70`](#insn-00bb8d70)
- ブロック [`00bb8d70`](#insn-00bb8d70) 範囲 `[['00bb8d70', '00bb8d7b']]`
  - `CONDITIONAL_JUMP` [`00bb8d78`](#insn-00bb8d78) → [`00bb8d88`](#insn-00bb8d88)
  - `FALL_THROUGH` [`00bb8d78`](#insn-00bb8d78) → [`00bb8d7c`](#insn-00bb8d7c)
- ブロック [`00bb8d7c`](#insn-00bb8d7c) 範囲 `[['00bb8d7c', '00bb8d7f']]`
  - `FALL_THROUGH` [`00bb8d7c`](#insn-00bb8d7c) → [`00bb8d80`](#insn-00bb8d80)
- ブロック [`00bb8d80`](#insn-00bb8d80) 範囲 `[['00bb8d80', '00bb8d87']]`
  - `FALL_THROUGH` [`00bb8d84`](#insn-00bb8d84) → [`00bb8d88`](#insn-00bb8d88)
- ブロック [`00bb8d88`](#insn-00bb8d88) 範囲 `[['00bb8d88', '00bb8d93']]`
  - `CONDITIONAL_JUMP` [`00bb8d90`](#insn-00bb8d90) → [`00bb8da0`](#insn-00bb8da0)
  - `FALL_THROUGH` [`00bb8d90`](#insn-00bb8d90) → [`00bb8d94`](#insn-00bb8d94)
- ブロック [`00bb8d94`](#insn-00bb8d94) 範囲 `[['00bb8d94', '00bb8d9f']]`
  - `FALL_THROUGH` [`00bb8d9c`](#insn-00bb8d9c) → [`00bb8da0`](#insn-00bb8da0)
- ブロック [`00bb8da0`](#insn-00bb8da0) 範囲 `[['00bb8da0', '00bb8dab']]`
  - `CONDITIONAL_JUMP` [`00bb8da8`](#insn-00bb8da8) → [`00bb8db8`](#insn-00bb8db8)
  - `FALL_THROUGH` [`00bb8da8`](#insn-00bb8da8) → [`00bb8dac`](#insn-00bb8dac)
- ブロック [`00bb8dac`](#insn-00bb8dac) 範囲 `[['00bb8dac', '00bb8db7']]`
  - `FALL_THROUGH` [`00bb8db4`](#insn-00bb8db4) → [`00bb8db8`](#insn-00bb8db8)
- ブロック [`00bb8db8`](#insn-00bb8db8) 範囲 `[['00bb8db8', '00bb8dc3']]`
  - `CONDITIONAL_JUMP` [`00bb8dc0`](#insn-00bb8dc0) → [`00bb8dd0`](#insn-00bb8dd0)
  - `FALL_THROUGH` [`00bb8dc0`](#insn-00bb8dc0) → [`00bb8dc4`](#insn-00bb8dc4)
- ブロック [`00bb8dc4`](#insn-00bb8dc4) 範囲 `[['00bb8dc4', '00bb8dcf']]`
  - `FALL_THROUGH` [`00bb8dcc`](#insn-00bb8dcc) → [`00bb8dd0`](#insn-00bb8dd0)
- ブロック [`00bb8dd0`](#insn-00bb8dd0) 範囲 `[['00bb8dd0', '00bb8ddb']]`
  - `CONDITIONAL_JUMP` [`00bb8dd8`](#insn-00bb8dd8) → [`00bb8de8`](#insn-00bb8de8)
  - `FALL_THROUGH` [`00bb8dd8`](#insn-00bb8dd8) → [`00bb8ddc`](#insn-00bb8ddc)
- ブロック [`00bb8ddc`](#insn-00bb8ddc) 範囲 `[['00bb8ddc', '00bb8de7']]`
  - `FALL_THROUGH` [`00bb8de4`](#insn-00bb8de4) → [`00bb8de8`](#insn-00bb8de8)
- ブロック [`00bb8de8`](#insn-00bb8de8) 範囲 `[['00bb8de8', '00bb8df3']]`
  - `CONDITIONAL_JUMP` [`00bb8df0`](#insn-00bb8df0) → [`00bb8e00`](#insn-00bb8e00)
  - `FALL_THROUGH` [`00bb8df0`](#insn-00bb8df0) → [`00bb8df4`](#insn-00bb8df4)
- ブロック [`00bb8df4`](#insn-00bb8df4) 範囲 `[['00bb8df4', '00bb8dff']]`
  - `FALL_THROUGH` [`00bb8dfc`](#insn-00bb8dfc) → [`00bb8e00`](#insn-00bb8e00)
- ブロック [`00bb8e00`](#insn-00bb8e00) 範囲 `[['00bb8e00', '00bb8e0b']]`
  - `CONDITIONAL_JUMP` [`00bb8e08`](#insn-00bb8e08) → [`00bb8e18`](#insn-00bb8e18)
  - `FALL_THROUGH` [`00bb8e08`](#insn-00bb8e08) → [`00bb8e0c`](#insn-00bb8e0c)
- ブロック [`00bb8e0c`](#insn-00bb8e0c) 範囲 `[['00bb8e0c', '00bb8e17']]`
  - `FALL_THROUGH` [`00bb8e14`](#insn-00bb8e14) → [`00bb8e18`](#insn-00bb8e18)
- ブロック [`00bb8e18`](#insn-00bb8e18) 範囲 `[['00bb8e18', '00bb8e23']]`
  - `CONDITIONAL_JUMP` [`00bb8e20`](#insn-00bb8e20) → [`00bb8e30`](#insn-00bb8e30)
  - `FALL_THROUGH` [`00bb8e20`](#insn-00bb8e20) → [`00bb8e24`](#insn-00bb8e24)
- ブロック [`00bb8e24`](#insn-00bb8e24) 範囲 `[['00bb8e24', '00bb8e2f']]`
  - `FALL_THROUGH` [`00bb8e2c`](#insn-00bb8e2c) → [`00bb8e30`](#insn-00bb8e30)
- ブロック [`00bb8e30`](#insn-00bb8e30) 範囲 `[['00bb8e30', '00bb8e3b']]`
  - `CONDITIONAL_JUMP` [`00bb8e38`](#insn-00bb8e38) → [`00bb8e48`](#insn-00bb8e48)
  - `FALL_THROUGH` [`00bb8e38`](#insn-00bb8e38) → [`00bb8e3c`](#insn-00bb8e3c)
- ブロック [`00bb8e3c`](#insn-00bb8e3c) 範囲 `[['00bb8e3c', '00bb8e47']]`
- ブロック [`00bb8e48`](#insn-00bb8e48) 範囲 `[['00bb8e48', '00bb8e57']]`
  - `FALL_THROUGH` [`00bb8e54`](#insn-00bb8e54) → [`00bb8e58`](#insn-00bb8e58)
- ブロック [`00bb8e58`](#insn-00bb8e58) 範囲 `[['00bb8e58', '00bb8e5b']]`

## 命令位置別の参照

- [`00bb8cf0`](#insn-00bb8cf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8cfc`](#insn-00bb8cfc) → `010a2d98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8d00`](#insn-00bb8d00) → [`00bb8d10`](#insn-00bb8d10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8d08`](#insn-00bb8d08) → `010a2da8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8d0c`](#insn-00bb8d0c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb8d14`](#insn-00bb8d14) → `010a2d80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8d18`](#insn-00bb8d18) → [`00bb8d28`](#insn-00bb8d28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8d20`](#insn-00bb8d20) → `010a2d90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8d24`](#insn-00bb8d24) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb8d2c`](#insn-00bb8d2c) → `010a2d68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8d30`](#insn-00bb8d30) → [`00bb8d40`](#insn-00bb8d40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8d38`](#insn-00bb8d38) → `010a2d78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8d3c`](#insn-00bb8d3c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb8d44`](#insn-00bb8d44) → `010a2d50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8d48`](#insn-00bb8d48) → [`00bb8d58`](#insn-00bb8d58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8d50`](#insn-00bb8d50) → `010a2d60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8d54`](#insn-00bb8d54) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb8d5c`](#insn-00bb8d5c) → `010a2d38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8d60`](#insn-00bb8d60) → [`00bb8d70`](#insn-00bb8d70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8d68`](#insn-00bb8d68) → `010a2d48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8d6c`](#insn-00bb8d6c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb8d74`](#insn-00bb8d74) → `010a2d20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8d78`](#insn-00bb8d78) → [`00bb8d88`](#insn-00bb8d88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8d80`](#insn-00bb8d80) → `010a2d30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8d84`](#insn-00bb8d84) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb8d8c`](#insn-00bb8d8c) → `010a2d08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8d90`](#insn-00bb8d90) → [`00bb8da0`](#insn-00bb8da0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8d98`](#insn-00bb8d98) → `010a2d18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8d9c`](#insn-00bb8d9c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb8da4`](#insn-00bb8da4) → `010a2cf0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8da8`](#insn-00bb8da8) → [`00bb8db8`](#insn-00bb8db8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8db0`](#insn-00bb8db0) → `010a2d00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8db4`](#insn-00bb8db4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb8dbc`](#insn-00bb8dbc) → `010a2cd8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8dc0`](#insn-00bb8dc0) → [`00bb8dd0`](#insn-00bb8dd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8dc8`](#insn-00bb8dc8) → `010a2ce8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8dcc`](#insn-00bb8dcc) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb8dd4`](#insn-00bb8dd4) → `010a2cc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8dd8`](#insn-00bb8dd8) → [`00bb8de8`](#insn-00bb8de8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8de0`](#insn-00bb8de0) → `010a2cd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8de4`](#insn-00bb8de4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb8dec`](#insn-00bb8dec) → `010a2ca8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8df0`](#insn-00bb8df0) → [`00bb8e00`](#insn-00bb8e00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8df8`](#insn-00bb8df8) → `010a2cb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8dfc`](#insn-00bb8dfc) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb8e04`](#insn-00bb8e04) → `010a2c90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8e08`](#insn-00bb8e08) → [`00bb8e18`](#insn-00bb8e18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8e10`](#insn-00bb8e10) → `010a2ca0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8e14`](#insn-00bb8e14) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb8e1c`](#insn-00bb8e1c) → `010a2c78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8e20`](#insn-00bb8e20) → [`00bb8e30`](#insn-00bb8e30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8e28`](#insn-00bb8e28) → `010a2c88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8e2c`](#insn-00bb8e2c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb8e34`](#insn-00bb8e34) → `010a2c60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8e38`](#insn-00bb8e38) → [`00bb8e48`](#insn-00bb8e48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8e3c`](#insn-00bb8e3c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8e4c`](#insn-00bb8e4c) → `010a2c70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8e50`](#insn-00bb8e50) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8e58`](#insn-00bb8e58) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb8cf0`](#insn-00bb8cf0)

~~~json
{
  "source": "00bb8cf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8cfc`](#insn-00bb8cfc)

~~~json
{
  "source": "00bb8cfc",
  "target": "010a2d98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d98",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8d00`](#insn-00bb8d00)

~~~json
{
  "source": "00bb8d00",
  "target": "00bb8d10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8d08`](#insn-00bb8d08)

~~~json
{
  "source": "00bb8d08",
  "target": "010a2da8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2da8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8d0c`](#insn-00bb8d0c)

~~~json
{
  "source": "00bb8d0c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8d14`](#insn-00bb8d14)

~~~json
{
  "source": "00bb8d14",
  "target": "010a2d80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d80",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8d18`](#insn-00bb8d18)

~~~json
{
  "source": "00bb8d18",
  "target": "00bb8d28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8d20`](#insn-00bb8d20)

~~~json
{
  "source": "00bb8d20",
  "target": "010a2d90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d90",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8d24`](#insn-00bb8d24)

~~~json
{
  "source": "00bb8d24",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8d2c`](#insn-00bb8d2c)

~~~json
{
  "source": "00bb8d2c",
  "target": "010a2d68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d68",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8d30`](#insn-00bb8d30)

~~~json
{
  "source": "00bb8d30",
  "target": "00bb8d40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8d38`](#insn-00bb8d38)

~~~json
{
  "source": "00bb8d38",
  "target": "010a2d78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8d3c`](#insn-00bb8d3c)

~~~json
{
  "source": "00bb8d3c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8d44`](#insn-00bb8d44)

~~~json
{
  "source": "00bb8d44",
  "target": "010a2d50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d50",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8d48`](#insn-00bb8d48)

~~~json
{
  "source": "00bb8d48",
  "target": "00bb8d58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8d50`](#insn-00bb8d50)

~~~json
{
  "source": "00bb8d50",
  "target": "010a2d60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8d54`](#insn-00bb8d54)

~~~json
{
  "source": "00bb8d54",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8d5c`](#insn-00bb8d5c)

~~~json
{
  "source": "00bb8d5c",
  "target": "010a2d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8d60`](#insn-00bb8d60)

~~~json
{
  "source": "00bb8d60",
  "target": "00bb8d70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8d68`](#insn-00bb8d68)

~~~json
{
  "source": "00bb8d68",
  "target": "010a2d48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8d6c`](#insn-00bb8d6c)

~~~json
{
  "source": "00bb8d6c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8d74`](#insn-00bb8d74)

~~~json
{
  "source": "00bb8d74",
  "target": "010a2d20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d20",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8d78`](#insn-00bb8d78)

~~~json
{
  "source": "00bb8d78",
  "target": "00bb8d88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8d80`](#insn-00bb8d80)

~~~json
{
  "source": "00bb8d80",
  "target": "010a2d30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8d84`](#insn-00bb8d84)

~~~json
{
  "source": "00bb8d84",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8d8c`](#insn-00bb8d8c)

~~~json
{
  "source": "00bb8d8c",
  "target": "010a2d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d08",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8d90`](#insn-00bb8d90)

~~~json
{
  "source": "00bb8d90",
  "target": "00bb8da0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8d98`](#insn-00bb8d98)

~~~json
{
  "source": "00bb8d98",
  "target": "010a2d18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8d9c`](#insn-00bb8d9c)

~~~json
{
  "source": "00bb8d9c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8da4`](#insn-00bb8da4)

~~~json
{
  "source": "00bb8da4",
  "target": "010a2cf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cf0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8da8`](#insn-00bb8da8)

~~~json
{
  "source": "00bb8da8",
  "target": "00bb8db8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8db0`](#insn-00bb8db0)

~~~json
{
  "source": "00bb8db0",
  "target": "010a2d00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8db4`](#insn-00bb8db4)

~~~json
{
  "source": "00bb8db4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8dbc`](#insn-00bb8dbc)

~~~json
{
  "source": "00bb8dbc",
  "target": "010a2cd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8dc0`](#insn-00bb8dc0)

~~~json
{
  "source": "00bb8dc0",
  "target": "00bb8dd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8dc8`](#insn-00bb8dc8)

~~~json
{
  "source": "00bb8dc8",
  "target": "010a2ce8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ce8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8dcc`](#insn-00bb8dcc)

~~~json
{
  "source": "00bb8dcc",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8dd4`](#insn-00bb8dd4)

~~~json
{
  "source": "00bb8dd4",
  "target": "010a2cc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cc0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8dd8`](#insn-00bb8dd8)

~~~json
{
  "source": "00bb8dd8",
  "target": "00bb8de8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8de0`](#insn-00bb8de0)

~~~json
{
  "source": "00bb8de0",
  "target": "010a2cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cd0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8de4`](#insn-00bb8de4)

~~~json
{
  "source": "00bb8de4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8dec`](#insn-00bb8dec)

~~~json
{
  "source": "00bb8dec",
  "target": "010a2ca8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ca8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8df0`](#insn-00bb8df0)

~~~json
{
  "source": "00bb8df0",
  "target": "00bb8e00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8df8`](#insn-00bb8df8)

~~~json
{
  "source": "00bb8df8",
  "target": "010a2cb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cb8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8dfc`](#insn-00bb8dfc)

~~~json
{
  "source": "00bb8dfc",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8e04`](#insn-00bb8e04)

~~~json
{
  "source": "00bb8e04",
  "target": "010a2c90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2c90",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8e08`](#insn-00bb8e08)

~~~json
{
  "source": "00bb8e08",
  "target": "00bb8e18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8e10`](#insn-00bb8e10)

~~~json
{
  "source": "00bb8e10",
  "target": "010a2ca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ca0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8e14`](#insn-00bb8e14)

~~~json
{
  "source": "00bb8e14",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8e1c`](#insn-00bb8e1c)

~~~json
{
  "source": "00bb8e1c",
  "target": "010a2c78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2c78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8e20`](#insn-00bb8e20)

~~~json
{
  "source": "00bb8e20",
  "target": "00bb8e30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8e28`](#insn-00bb8e28)

~~~json
{
  "source": "00bb8e28",
  "target": "010a2c88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2c88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8e2c`](#insn-00bb8e2c)

~~~json
{
  "source": "00bb8e2c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8e34`](#insn-00bb8e34)

~~~json
{
  "source": "00bb8e34",
  "target": "010a2c60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2c60",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8e38`](#insn-00bb8e38)

~~~json
{
  "source": "00bb8e38",
  "target": "00bb8e48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8e3c`](#insn-00bb8e3c)

~~~json
{
  "source": "00bb8e3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8e4c`](#insn-00bb8e4c)

~~~json
{
  "source": "00bb8e4c",
  "target": "010a2c70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2c70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8e50`](#insn-00bb8e50)

~~~json
{
  "source": "00bb8e50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8e58`](#insn-00bb8e58)

~~~json
{
  "source": "00bb8e58",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
