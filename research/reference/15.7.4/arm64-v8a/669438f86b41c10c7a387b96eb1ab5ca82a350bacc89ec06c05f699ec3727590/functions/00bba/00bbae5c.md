# 00bbae5c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbae18`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbae18.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-8c9c18788f61437b73c01c200709e42d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c378a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378a4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-c242615ff8053c692cfc4dfce9de3f83)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbae5c",
  "name": "_ZNSt11logic_errorD1Ev",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "801e6e4b3b1a56ba8d9ddc5890ccfe0c2b35e4aa81b2b0bc3b0e21008b9233f5",
  "source_text_sha256": "801e6e4b3b1a56ba8d9ddc5890ccfe0c2b35e4aa81b2b0bc3b0e21008b9233f5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbae5c",
        "00bbaeb3"
      ]
    ],
    "bytes_sha256": "b989ad419d9c89c09b15640d81d16a54b6284ec11937c573c6aaef5aec507766",
    "instruction_count": 22,
    "instruction_bytes": 88,
    "body_bytes": 88,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bdb250](../00bdb/00bdb250.md)
- [00be1130](../00be1/00be1130.md)
- [00be1210](../00be1/00be1210.md)
- [00be1e60](../00be1/00be1e60.md)
- [00be1e70](../00be1/00be1e70.md)

## 呼び出し先

- [00bd6e30](../00bd6/00bd6e30.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb490](../00bdb/00bdb490.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1548 bytes

~~~c

void _ZNSt11logic_errorD1Ev(long *param_1)

{
  int iVar1;
  long lVar2;
  
                    /* catch() { ... } // from try @ 00bb4d84 with catch @ 00bbae60 */
                    /* catch() { ... } // from try @ 00bb49a4 with catch @ 00bbae64 */
                    /* catch() { ... } // from try @ 00bb45e4 with catch @ 00bbae68 */
                    /* catch() { ... } // from try @ 00bb7cf4 with catch @ 00bbae6c */
                    /* catch() { ... } // from try @ 00bb9d34 with catch @ 00bbae70 */
                    /* catch() { ... } // from try @ 00bb996c with catch @ 00bbae74 */
                    /* catch() { ... } // from try @ 00bb9978 with catch @ 00bbae78 */
  lVar2 = param_1[1];
                    /* catch() { ... } // from try @ 00bb3640 with catch @ 00bbae7c */
  *param_1 = (long)(PTR__ZTVSt11logic_error_00c1bc60 + 0x10);
                    /* catch() { ... } // from try @ 00bb3584 with catch @ 00bbae8c */
  iVar1 = FUN_00bd6e30(0xffffffff,lVar2 + -8);
                    /* catch() { ... } // from try @ 00bb7c40 with catch @ 00bbae90 */
                    /* catch() { ... } // from try @ 00bb35ec with catch @ 00bbae94 */
  if (iVar1 + -1 < 0) {
                    /* catch() { ... } // from try @ 00bb3878 with catch @ 00bbae98 */
                    /* catch() { ... } // from try @ 00bb386c with catch @ 00bbae9c */
    _ZdlPv((void *)(lVar2 + -0x18));
  }
                    /* catch() { ... } // from try @ 00bb9d40 with catch @ 00bbaea4 */
  _ZNSt20bad_array_new_lengthD1Ev(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbae5c"></a> `00bbae5c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbae60"></a> `00bbae60` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbae64"></a> `00bbae64` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbae68"></a> `00bbae68` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbae6c"></a> `00bbae6c` | `08 03 00 b0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbae70"></a> `00bbae70` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbae74"></a> `00bbae74` | `08 31 46 f9` | ldr x8,[x8, #0xc60] | `FALL_THROUGH`
<a id="insn-00bbae78"></a> `00bbae78` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbae7c"></a> `00bbae7c` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbae80"></a> `00bbae80` | `81 22 00 d1` | sub x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00bbae84"></a> `00bbae84` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbae88"></a> `00bbae88` | `00 00 80 12` | mov w0,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bbae8c"></a> `00bbae8c` | `e9 6f 00 94` | bl 0x00bd6e30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbae90"></a> `00bbae90` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbae94"></a> `00bbae94` | `65 00 00 54` | b.pl 0x00bbaea0 | `CONDITIONAL_JUMP`
<a id="insn-00bbae98"></a> `00bbae98` | `80 62 00 d1` | sub x0,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00bbae9c"></a> `00bbae9c` | `71 80 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaea0"></a> `00bbaea0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbaea4"></a> `00bbaea4` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaea8"></a> `00bbaea8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbaeac"></a> `00bbaeac` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbaeb0"></a> `00bbaeb0` | `78 81 00 14` | b 0x00bdb490 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbae5c`](#insn-00bbae5c) 範囲 `[['00bbae5c', '00bbae5f']]`
  - `FALL_THROUGH` [`00bbae5c`](#insn-00bbae5c) → [`00bbae60`](#insn-00bbae60)
- ブロック [`00bbae60`](#insn-00bbae60) 範囲 `[['00bbae60', '00bbae63']]`
  - `FALL_THROUGH` [`00bbae60`](#insn-00bbae60) → [`00bbae64`](#insn-00bbae64)
- ブロック [`00bbae64`](#insn-00bbae64) 範囲 `[['00bbae64', '00bbae67']]`
  - `FALL_THROUGH` [`00bbae64`](#insn-00bbae64) → [`00bbae68`](#insn-00bbae68)
- ブロック [`00bbae68`](#insn-00bbae68) 範囲 `[['00bbae68', '00bbae6b']]`
  - `FALL_THROUGH` [`00bbae68`](#insn-00bbae68) → [`00bbae6c`](#insn-00bbae6c)
- ブロック [`00bbae6c`](#insn-00bbae6c) 範囲 `[['00bbae6c', '00bbae6f']]`
  - `FALL_THROUGH` [`00bbae6c`](#insn-00bbae6c) → [`00bbae70`](#insn-00bbae70)
- ブロック [`00bbae70`](#insn-00bbae70) 範囲 `[['00bbae70', '00bbae73']]`
  - `FALL_THROUGH` [`00bbae70`](#insn-00bbae70) → [`00bbae74`](#insn-00bbae74)
- ブロック [`00bbae74`](#insn-00bbae74) 範囲 `[['00bbae74', '00bbae77']]`
  - `FALL_THROUGH` [`00bbae74`](#insn-00bbae74) → [`00bbae78`](#insn-00bbae78)
- ブロック [`00bbae78`](#insn-00bbae78) 範囲 `[['00bbae78', '00bbae7b']]`
  - `FALL_THROUGH` [`00bbae78`](#insn-00bbae78) → [`00bbae7c`](#insn-00bbae7c)
- ブロック [`00bbae7c`](#insn-00bbae7c) 範囲 `[['00bbae7c', '00bbae8b']]`
  - `FALL_THROUGH` [`00bbae88`](#insn-00bbae88) → [`00bbae8c`](#insn-00bbae8c)
- ブロック [`00bbae8c`](#insn-00bbae8c) 範囲 `[['00bbae8c', '00bbae8f']]`
  - `FALL_THROUGH` [`00bbae8c`](#insn-00bbae8c) → [`00bbae90`](#insn-00bbae90)
- ブロック [`00bbae90`](#insn-00bbae90) 範囲 `[['00bbae90', '00bbae93']]`
  - `FALL_THROUGH` [`00bbae90`](#insn-00bbae90) → [`00bbae94`](#insn-00bbae94)
- ブロック [`00bbae94`](#insn-00bbae94) 範囲 `[['00bbae94', '00bbae97']]`
  - `CONDITIONAL_JUMP` [`00bbae94`](#insn-00bbae94) → [`00bbaea0`](#insn-00bbaea0)
  - `FALL_THROUGH` [`00bbae94`](#insn-00bbae94) → [`00bbae98`](#insn-00bbae98)
- ブロック [`00bbae98`](#insn-00bbae98) 範囲 `[['00bbae98', '00bbae9b']]`
  - `FALL_THROUGH` [`00bbae98`](#insn-00bbae98) → [`00bbae9c`](#insn-00bbae9c)
- ブロック [`00bbae9c`](#insn-00bbae9c) 範囲 `[['00bbae9c', '00bbae9f']]`
  - `FALL_THROUGH` [`00bbae9c`](#insn-00bbae9c) → [`00bbaea0`](#insn-00bbaea0)
- ブロック [`00bbaea0`](#insn-00bbaea0) 範囲 `[['00bbaea0', '00bbaea3']]`
  - `FALL_THROUGH` [`00bbaea0`](#insn-00bbaea0) → [`00bbaea4`](#insn-00bbaea4)
- ブロック [`00bbaea4`](#insn-00bbaea4) 範囲 `[['00bbaea4', '00bbaeb3']]`

## 命令位置別の参照

- [`00bbae60`](#insn-00bbae60) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae64`](#insn-00bbae64) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae74`](#insn-00bbae74) → `00c1bc60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbae84`](#insn-00bbae84) → `00c16930`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00bbae8c`](#insn-00bbae8c) → [`00bd6e30`](../00bd6/00bd6e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e30` · 推定シンボル `None` · 推定型 `None`
- [`00bbae94`](#insn-00bbae94) → [`00bbaea0`](#insn-00bbaea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae9c`](#insn-00bbae9c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bbaea4`](#insn-00bbaea4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaea8`](#insn-00bbaea8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaeb0`](#insn-00bbaeb0) → [`00bdb490`](../00bdb/00bdb490.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb490` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbae60`](#insn-00bbae60)

~~~json
{
  "source": "00bbae60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae64`](#insn-00bbae64)

~~~json
{
  "source": "00bbae64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae74`](#insn-00bbae74)

~~~json
{
  "source": "00bbae74",
  "target": "00c1bc60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bc60",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbae84`](#insn-00bbae84)

~~~json
{
  "source": "00bbae84",
  "target": "00c16930",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16920",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bbae8c`](#insn-00bbae8c)

~~~json
{
  "source": "00bbae8c",
  "target": "00bd6e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbae94`](#insn-00bbae94)

~~~json
{
  "source": "00bbae94",
  "target": "00bbaea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae9c`](#insn-00bbae9c)

~~~json
{
  "source": "00bbae9c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaea4`](#insn-00bbaea4)

~~~json
{
  "source": "00bbaea4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaea8`](#insn-00bbaea8)

~~~json
{
  "source": "00bbaea8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaeb0`](#insn-00bbaeb0)

~~~json
{
  "source": "00bbaeb0",
  "target": "00bdb490",
  "target_space": "ram",
  "resolution": "function"
}
~~~
