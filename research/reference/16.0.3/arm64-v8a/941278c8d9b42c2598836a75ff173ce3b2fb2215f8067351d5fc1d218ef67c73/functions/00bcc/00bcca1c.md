# 00bcca1c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcba28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcba28.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/machine_only_observed-0022.md#compare-f770cbc6e39d00aa67565a505f9dbcbf)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcca1c",
  "name": "FUN_00bcca1c",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "13fbd37beaa8f8d15eee91b83baf8229e61904ae00ba273c895d979488d745dc",
  "source_text_sha256": "13fbd37beaa8f8d15eee91b83baf8229e61904ae00ba273c895d979488d745dc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcca1c",
        "00bcca33"
      ]
    ],
    "bytes_sha256": "75ef2405c4213c05bc9eac32c4f2ee630b402c9fe4b9e056637c1f9273a27862",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 191 bytes

~~~c

void FUN_00bcca1c(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)*param_1;
  if (__ptr != (void *)0x0) {
    param_1[1] = __ptr;
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcca1c"></a> `00bcca1c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcca20"></a> `00bcca20` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bcca24"></a> `00bcca24` | `60 00 00 b4` | cbz x0,0x00bcca30 | `CONDITIONAL_JUMP`
<a id="insn-00bcca28"></a> `00bcca28` | `00 05 00 f9` | str x0,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcca2c"></a> `00bcca2c` | `49 31 02 14` | b 0x00c58f50 | `CALL_TERMINATOR`
<a id="insn-00bcca30"></a> `00bcca30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcca1c`](#insn-00bcca1c) 範囲 `[['00bcca1c', '00bcca27']]`
  - `CONDITIONAL_JUMP` [`00bcca24`](#insn-00bcca24) → [`00bcca30`](#insn-00bcca30)
  - `FALL_THROUGH` [`00bcca24`](#insn-00bcca24) → [`00bcca28`](#insn-00bcca28)
- ブロック [`00bcca28`](#insn-00bcca28) 範囲 `[['00bcca28', '00bcca2f']]`
- ブロック [`00bcca30`](#insn-00bcca30) 範囲 `[['00bcca30', '00bcca33']]`

## 命令位置別の参照

- [`00bcca24`](#insn-00bcca24) → [`00bcca30`](#insn-00bcca30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcca2c`](#insn-00bcca2c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcca24`](#insn-00bcca24)

~~~json
{
  "source": "00bcca24",
  "target": "00bcca30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcca2c`](#insn-00bcca2c)

~~~json
{
  "source": "00bcca2c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
