# 00b0cfcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b0cf88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cf88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0009.md#compare-62736d35255178387459280806d19c58)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b6d140`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d140.md) · 移動量 `+0x60174`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0062.md#compare-3d28e4fa1e73cd51cea692a6a657c303)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0cfcc",
  "name": "_ZN11flatbuffers11SymbolTableINS_10ServiceDefEED2Ev",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c27ed1249d4d905fedae3fc2e41b63a7fd8b108184eeb399359b984c0490946f",
  "source_text_sha256": "c27ed1249d4d905fedae3fc2e41b63a7fd8b108184eeb399359b984c0490946f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0cfcc",
        "00b0d0b3"
      ]
    ],
    "bytes_sha256": "ec07fd971788b2c31d71b9fb0b3bea229ee88fa4f940184fa488ed5d0b2bd4da",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdea20](../00bde/00bdea20.md)

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00bde9f0](../00bde/00bde9f0.md)
- [00bdeb80](../00bde/00bdeb80.md)
- [00bdebd0](../00bde/00bdebd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2549 bytes

~~~c

void _ZN11flatbuffers11SymbolTableINS_10ServiceDefEED2Ev(long param_1)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  undefined8 *__ptr;
  void *__ptr_00;
  void *__ptr_01;
  
                    /* try { // try from 00b0cfe0 to 00c0cfe7 has its CatchHandler @ 00b0cffc */
  __ptr = *(undefined8 **)(param_1 + 0x18);
  puVar1 = *(undefined8 **)(param_1 + 0x20);
                    /* catch() { ... } // from try @ 00b0cf70 with catch @ 00b0cfe8
                       try { // try from 00b0cfe8 to 00c0d02f has its CatchHandler @ 00b0ce38 */
                    /* catch() { ... } // from try @ 00b0cf1c with catch @ 00b0cfec */
  if (__ptr != puVar1) {
    do {
      __ptr_00 = (void *)*__ptr;
      if (__ptr_00 != (void *)0x0) {
        puVar1 = *(undefined8 **)((long)__ptr_00 + 0xb0);
        puVar2 = *(undefined8 **)((long)__ptr_00 + 0xb8);
        if (puVar1 != puVar2) {
          do {
            __ptr_01 = (void *)*puVar1;
            if (__ptr_01 != (void *)0x0) {
              _ZN11flatbuffers10DefinitionD2Ev(__ptr_01);
              _ZdlPv(__ptr_01);
              puVar2 = *(undefined8 **)((long)__ptr_00 + 0xb8);
            }
            puVar1 = puVar1 + 1;
          } while (puVar1 != puVar2);
          puVar1 = *(undefined8 **)((long)__ptr_00 + 0xb0);
        }
        if (puVar1 != (undefined8 *)0x0) {
          *(undefined8 **)((long)__ptr_00 + 0xb8) = puVar1;
          _ZdlPv(puVar1);
        }
        _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE7destroyEPNS_11__tree_nodeISB_PvEE
                  ((long)__ptr_00 + 0x98,*(undefined8 *)((long)__ptr_00 + 0xa0));
        _ZN11flatbuffers10DefinitionD2Ev(__ptr_00);
        _ZdlPv(__ptr_00);
        puVar1 = *(undefined8 **)(param_1 + 0x20);
      }
      __ptr = __ptr + 1;
    } while (__ptr != puVar1);
    __ptr = *(undefined8 **)(param_1 + 0x18);
  }
  if (__ptr != (undefined8 *)0x0) {
    *(undefined8 **)(param_1 + 0x20) = __ptr;
                    /* catch() { ... } // from try @ 00b0cea4 with catch @ 00b0cffc
                       catch() { ... } // from try @ 00b0cfe0 with catch @ 00b0cffc */
    _ZdlPv(__ptr);
  }
  _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE7destroyEPNS_11__tree_nodeISB_PvEE
            (param_1,*(undefined8 *)(param_1 + 8));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b0cfcc"></a> `00b0cfcc` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00b0cfd0"></a> `00b0cfd0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cfd4"></a> `00b0cfd4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0cfd8"></a> `00b0cfd8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0cfdc"></a> `00b0cfdc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b0cfe0"></a> `00b0cfe0` | `14 a0 41 a9` | ldp x20,x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00b0cfe4"></a> `00b0cfe4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b0cfe8"></a> `00b0cfe8` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00b0cfec"></a> `00b0cfec` | `e1 02 00 54` | b.ne 0x00b0d048 | `CONDITIONAL_JUMP`
<a id="insn-00b0cff0"></a> `00b0cff0` | `94 00 00 b4` | cbz x20,0x00b0d000 | `CONDITIONAL_JUMP`
<a id="insn-00b0cff4"></a> `00b0cff4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0cff8"></a> `00b0cff8` | `74 12 00 f9` | str x20,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b0cffc"></a> `00b0cffc` | `19 38 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b0d000"></a> `00b0d000` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b0d004"></a> `00b0d004` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b0d008"></a> `00b0d008` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0d00c"></a> `00b0d00c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0d010"></a> `00b0d010` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0d014"></a> `00b0d014` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00b0d018"></a> `00b0d018` | `da 46 03 14` | b 0x00bdeb80 | `CALL_TERMINATOR`
<a id="insn-00b0d01c"></a> `00b0d01c` | `a1 52 40 f9` | ldr x1,[x21, #0xa0] | `FALL_THROUGH`
<a id="insn-00b0d020"></a> `00b0d020` | `a0 62 02 91` | add x0,x21,#0x98 | `FALL_THROUGH`
<a id="insn-00b0d024"></a> `00b0d024` | `eb 46 03 94` | bl 0x00bdebd0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0d028"></a> `00b0d028` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b0d02c"></a> `00b0d02c` | `71 46 03 94` | bl 0x00bde9f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0d030"></a> `00b0d030` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b0d034"></a> `00b0d034` | `0b 38 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b0d038"></a> `00b0d038` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b0d03c"></a> `00b0d03c` | `94 22 00 91` | add x20,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00b0d040"></a> `00b0d040` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00b0d044"></a> `00b0d044` | `20 03 00 54` | b.eq 0x00b0d0a8 | `CONDITIONAL_JUMP`
<a id="insn-00b0d048"></a> `00b0d048` | `95 02 40 f9` | ldr x21,[x20] | `FALL_THROUGH`
<a id="insn-00b0d04c"></a> `00b0d04c` | `95 ff ff b4` | cbz x21,0x00b0d03c | `CONDITIONAL_JUMP`
<a id="insn-00b0d050"></a> `00b0d050` | `b6 22 4b a9` | ldp x22,x8,[x21, #0xb0] | `FALL_THROUGH`
<a id="insn-00b0d054"></a> `00b0d054` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00b0d058"></a> `00b0d058` | `c1 00 00 54` | b.ne 0x00b0d070 | `CONDITIONAL_JUMP`
<a id="insn-00b0d05c"></a> `00b0d05c` | `f6 01 00 b5` | cbnz x22,0x00b0d098 | `CONDITIONAL_JUMP`
<a id="insn-00b0d060"></a> `00b0d060` | `ef ff ff 17` | b 0x00b0d01c | `UNCONDITIONAL_JUMP`
<a id="insn-00b0d064"></a> `00b0d064` | `d6 22 00 91` | add x22,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00b0d068"></a> `00b0d068` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00b0d06c"></a> `00b0d06c` | `20 01 00 54` | b.eq 0x00b0d090 | `CONDITIONAL_JUMP`
<a id="insn-00b0d070"></a> `00b0d070` | `d7 02 40 f9` | ldr x23,[x22] | `FALL_THROUGH`
<a id="insn-00b0d074"></a> `00b0d074` | `97 ff ff b4` | cbz x23,0x00b0d064 | `CONDITIONAL_JUMP`
<a id="insn-00b0d078"></a> `00b0d078` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b0d07c"></a> `00b0d07c` | `5d 46 03 94` | bl 0x00bde9f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0d080"></a> `00b0d080` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b0d084"></a> `00b0d084` | `f7 37 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b0d088"></a> `00b0d088` | `a8 5e 40 f9` | ldr x8,[x21, #0xb8] | `FALL_THROUGH`
<a id="insn-00b0d08c"></a> `00b0d08c` | `f6 ff ff 17` | b 0x00b0d064 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0d090"></a> `00b0d090` | `b6 5a 40 f9` | ldr x22,[x21, #0xb0] | `FALL_THROUGH`
<a id="insn-00b0d094"></a> `00b0d094` | `56 fc ff b4` | cbz x22,0x00b0d01c | `CONDITIONAL_JUMP`
<a id="insn-00b0d098"></a> `00b0d098` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b0d09c"></a> `00b0d09c` | `b6 5e 00 f9` | str x22,[x21, #0xb8] | `FALL_THROUGH`
<a id="insn-00b0d0a0"></a> `00b0d0a0` | `f0 37 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b0d0a4"></a> `00b0d0a4` | `de ff ff 17` | b 0x00b0d01c | `UNCONDITIONAL_JUMP`
<a id="insn-00b0d0a8"></a> `00b0d0a8` | `74 0e 40 f9` | ldr x20,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b0d0ac"></a> `00b0d0ac` | `54 fa ff b5` | cbnz x20,0x00b0cff4 | `CONDITIONAL_JUMP`
<a id="insn-00b0d0b0"></a> `00b0d0b0` | `d4 ff ff 17` | b 0x00b0d000 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b0cfcc`](#insn-00b0cfcc) 範囲 `[['00b0cfcc', '00b0cfdf']]`
  - `FALL_THROUGH` [`00b0cfdc`](#insn-00b0cfdc) → [`00b0cfe0`](#insn-00b0cfe0)
- ブロック [`00b0cfe0`](#insn-00b0cfe0) 範囲 `[['00b0cfe0', '00b0cfe7']]`
  - `FALL_THROUGH` [`00b0cfe4`](#insn-00b0cfe4) → [`00b0cfe8`](#insn-00b0cfe8)
- ブロック [`00b0cfe8`](#insn-00b0cfe8) 範囲 `[['00b0cfe8', '00b0cfeb']]`
  - `FALL_THROUGH` [`00b0cfe8`](#insn-00b0cfe8) → [`00b0cfec`](#insn-00b0cfec)
- ブロック [`00b0cfec`](#insn-00b0cfec) 範囲 `[['00b0cfec', '00b0cfef']]`
  - `CONDITIONAL_JUMP` [`00b0cfec`](#insn-00b0cfec) → [`00b0d048`](#insn-00b0d048)
  - `FALL_THROUGH` [`00b0cfec`](#insn-00b0cfec) → [`00b0cff0`](#insn-00b0cff0)
- ブロック [`00b0cff0`](#insn-00b0cff0) 範囲 `[['00b0cff0', '00b0cff3']]`
  - `CONDITIONAL_JUMP` [`00b0cff0`](#insn-00b0cff0) → [`00b0d000`](#insn-00b0d000)
  - `FALL_THROUGH` [`00b0cff0`](#insn-00b0cff0) → [`00b0cff4`](#insn-00b0cff4)
- ブロック [`00b0cff4`](#insn-00b0cff4) 範囲 `[['00b0cff4', '00b0cffb']]`
  - `FALL_THROUGH` [`00b0cff8`](#insn-00b0cff8) → [`00b0cffc`](#insn-00b0cffc)
- ブロック [`00b0cffc`](#insn-00b0cffc) 範囲 `[['00b0cffc', '00b0cfff']]`
  - `FALL_THROUGH` [`00b0cffc`](#insn-00b0cffc) → [`00b0d000`](#insn-00b0d000)
- ブロック [`00b0d000`](#insn-00b0d000) 範囲 `[['00b0d000', '00b0d01b']]`
- ブロック [`00b0d01c`](#insn-00b0d01c) 範囲 `[['00b0d01c', '00b0d03b']]`
  - `FALL_THROUGH` [`00b0d038`](#insn-00b0d038) → [`00b0d03c`](#insn-00b0d03c)
- ブロック [`00b0d03c`](#insn-00b0d03c) 範囲 `[['00b0d03c', '00b0d047']]`
  - `CONDITIONAL_JUMP` [`00b0d044`](#insn-00b0d044) → [`00b0d0a8`](#insn-00b0d0a8)
  - `FALL_THROUGH` [`00b0d044`](#insn-00b0d044) → [`00b0d048`](#insn-00b0d048)
- ブロック [`00b0d048`](#insn-00b0d048) 範囲 `[['00b0d048', '00b0d04f']]`
  - `CONDITIONAL_JUMP` [`00b0d04c`](#insn-00b0d04c) → [`00b0d03c`](#insn-00b0d03c)
  - `FALL_THROUGH` [`00b0d04c`](#insn-00b0d04c) → [`00b0d050`](#insn-00b0d050)
- ブロック [`00b0d050`](#insn-00b0d050) 範囲 `[['00b0d050', '00b0d05b']]`
  - `CONDITIONAL_JUMP` [`00b0d058`](#insn-00b0d058) → [`00b0d070`](#insn-00b0d070)
  - `FALL_THROUGH` [`00b0d058`](#insn-00b0d058) → [`00b0d05c`](#insn-00b0d05c)
- ブロック [`00b0d05c`](#insn-00b0d05c) 範囲 `[['00b0d05c', '00b0d05f']]`
  - `CONDITIONAL_JUMP` [`00b0d05c`](#insn-00b0d05c) → [`00b0d098`](#insn-00b0d098)
  - `FALL_THROUGH` [`00b0d05c`](#insn-00b0d05c) → [`00b0d060`](#insn-00b0d060)
- ブロック [`00b0d060`](#insn-00b0d060) 範囲 `[['00b0d060', '00b0d063']]`
  - `UNCONDITIONAL_JUMP` [`00b0d060`](#insn-00b0d060) → [`00b0d01c`](#insn-00b0d01c)
- ブロック [`00b0d064`](#insn-00b0d064) 範囲 `[['00b0d064', '00b0d06f']]`
  - `CONDITIONAL_JUMP` [`00b0d06c`](#insn-00b0d06c) → [`00b0d090`](#insn-00b0d090)
  - `FALL_THROUGH` [`00b0d06c`](#insn-00b0d06c) → [`00b0d070`](#insn-00b0d070)
- ブロック [`00b0d070`](#insn-00b0d070) 範囲 `[['00b0d070', '00b0d077']]`
  - `CONDITIONAL_JUMP` [`00b0d074`](#insn-00b0d074) → [`00b0d064`](#insn-00b0d064)
  - `FALL_THROUGH` [`00b0d074`](#insn-00b0d074) → [`00b0d078`](#insn-00b0d078)
- ブロック [`00b0d078`](#insn-00b0d078) 範囲 `[['00b0d078', '00b0d08f']]`
  - `UNCONDITIONAL_JUMP` [`00b0d08c`](#insn-00b0d08c) → [`00b0d064`](#insn-00b0d064)
- ブロック [`00b0d090`](#insn-00b0d090) 範囲 `[['00b0d090', '00b0d097']]`
  - `CONDITIONAL_JUMP` [`00b0d094`](#insn-00b0d094) → [`00b0d01c`](#insn-00b0d01c)
  - `FALL_THROUGH` [`00b0d094`](#insn-00b0d094) → [`00b0d098`](#insn-00b0d098)
- ブロック [`00b0d098`](#insn-00b0d098) 範囲 `[['00b0d098', '00b0d0a7']]`
  - `UNCONDITIONAL_JUMP` [`00b0d0a4`](#insn-00b0d0a4) → [`00b0d01c`](#insn-00b0d01c)
- ブロック [`00b0d0a8`](#insn-00b0d0a8) 範囲 `[['00b0d0a8', '00b0d0af']]`
  - `CONDITIONAL_JUMP` [`00b0d0ac`](#insn-00b0d0ac) → [`00b0cff4`](#insn-00b0cff4)
  - `FALL_THROUGH` [`00b0d0ac`](#insn-00b0d0ac) → [`00b0d0b0`](#insn-00b0d0b0)
- ブロック [`00b0d0b0`](#insn-00b0d0b0) 範囲 `[['00b0d0b0', '00b0d0b3']]`
  - `UNCONDITIONAL_JUMP` [`00b0d0b0`](#insn-00b0d0b0) → [`00b0d000`](#insn-00b0d000)

## 命令位置別の参照

- [`00b0cfcc`](#insn-00b0cfcc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cfd0`](#insn-00b0cfd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cfd4`](#insn-00b0cfd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cfd8`](#insn-00b0cfd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cfec`](#insn-00b0cfec) → [`00b0d048`](#insn-00b0d048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cff0`](#insn-00b0cff0) → [`00b0d000`](#insn-00b0d000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cffc`](#insn-00b0cffc) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b0d008`](#insn-00b0d008) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0d00c`](#insn-00b0d00c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0d010`](#insn-00b0d010) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0d018`](#insn-00b0d018) → [`00bdeb80`](../00bde/00bdeb80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdeb80` · 推定シンボル `None` · 推定型 `None`
- [`00b0d024`](#insn-00b0d024) → [`00bdebd0`](../00bde/00bdebd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdebd0` · 推定シンボル `None` · 推定型 `None`
- [`00b0d02c`](#insn-00b0d02c) → [`00bde9f0`](../00bde/00bde9f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde9f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0d034`](#insn-00b0d034) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b0d044`](#insn-00b0d044) → [`00b0d0a8`](#insn-00b0d0a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0d04c`](#insn-00b0d04c) → [`00b0d03c`](#insn-00b0d03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0d058`](#insn-00b0d058) → [`00b0d070`](#insn-00b0d070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0d05c`](#insn-00b0d05c) → [`00b0d098`](#insn-00b0d098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0d060`](#insn-00b0d060) → [`00b0d01c`](#insn-00b0d01c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0d06c`](#insn-00b0d06c) → [`00b0d090`](#insn-00b0d090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0d074`](#insn-00b0d074) → [`00b0d064`](#insn-00b0d064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0d07c`](#insn-00b0d07c) → [`00bde9f0`](../00bde/00bde9f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde9f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0d084`](#insn-00b0d084) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b0d08c`](#insn-00b0d08c) → [`00b0d064`](#insn-00b0d064) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0d094`](#insn-00b0d094) → [`00b0d01c`](#insn-00b0d01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0d0a0`](#insn-00b0d0a0) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b0d0a4`](#insn-00b0d0a4) → [`00b0d01c`](#insn-00b0d01c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0d0ac`](#insn-00b0d0ac) → [`00b0cff4`](#insn-00b0cff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0d0b0`](#insn-00b0d0b0) → [`00b0d000`](#insn-00b0d000) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0cfcc`](#insn-00b0cfcc)

~~~json
{
  "source": "00b0cfcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cfd0`](#insn-00b0cfd0)

~~~json
{
  "source": "00b0cfd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cfd4`](#insn-00b0cfd4)

~~~json
{
  "source": "00b0cfd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cfd8`](#insn-00b0cfd8)

~~~json
{
  "source": "00b0cfd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cfec`](#insn-00b0cfec)

~~~json
{
  "source": "00b0cfec",
  "target": "00b0d048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cff0`](#insn-00b0cff0)

~~~json
{
  "source": "00b0cff0",
  "target": "00b0d000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cffc`](#insn-00b0cffc)

~~~json
{
  "source": "00b0cffc",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0d008`](#insn-00b0d008)

~~~json
{
  "source": "00b0d008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0d00c`](#insn-00b0d00c)

~~~json
{
  "source": "00b0d00c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0d010`](#insn-00b0d010)

~~~json
{
  "source": "00b0d010",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0d018`](#insn-00b0d018)

~~~json
{
  "source": "00b0d018",
  "target": "00bdeb80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0d024`](#insn-00b0d024)

~~~json
{
  "source": "00b0d024",
  "target": "00bdebd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0d02c`](#insn-00b0d02c)

~~~json
{
  "source": "00b0d02c",
  "target": "00bde9f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0d034`](#insn-00b0d034)

~~~json
{
  "source": "00b0d034",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0d044`](#insn-00b0d044)

~~~json
{
  "source": "00b0d044",
  "target": "00b0d0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0d04c`](#insn-00b0d04c)

~~~json
{
  "source": "00b0d04c",
  "target": "00b0d03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0d058`](#insn-00b0d058)

~~~json
{
  "source": "00b0d058",
  "target": "00b0d070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0d05c`](#insn-00b0d05c)

~~~json
{
  "source": "00b0d05c",
  "target": "00b0d098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0d060`](#insn-00b0d060)

~~~json
{
  "source": "00b0d060",
  "target": "00b0d01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0d06c`](#insn-00b0d06c)

~~~json
{
  "source": "00b0d06c",
  "target": "00b0d090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0d074`](#insn-00b0d074)

~~~json
{
  "source": "00b0d074",
  "target": "00b0d064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0d07c`](#insn-00b0d07c)

~~~json
{
  "source": "00b0d07c",
  "target": "00bde9f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0d084`](#insn-00b0d084)

~~~json
{
  "source": "00b0d084",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0d08c`](#insn-00b0d08c)

~~~json
{
  "source": "00b0d08c",
  "target": "00b0d064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0d094`](#insn-00b0d094)

~~~json
{
  "source": "00b0d094",
  "target": "00b0d01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0d0a0`](#insn-00b0d0a0)

~~~json
{
  "source": "00b0d0a0",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0d0a4`](#insn-00b0d0a4)

~~~json
{
  "source": "00b0d0a4",
  "target": "00b0d01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0d0ac`](#insn-00b0d0ac)

~~~json
{
  "source": "00b0d0ac",
  "target": "00b0cff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0d0b0`](#insn-00b0d0b0)

~~~json
{
  "source": "00b0d0b0",
  "target": "00b0d000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
