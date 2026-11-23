# 00bbb2bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbb384`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb384.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-751a97a333da4e0b741e563db8c6f2dc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbb2bc",
  "name": "FUN_00bbb2bc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0005d1ea9e7b93d9fbfd215cd1ba52af5cf03578aaf3c927ce7ea4aeb14a2fd0",
  "source_text_sha256": "0005d1ea9e7b93d9fbfd215cd1ba52af5cf03578aaf3c927ce7ea4aeb14a2fd0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbb2bc",
        "00bbb2e7"
      ]
    ],
    "bytes_sha256": "6d2ce54feaa3ee363c049c1b02b3d8252e2821a2668e6c581aca0e72a65afcbe",
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
- [00be1d90](../00be1/00be1d90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 94 bytes

~~~c

void FUN_00bbb2bc(void *param_1)

{
  _ZNSt9type_infoD2Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbb2bc"></a> `00bbb2bc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbb2c0"></a> `00bbb2c0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbb2c4"></a> `00bbb2c4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb2c8"></a> `00bbb2c8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbb2cc"></a> `00bbb2cc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbb2d0"></a> `00bbb2d0` | `b0 9a 00 94` | bl 0x00be1d90 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb2d4"></a> `00bbb2d4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb2d8"></a> `00bbb2d8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb2dc"></a> `00bbb2dc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbb2e0"></a> `00bbb2e0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbb2e4"></a> `00bbb2e4` | `1f 7f 00 14` | b 0x00bdaf60 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbb2bc`](#insn-00bbb2bc) 範囲 `[['00bbb2bc', '00bbb2e7']]`

## 命令位置別の参照

- [`00bbb2c0`](#insn-00bbb2c0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb2c4`](#insn-00bbb2c4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb2d0`](#insn-00bbb2d0) → [`00be1d90`](../00be1/00be1d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1d90` · 推定シンボル `None` · 推定型 `None`
- [`00bbb2d8`](#insn-00bbb2d8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb2dc`](#insn-00bbb2dc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb2e4`](#insn-00bbb2e4) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbb2c0`](#insn-00bbb2c0)

~~~json
{
  "source": "00bbb2c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb2c4`](#insn-00bbb2c4)

~~~json
{
  "source": "00bbb2c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb2d0`](#insn-00bbb2d0)

~~~json
{
  "source": "00bbb2d0",
  "target": "00be1d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb2d8`](#insn-00bbb2d8)

~~~json
{
  "source": "00bbb2d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb2dc`](#insn-00bbb2dc)

~~~json
{
  "source": "00bbb2dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb2e4`](#insn-00bbb2e4)

~~~json
{
  "source": "00bbb2e4",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
