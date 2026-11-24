# 00bfacb4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfa88c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa88c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-be93438562e67bc96becebe03ab9fdd6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfad50`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-47a8a3b4d645834483eb3d70d4e4c034)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfacb4",
  "name": "_ZNSt6__ndk113random_deviceC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "36b58cce38a11c2386bd499de5f82c52de0ab6a0f5711b84de4cdde2d82d0a41",
  "source_text_sha256": "36b58cce38a11c2386bd499de5f82c52de0ab6a0f5711b84de4cdde2d82d0a41",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfacb4",
        "00bfad3b"
      ]
    ],
    "bytes_sha256": "b936620411dccdb63341dfe97a75818786ac4b6372a0bd60a20eaca03bb29c6c",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c583a0](../00c58/00c583a0.md)

## 呼び出し先

- [00c580b0](../00c58/00c580b0.md)
- [00c580c0](../00c58/00c580c0.md)
- [00c58120](../00c58/00c58120.md)
- [00c5d610](../00c5d/00c5d610.md)

## 関連文字列（未確認候補）

~~~text
"random_device failed to open "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 877 bytes

~~~c

void _ZNSt6__ndk113random_deviceC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
               (int *param_1,byte *param_2)

{
  undefined4 uVar1;
  int iVar2;
  undefined4 *puVar3;
  byte *__file;
  byte local_38;
  undefined1 auStack_37 [15];
  undefined1 *local_28;
  
  __file = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    __file = param_2 + 1;
  }
  iVar2 = open((char *)__file,0);
  *param_1 = iVar2;
  if (-1 < iVar2) {
    return;
  }
  puVar3 = (undefined4 *)__errno();
  uVar1 = *puVar3;
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (&local_38,"random_device failed to open ",param_2);
  if ((local_38 & 1) == 0) {
    local_28 = auStack_37;
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(uVar1,local_28);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfacb4"></a> `00bfacb4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfacb8"></a> `00bfacb8` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfacbc"></a> `00bfacbc` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfacc0"></a> `00bfacc0` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfacc4"></a> `00bfacc4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bfacc8"></a> `00bfacc8` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00bfaccc"></a> `00bfaccc` | `29 08 40 f9` | ldr x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bfacd0"></a> `00bfacd0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bfacd4"></a> `00bfacd4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfacd8"></a> `00bfacd8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfacdc"></a> `00bfacdc` | `20 15 81 9a` | csinc x0,x9,x1,ne | `FALL_THROUGH`
<a id="insn-00bface0"></a> `00bface0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bface4"></a> `00bface4` | `4b 8a 01 94` | bl 0x00c5d610 | `UNCONDITIONAL_CALL`
<a id="insn-00bface8"></a> `00bface8` | `80 02 00 b9` | str w0,[x20] | `FALL_THROUGH`
<a id="insn-00bfacec"></a> `00bfacec` | `c0 00 f8 37` | tbnz w0,#0x1f,0x00bfad04 | `CONDITIONAL_JUMP`
<a id="insn-00bfacf0"></a> `00bfacf0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfacf4"></a> `00bfacf4` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfacf8"></a> `00bfacf8` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfacfc"></a> `00bfacfc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfad00"></a> `00bfad00` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfad04"></a> `00bfad04` | `ef 74 01 94` | bl 0x00c580c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfad08"></a> `00bfad08` | `14 00 40 b9` | ldr w20,[x0] | `FALL_THROUGH`
<a id="insn-00bfad0c"></a> `00bfad0c` | `c0 b5 ff d0` | adrp x0,0x2b4000 | `FALL_THROUGH`
<a id="insn-00bfad10"></a> `00bfad10` | `00 08 28 91` | add x0,x0,#0xa02 | `FALL_THROUGH`
<a id="insn-00bfad14"></a> `00bfad14` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfad18"></a> `00bfad18` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfad1c"></a> `00bfad1c` | `f3 23 00 91` | add x19,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfad20"></a> `00bfad20` | `e4 74 01 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfad24"></a> `00bfad24` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfad28"></a> `00bfad28` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bfad2c"></a> `00bfad2c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfad30"></a> `00bfad30` | `21 15 93 9a` | csinc x1,x9,x19,ne | `FALL_THROUGH`
<a id="insn-00bfad34"></a> `00bfad34` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00bfad38"></a> `00bfad38` | `fa 74 01 94` | bl 0x00c58120 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfacb4`](#insn-00bfacb4) 範囲 `[['00bfacb4', '00bfacef']]`
  - `CONDITIONAL_JUMP` [`00bfacec`](#insn-00bfacec) → [`00bfad04`](#insn-00bfad04)
  - `FALL_THROUGH` [`00bfacec`](#insn-00bfacec) → [`00bfacf0`](#insn-00bfacf0)
- ブロック [`00bfacf0`](#insn-00bfacf0) 範囲 `[['00bfacf0', '00bfad03']]`
- ブロック [`00bfad04`](#insn-00bfad04) 範囲 `[['00bfad04', '00bfad3b']]`

## 命令位置別の参照

- [`00bfacbc`](#insn-00bfacbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfacc0`](#insn-00bfacc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bface4`](#insn-00bface4) → [`00c5d610`](../00c5d/00c5d610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d610` · 推定シンボル `None` · 推定型 `None`
- [`00bfacec`](#insn-00bfacec) → [`00bfad04`](#insn-00bfad04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfacf0`](#insn-00bfacf0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfacf4`](#insn-00bfacf4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfad04`](#insn-00bfad04) → [`00c580c0`](../00c58/00c580c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580c0` · 推定シンボル `None` · 推定型 `None`
- [`00bfad10`](#insn-00bfad10) → `002b4a02`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfad20`](#insn-00bfad20) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bfad24`](#insn-00bfad24) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfad28`](#insn-00bfad28) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfad38`](#insn-00bfad38) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfacbc`](#insn-00bfacbc)

~~~json
{
  "source": "00bfacbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfacc0`](#insn-00bfacc0)

~~~json
{
  "source": "00bfacc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bface4`](#insn-00bface4)

~~~json
{
  "source": "00bface4",
  "target": "00c5d610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfacec`](#insn-00bfacec)

~~~json
{
  "source": "00bfacec",
  "target": "00bfad04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfacf0`](#insn-00bfacf0)

~~~json
{
  "source": "00bfacf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfacf4`](#insn-00bfacf4)

~~~json
{
  "source": "00bfacf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfad04`](#insn-00bfad04)

~~~json
{
  "source": "00bfad04",
  "target": "00c580c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfad10`](#insn-00bfad10)

~~~json
{
  "source": "00bfad10",
  "target": "002b4a02",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b4a02",
  "offset": 0,
  "size": 30,
  "datatype": "string",
  "bytes": "72616e646f6d5f646576696365206661696c656420746f206f70656e2000",
  "capture_start": "002b4a02",
  "capture_bytes": 30,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfad20`](#insn-00bfad20)

~~~json
{
  "source": "00bfad20",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfad24`](#insn-00bfad24)

~~~json
{
  "source": "00bfad24",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfad28`](#insn-00bfad28)

~~~json
{
  "source": "00bfad28",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfad38`](#insn-00bfad38)

~~~json
{
  "source": "00bfad38",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
