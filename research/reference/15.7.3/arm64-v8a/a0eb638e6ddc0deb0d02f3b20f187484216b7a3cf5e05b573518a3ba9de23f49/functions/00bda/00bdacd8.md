# 00bdacd8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 要確認
  - [v15.7.2 → v15.7.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/review-0042.md#review-7cd726866e80200c4c5d96aed6cbf1c5)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 要確認
  - [v15.7.3 → v15.7.4 候補と検査根拠](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/review-0020.md#review-7cd726866e80200c4c5d96aed6cbf1c5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdacd8",
  "name": "FUN_00bdacd8",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c895b00262d6911d0d5a31a0ec7a2a7d69af6efb6c92338267a1c278f7db5e8b",
  "source_text_sha256": "c895b00262d6911d0d5a31a0ec7a2a7d69af6efb6c92338267a1c278f7db5e8b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdacd8",
        "00bdad07"
      ]
    ],
    "bytes_sha256": "042968977edecbf432e765b19c2c490e856fd0bc1bc8e33a1dae1076260ffcf6",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bd7ff4](../00bd7/00bd7ff4.md)

## 呼び出し先

解決済みの記録なし。

## 関連文字列（未確認候補）

~~~text
"unknown register"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 279 bytes

~~~c

char * FUN_00bdacd8(int param_1)

{
  if (param_1 + 2U < 0x62) {
                    /* try { // try from 00bdacf0 to 00cdad27 has its CatchHandler @ 00bdad58 */
    return &DAT_002fe11c + *(int *)(&DAT_002fe11c + (ulong)(param_1 + 2U) * 4);
  }
  return "unknown register";
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdacd8"></a> `00bdacd8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bdacdc"></a> `00bdacdc` | `08 08 00 11` | add w8,w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bdace0"></a> `00bdace0` | `1f 85 01 71` | cmp w8,#0x61 | `FALL_THROUGH`
<a id="insn-00bdace4"></a> `00bdace4` | `c8 00 00 54` | b.hi 0x00bdacfc | `CONDITIONAL_JUMP`
<a id="insn-00bdace8"></a> `00bdace8` | `29 b9 ff 90` | adrp x9,0x2fe000 | `FALL_THROUGH`
<a id="insn-00bdacec"></a> `00bdacec` | `29 71 04 91` | add x9,x9,#0x11c | `FALL_THROUGH`
<a id="insn-00bdacf0"></a> `00bdacf0` | `28 59 a8 b8` | ldrsw x8,[x9, w8, UXTW #0x2] | `FALL_THROUGH`
<a id="insn-00bdacf4"></a> `00bdacf4` | `20 01 08 8b` | add x0,x9,x8 | `FALL_THROUGH`
<a id="insn-00bdacf8"></a> `00bdacf8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdacfc"></a> `00bdacfc` | `60 b6 ff d0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bdad00"></a> `00bdad00` | `00 d4 00 91` | add x0,x0,#0x35 | `FALL_THROUGH`
<a id="insn-00bdad04"></a> `00bdad04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdacd8`](#insn-00bdacd8) 範囲 `[['00bdacd8', '00bdace7']]`
  - `CONDITIONAL_JUMP` [`00bdace4`](#insn-00bdace4) → [`00bdacfc`](#insn-00bdacfc)
  - `FALL_THROUGH` [`00bdace4`](#insn-00bdace4) → [`00bdace8`](#insn-00bdace8)
- ブロック [`00bdace8`](#insn-00bdace8) 範囲 `[['00bdace8', '00bdacef']]`
  - `FALL_THROUGH` [`00bdacec`](#insn-00bdacec) → [`00bdacf0`](#insn-00bdacf0)
- ブロック [`00bdacf0`](#insn-00bdacf0) 範囲 `[['00bdacf0', '00bdacfb']]`
- ブロック [`00bdacfc`](#insn-00bdacfc) 範囲 `[['00bdacfc', '00bdad07']]`

## 命令位置別の参照

- [`00bdace4`](#insn-00bdace4) → [`00bdacfc`](#insn-00bdacfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdacf0`](#insn-00bdacf0) → `002fe11c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad00`](#insn-00bdad00) → `002a8035`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdace4`](#insn-00bdace4)

~~~json
{
  "source": "00bdace4",
  "target": "00bdacfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdacf0`](#insn-00bdacf0)

~~~json
{
  "source": "00bdacf0",
  "target": "002fe11c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad00`](#insn-00bdad00)

~~~json
{
  "source": "00bdad00",
  "target": "002a8035",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8035",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "756e6b6e6f776e20726567697374657200",
  "capture_start": "002a8035",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
