# 00bdde4c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6e94c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e94c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0017.md#compare-6bba82fc3db720495c6bb0f6d3355ddc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bde274`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde274.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0010.md#compare-4c72544e4d329b4ae4c3615c84d60ded)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdde4c",
  "name": "_ZN8firebase4auth4UserD0Ev",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "96c5c421be0f76db1429b3273e76fd68a077e6612abd0bc7d18688552c741244",
  "source_text_sha256": "96c5c421be0f76db1429b3273e76fd68a077e6612abd0bc7d18688552c741244",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdde4c",
        "00bdde83"
      ]
    ],
    "bytes_sha256": "a7c69478ce5a7105d1c4b57ad871b8a1b5c8c2dea8d31751e50cfbc226df80d7",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c5d780](../00c5d/00c5d780.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 261 bytes

~~~c

void _ZN8firebase4auth4UserD0Ev(long *param_1)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVN8firebase4auth4UserE_00c9b5c0;
  param_1[0x13] = 0;
  *param_1 = (long)(puVar1 + 0x10);
  _ZN8firebase4auth17UserInfoInterfaceD2Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdde4c"></a> `00bdde4c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdde50"></a> `00bdde50` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdde54"></a> `00bdde54` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdde58"></a> `00bdde58` | `e8 05 00 d0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdde5c"></a> `00bdde5c` | `08 e1 42 f9` | ldr x8,[x8, #0x5c0] | `FALL_THROUGH`
<a id="insn-00bdde60"></a> `00bdde60` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdde64"></a> `00bdde64` | `1f 4c 00 f9` | str xzr,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdde68"></a> `00bdde68` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bdde6c"></a> `00bdde6c` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdde70"></a> `00bdde70` | `44 fe 01 94` | bl 0x00c5d780 | `UNCONDITIONAL_CALL`
<a id="insn-00bdde74"></a> `00bdde74` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdde78"></a> `00bdde78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdde7c"></a> `00bdde7c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdde80"></a> `00bdde80` | `0c e7 01 14` | b 0x00c57ab0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdde4c`](#insn-00bdde4c) 範囲 `[['00bdde4c', '00bdde83']]`

## 命令位置別の参照

- [`00bdde4c`](#insn-00bdde4c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdde50`](#insn-00bdde50) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdde5c`](#insn-00bdde5c) → `00c9b5c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdde6c`](#insn-00bdde6c) → `00c924a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bdde70`](#insn-00bdde70) → [`00c5d780`](../00c5d/00c5d780.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d780` · 推定シンボル `None` · 推定型 `None`
- [`00bdde74`](#insn-00bdde74) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdde80`](#insn-00bdde80) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdde4c`](#insn-00bdde4c)

~~~json
{
  "source": "00bdde4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdde50`](#insn-00bdde50)

~~~json
{
  "source": "00bdde50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdde5c`](#insn-00bdde5c)

~~~json
{
  "source": "00bdde5c",
  "target": "00c9b5c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b5c0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdde6c`](#insn-00bdde6c)

~~~json
{
  "source": "00bdde6c",
  "target": "00c924a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92498",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bdde70`](#insn-00bdde70)

~~~json
{
  "source": "00bdde70",
  "target": "00c5d780",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdde74`](#insn-00bdde74)

~~~json
{
  "source": "00bdde74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdde80`](#insn-00bdde80)

~~~json
{
  "source": "00bdde80",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
