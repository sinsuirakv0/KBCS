# 00bfbbec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfbb50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-cea63bcd13e52694f761ee4ca26a612b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfcbe0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcbe0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-81f8c58ae8e46beb16079a078d600e9d)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbbec",
  "name": "_ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "67bfe29a72f6e96397eba1abfdf93da23d29996393dc0d5b352ad13be166092b",
  "source_text_sha256": "67bfe29a72f6e96397eba1abfdf93da23d29996393dc0d5b352ad13be166092b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbbec",
        "00bfbc17"
      ]
    ],
    "bytes_sha256": "4208d7620819a9d4e75743ca9c313fc0b2a489aa4ee787d8161064934a88620f",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c5e410](../00c5e/00c5e410.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 161 bytes

~~~c

void _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED0Ev(void *param_1)

{
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbbec"></a> `00bfbbec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbbf0"></a> `00bfbbf0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfbbf4"></a> `00bfbbf4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbbf8"></a> `00bfbbf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfbbfc"></a> `00bfbbfc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfbc00"></a> `00bfbc00` | `04 8a 01 94` | bl 0x00c5e410 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbc04"></a> `00bfbc04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfbc08"></a> `00bfbc08` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbc0c"></a> `00bfbc0c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfbc10"></a> `00bfbc10` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfbc14"></a> `00bfbc14` | `db 70 01 14` | b 0x00c57f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbbec`](#insn-00bfbbec) 範囲 `[['00bfbbec', '00bfbc17']]`

## 命令位置別の参照

- [`00bfbbf0`](#insn-00bfbbf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbbf4`](#insn-00bfbbf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbc00`](#insn-00bfbc00) → [`00c5e410`](../00c5e/00c5e410.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e410` · 推定シンボル `None` · 推定型 `None`
- [`00bfbc08`](#insn-00bfbc08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbc0c`](#insn-00bfbc0c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbc14`](#insn-00bfbc14) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbbf0`](#insn-00bfbbf0)

~~~json
{
  "source": "00bfbbf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbbf4`](#insn-00bfbbf4)

~~~json
{
  "source": "00bfbbf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbc00`](#insn-00bfbc00)

~~~json
{
  "source": "00bfbc00",
  "target": "00c5e410",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbc08`](#insn-00bfbc08)

~~~json
{
  "source": "00bfbc08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbc0c`](#insn-00bfbc0c)

~~~json
{
  "source": "00bfbc0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbc14`](#insn-00bfbc14)

~~~json
{
  "source": "00bfbc14",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
