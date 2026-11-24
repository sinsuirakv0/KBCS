# 00bbadcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbad88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbad88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-3033a4ba3723bd1f37aa8b1acdc1da34)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c37814`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37814.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-6a5ad0446b1d570c3f98ba715aa9bf61)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbadcc",
  "name": "_ZNSt9bad_allocD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb9a665288e7dedbd6548ffd2f05cce38a2a487ec2013fb800908f569585e707",
  "source_text_sha256": "eb9a665288e7dedbd6548ffd2f05cce38a2a487ec2013fb800908f569585e707",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbadcc",
        "00bbadf7"
      ]
    ],
    "bytes_sha256": "bffe68b062d00d69b3c80086da031af9f1efed23128f1d2419686ee8dc23e0ee",
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

- [00bdb060](../00bdb/00bdb060.md)
- [00bdbc00](../00bdb/00bdbc00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 983 bytes

~~~c

void _ZNSt9bad_allocD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00bb6f54 with catch @ 00bbadd0 */
                    /* catch() { ... } // from try @ 00bb6ba0 with catch @ 00bbadd4 */
                    /* catch() { ... } // from try @ 00bb6b88 with catch @ 00bbadd8 */
                    /* catch() { ... } // from try @ 00bb67d4 with catch @ 00bbaddc */
                    /* catch() { ... } // from try @ 00bb67ec with catch @ 00bbade0 */
  _ZNSt20bad_array_new_lengthD1Ev();
                    /* catch() { ... } // from try @ 00bb6420 with catch @ 00bbade4 */
                    /* catch() { ... } // from try @ 00bb6438 with catch @ 00bbade8 */
                    /* catch() { ... } // from try @ 00bb6084 with catch @ 00bbadec */
                    /* catch() { ... } // from try @ 00bb606c with catch @ 00bbadf0 */
                    /* catch() { ... } // from try @ 00bb5cc4 with catch @ 00bbadf4 */
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbadcc"></a> `00bbadcc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbadd0"></a> `00bbadd0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbadd4"></a> `00bbadd4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbadd8"></a> `00bbadd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbaddc"></a> `00bbaddc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbade0"></a> `00bbade0` | `88 83 00 94` | bl 0x00bdbc00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbade4"></a> `00bbade4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbade8"></a> `00bbade8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbadec"></a> `00bbadec` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbadf0"></a> `00bbadf0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbadf4"></a> `00bbadf4` | `9b 80 00 14` | b 0x00bdb060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbadcc`](#insn-00bbadcc) 範囲 `[['00bbadcc', '00bbadcf']]`
  - `FALL_THROUGH` [`00bbadcc`](#insn-00bbadcc) → [`00bbadd0`](#insn-00bbadd0)
- ブロック [`00bbadd0`](#insn-00bbadd0) 範囲 `[['00bbadd0', '00bbadd3']]`
  - `FALL_THROUGH` [`00bbadd0`](#insn-00bbadd0) → [`00bbadd4`](#insn-00bbadd4)
- ブロック [`00bbadd4`](#insn-00bbadd4) 範囲 `[['00bbadd4', '00bbadd7']]`
  - `FALL_THROUGH` [`00bbadd4`](#insn-00bbadd4) → [`00bbadd8`](#insn-00bbadd8)
- ブロック [`00bbadd8`](#insn-00bbadd8) 範囲 `[['00bbadd8', '00bbaddb']]`
  - `FALL_THROUGH` [`00bbadd8`](#insn-00bbadd8) → [`00bbaddc`](#insn-00bbaddc)
- ブロック [`00bbaddc`](#insn-00bbaddc) 範囲 `[['00bbaddc', '00bbaddf']]`
  - `FALL_THROUGH` [`00bbaddc`](#insn-00bbaddc) → [`00bbade0`](#insn-00bbade0)
- ブロック [`00bbade0`](#insn-00bbade0) 範囲 `[['00bbade0', '00bbade3']]`
  - `FALL_THROUGH` [`00bbade0`](#insn-00bbade0) → [`00bbade4`](#insn-00bbade4)
- ブロック [`00bbade4`](#insn-00bbade4) 範囲 `[['00bbade4', '00bbade7']]`
  - `FALL_THROUGH` [`00bbade4`](#insn-00bbade4) → [`00bbade8`](#insn-00bbade8)
- ブロック [`00bbade8`](#insn-00bbade8) 範囲 `[['00bbade8', '00bbadeb']]`
  - `FALL_THROUGH` [`00bbade8`](#insn-00bbade8) → [`00bbadec`](#insn-00bbadec)
- ブロック [`00bbadec`](#insn-00bbadec) 範囲 `[['00bbadec', '00bbadef']]`
  - `FALL_THROUGH` [`00bbadec`](#insn-00bbadec) → [`00bbadf0`](#insn-00bbadf0)
- ブロック [`00bbadf0`](#insn-00bbadf0) 範囲 `[['00bbadf0', '00bbadf3']]`
  - `FALL_THROUGH` [`00bbadf0`](#insn-00bbadf0) → [`00bbadf4`](#insn-00bbadf4)
- ブロック [`00bbadf4`](#insn-00bbadf4) 範囲 `[['00bbadf4', '00bbadf7']]`

## 命令位置別の参照

- [`00bbadd0`](#insn-00bbadd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadd4`](#insn-00bbadd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbade0`](#insn-00bbade0) → [`00bdbc00`](../00bdb/00bdbc00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdbc00` · 推定シンボル `None` · 推定型 `None`
- [`00bbade8`](#insn-00bbade8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadec`](#insn-00bbadec) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadf4`](#insn-00bbadf4) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbadd0`](#insn-00bbadd0)

~~~json
{
  "source": "00bbadd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadd4`](#insn-00bbadd4)

~~~json
{
  "source": "00bbadd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbade0`](#insn-00bbade0)

~~~json
{
  "source": "00bbade0",
  "target": "00bdbc00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbade8`](#insn-00bbade8)

~~~json
{
  "source": "00bbade8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadec`](#insn-00bbadec)

~~~json
{
  "source": "00bbadec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadf4`](#insn-00bbadf4)

~~~json
{
  "source": "00bbadf4",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
