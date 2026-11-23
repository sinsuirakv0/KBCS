# 00bbac6c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbad34`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbad34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-1c5eb7bb1656e4043339656d13da5a34)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbac6c",
  "name": "_ZNSt13bad_exceptionD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "420a010908402ca3732f70cc043d67b5c48fff5af707aeb7b4c2bc02a3e98bab",
  "source_text_sha256": "420a010908402ca3732f70cc043d67b5c48fff5af707aeb7b4c2bc02a3e98bab",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbac6c",
        "00bbac97"
      ]
    ],
    "bytes_sha256": "dcca32c893641243b50ee9167ef01f40743ad5902ca2cadc77f799b134c65e6f",
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
- [00be1d50](../00be1/00be1d50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1240 bytes

~~~c

void _ZNSt13bad_exceptionD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00bba0c8 with catch @ 00bbac70
                       catch() { ... } // from try @ 00bba218 with catch @ 00bbac70 */
                    /* catch() { ... } // from try @ 00bba0b0 with catch @ 00bbac74
                       catch() { ... } // from try @ 00bba200 with catch @ 00bbac74 */
                    /* catch() { ... } // from try @ 00bba094 with catch @ 00bbac78
                       catch() { ... } // from try @ 00bba1e8 with catch @ 00bbac78 */
                    /* catch() { ... } // from try @ 00bb7698 with catch @ 00bbac7c */
                    /* catch() { ... } // from try @ 00bb72e8 with catch @ 00bbac80 */
  _ZNSt20bad_array_new_lengthD1Ev();
                    /* catch() { ... } // from try @ 00bb6f34 with catch @ 00bbac84 */
                    /* catch() { ... } // from try @ 00bb6b80 with catch @ 00bbac88 */
                    /* catch() { ... } // from try @ 00bb67cc with catch @ 00bbac8c */
                    /* catch() { ... } // from try @ 00bb6418 with catch @ 00bbac90 */
                    /* catch() { ... } // from try @ 00bb6064 with catch @ 00bbac94 */
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbac6c"></a> `00bbac6c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbac70"></a> `00bbac70` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbac74"></a> `00bbac74` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbac78"></a> `00bbac78` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbac7c"></a> `00bbac7c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbac80"></a> `00bbac80` | `34 9c 00 94` | bl 0x00be1d50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbac84"></a> `00bbac84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbac88"></a> `00bbac88` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbac8c"></a> `00bbac8c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbac90"></a> `00bbac90` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbac94"></a> `00bbac94` | `b3 80 00 14` | b 0x00bdaf60 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbac6c`](#insn-00bbac6c) 範囲 `[['00bbac6c', '00bbac6f']]`
  - `FALL_THROUGH` [`00bbac6c`](#insn-00bbac6c) → [`00bbac70`](#insn-00bbac70)
- ブロック [`00bbac70`](#insn-00bbac70) 範囲 `[['00bbac70', '00bbac73']]`
  - `FALL_THROUGH` [`00bbac70`](#insn-00bbac70) → [`00bbac74`](#insn-00bbac74)
- ブロック [`00bbac74`](#insn-00bbac74) 範囲 `[['00bbac74', '00bbac77']]`
  - `FALL_THROUGH` [`00bbac74`](#insn-00bbac74) → [`00bbac78`](#insn-00bbac78)
- ブロック [`00bbac78`](#insn-00bbac78) 範囲 `[['00bbac78', '00bbac7b']]`
  - `FALL_THROUGH` [`00bbac78`](#insn-00bbac78) → [`00bbac7c`](#insn-00bbac7c)
- ブロック [`00bbac7c`](#insn-00bbac7c) 範囲 `[['00bbac7c', '00bbac7f']]`
  - `FALL_THROUGH` [`00bbac7c`](#insn-00bbac7c) → [`00bbac80`](#insn-00bbac80)
- ブロック [`00bbac80`](#insn-00bbac80) 範囲 `[['00bbac80', '00bbac83']]`
  - `FALL_THROUGH` [`00bbac80`](#insn-00bbac80) → [`00bbac84`](#insn-00bbac84)
- ブロック [`00bbac84`](#insn-00bbac84) 範囲 `[['00bbac84', '00bbac87']]`
  - `FALL_THROUGH` [`00bbac84`](#insn-00bbac84) → [`00bbac88`](#insn-00bbac88)
- ブロック [`00bbac88`](#insn-00bbac88) 範囲 `[['00bbac88', '00bbac8b']]`
  - `FALL_THROUGH` [`00bbac88`](#insn-00bbac88) → [`00bbac8c`](#insn-00bbac8c)
- ブロック [`00bbac8c`](#insn-00bbac8c) 範囲 `[['00bbac8c', '00bbac8f']]`
  - `FALL_THROUGH` [`00bbac8c`](#insn-00bbac8c) → [`00bbac90`](#insn-00bbac90)
- ブロック [`00bbac90`](#insn-00bbac90) 範囲 `[['00bbac90', '00bbac93']]`
  - `FALL_THROUGH` [`00bbac90`](#insn-00bbac90) → [`00bbac94`](#insn-00bbac94)
- ブロック [`00bbac94`](#insn-00bbac94) 範囲 `[['00bbac94', '00bbac97']]`

## 命令位置別の参照

- [`00bbac70`](#insn-00bbac70) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac74`](#insn-00bbac74) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac80`](#insn-00bbac80) → [`00be1d50`](../00be1/00be1d50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1d50` · 推定シンボル `None` · 推定型 `None`
- [`00bbac88`](#insn-00bbac88) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac8c`](#insn-00bbac8c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac94`](#insn-00bbac94) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbac70`](#insn-00bbac70)

~~~json
{
  "source": "00bbac70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac74`](#insn-00bbac74)

~~~json
{
  "source": "00bbac74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac80`](#insn-00bbac80)

~~~json
{
  "source": "00bbac80",
  "target": "00be1d50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbac88`](#insn-00bbac88)

~~~json
{
  "source": "00bbac88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac8c`](#insn-00bbac8c)

~~~json
{
  "source": "00bbac8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac94`](#insn-00bbac94)

~~~json
{
  "source": "00bbac94",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
