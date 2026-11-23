# 00baee6c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baef34`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-fdeb511748d4d63802ecb6f0b2779551)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baee6c",
  "name": "_ZNSt6__ndk116__narrow_to_utf8ILm32EED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bc77379b2f97043393c6ec3a913d84319d0bde4f3ec066308aa5c90d796dd2ef",
  "source_text_sha256": "bc77379b2f97043393c6ec3a913d84319d0bde4f3ec066308aa5c90d796dd2ef",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baee6c",
        "00baee97"
      ]
    ],
    "bytes_sha256": "c467e8c018959a7f81bb8f3f63c3a28d8b03bb10863f729ad3b90e4557ed04ff",
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

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1b00](../00be1/00be1b00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 145 bytes

~~~c

void _ZNSt6__ndk116__narrow_to_utf8ILm32EED0Ev(void *param_1)

{
  _ZNSt6__ndk116__narrow_to_utf8ILm32EED1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baee6c"></a> `00baee6c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baee70"></a> `00baee70` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00baee74"></a> `00baee74` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baee78"></a> `00baee78` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00baee7c"></a> `00baee7c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baee80"></a> `00baee80` | `20 cb 00 94` | bl 0x00be1b00 | `UNCONDITIONAL_CALL`
<a id="insn-00baee84"></a> `00baee84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baee88"></a> `00baee88` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baee8c"></a> `00baee8c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00baee90"></a> `00baee90` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baee94"></a> `00baee94` | `33 b0 00 14` | b 0x00bdaf60 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baee6c`](#insn-00baee6c) 範囲 `[['00baee6c', '00baee97']]`

## 命令位置別の参照

- [`00baee70`](#insn-00baee70) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee74`](#insn-00baee74) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee80`](#insn-00baee80) → [`00be1b00`](../00be1/00be1b00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1b00` · 推定シンボル `None` · 推定型 `None`
- [`00baee88`](#insn-00baee88) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee8c`](#insn-00baee8c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee94`](#insn-00baee94) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baee70`](#insn-00baee70)

~~~json
{
  "source": "00baee70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee74`](#insn-00baee74)

~~~json
{
  "source": "00baee74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee80`](#insn-00baee80)

~~~json
{
  "source": "00baee80",
  "target": "00be1b00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baee88`](#insn-00baee88)

~~~json
{
  "source": "00baee88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee8c`](#insn-00baee8c)

~~~json
{
  "source": "00baee8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee94`](#insn-00baee94)

~~~json
{
  "source": "00baee94",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
