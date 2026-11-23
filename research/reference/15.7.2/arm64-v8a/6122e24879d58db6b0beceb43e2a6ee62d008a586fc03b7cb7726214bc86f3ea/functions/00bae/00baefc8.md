# 00baefc8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baf090`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf090.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-9b9ce184920c258bb3fb876a6d5dc49b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baefc8",
  "name": "_ZNSt6__ndk18numpunctIwED1Ev",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5919f904ce1447580872d7288890fa1ce5c907ce500360a978adbfb960fe3931",
  "source_text_sha256": "5919f904ce1447580872d7288890fa1ce5c907ce500360a978adbfb960fe3931",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baefc8",
        "00baf017"
      ]
    ],
    "bytes_sha256": "e9c95521dfb373d644fe235c61a6db559b2ebfc546766fe7ada4959eb9874eb9",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1b50](../00be1/00be1b50.md)
- [00be1b60](../00be1/00be1b60.md)
- [00be1bb0](../00be1/00be1bb0.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb3b0](../00bdb/00bdb3b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 265 bytes

~~~c

void _ZNSt6__ndk18numpunctIwED1Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk18numpunctIwEE_00c1bec0 + 0x10);
  if ((*(byte *)(param_1 + 3) & 1) != 0) {
    _ZdlPv((void *)param_1[5]);
  }
  _ZNSt6__ndk119__shared_weak_countD2Ev(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baefc8"></a> `00baefc8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baefcc"></a> `00baefcc` | `68 03 00 b0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00baefd0"></a> `00baefd0` | `08 61 47 f9` | ldr x8,[x8, #0xec0] | `FALL_THROUGH`
<a id="insn-00baefd4"></a> `00baefd4` | `09 60 40 39` | ldrb w9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baefd8"></a> `00baefd8` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00baefdc"></a> `00baefdc` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00baefe0"></a> `00baefe0` | `a9 01 00 36` | tbz w9,#0x0,0x00baf014 | `CONDITIONAL_JUMP`
<a id="insn-00baefe4"></a> `00baefe4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baefe8"></a> `00baefe8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00baefec"></a> `00baefec` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baeff0"></a> `00baeff0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00baeff4"></a> `00baeff4` | `08 14 40 f9` | ldr x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00baeff8"></a> `00baeff8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baeffc"></a> `00baeffc` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00baf000"></a> `00baf000` | `d8 af 00 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00baf004"></a> `00baf004` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baf008"></a> `00baf008` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baf00c"></a> `00baf00c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00baf010"></a> `00baf010` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baf014"></a> `00baf014` | `e7 b0 00 14` | b 0x00bdb3b0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baefc8`](#insn-00baefc8) 範囲 `[['00baefc8', '00baefe3']]`
  - `CONDITIONAL_JUMP` [`00baefe0`](#insn-00baefe0) → [`00baf014`](#insn-00baf014)
  - `FALL_THROUGH` [`00baefe0`](#insn-00baefe0) → [`00baefe4`](#insn-00baefe4)
- ブロック [`00baefe4`](#insn-00baefe4) 範囲 `[['00baefe4', '00baf013']]`
  - `FALL_THROUGH` [`00baf010`](#insn-00baf010) → [`00baf014`](#insn-00baf014)
- ブロック [`00baf014`](#insn-00baf014) 範囲 `[['00baf014', '00baf017']]`

## 命令位置別の参照

- [`00baefd0`](#insn-00baefd0) → `00c1bec0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00baefdc`](#insn-00baefdc) → `00c13ac8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00baefe0`](#insn-00baefe0) → [`00baf014`](#insn-00baf014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baefe8`](#insn-00baefe8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baefec`](#insn-00baefec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf000`](#insn-00baf000) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00baf008`](#insn-00baf008) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf00c`](#insn-00baf00c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf014`](#insn-00baf014) → [`00bdb3b0`](../00bdb/00bdb3b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb3b0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baefd0`](#insn-00baefd0)

~~~json
{
  "source": "00baefd0",
  "target": "00c1bec0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bec0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00baefdc`](#insn-00baefdc)

~~~json
{
  "source": "00baefdc",
  "target": "00c13ac8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13ab8",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00baefe0`](#insn-00baefe0)

~~~json
{
  "source": "00baefe0",
  "target": "00baf014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baefe8`](#insn-00baefe8)

~~~json
{
  "source": "00baefe8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baefec`](#insn-00baefec)

~~~json
{
  "source": "00baefec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf000`](#insn-00baf000)

~~~json
{
  "source": "00baf000",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf008`](#insn-00baf008)

~~~json
{
  "source": "00baf008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf00c`](#insn-00baf00c)

~~~json
{
  "source": "00baf00c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf014`](#insn-00baf014)

~~~json
{
  "source": "00baf014",
  "target": "00bdb3b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
