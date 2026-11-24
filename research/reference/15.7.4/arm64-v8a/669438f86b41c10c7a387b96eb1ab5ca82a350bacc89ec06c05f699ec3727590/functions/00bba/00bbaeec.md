# 00bbaeec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbaea8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-1d802bfb403122a36c84e212e615ae07)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c37934`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37934.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-23a60e65c13e9c8ae4ae64c6701af549)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaeec",
  "name": "_ZNSt14overflow_errorD1Ev",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77ec89ca0d940a7fb84d34cbd433ef99148ffbf8ac86c312c0cbe0ddf49f8adc",
  "source_text_sha256": "77ec89ca0d940a7fb84d34cbd433ef99148ffbf8ac86c312c0cbe0ddf49f8adc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaeec",
        "00bbaf43"
      ]
    ],
    "bytes_sha256": "a743181e256ae80ba62f9b04678cb05cb80d5b0e27dce3dbb30adc10cf037651",
    "instruction_count": 22,
    "instruction_bytes": 88,
    "body_bytes": 88,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdda70](../00bdd/00bdda70.md)
- [00be0f70](../00be0/00be0f70.md)
- [00be0fd0](../00be0/00be0fd0.md)
- [00be11a0](../00be1/00be11a0.md)
- [00be1e80](../00be1/00be1e80.md)

## 呼び出し先

- [00bd6e30](../00bd6/00bd6e30.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb490](../00bdb/00bdb490.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 335 bytes

~~~c

void _ZNSt14overflow_errorD1Ev(long *param_1)

{
  int iVar1;
  long lVar2;
  
  lVar2 = param_1[1];
  *param_1 = (long)(PTR__ZTVSt13runtime_error_00c1bc68 + 0x10);
  iVar1 = FUN_00bd6e30(0xffffffff,lVar2 + -8);
  if (iVar1 + -1 < 0) {
    _ZdlPv((void *)(lVar2 + -0x18));
  }
  _ZNSt20bad_array_new_lengthD1Ev(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaeec"></a> `00bbaeec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbaef0"></a> `00bbaef0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbaef4"></a> `00bbaef4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaef8"></a> `00bbaef8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbaefc"></a> `00bbaefc` | `08 03 00 b0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbaf00"></a> `00bbaf00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbaf04"></a> `00bbaf04` | `08 35 46 f9` | ldr x8,[x8, #0xc68] | `FALL_THROUGH`
<a id="insn-00bbaf08"></a> `00bbaf08` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbaf0c"></a> `00bbaf0c` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbaf10"></a> `00bbaf10` | `81 22 00 d1` | sub x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00bbaf14"></a> `00bbaf14` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbaf18"></a> `00bbaf18` | `00 00 80 12` | mov w0,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bbaf1c"></a> `00bbaf1c` | `c5 6f 00 94` | bl 0x00bd6e30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaf20"></a> `00bbaf20` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbaf24"></a> `00bbaf24` | `65 00 00 54` | b.pl 0x00bbaf30 | `CONDITIONAL_JUMP`
<a id="insn-00bbaf28"></a> `00bbaf28` | `80 62 00 d1` | sub x0,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00bbaf2c"></a> `00bbaf2c` | `4d 80 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaf30"></a> `00bbaf30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbaf34"></a> `00bbaf34` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaf38"></a> `00bbaf38` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbaf3c"></a> `00bbaf3c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbaf40"></a> `00bbaf40` | `54 81 00 14` | b 0x00bdb490 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaeec`](#insn-00bbaeec) 範囲 `[['00bbaeec', '00bbaf27']]`
  - `CONDITIONAL_JUMP` [`00bbaf24`](#insn-00bbaf24) → [`00bbaf30`](#insn-00bbaf30)
  - `FALL_THROUGH` [`00bbaf24`](#insn-00bbaf24) → [`00bbaf28`](#insn-00bbaf28)
- ブロック [`00bbaf28`](#insn-00bbaf28) 範囲 `[['00bbaf28', '00bbaf2f']]`
  - `FALL_THROUGH` [`00bbaf2c`](#insn-00bbaf2c) → [`00bbaf30`](#insn-00bbaf30)
- ブロック [`00bbaf30`](#insn-00bbaf30) 範囲 `[['00bbaf30', '00bbaf43']]`

## 命令位置別の参照

- [`00bbaef0`](#insn-00bbaef0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaef4`](#insn-00bbaef4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf04`](#insn-00bbaf04) → `00c1bc68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbaf14`](#insn-00bbaf14) → `00c16958`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00bbaf1c`](#insn-00bbaf1c) → [`00bd6e30`](../00bd6/00bd6e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e30` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf24`](#insn-00bbaf24) → [`00bbaf30`](#insn-00bbaf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf2c`](#insn-00bbaf2c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf34`](#insn-00bbaf34) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf38`](#insn-00bbaf38) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf40`](#insn-00bbaf40) → [`00bdb490`](../00bdb/00bdb490.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb490` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaef0`](#insn-00bbaef0)

~~~json
{
  "source": "00bbaef0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaef4`](#insn-00bbaef4)

~~~json
{
  "source": "00bbaef4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf04`](#insn-00bbaf04)

~~~json
{
  "source": "00bbaf04",
  "target": "00c1bc68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bc68",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbaf14`](#insn-00bbaf14)

~~~json
{
  "source": "00bbaf14",
  "target": "00c16958",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16948",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bbaf1c`](#insn-00bbaf1c)

~~~json
{
  "source": "00bbaf1c",
  "target": "00bd6e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaf24`](#insn-00bbaf24)

~~~json
{
  "source": "00bbaf24",
  "target": "00bbaf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf2c`](#insn-00bbaf2c)

~~~json
{
  "source": "00bbaf2c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaf34`](#insn-00bbaf34)

~~~json
{
  "source": "00bbaf34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf38`](#insn-00bbaf38)

~~~json
{
  "source": "00bbaf38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf40`](#insn-00bbaf40)

~~~json
{
  "source": "00bbaf40",
  "target": "00bdb490",
  "target_space": "ram",
  "resolution": "function"
}
~~~
