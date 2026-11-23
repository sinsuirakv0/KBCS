# 00bbaff8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbb0c0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb0c0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-c4d4916c2532f806ae28ebc7a8aa1a3d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaff8",
  "name": "_ZNSt8bad_castD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b4bbe4d918b565e77cb003df5f54a414349b271dade725a75222b6de84767d6f",
  "source_text_sha256": "b4bbe4d918b565e77cb003df5f54a414349b271dade725a75222b6de84767d6f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaff8",
        "00bbb023"
      ]
    ],
    "bytes_sha256": "9dbe6c66be10406844e17e89662f8b4992a82218be115876c163b6e132eefd35",
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
- [00be1390](../00be1/00be1390.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 99 bytes

~~~c

void _ZNSt8bad_castD0Ev(void *param_1)

{
  _ZNSt8bad_castD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaff8"></a> `00bbaff8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbaffc"></a> `00bbaffc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbb000"></a> `00bbb000` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb004"></a> `00bbb004` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbb008"></a> `00bbb008` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbb00c"></a> `00bbb00c` | `e1 98 00 94` | bl 0x00be1390 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb010"></a> `00bbb010` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb014"></a> `00bbb014` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb018"></a> `00bbb018` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbb01c"></a> `00bbb01c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbb020"></a> `00bbb020` | `d0 7f 00 14` | b 0x00bdaf60 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaff8`](#insn-00bbaff8) 範囲 `[['00bbaff8', '00bbb023']]`

## 命令位置別の参照

- [`00bbaffc`](#insn-00bbaffc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb000`](#insn-00bbb000) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb00c`](#insn-00bbb00c) → [`00be1390`](../00be1/00be1390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1390` · 推定シンボル `None` · 推定型 `None`
- [`00bbb014`](#insn-00bbb014) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb018`](#insn-00bbb018) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb020`](#insn-00bbb020) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaffc`](#insn-00bbaffc)

~~~json
{
  "source": "00bbaffc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb000`](#insn-00bbb000)

~~~json
{
  "source": "00bbb000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb00c`](#insn-00bbb00c)

~~~json
{
  "source": "00bbb00c",
  "target": "00be1390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb014`](#insn-00bbb014)

~~~json
{
  "source": "00bbb014",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb018`](#insn-00bbb018)

~~~json
{
  "source": "00bbb018",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb020`](#insn-00bbb020)

~~~json
{
  "source": "00bbb020",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
