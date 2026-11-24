# 00bb5acc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bb5a88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5a88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-411f40608cd00fa33a1cc29dbda9609b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c32514`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c32514.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0076.md#compare-6cb6c3cf75e4f85732121abd693eabc6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb5acc",
  "name": "_ZNSt6__ndk110__time_putC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1d745c7a23b71a2781e486e1f315c346c39e55eebc7768dbc8fa8c5601ff80b9",
  "source_text_sha256": "1d745c7a23b71a2781e486e1f315c346c39e55eebc7768dbc8fa8c5601ff80b9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb5acc",
        "00bb5b67"
      ]
    ],
    "bytes_sha256": "9bc7fd940b3c02e5c2d462eb6ad00982eec12a424c64119edab8c7729754200f",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be18c0](../00be1/00be18c0.md)

## 呼び出し先

- [00bd70ec](../00bd7/00bd70ec.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb260](../00bdb/00bdb260.md)
- [00be0fb0](../00be0/00be0fb0.md)
- [00be1570](../00be1/00be1570.md)

## 関連文字列（未確認候補）

~~~text
"time_put_byname failed to construct for "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1090 bytes

~~~c

void _ZNSt6__ndk110__time_putC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
               (undefined8 *param_1,byte *param_2)

{
  undefined1 *puVar1;
  __locale_t p_Var2;
  undefined8 uVar3;
  byte *__locale;
  byte local_38;
  undefined1 auStack_37 [15];
  undefined1 *local_28;
  
  __locale = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    __locale = param_2 + 1;
  }
  p_Var2 = newlocale(0x1fbf,(char *)__locale,(__locale_t)0x0);
  *param_1 = p_Var2;
  if (p_Var2 != (__locale_t)0x0) {
                    /* try { // try from 00bb5b10 to 00cb5b17 has its CatchHandler @ 00bbacdc */
    return;
  }
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (&local_38,"time_put_byname failed to construct for ",param_2);
  puVar1 = local_28;
  if ((local_38 & 1) == 0) {
    puVar1 = auStack_37;
  }
  uVar3 = _ZNSt6__ndk121__throw_runtime_errorEPKc(puVar1);
  if ((local_38 & 1) != 0) {
    _ZdlPv(local_28);
  }
                    /* WARNING: Subroutine does not return */
  FUN_00bd70ec(uVar3);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb5acc"></a> `00bb5acc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bb5ad0"></a> `00bb5ad0` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bb5ad4"></a> `00bb5ad4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb5ad8"></a> `00bb5ad8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb5adc"></a> `00bb5adc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bb5ae0"></a> `00bb5ae0` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00bb5ae4"></a> `00bb5ae4` | `29 08 40 f9` | ldr x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bb5ae8"></a> `00bb5ae8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bb5aec"></a> `00bb5aec` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bb5af0"></a> `00bb5af0` | `e0 f7 83 52` | mov w0,#0x1fbf | `FALL_THROUGH`
<a id="insn-00bb5af4"></a> `00bb5af4` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bb5af8"></a> `00bb5af8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb5afc"></a> `00bb5afc` | `21 15 81 9a` | csinc x1,x9,x1,ne | `FALL_THROUGH`
<a id="insn-00bb5b00"></a> `00bb5b00` | `9c ae 00 94` | bl 0x00be1570 | `UNCONDITIONAL_CALL`
<a id="insn-00bb5b04"></a> `00bb5b04` | `80 02 00 f9` | str x0,[x20] | `FALL_THROUGH`
<a id="insn-00bb5b08"></a> `00bb5b08` | `c0 00 00 b4` | cbz x0,0x00bb5b20 | `CONDITIONAL_JUMP`
<a id="insn-00bb5b0c"></a> `00bb5b0c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb5b10"></a> `00bb5b10` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb5b14"></a> `00bb5b14` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bb5b18"></a> `00bb5b18` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bb5b1c"></a> `00bb5b1c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bb5b20"></a> `00bb5b20` | `60 b7 ff b0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bb5b24"></a> `00bb5b24` | `00 0c 04 91` | add x0,x0,#0x103 | `FALL_THROUGH`
<a id="insn-00bb5b28"></a> `00bb5b28` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bb5b2c"></a> `00bb5b2c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bb5b30"></a> `00bb5b30` | `f3 23 00 91` | add x19,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bb5b34"></a> `00bb5b34` | `cb 95 00 94` | bl 0x00bdb260 | `UNCONDITIONAL_CALL`
<a id="insn-00bb5b38"></a> `00bb5b38` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bb5b3c"></a> `00bb5b3c` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bb5b40"></a> `00bb5b40` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb5b44"></a> `00bb5b44` | `20 15 93 9a` | csinc x0,x9,x19,ne | `FALL_THROUGH`
<a id="insn-00bb5b48"></a> `00bb5b48` | `1a ad 00 94` | bl 0x00be0fb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb5b4c"></a> `00bb5b4c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bb5b50"></a> `00bb5b50` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb5b54"></a> `00bb5b54` | `68 00 00 36` | tbz w8,#0x0,0x00bb5b60 | `CONDITIONAL_JUMP`
<a id="insn-00bb5b58"></a> `00bb5b58` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bb5b5c"></a> `00bb5b5c` | `41 95 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb5b60"></a> `00bb5b60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb5b64"></a> `00bb5b64` | `62 85 00 94` | bl 0x00bd70ec | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb5acc`](#insn-00bb5acc) 範囲 `[['00bb5acc', '00bb5b0b']]`
  - `CONDITIONAL_JUMP` [`00bb5b08`](#insn-00bb5b08) → [`00bb5b20`](#insn-00bb5b20)
  - `FALL_THROUGH` [`00bb5b08`](#insn-00bb5b08) → [`00bb5b0c`](#insn-00bb5b0c)
- ブロック [`00bb5b0c`](#insn-00bb5b0c) 範囲 `[['00bb5b0c', '00bb5b0f']]`
  - `FALL_THROUGH` [`00bb5b0c`](#insn-00bb5b0c) → [`00bb5b10`](#insn-00bb5b10)
- ブロック [`00bb5b10`](#insn-00bb5b10) 範囲 `[['00bb5b10', '00bb5b1f']]`
- ブロック [`00bb5b20`](#insn-00bb5b20) 範囲 `[['00bb5b20', '00bb5b57']]`
  - `CONDITIONAL_JUMP` [`00bb5b54`](#insn-00bb5b54) → [`00bb5b60`](#insn-00bb5b60)
  - `FALL_THROUGH` [`00bb5b54`](#insn-00bb5b54) → [`00bb5b58`](#insn-00bb5b58)
- ブロック [`00bb5b58`](#insn-00bb5b58) 範囲 `[['00bb5b58', '00bb5b5f']]`
  - `FALL_THROUGH` [`00bb5b5c`](#insn-00bb5b5c) → [`00bb5b60`](#insn-00bb5b60)
- ブロック [`00bb5b60`](#insn-00bb5b60) 範囲 `[['00bb5b60', '00bb5b67']]`

## 命令位置別の参照

- [`00bb5ad4`](#insn-00bb5ad4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb5ad8`](#insn-00bb5ad8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb5b00`](#insn-00bb5b00) → [`00be1570`](../00be1/00be1570.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1570` · 推定シンボル `None` · 推定型 `None`
- [`00bb5b08`](#insn-00bb5b08) → [`00bb5b20`](#insn-00bb5b20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb5b0c`](#insn-00bb5b0c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb5b10`](#insn-00bb5b10) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb5b24`](#insn-00bb5b24) → `002a2103`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bb5b34`](#insn-00bb5b34) → [`00bdb260`](../00bdb/00bdb260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb260` · 推定シンボル `None` · 推定型 `None`
- [`00bb5b38`](#insn-00bb5b38) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb5b3c`](#insn-00bb5b3c) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb5b48`](#insn-00bb5b48) → [`00be0fb0`](../00be0/00be0fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0fb0` · 推定シンボル `None` · 推定型 `None`
- [`00bb5b4c`](#insn-00bb5b4c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb5b54`](#insn-00bb5b54) → [`00bb5b60`](#insn-00bb5b60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb5b58`](#insn-00bb5b58) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb5b5c`](#insn-00bb5b5c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb5b64`](#insn-00bb5b64) → [`00bd70ec`](../00bd7/00bd70ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd70ec` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb5ad4`](#insn-00bb5ad4)

~~~json
{
  "source": "00bb5ad4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb5ad8`](#insn-00bb5ad8)

~~~json
{
  "source": "00bb5ad8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb5b00`](#insn-00bb5b00)

~~~json
{
  "source": "00bb5b00",
  "target": "00be1570",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb5b08`](#insn-00bb5b08)

~~~json
{
  "source": "00bb5b08",
  "target": "00bb5b20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb5b0c`](#insn-00bb5b0c)

~~~json
{
  "source": "00bb5b0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb5b10`](#insn-00bb5b10)

~~~json
{
  "source": "00bb5b10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb5b24`](#insn-00bb5b24)

~~~json
{
  "source": "00bb5b24",
  "target": "002a2103",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2103",
  "offset": 0,
  "size": 41,
  "datatype": "string",
  "bytes": "74696d655f7075745f62796e616d65206661696c656420746f20636f6e737472",
  "capture_start": "002a2103",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bb5b34`](#insn-00bb5b34)

~~~json
{
  "source": "00bb5b34",
  "target": "00bdb260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb5b38`](#insn-00bb5b38)

~~~json
{
  "source": "00bb5b38",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb5b3c`](#insn-00bb5b3c)

~~~json
{
  "source": "00bb5b3c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb5b48`](#insn-00bb5b48)

~~~json
{
  "source": "00bb5b48",
  "target": "00be0fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb5b4c`](#insn-00bb5b4c)

~~~json
{
  "source": "00bb5b4c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb5b54`](#insn-00bb5b54)

~~~json
{
  "source": "00bb5b54",
  "target": "00bb5b60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb5b58`](#insn-00bb5b58)

~~~json
{
  "source": "00bb5b58",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb5b5c`](#insn-00bb5b5c)

~~~json
{
  "source": "00bb5b5c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb5b64`](#insn-00bb5b64)

~~~json
{
  "source": "00bb5b64",
  "target": "00bd70ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
