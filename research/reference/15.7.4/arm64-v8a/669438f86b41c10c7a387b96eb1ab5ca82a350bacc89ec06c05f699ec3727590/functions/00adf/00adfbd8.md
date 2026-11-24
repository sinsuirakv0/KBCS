# 00adfbd8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adfb94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfb94.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0004.md#compare-f08aa990f95f33beb2d93bcc452e0cbd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b3f5b0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f5b0.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0055.md#compare-a5460cee243322c80f5c044ba0616789)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adfbd8",
  "name": "FUN_00adfbd8",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "662259eb59ac85ac81f17aa66a9e7cb5b0bd6f7d879e66916afab1a81167fa63",
  "source_text_sha256": "662259eb59ac85ac81f17aa66a9e7cb5b0bd6f7d879e66916afab1a81167fa63",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adfbd8",
        "00adfcb7"
      ]
    ],
    "bytes_sha256": "686600ba041f74ae69b876d15a027aa100c0553201b35cc851cf892919471c67",
    "instruction_count": 56,
    "instruction_bytes": 224,
    "body_bytes": 224,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00444c54](../00444/00444c54.md)
- [0044592c](../00445/0044592c.md)
- [00467c58](../00467/00467c58.md)
- [00886014](../00886/00886014.md)
- [00bdb7c0](../00bdb/00bdb7c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4120 bytes

~~~c

void FUN_00adfbd8(undefined8 param_1,undefined8 *param_2,undefined8 *param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  int extraout_var;
  int extraout_w1;
  int extraout_var_00;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  
                    /* try { // try from 00adfbec to 00bdfbef has its CatchHandler @ 00adfc44 */
  uVar4 = *param_3;
  uVar5 = *param_2;
                    /* try { // try from 00adfc04 to 00bdfc23 has its CatchHandler @ 00adfc40 */
  FUN_00444c54(uVar4,0xbe,0xbe,0xbe,0xff);
                    /* catch() { ... } // from try @ 00adf228 with catch @ 00adfc24
                       catch() { ... } // from try @ 00adf338 with catch @ 00adfc24
                       catch() { ... } // from try @ 00adf434 with catch @ 00adfc24
                       try { // try from 00adfc24 to 00bdfd23 has its CatchHandler @ 00adec50 */
                    /* catch() { ... } // from try @ 00adfbd0 with catch @ 00adfc28 */
                    /* catch() { ... } // from try @ 00adf074 with catch @ 00adfc2c */
                    /* catch() { ... } // from try @ 00adf070 with catch @ 00adfc30 */
                    /* catch() { ... } // from try @ 00adf020 with catch @ 00adfc34 */
  lVar3 = __dynamic_cast(DAT_00c24ab8,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00be8e98,
                         &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00be8ea8,0);
                    /* catch() { ... } // from try @ 00adef60 with catch @ 00adfc38 */
  uVar6 = *(undefined8 *)(lVar3 + 0x38);
                    /* catch() { ... } // from try @ 00adef9c with catch @ 00adfc3c
                       catch() { ... } // from try @ 00adf27c with catch @ 00adfc3c */
                    /* catch() { ... } // from try @ 00adfb98 with catch @ 00adfc40
                       catch() { ... } // from try @ 00adfc04 with catch @ 00adfc40 */
  iVar1 = FUN_00886014(uVar5);
                    /* catch() { ... } // from try @ 00adfb7c with catch @ 00adfc44
                       catch() { ... } // from try @ 00adfbb4 with catch @ 00adfc44
                       catch() { ... } // from try @ 00adfbec with catch @ 00adfc44 */
                    /* catch() { ... } // from try @ 00adf10c with catch @ 00adfc48 */
                    /* catch() { ... } // from try @ 00adf600 with catch @ 00adfc4c */
  FUN_00886014(uVar5);
                    /* catch() { ... } // from try @ 00adfaf8 with catch @ 00adfc50
                       catch() { ... } // from try @ 00adfb30 with catch @ 00adfc50 */
                    /* catch() { ... } // from try @ 00adee60 with catch @ 00adfc54 */
                    /* catch() { ... } // from try @ 00adecc4 with catch @ 00adfc58
                       catch() { ... } // from try @ 00adfadc with catch @ 00adfc58 */
  lVar3 = __dynamic_cast(DAT_00c24ab8,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00be8e98,
                         &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00be8ea8,0);
  iVar2 = FUN_00467c58(*(undefined8 *)(lVar3 + 0x38));
                    /* catch() { ... } // from try @ 00adfac4 with catch @ 00adfc74
                       catch() { ... } // from try @ 00adfb14 with catch @ 00adfc74
                       catch() { ... } // from try @ 00adfb64 with catch @ 00adfc74 */
                    /* catch() { ... } // from try @ 00adedb8 with catch @ 00adfc78 */
  FUN_00886014(uVar5);
                    /* catch() { ... } // from try @ 00adfa90 with catch @ 00adfc7c */
  FUN_00886014(uVar5);
                    /* catch() { ... } // from try @ 00adfa74 with catch @ 00adfc88
                       catch() { ... } // from try @ 00adfaac with catch @ 00adfc88 */
                    /* catch() { ... } // from try @ 00adfa40 with catch @ 00adfc9c */
                    /* catch() { ... } // from try @ 00adf8a0 with catch @ 00adfca0 */
                    /* catch() { ... } // from try @ 00adf850 with catch @ 00adfca4
                       catch() { ... } // from try @ 00adf8d8 with catch @ 00adfca4 */
  FUN_0044592c(uVar4,uVar6,(extraout_w1 + iVar1) - iVar2,extraout_var_00 + extraout_var,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adfbd8"></a> `00adfbd8` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00adfbdc"></a> `00adfbdc` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfbe0"></a> `00adfbe0` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adfbe4"></a> `00adfbe4` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adfbe8"></a> `00adfbe8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adfbec"></a> `00adfbec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00adfbf0"></a> `00adfbf0` | `53 00 40 f9` | ldr x19,[x2] | `FALL_THROUGH`
<a id="insn-00adfbf4"></a> `00adfbf4` | `34 00 40 f9` | ldr x20,[x1] | `FALL_THROUGH`
<a id="insn-00adfbf8"></a> `00adfbf8` | `c1 17 80 52` | mov w1,#0xbe | `FALL_THROUGH`
<a id="insn-00adfbfc"></a> `00adfbfc` | `c2 17 80 52` | mov w2,#0xbe | `FALL_THROUGH`
<a id="insn-00adfc00"></a> `00adfc00` | `c3 17 80 52` | mov w3,#0xbe | `FALL_THROUGH`
<a id="insn-00adfc04"></a> `00adfc04` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00adfc08"></a> `00adfc08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfc0c"></a> `00adfc0c` | `12 94 e5 97` | bl 0x00444c54 | `UNCONDITIONAL_CALL`
<a id="insn-00adfc10"></a> `00adfc10` | `39 0a 00 b0` | adrp x25,0xc24000 | `FALL_THROUGH`
<a id="insn-00adfc14"></a> `00adfc14` | `55 08 00 b0` | adrp x21,0xbe8000 | `FALL_THROUGH`
<a id="insn-00adfc18"></a> `00adfc18` | `b5 62 3a 91` | add x21,x21,#0xe98 | `FALL_THROUGH`
<a id="insn-00adfc1c"></a> `00adfc1c` | `20 5f 45 f9` | ldr x0,[x25, #0xab8] | `FALL_THROUGH`
<a id="insn-00adfc20"></a> `00adfc20` | `56 08 00 b0` | adrp x22,0xbe8000 | `FALL_THROUGH`
<a id="insn-00adfc24"></a> `00adfc24` | `d6 a2 3a 91` | add x22,x22,#0xea8 | `FALL_THROUGH`
<a id="insn-00adfc28"></a> `00adfc28` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00adfc2c"></a> `00adfc2c` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00adfc30"></a> `00adfc30` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00adfc34"></a> `00adfc34` | `e3 ee 03 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00adfc38"></a> `00adfc38` | `17 1c 40 f9` | ldr x23,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00adfc3c"></a> `00adfc3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adfc40"></a> `00adfc40` | `f5 98 f6 97` | bl 0x00886014 | `UNCONDITIONAL_CALL`
<a id="insn-00adfc44"></a> `00adfc44` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00adfc48"></a> `00adfc48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adfc4c"></a> `00adfc4c` | `f2 98 f6 97` | bl 0x00886014 | `UNCONDITIONAL_CALL`
<a id="insn-00adfc50"></a> `00adfc50` | `20 5f 45 f9` | ldr x0,[x25, #0xab8] | `FALL_THROUGH`
<a id="insn-00adfc54"></a> `00adfc54` | `38 00 18 0b` | add w24,w1,w24 | `FALL_THROUGH`
<a id="insn-00adfc58"></a> `00adfc58` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00adfc5c"></a> `00adfc5c` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00adfc60"></a> `00adfc60` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00adfc64"></a> `00adfc64` | `d7 ee 03 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00adfc68"></a> `00adfc68` | `00 1c 40 f9` | ldr x0,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00adfc6c"></a> `00adfc6c` | `fb 1f e6 97` | bl 0x00467c58 | `UNCONDITIONAL_CALL`
<a id="insn-00adfc70"></a> `00adfc70` | `15 03 00 4b` | sub w21,w24,w0 | `FALL_THROUGH`
<a id="insn-00adfc74"></a> `00adfc74` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adfc78"></a> `00adfc78` | `e7 98 f6 97` | bl 0x00886014 | `UNCONDITIONAL_CALL`
<a id="insn-00adfc7c"></a> `00adfc7c` | `16 fc 60 d3` | lsr x22,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00adfc80"></a> `00adfc80` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adfc84"></a> `00adfc84` | `e4 98 f6 97` | bl 0x00886014 | `UNCONDITIONAL_CALL`
<a id="insn-00adfc88"></a> `00adfc88` | `28 fc 60 d3` | lsr x8,x1,#0x20 | `FALL_THROUGH`
<a id="insn-00adfc8c"></a> `00adfc8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfc90"></a> `00adfc90` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00adfc94"></a> `00adfc94` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00adfc98"></a> `00adfc98` | `03 01 16 0b` | add w3,w8,w22 | `FALL_THROUGH`
<a id="insn-00adfc9c"></a> `00adfc9c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00adfca0"></a> `00adfca0` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adfca4"></a> `00adfca4` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfca8"></a> `00adfca8` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adfcac"></a> `00adfcac` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adfcb0"></a> `00adfcb0` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00adfcb4"></a> `00adfcb4` | `1e 97 e5 17` | b 0x0044592c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adfbd8`](#insn-00adfbd8) 範囲 `[['00adfbd8', '00adfbeb']]`
  - `FALL_THROUGH` [`00adfbe8`](#insn-00adfbe8) → [`00adfbec`](#insn-00adfbec)
- ブロック [`00adfbec`](#insn-00adfbec) 範囲 `[['00adfbec', '00adfc03']]`
  - `FALL_THROUGH` [`00adfc00`](#insn-00adfc00) → [`00adfc04`](#insn-00adfc04)
- ブロック [`00adfc04`](#insn-00adfc04) 範囲 `[['00adfc04', '00adfc23']]`
  - `FALL_THROUGH` [`00adfc20`](#insn-00adfc20) → [`00adfc24`](#insn-00adfc24)
- ブロック [`00adfc24`](#insn-00adfc24) 範囲 `[['00adfc24', '00adfc27']]`
  - `FALL_THROUGH` [`00adfc24`](#insn-00adfc24) → [`00adfc28`](#insn-00adfc28)
- ブロック [`00adfc28`](#insn-00adfc28) 範囲 `[['00adfc28', '00adfc2b']]`
  - `FALL_THROUGH` [`00adfc28`](#insn-00adfc28) → [`00adfc2c`](#insn-00adfc2c)
- ブロック [`00adfc2c`](#insn-00adfc2c) 範囲 `[['00adfc2c', '00adfc2f']]`
  - `FALL_THROUGH` [`00adfc2c`](#insn-00adfc2c) → [`00adfc30`](#insn-00adfc30)
- ブロック [`00adfc30`](#insn-00adfc30) 範囲 `[['00adfc30', '00adfc33']]`
  - `FALL_THROUGH` [`00adfc30`](#insn-00adfc30) → [`00adfc34`](#insn-00adfc34)
- ブロック [`00adfc34`](#insn-00adfc34) 範囲 `[['00adfc34', '00adfc37']]`
  - `FALL_THROUGH` [`00adfc34`](#insn-00adfc34) → [`00adfc38`](#insn-00adfc38)
- ブロック [`00adfc38`](#insn-00adfc38) 範囲 `[['00adfc38', '00adfc3b']]`
  - `FALL_THROUGH` [`00adfc38`](#insn-00adfc38) → [`00adfc3c`](#insn-00adfc3c)
- ブロック [`00adfc3c`](#insn-00adfc3c) 範囲 `[['00adfc3c', '00adfc3f']]`
  - `FALL_THROUGH` [`00adfc3c`](#insn-00adfc3c) → [`00adfc40`](#insn-00adfc40)
- ブロック [`00adfc40`](#insn-00adfc40) 範囲 `[['00adfc40', '00adfc43']]`
  - `FALL_THROUGH` [`00adfc40`](#insn-00adfc40) → [`00adfc44`](#insn-00adfc44)
- ブロック [`00adfc44`](#insn-00adfc44) 範囲 `[['00adfc44', '00adfc47']]`
  - `FALL_THROUGH` [`00adfc44`](#insn-00adfc44) → [`00adfc48`](#insn-00adfc48)
- ブロック [`00adfc48`](#insn-00adfc48) 範囲 `[['00adfc48', '00adfc4b']]`
  - `FALL_THROUGH` [`00adfc48`](#insn-00adfc48) → [`00adfc4c`](#insn-00adfc4c)
- ブロック [`00adfc4c`](#insn-00adfc4c) 範囲 `[['00adfc4c', '00adfc4f']]`
  - `FALL_THROUGH` [`00adfc4c`](#insn-00adfc4c) → [`00adfc50`](#insn-00adfc50)
- ブロック [`00adfc50`](#insn-00adfc50) 範囲 `[['00adfc50', '00adfc53']]`
  - `FALL_THROUGH` [`00adfc50`](#insn-00adfc50) → [`00adfc54`](#insn-00adfc54)
- ブロック [`00adfc54`](#insn-00adfc54) 範囲 `[['00adfc54', '00adfc57']]`
  - `FALL_THROUGH` [`00adfc54`](#insn-00adfc54) → [`00adfc58`](#insn-00adfc58)
- ブロック [`00adfc58`](#insn-00adfc58) 範囲 `[['00adfc58', '00adfc73']]`
  - `FALL_THROUGH` [`00adfc70`](#insn-00adfc70) → [`00adfc74`](#insn-00adfc74)
- ブロック [`00adfc74`](#insn-00adfc74) 範囲 `[['00adfc74', '00adfc77']]`
  - `FALL_THROUGH` [`00adfc74`](#insn-00adfc74) → [`00adfc78`](#insn-00adfc78)
- ブロック [`00adfc78`](#insn-00adfc78) 範囲 `[['00adfc78', '00adfc7b']]`
  - `FALL_THROUGH` [`00adfc78`](#insn-00adfc78) → [`00adfc7c`](#insn-00adfc7c)
- ブロック [`00adfc7c`](#insn-00adfc7c) 範囲 `[['00adfc7c', '00adfc87']]`
  - `FALL_THROUGH` [`00adfc84`](#insn-00adfc84) → [`00adfc88`](#insn-00adfc88)
- ブロック [`00adfc88`](#insn-00adfc88) 範囲 `[['00adfc88', '00adfc9b']]`
  - `FALL_THROUGH` [`00adfc98`](#insn-00adfc98) → [`00adfc9c`](#insn-00adfc9c)
- ブロック [`00adfc9c`](#insn-00adfc9c) 範囲 `[['00adfc9c', '00adfc9f']]`
  - `FALL_THROUGH` [`00adfc9c`](#insn-00adfc9c) → [`00adfca0`](#insn-00adfca0)
- ブロック [`00adfca0`](#insn-00adfca0) 範囲 `[['00adfca0', '00adfca3']]`
  - `FALL_THROUGH` [`00adfca0`](#insn-00adfca0) → [`00adfca4`](#insn-00adfca4)
- ブロック [`00adfca4`](#insn-00adfca4) 範囲 `[['00adfca4', '00adfcb7']]`

## 命令位置別の参照

- [`00adfbd8`](#insn-00adfbd8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfbdc`](#insn-00adfbdc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfbe0`](#insn-00adfbe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfbe4`](#insn-00adfbe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfbe8`](#insn-00adfbe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc0c`](#insn-00adfc0c) → [`00444c54`](../00444/00444c54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00444c54` · 推定シンボル `None` · 推定型 `None`
- [`00adfc1c`](#insn-00adfc1c) → `00c24ab8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfc28`](#insn-00adfc28) → `00be8e98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00adfc2c`](#insn-00adfc2c) → `00be8ea8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00adfc34`](#insn-00adfc34) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00adfc40`](#insn-00adfc40) → [`00886014`](../00886/00886014.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00886014` · 推定シンボル `None` · 推定型 `None`
- [`00adfc4c`](#insn-00adfc4c) → [`00886014`](../00886/00886014.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00886014` · 推定シンボル `None` · 推定型 `None`
- [`00adfc50`](#insn-00adfc50) → `00c24ab8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfc58`](#insn-00adfc58) → `00be8e98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00adfc5c`](#insn-00adfc5c) → `00be8ea8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00adfc64`](#insn-00adfc64) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00adfc6c`](#insn-00adfc6c) → [`00467c58`](../00467/00467c58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467c58` · 推定シンボル `None` · 推定型 `None`
- [`00adfc78`](#insn-00adfc78) → [`00886014`](../00886/00886014.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00886014` · 推定シンボル `None` · 推定型 `None`
- [`00adfc84`](#insn-00adfc84) → [`00886014`](../00886/00886014.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00886014` · 推定シンボル `None` · 推定型 `None`
- [`00adfca0`](#insn-00adfca0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfca4`](#insn-00adfca4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfca8`](#insn-00adfca8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcac`](#insn-00adfcac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcb0`](#insn-00adfcb0) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcb4`](#insn-00adfcb4) → [`0044592c`](../00445/0044592c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044592c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adfbd8`](#insn-00adfbd8)

~~~json
{
  "source": "00adfbd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfbdc`](#insn-00adfbdc)

~~~json
{
  "source": "00adfbdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfbe0`](#insn-00adfbe0)

~~~json
{
  "source": "00adfbe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfbe4`](#insn-00adfbe4)

~~~json
{
  "source": "00adfbe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfbe8`](#insn-00adfbe8)

~~~json
{
  "source": "00adfbe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc0c`](#insn-00adfc0c)

~~~json
{
  "source": "00adfc0c",
  "target": "00444c54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfc1c`](#insn-00adfc1c)

~~~json
{
  "source": "00adfc1c",
  "target": "00c24ab8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24ab8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfc28`](#insn-00adfc28)

~~~json
{
  "source": "00adfc28",
  "target": "00be8e98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be8e98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adfc2c`](#insn-00adfc2c)

~~~json
{
  "source": "00adfc2c",
  "target": "00be8ea8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be8ea8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adfc34`](#insn-00adfc34)

~~~json
{
  "source": "00adfc34",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfc40`](#insn-00adfc40)

~~~json
{
  "source": "00adfc40",
  "target": "00886014",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfc4c`](#insn-00adfc4c)

~~~json
{
  "source": "00adfc4c",
  "target": "00886014",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfc50`](#insn-00adfc50)

~~~json
{
  "source": "00adfc50",
  "target": "00c24ab8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24ab8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfc58`](#insn-00adfc58)

~~~json
{
  "source": "00adfc58",
  "target": "00be8e98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be8e98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adfc5c`](#insn-00adfc5c)

~~~json
{
  "source": "00adfc5c",
  "target": "00be8ea8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be8ea8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adfc64`](#insn-00adfc64)

~~~json
{
  "source": "00adfc64",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfc6c`](#insn-00adfc6c)

~~~json
{
  "source": "00adfc6c",
  "target": "00467c58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfc78`](#insn-00adfc78)

~~~json
{
  "source": "00adfc78",
  "target": "00886014",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfc84`](#insn-00adfc84)

~~~json
{
  "source": "00adfc84",
  "target": "00886014",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfca0`](#insn-00adfca0)

~~~json
{
  "source": "00adfca0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfca4`](#insn-00adfca4)

~~~json
{
  "source": "00adfca4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfca8`](#insn-00adfca8)

~~~json
{
  "source": "00adfca8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcac`](#insn-00adfcac)

~~~json
{
  "source": "00adfcac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcb0`](#insn-00adfcb0)

~~~json
{
  "source": "00adfcb0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcb4`](#insn-00adfcb4)

~~~json
{
  "source": "00adfcb4",
  "target": "0044592c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
