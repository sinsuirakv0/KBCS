# 00bbaddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbad14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbad14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-0220b8044049ed20c7767f252f469d35)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbae20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-34e5a7301ee267c9b93a70e645735fbc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaddc",
  "name": "_ZNSt20bad_array_new_lengthD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8a80914d12dacfc9e757b7252b5e6e74e3502f084c762ef55eb87ad43b8f3d17",
  "source_text_sha256": "8a80914d12dacfc9e757b7252b5e6e74e3502f084c762ef55eb87ad43b8f3d17",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaddc",
        "00bbae07"
      ]
    ],
    "bytes_sha256": "56ed712271fb7b83b9aeb26e0be7f61ba186f0b6c3ac13abc00a3a276c0f8566",
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
- [00bdb1a0](../00bdb/00bdb1a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 647 bytes

~~~c

void _ZNSt20bad_array_new_lengthD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00bb45b0 with catch @ 00bbadf0 */
  _ZNSt20bad_array_new_lengthD1Ev();
                    /* catch() { ... } // from try @ 00bb764c with catch @ 00bbadf4 */
                    /* catch() { ... } // from try @ 00bb729c with catch @ 00bbadf8 */
                    /* catch() { ... } // from try @ 00bb6ee8 with catch @ 00bbadfc */
                    /* catch() { ... } // from try @ 00bb6b34 with catch @ 00bbae00 */
                    /* catch() { ... } // from try @ 00bb6780 with catch @ 00bbae04 */
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaddc"></a> `00bbaddc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbade0"></a> `00bbade0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbade4"></a> `00bbade4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbade8"></a> `00bbade8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbadec"></a> `00bbadec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbadf0"></a> `00bbadf0` | `ec 80 00 94` | bl 0x00bdb1a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbadf4"></a> `00bbadf4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbadf8"></a> `00bbadf8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbadfc"></a> `00bbadfc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbae00"></a> `00bbae00` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbae04"></a> `00bbae04` | `83 80 00 14` | b 0x00bdb010 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaddc`](#insn-00bbaddc) 範囲 `[['00bbaddc', '00bbadef']]`
  - `FALL_THROUGH` [`00bbadec`](#insn-00bbadec) → [`00bbadf0`](#insn-00bbadf0)
- ブロック [`00bbadf0`](#insn-00bbadf0) 範囲 `[['00bbadf0', '00bbadf3']]`
  - `FALL_THROUGH` [`00bbadf0`](#insn-00bbadf0) → [`00bbadf4`](#insn-00bbadf4)
- ブロック [`00bbadf4`](#insn-00bbadf4) 範囲 `[['00bbadf4', '00bbadf7']]`
  - `FALL_THROUGH` [`00bbadf4`](#insn-00bbadf4) → [`00bbadf8`](#insn-00bbadf8)
- ブロック [`00bbadf8`](#insn-00bbadf8) 範囲 `[['00bbadf8', '00bbadfb']]`
  - `FALL_THROUGH` [`00bbadf8`](#insn-00bbadf8) → [`00bbadfc`](#insn-00bbadfc)
- ブロック [`00bbadfc`](#insn-00bbadfc) 範囲 `[['00bbadfc', '00bbadff']]`
  - `FALL_THROUGH` [`00bbadfc`](#insn-00bbadfc) → [`00bbae00`](#insn-00bbae00)
- ブロック [`00bbae00`](#insn-00bbae00) 範囲 `[['00bbae00', '00bbae03']]`
  - `FALL_THROUGH` [`00bbae00`](#insn-00bbae00) → [`00bbae04`](#insn-00bbae04)
- ブロック [`00bbae04`](#insn-00bbae04) 範囲 `[['00bbae04', '00bbae07']]`

## 命令位置別の参照

- [`00bbade0`](#insn-00bbade0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbade4`](#insn-00bbade4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadf0`](#insn-00bbadf0) → [`00bdb1a0`](../00bdb/00bdb1a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbadf8`](#insn-00bbadf8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadfc`](#insn-00bbadfc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae04`](#insn-00bbae04) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbade0`](#insn-00bbade0)

~~~json
{
  "source": "00bbade0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbade4`](#insn-00bbade4)

~~~json
{
  "source": "00bbade4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadf0`](#insn-00bbadf0)

~~~json
{
  "source": "00bbadf0",
  "target": "00bdb1a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbadf8`](#insn-00bbadf8)

~~~json
{
  "source": "00bbadf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadfc`](#insn-00bbadfc)

~~~json
{
  "source": "00bbadfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae04`](#insn-00bbae04)

~~~json
{
  "source": "00bbae04",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
