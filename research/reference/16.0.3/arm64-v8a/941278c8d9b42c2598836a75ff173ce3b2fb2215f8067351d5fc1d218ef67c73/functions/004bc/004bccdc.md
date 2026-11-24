# 004bccdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `004bc9bc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc9bc.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0006.md#compare-ed57e87d0ebdf92872324651689293a3)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004bccdc",
  "name": "_ZNK5Botan8CBC_Mode18update_granularityEv",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "76f24c7cbcd62af4ec09681f545ee6d7abf47867ec726159413eb5eeb66f86a3",
  "source_text_sha256": "76f24c7cbcd62af4ec09681f545ee6d7abf47867ec726159413eb5eeb66f86a3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004bccdc",
        "004bcd23"
      ]
    ],
    "bytes_sha256": "7794b36744b12964adc11edc734178a4d72a9c80f0595556f3fa19d801d181eb",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 277 bytes

~~~c

long _ZNK5Botan8CBC_Mode18update_granularityEv(long param_1)

{
  long lVar1;
  long lVar2;
  long *plVar3;
  
  plVar3 = *(long **)(param_1 + 8);
  lVar1 = (**(code **)(*plVar3 + 0x38))(plVar3);
  lVar2 = (**(code **)(*plVar3 + 0x30))(plVar3);
  return lVar1 * lVar2 * 4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004bccdc"></a> `004bccdc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-004bcce0"></a> `004bcce0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004bcce4"></a> `004bcce4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-004bcce8"></a> `004bcce8` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004bccec"></a> `004bccec` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-004bccf0"></a> `004bccf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bccf4"></a> `004bccf4` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-004bccf8"></a> `004bccf8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004bccfc"></a> `004bccfc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-004bcd00"></a> `004bcd00` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004bcd04"></a> `004bcd04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bcd08"></a> `004bcd08` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-004bcd0c"></a> `004bcd0c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004bcd10"></a> `004bcd10` | `88 7e 00 9b` | mul x8,x20,x0 | `FALL_THROUGH`
<a id="insn-004bcd14"></a> `004bcd14` | `00 f5 7e d3` | lsl x0,x8,#0x2 | `FALL_THROUGH`
<a id="insn-004bcd18"></a> `004bcd18` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004bcd1c"></a> `004bcd1c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-004bcd20"></a> `004bcd20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004bccdc`](#insn-004bccdc) 範囲 `[['004bccdc', '004bcd23']]`

## 命令位置別の参照

- [`004bccdc`](#insn-004bccdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcce0`](#insn-004bcce0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcd18`](#insn-004bcd18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcd1c`](#insn-004bcd1c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004bccdc`](#insn-004bccdc)

~~~json
{
  "source": "004bccdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcce0`](#insn-004bcce0)

~~~json
{
  "source": "004bcce0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcd18`](#insn-004bcd18)

~~~json
{
  "source": "004bcd18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcd1c`](#insn-004bcd1c)

~~~json
{
  "source": "004bcd1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
