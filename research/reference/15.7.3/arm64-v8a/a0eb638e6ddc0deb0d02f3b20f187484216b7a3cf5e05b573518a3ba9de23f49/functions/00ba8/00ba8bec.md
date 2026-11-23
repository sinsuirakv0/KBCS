# 00ba8bec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ba8b24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8b24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0077.md#compare-b72f044c14de65db8f8b975adcd71258)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ba8c30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8c30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0016.md#compare-eaf1174c5282afdcbb4206c5c77b2406)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba8bec",
  "name": "_ZNSt6__ndk114collate_bynameIcED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "58a48254c836d1a87cb5c7aa54127d6313063da449632fac2646ee3dd1f4357e",
  "source_text_sha256": "58a48254c836d1a87cb5c7aa54127d6313063da449632fac2646ee3dd1f4357e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba8bec",
        "00ba8c17"
      ]
    ],
    "bytes_sha256": "d905725df001b861430a640d6f657e3f3ea72b7d1bd748222790f97b8d0259eb",
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

- [00bdb010](../00bdb/00bdb010.md)
- [00be18f0](../00be1/00be18f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 327 bytes

~~~c

void _ZNSt6__ndk114collate_bynameIcED0Ev(void *param_1)

{
                    /* try { // try from 00ba8bf0 to 00ca8bf7 has its CatchHandler @ 00ba8d48 */
  _ZNSt6__ndk114collate_bynameIcED1Ev();
                    /* try { // try from 00ba8c0c to 00ca8c13 has its CatchHandler @ 00ba8db0 */
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba8bec"></a> `00ba8bec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00ba8bf0"></a> `00ba8bf0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ba8bf4"></a> `00ba8bf4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba8bf8"></a> `00ba8bf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ba8bfc"></a> `00ba8bfc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ba8c00"></a> `00ba8c00` | `3c e3 00 94` | bl 0x00be18f0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba8c04"></a> `00ba8c04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba8c08"></a> `00ba8c08` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba8c0c"></a> `00ba8c0c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ba8c10"></a> `00ba8c10` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00ba8c14"></a> `00ba8c14` | `ff c8 00 14` | b 0x00bdb010 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ba8bec`](#insn-00ba8bec) 範囲 `[['00ba8bec', '00ba8bef']]`
  - `FALL_THROUGH` [`00ba8bec`](#insn-00ba8bec) → [`00ba8bf0`](#insn-00ba8bf0)
- ブロック [`00ba8bf0`](#insn-00ba8bf0) 範囲 `[['00ba8bf0', '00ba8c0b']]`
  - `FALL_THROUGH` [`00ba8c08`](#insn-00ba8c08) → [`00ba8c0c`](#insn-00ba8c0c)
- ブロック [`00ba8c0c`](#insn-00ba8c0c) 範囲 `[['00ba8c0c', '00ba8c17']]`

## 命令位置別の参照

- [`00ba8bf0`](#insn-00ba8bf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8bf4`](#insn-00ba8bf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8c00`](#insn-00ba8c00) → [`00be18f0`](../00be1/00be18f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be18f0` · 推定シンボル `None` · 推定型 `None`
- [`00ba8c08`](#insn-00ba8c08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8c0c`](#insn-00ba8c0c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8c14`](#insn-00ba8c14) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba8bf0`](#insn-00ba8bf0)

~~~json
{
  "source": "00ba8bf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8bf4`](#insn-00ba8bf4)

~~~json
{
  "source": "00ba8bf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8c00`](#insn-00ba8c00)

~~~json
{
  "source": "00ba8c00",
  "target": "00be18f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba8c08`](#insn-00ba8c08)

~~~json
{
  "source": "00ba8c08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8c0c`](#insn-00ba8c0c)

~~~json
{
  "source": "00ba8c0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8c14`](#insn-00ba8c14)

~~~json
{
  "source": "00ba8c14",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
