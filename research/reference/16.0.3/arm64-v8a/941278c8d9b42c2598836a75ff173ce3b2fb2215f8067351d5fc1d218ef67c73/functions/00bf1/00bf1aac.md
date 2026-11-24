# 00bf1aac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf0ab8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0ab8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0010.md#compare-351fa5dba34471c903b5ff2fb468c08a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf1aac",
  "name": "_ZNSt13runtime_errorC1ERKS_",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a4a1fde258bb9c43ea24e89a2389c646c167c275307773ff25de635039256ce2",
  "source_text_sha256": "a4a1fde258bb9c43ea24e89a2389c646c167c275307773ff25de635039256ce2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf1aac",
        "00bf1ae3"
      ]
    ],
    "bytes_sha256": "5cac9648e01d19b6d970284a67c6efac4b21d09615ed027c781d78a9f4e1c7df",
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

- [00c54d30](../00c54/00c54d30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 245 bytes

~~~c

void _ZNSt13runtime_errorC1ERKS_(long *param_1,long param_2)

{
  long lVar1;
  
  lVar1 = *(long *)(param_2 + 8);
  *param_1 = (long)(PTR__ZTVSt13runtime_error_00c9cb38 + 0x10);
  param_1[1] = lVar1;
  FUN_00c54d30(1,lVar1 + -8);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf1aac"></a> `00bf1aac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf1ab0"></a> `00bf1ab0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bf1ab4"></a> `00bf1ab4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf1ab8"></a> `00bf1ab8` | `48 05 00 f0` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bf1abc"></a> `00bf1abc` | `08 9d 45 f9` | ldr x8,[x8, #0xb38] | `FALL_THROUGH`
<a id="insn-00bf1ac0"></a> `00bf1ac0` | `29 04 40 f9` | ldr x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bf1ac4"></a> `00bf1ac4` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bf1ac8"></a> `00bf1ac8` | `21 21 00 d1` | sub x1,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bf1acc"></a> `00bf1acc` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bf1ad0"></a> `00bf1ad0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bf1ad4"></a> `00bf1ad4` | `97 8c 01 94` | bl 0x00c54d30 | `UNCONDITIONAL_CALL`
<a id="insn-00bf1ad8"></a> `00bf1ad8` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bf1adc"></a> `00bf1adc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf1ae0"></a> `00bf1ae0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf1aac`](#insn-00bf1aac) 範囲 `[['00bf1aac', '00bf1ae3']]`

## 命令位置別の参照

- [`00bf1ab0`](#insn-00bf1ab0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1abc`](#insn-00bf1abc) → `00c9cb38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bf1acc`](#insn-00bf1acc) → `00c977a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00bf1ad4`](#insn-00bf1ad4) → [`00c54d30`](../00c54/00c54d30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d30` · 推定シンボル `None` · 推定型 `None`
- [`00bf1ad8`](#insn-00bf1ad8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf1ab0`](#insn-00bf1ab0)

~~~json
{
  "source": "00bf1ab0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1abc`](#insn-00bf1abc)

~~~json
{
  "source": "00bf1abc",
  "target": "00c9cb38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9cb38",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bf1acc`](#insn-00bf1acc)

~~~json
{
  "source": "00bf1acc",
  "target": "00c977a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c97790",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bf1ad4`](#insn-00bf1ad4)

~~~json
{
  "source": "00bf1ad4",
  "target": "00c54d30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf1ad8`](#insn-00bf1ad8)

~~~json
{
  "source": "00bf1ad8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
