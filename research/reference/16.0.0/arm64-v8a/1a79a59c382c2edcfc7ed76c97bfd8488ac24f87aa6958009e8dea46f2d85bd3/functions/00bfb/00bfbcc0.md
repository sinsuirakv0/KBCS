# 00bfbcc0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7f278`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f278.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-91071ea59e1b8f8a6bb74748083a86dc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfc0e8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc0e8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-f5bfb0f544c704ecb29acdbada06cf47)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbcc0",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cba33e4d2c036e6bc5b084ae2774b2c4fe91d08fa1c01da78f2d759d4831ec5f",
  "source_text_sha256": "cba33e4d2c036e6bc5b084ae2774b2c4fe91d08fa1c01da78f2d759d4831ec5f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbcc0",
        "00bfbd17"
      ]
    ],
    "bytes_sha256": "edd5ac244d1429acf300fee68b26a9e287a49054993ea8311b408f41bd299bc9",
    "instruction_count": 22,
    "instruction_bytes": 88,
    "body_bytes": 88,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57de0](../00c57/00c57de0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 463 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE
               (long *param_1)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEE_00c9ae30;
  param_1[8] = 0;
  param_1[2] = (long)(puVar1 + 0x40);
  *param_1 = (long)(puVar1 + 0x18);
  param_1[1] = 0;
  _ZNSt6__ndk18ios_base4initEPv(param_1 + 2);
  param_1[0x13] = 0;
  *(undefined4 *)(param_1 + 0x14) = 0xffffffff;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbcc0"></a> `00bfbcc0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbcc4"></a> `00bfbcc4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfbcc8"></a> `00bfbcc8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbccc"></a> `00bfbccc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfbcd0"></a> `00bfbcd0` | `e8 04 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-00bfbcd4"></a> `00bfbcd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfbcd8"></a> `00bfbcd8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfbcdc"></a> `00bfbcdc` | `08 19 47 f9` | ldr x8,[x8, #0xe30] | `FALL_THROUGH`
<a id="insn-00bfbce0"></a> `00bfbce0` | `1f 20 00 f9` | str xzr,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bfbce4"></a> `00bfbce4` | `09 01 01 91` | add x9,x8,#0x40 | `FALL_THROUGH`
<a id="insn-00bfbce8"></a> `00bfbce8` | `08 61 00 91` | add x8,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00bfbcec"></a> `00bfbcec` | `89 0e 01 f8` | str x9,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-00bfbcf0"></a> `00bfbcf0` | `08 7c 00 a9` | stp x8,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bfbcf4"></a> `00bfbcf4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfbcf8"></a> `00bfbcf8` | `3a 70 01 94` | bl 0x00c57de0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbcfc"></a> `00bfbcfc` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bfbd00"></a> `00bfbd00` | `7f 4e 00 f9` | str xzr,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00bfbd04"></a> `00bfbd04` | `68 a2 00 b9` | str w8,[x19, #0xa0] | `FALL_THROUGH`
<a id="insn-00bfbd08"></a> `00bfbd08` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbd0c"></a> `00bfbd0c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfbd10"></a> `00bfbd10` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfbd14"></a> `00bfbd14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbcc0`](#insn-00bfbcc0) 範囲 `[['00bfbcc0', '00bfbd17']]`

## 命令位置別の参照

- [`00bfbcc4`](#insn-00bfbcc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbcc8`](#insn-00bfbcc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbcdc`](#insn-00bfbcdc) → `00c9ae30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfbcec`](#insn-00bfbcec) → `00c92a38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfbcf0`](#insn-00bfbcf0) → `00c92a10`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfbcf8`](#insn-00bfbcf8) → [`00c57de0`](../00c57/00c57de0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57de0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbd08`](#insn-00bfbd08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbd0c`](#insn-00bfbd0c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbcc4`](#insn-00bfbcc4)

~~~json
{
  "source": "00bfbcc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbcc8`](#insn-00bfbcc8)

~~~json
{
  "source": "00bfbcc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbcdc`](#insn-00bfbcdc)

~~~json
{
  "source": "00bfbcdc",
  "target": "00c9ae30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ae30",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfbcec`](#insn-00bfbcec)

~~~json
{
  "source": "00bfbcec",
  "target": "00c92a38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92a38",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfbcf0`](#insn-00bfbcf0)

~~~json
{
  "source": "00bfbcf0",
  "target": "00c92a10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92a10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfbcf8`](#insn-00bfbcf8)

~~~json
{
  "source": "00bfbcf8",
  "target": "00c57de0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbd08`](#insn-00bfbd08)

~~~json
{
  "source": "00bfbd08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbd0c`](#insn-00bfbd0c)

~~~json
{
  "source": "00bfbd0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
