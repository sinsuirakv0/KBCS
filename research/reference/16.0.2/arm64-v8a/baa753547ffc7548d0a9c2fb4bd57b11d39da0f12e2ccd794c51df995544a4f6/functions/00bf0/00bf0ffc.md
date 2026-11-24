# 00bf0ffc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf0f60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0f60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/machine_only_observed-0022.md#compare-80ee406fb285ddf5324840dbf7736346)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf1ff0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1ff0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/machine_only_observed-0022.md#compare-436aa2441c6ec7eb11b3ca7d4a5354b4)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf0ffc",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "762f986ee785cfbcd659f0684b8e3f9cc905ba43b9c71808663e528c38a01305",
  "source_text_sha256": "762f986ee785cfbcd659f0684b8e3f9cc905ba43b9c71808663e528c38a01305",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf0ffc",
        "00bf1013"
      ]
    ],
    "bytes_sha256": "4ca25e3468a65f1f9a0b9cb256c2873296ba9bc322813e4e4634c3f3cbb67f81",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e120](../00c5e/00c5e120.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 191 bytes

~~~c

void _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(byte *param_1)

{
  if ((*param_1 & 1) == 0) {
    return;
  }
  _ZdlPv(*(void **)(param_1 + 0x10));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf0ffc"></a> `00bf0ffc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bf1000"></a> `00bf1000` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00bf1004"></a> `00bf1004` | `48 00 00 37` | tbnz w8,#0x0,0x00bf100c | `CONDITIONAL_JUMP`
<a id="insn-00bf1008"></a> `00bf1008` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf100c"></a> `00bf100c` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bf1010"></a> `00bf1010` | `dc 9b 01 14` | b 0x00c57f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf0ffc`](#insn-00bf0ffc) 範囲 `[['00bf0ffc', '00bf1007']]`
  - `CONDITIONAL_JUMP` [`00bf1004`](#insn-00bf1004) → [`00bf100c`](#insn-00bf100c)
  - `FALL_THROUGH` [`00bf1004`](#insn-00bf1004) → [`00bf1008`](#insn-00bf1008)
- ブロック [`00bf1008`](#insn-00bf1008) 範囲 `[['00bf1008', '00bf100b']]`
- ブロック [`00bf100c`](#insn-00bf100c) 範囲 `[['00bf100c', '00bf1013']]`

## 命令位置別の参照

- [`00bf1004`](#insn-00bf1004) → [`00bf100c`](#insn-00bf100c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1010`](#insn-00bf1010) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf1004`](#insn-00bf1004)

~~~json
{
  "source": "00bf1004",
  "target": "00bf100c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1010`](#insn-00bf1010)

~~~json
{
  "source": "00bf1010",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
