# 00baeec4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baef8c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef8c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-9452ae0277af4a1ff67469544de3dcaf)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baeec4",
  "name": "_ZNSt6__ndk117__widen_from_utf8ILm32EED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e921948de5af103d49d283800e2dbda74e9e79e0126111a6706542ac50073a07",
  "source_text_sha256": "e921948de5af103d49d283800e2dbda74e9e79e0126111a6706542ac50073a07",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baeec4",
        "00baeeef"
      ]
    ],
    "bytes_sha256": "1e01a32eb8c479a57c5ecdf54bcffd90d22f1252d6885250b1538f4fc66d5633",
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
- [00be1b20](../00be1/00be1b20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 146 bytes

~~~c

void _ZNSt6__ndk117__widen_from_utf8ILm32EED0Ev(void *param_1)

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
<a id="insn-00baeec4"></a> `00baeec4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baeec8"></a> `00baeec8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00baeecc"></a> `00baeecc` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baeed0"></a> `00baeed0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00baeed4"></a> `00baeed4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baeed8"></a> `00baeed8` | `12 cb 00 94` | bl 0x00be1b20 | `UNCONDITIONAL_CALL`
<a id="insn-00baeedc"></a> `00baeedc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baeee0"></a> `00baeee0` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baeee4"></a> `00baeee4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00baeee8"></a> `00baeee8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baeeec"></a> `00baeeec` | `1d b0 00 14` | b 0x00bdaf60 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baeec4`](#insn-00baeec4) 範囲 `[['00baeec4', '00baeeef']]`

## 命令位置別の参照

- [`00baeec8`](#insn-00baeec8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeecc`](#insn-00baeecc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeed8`](#insn-00baeed8) → [`00be1b20`](../00be1/00be1b20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1b20` · 推定シンボル `None` · 推定型 `None`
- [`00baeee0`](#insn-00baeee0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeee4`](#insn-00baeee4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeeec`](#insn-00baeeec) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baeec8`](#insn-00baeec8)

~~~json
{
  "source": "00baeec8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeecc`](#insn-00baeecc)

~~~json
{
  "source": "00baeecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeed8`](#insn-00baeed8)

~~~json
{
  "source": "00baeed8",
  "target": "00be1b20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baeee0`](#insn-00baeee0)

~~~json
{
  "source": "00baeee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeee4`](#insn-00baeee4)

~~~json
{
  "source": "00baeee4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeeec`](#insn-00baeeec)

~~~json
{
  "source": "00baeeec",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
