# 00bbacf8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbac30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbac30.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-026383cd41d1f819165735de3e296007)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbad3c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad3c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-c4ccec6db878d90ad1d5ab078291a010)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbacf8",
  "name": "_ZNSt9exceptionD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "91ebc617da88d03cd05fa623b4417b5d8a5fbeb1a1f78db9997d5a879008e22a",
  "source_text_sha256": "91ebc617da88d03cd05fa623b4417b5d8a5fbeb1a1f78db9997d5a879008e22a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbacf8",
        "00bbad23"
      ]
    ],
    "bytes_sha256": "1ca7d3888f13fa9deaec329e5503cab803b34f08aeb71e56e9c754490c353830",
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
- [00be1df0](../00be1/00be1df0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1487 bytes

~~~c

void _ZNSt9exceptionD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00bb39c4 with catch @ 00bbacfc */
                    /* catch() { ... } // from try @ 00bb41c0 with catch @ 00bbad00 */
                    /* catch() { ... } // from try @ 00bb3dd4 with catch @ 00bbad04 */
                    /* catch() { ... } // from try @ 00bb39b4 with catch @ 00bbad08 */
                    /* catch() { ... } // from try @ 00bba298 with catch @ 00bbad0c
                       catch() { ... } // from try @ 00bba3e8 with catch @ 00bbad0c */
  _ZNSt20bad_array_new_lengthD1Ev();
                    /* catch() { ... } // from try @ 00bba280 with catch @ 00bbad10
                       catch() { ... } // from try @ 00bba3d0 with catch @ 00bbad10 */
                    /* catch() { ... } // from try @ 00bba268 with catch @ 00bbad14
                       catch() { ... } // from try @ 00bba3b8 with catch @ 00bbad14 */
                    /* catch() { ... } // from try @ 00bba250 with catch @ 00bbad18
                       catch() { ... } // from try @ 00bba3a0 with catch @ 00bbad18 */
                    /* catch() { ... } // from try @ 00bba238 with catch @ 00bbad1c
                       catch() { ... } // from try @ 00bba388 with catch @ 00bbad1c */
                    /* catch() { ... } // from try @ 00bba220 with catch @ 00bbad20
                       catch() { ... } // from try @ 00bba370 with catch @ 00bbad20 */
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbacf8"></a> `00bbacf8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbacfc"></a> `00bbacfc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbad00"></a> `00bbad00` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbad04"></a> `00bbad04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbad08"></a> `00bbad08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbad0c"></a> `00bbad0c` | `39 9c 00 94` | bl 0x00be1df0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad10"></a> `00bbad10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbad14"></a> `00bbad14` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbad18"></a> `00bbad18` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbad1c"></a> `00bbad1c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbad20"></a> `00bbad20` | `bc 80 00 14` | b 0x00bdb010 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbacf8`](#insn-00bbacf8) 範囲 `[['00bbacf8', '00bbacfb']]`
  - `FALL_THROUGH` [`00bbacf8`](#insn-00bbacf8) → [`00bbacfc`](#insn-00bbacfc)
- ブロック [`00bbacfc`](#insn-00bbacfc) 範囲 `[['00bbacfc', '00bbacff']]`
  - `FALL_THROUGH` [`00bbacfc`](#insn-00bbacfc) → [`00bbad00`](#insn-00bbad00)
- ブロック [`00bbad00`](#insn-00bbad00) 範囲 `[['00bbad00', '00bbad03']]`
  - `FALL_THROUGH` [`00bbad00`](#insn-00bbad00) → [`00bbad04`](#insn-00bbad04)
- ブロック [`00bbad04`](#insn-00bbad04) 範囲 `[['00bbad04', '00bbad07']]`
  - `FALL_THROUGH` [`00bbad04`](#insn-00bbad04) → [`00bbad08`](#insn-00bbad08)
- ブロック [`00bbad08`](#insn-00bbad08) 範囲 `[['00bbad08', '00bbad0b']]`
  - `FALL_THROUGH` [`00bbad08`](#insn-00bbad08) → [`00bbad0c`](#insn-00bbad0c)
- ブロック [`00bbad0c`](#insn-00bbad0c) 範囲 `[['00bbad0c', '00bbad0f']]`
  - `FALL_THROUGH` [`00bbad0c`](#insn-00bbad0c) → [`00bbad10`](#insn-00bbad10)
- ブロック [`00bbad10`](#insn-00bbad10) 範囲 `[['00bbad10', '00bbad13']]`
  - `FALL_THROUGH` [`00bbad10`](#insn-00bbad10) → [`00bbad14`](#insn-00bbad14)
- ブロック [`00bbad14`](#insn-00bbad14) 範囲 `[['00bbad14', '00bbad17']]`
  - `FALL_THROUGH` [`00bbad14`](#insn-00bbad14) → [`00bbad18`](#insn-00bbad18)
- ブロック [`00bbad18`](#insn-00bbad18) 範囲 `[['00bbad18', '00bbad1b']]`
  - `FALL_THROUGH` [`00bbad18`](#insn-00bbad18) → [`00bbad1c`](#insn-00bbad1c)
- ブロック [`00bbad1c`](#insn-00bbad1c) 範囲 `[['00bbad1c', '00bbad1f']]`
  - `FALL_THROUGH` [`00bbad1c`](#insn-00bbad1c) → [`00bbad20`](#insn-00bbad20)
- ブロック [`00bbad20`](#insn-00bbad20) 範囲 `[['00bbad20', '00bbad23']]`

## 命令位置別の参照

- [`00bbacfc`](#insn-00bbacfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad00`](#insn-00bbad00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad0c`](#insn-00bbad0c) → [`00be1df0`](../00be1/00be1df0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1df0` · 推定シンボル `None` · 推定型 `None`
- [`00bbad14`](#insn-00bbad14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad18`](#insn-00bbad18) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad20`](#insn-00bbad20) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbacfc`](#insn-00bbacfc)

~~~json
{
  "source": "00bbacfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad00`](#insn-00bbad00)

~~~json
{
  "source": "00bbad00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad0c`](#insn-00bbad0c)

~~~json
{
  "source": "00bbad0c",
  "target": "00be1df0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad14`](#insn-00bbad14)

~~~json
{
  "source": "00bbad14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad18`](#insn-00bbad18)

~~~json
{
  "source": "00bbad18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad20`](#insn-00bbad20)

~~~json
{
  "source": "00bbad20",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
