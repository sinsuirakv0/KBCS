# 00bff3bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b82974`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82974.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-944134fced05ccdf19575960fdc754ff)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bff7e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff7e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0087.md#compare-23d54047330897c62ce26675221ceb97)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bff3bc",
  "name": "_ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56096bb493ee35ec396e865a055d0393d523d44e25b98ac74dcc88b2ee8b13d4",
  "source_text_sha256": "56096bb493ee35ec396e865a055d0393d523d44e25b98ac74dcc88b2ee8b13d4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bff3bc",
        "00bff42f"
      ]
    ],
    "bytes_sha256": "862b6ee952c052ca75eb0d8071080cda12291b8eacf88f41054cb8cb1c579f08",
    "instruction_count": 29,
    "instruction_bytes": 116,
    "body_bytes": 116,
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

## 疑似コード / UTF-8 687 bytes

~~~c

void _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE
               (long *param_1)

{
  undefined *puVar1;
  
  puVar1 = 
  PTR__ZTCNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEE0_NS_13basic_istreamIcS2_EE_00c9b720;
  param_1[9] = 0;
  param_1[3] = (long)(puVar1 + 0x40);
  *param_1 = (long)(puVar1 + 0x18);
  param_1[1] = 0;
  _ZNSt6__ndk18ios_base4initEPv(param_1 + 3);
  puVar1 = PTR__ZTVNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEE_00c9b728;
  *(undefined4 *)(param_1 + 0x15) = 0xffffffff;
  param_1[0x14] = 0;
  *param_1 = (long)(puVar1 + 0x18);
  param_1[2] = (long)(puVar1 + 0x40);
  param_1[3] = (long)(puVar1 + 0x68);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bff3bc"></a> `00bff3bc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bff3c0"></a> `00bff3c0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bff3c4"></a> `00bff3c4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bff3c8"></a> `00bff3c8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bff3cc"></a> `00bff3cc` | `e8 04 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bff3d0"></a> `00bff3d0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bff3d4"></a> `00bff3d4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bff3d8"></a> `00bff3d8` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00bff3dc"></a> `00bff3dc` | `1f 24 00 f9` | str xzr,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00bff3e0"></a> `00bff3e0` | `09 01 01 91` | add x9,x8,#0x40 | `FALL_THROUGH`
<a id="insn-00bff3e4"></a> `00bff3e4` | `08 61 00 91` | add x8,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00bff3e8"></a> `00bff3e8` | `89 8e 01 f8` | str x9,[x20, #0x18]! | `FALL_THROUGH`
<a id="insn-00bff3ec"></a> `00bff3ec` | `08 7c 00 a9` | stp x8,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bff3f0"></a> `00bff3f0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bff3f4"></a> `00bff3f4` | `7b 62 01 94` | bl 0x00c57de0 | `UNCONDITIONAL_CALL`
<a id="insn-00bff3f8"></a> `00bff3f8` | `e8 04 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bff3fc"></a> `00bff3fc` | `09 00 80 12` | mov w9,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bff400"></a> `00bff400` | `08 95 43 f9` | ldr x8,[x8, #0x728] | `FALL_THROUGH`
<a id="insn-00bff404"></a> `00bff404` | `69 aa 00 b9` | str w9,[x19, #0xa8] | `FALL_THROUGH`
<a id="insn-00bff408"></a> `00bff408` | `7f 52 00 f9` | str xzr,[x19, #0xa0] | `FALL_THROUGH`
<a id="insn-00bff40c"></a> `00bff40c` | `09 61 00 91` | add x9,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00bff410"></a> `00bff410` | `0a a1 01 91` | add x10,x8,#0x68 | `FALL_THROUGH`
<a id="insn-00bff414"></a> `00bff414` | `08 01 01 91` | add x8,x8,#0x40 | `FALL_THROUGH`
<a id="insn-00bff418"></a> `00bff418` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00bff41c"></a> `00bff41c` | `68 2a 01 a9` | stp x8,x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bff420"></a> `00bff420` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bff424"></a> `00bff424` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bff428"></a> `00bff428` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bff42c"></a> `00bff42c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bff3bc`](#insn-00bff3bc) 範囲 `[['00bff3bc', '00bff42f']]`

## 命令位置別の参照

- [`00bff3c0`](#insn-00bff3c0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff3c4`](#insn-00bff3c4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff3d8`](#insn-00bff3d8) → `00c9b720`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bff3e8`](#insn-00bff3e8) → `00c92f58`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bff3ec`](#insn-00bff3ec) → `00c92f30`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bff3f4`](#insn-00bff3f4) → [`00c57de0`](../00c57/00c57de0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57de0` · 推定シンボル `None` · 推定型 `None`
- [`00bff400`](#insn-00bff400) → `00c9b728`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bff418`](#insn-00bff418) → `00c92ad0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[120]`
- [`00bff41c`](#insn-00bff41c) → `00c92af8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[120]`
- [`00bff41c`](#insn-00bff41c) → `00c92b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[120]`
- [`00bff420`](#insn-00bff420) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff424`](#insn-00bff424) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bff3c0`](#insn-00bff3c0)

~~~json
{
  "source": "00bff3c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff3c4`](#insn-00bff3c4)

~~~json
{
  "source": "00bff3c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff3d8`](#insn-00bff3d8)

~~~json
{
  "source": "00bff3d8",
  "target": "00c9b720",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b720",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bff3e8`](#insn-00bff3e8)

~~~json
{
  "source": "00bff3e8",
  "target": "00c92f58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92f18",
  "offset": 64,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bff3ec`](#insn-00bff3ec)

~~~json
{
  "source": "00bff3ec",
  "target": "00c92f30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92f18",
  "offset": 24,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bff3f4`](#insn-00bff3f4)

~~~json
{
  "source": "00bff3f4",
  "target": "00c57de0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff400`](#insn-00bff400)

~~~json
{
  "source": "00bff400",
  "target": "00c9b728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b728",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bff418`](#insn-00bff418)

~~~json
{
  "source": "00bff418",
  "target": "00c92ad0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92ab8",
  "offset": 24,
  "size": 120,
  "datatype": "undefined1[120]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bff41c`](#insn-00bff41c)

~~~json
{
  "source": "00bff41c",
  "target": "00c92af8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92ab8",
  "offset": 64,
  "size": 120,
  "datatype": "undefined1[120]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bff41c`](#insn-00bff41c)

~~~json
{
  "source": "00bff41c",
  "target": "00c92b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92ab8",
  "offset": 104,
  "size": 120,
  "datatype": "undefined1[120]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bff420`](#insn-00bff420)

~~~json
{
  "source": "00bff420",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff424`](#insn-00bff424)

~~~json
{
  "source": "00bff424",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
