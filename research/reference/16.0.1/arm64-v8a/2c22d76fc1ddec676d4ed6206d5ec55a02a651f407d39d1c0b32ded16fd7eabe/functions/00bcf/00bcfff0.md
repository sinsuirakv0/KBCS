# 00bcfff0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcfbc8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfbc8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/reference_unresolved-0001.md#compare-9d17ab396219bc492d194f4d7c536743)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd008c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd008c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/reference_unresolved-0001.md#compare-dc7ff6d382c2850b90383e15eb4b24cf)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfff0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4UserEEEvPv",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a6e61bb8eb9afc08916d27070a0962d83813c5de22f9f63bc80009c0a66629e3",
  "source_text_sha256": "a6e61bb8eb9afc08916d27070a0962d83813c5de22f9f63bc80009c0a66629e3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfff0",
        "00bd0003"
      ]
    ],
    "bytes_sha256": "1f32248c643eb24f1357c02126bb7b159d61ed737b5fd3cd9e19d7f1b13c4b02",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 351 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4UserEEEvPv(long *param_1)

{
  if (param_1 != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x00bcfffc. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*param_1 + 8))();
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcfff0"></a> `00bcfff0` | `80 00 00 b4` | cbz x0,0x00bd0000 | `CONDITIONAL_JUMP`
<a id="insn-00bcfff4"></a> `00bcfff4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcfff8"></a> `00bcfff8` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfffc"></a> `00bcfffc` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00bd0000"></a> `00bd0000` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfff0`](#insn-00bcfff0) 範囲 `[['00bcfff0', '00bcfff3']]`
  - `CONDITIONAL_JUMP` [`00bcfff0`](#insn-00bcfff0) → [`00bd0000`](#insn-00bd0000)
  - `FALL_THROUGH` [`00bcfff0`](#insn-00bcfff0) → [`00bcfff4`](#insn-00bcfff4)
- ブロック [`00bcfff4`](#insn-00bcfff4) 範囲 `[['00bcfff4', '00bcffff']]`
- ブロック [`00bd0000`](#insn-00bd0000) 範囲 `[['00bd0000', '00bd0003']]`

## 命令位置別の参照

- [`00bcfff0`](#insn-00bcfff0) → [`00bd0000`](#insn-00bd0000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfff0`](#insn-00bcfff0)

~~~json
{
  "source": "00bcfff0",
  "target": "00bd0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
