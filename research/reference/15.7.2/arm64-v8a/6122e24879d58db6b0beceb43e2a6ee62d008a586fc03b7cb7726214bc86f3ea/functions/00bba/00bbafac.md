# 00bbafac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbb074`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb074.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-f3c519132be3cbe89010c8f36e812d25)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbafac",
  "name": "_ZNSt9type_infoD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2ab2390b57f213c0acc4711cc900f8cd3cbd42470e20dcf35947edf45494c388",
  "source_text_sha256": "2ab2390b57f213c0acc4711cc900f8cd3cbd42470e20dcf35947edf45494c388",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbafac",
        "00bbafd7"
      ]
    ],
    "bytes_sha256": "ed349d478e682db5c7d9382393de6fa4d071666ab82eb2e9d637fe1277023983",
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
- [00be1da0](../00be1/00be1da0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 101 bytes

~~~c

void _ZNSt9type_infoD0Ev(void *param_1)

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
<a id="insn-00bbafac"></a> `00bbafac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbafb0"></a> `00bbafb0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbafb4"></a> `00bbafb4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbafb8"></a> `00bbafb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbafbc"></a> `00bbafbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbafc0"></a> `00bbafc0` | `78 9b 00 94` | bl 0x00be1da0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbafc4"></a> `00bbafc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbafc8"></a> `00bbafc8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbafcc"></a> `00bbafcc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbafd0"></a> `00bbafd0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbafd4"></a> `00bbafd4` | `e3 7f 00 14` | b 0x00bdaf60 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbafac`](#insn-00bbafac) 範囲 `[['00bbafac', '00bbafd7']]`

## 命令位置別の参照

- [`00bbafb0`](#insn-00bbafb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafb4`](#insn-00bbafb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafc0`](#insn-00bbafc0) → [`00be1da0`](../00be1/00be1da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1da0` · 推定シンボル `None` · 推定型 `None`
- [`00bbafc8`](#insn-00bbafc8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafcc`](#insn-00bbafcc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafd4`](#insn-00bbafd4) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbafb0`](#insn-00bbafb0)

~~~json
{
  "source": "00bbafb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafb4`](#insn-00bbafb4)

~~~json
{
  "source": "00bbafb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafc0`](#insn-00bbafc0)

~~~json
{
  "source": "00bbafc0",
  "target": "00be1da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbafc8`](#insn-00bbafc8)

~~~json
{
  "source": "00bbafc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafcc`](#insn-00bbafcc)

~~~json
{
  "source": "00bbafcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafd4`](#insn-00bbafd4)

~~~json
{
  "source": "00bbafd4",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
