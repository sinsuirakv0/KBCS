# 00bbab7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbac44`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbac44.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-81fda719d480a78b7ddca961f0a4e21a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbab7c",
  "name": "_ZSt15set_new_handlerPFvvE",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f9d651763cedec1950563350dc0815a15185c682364fd85914efd5dd7f9f7a63",
  "source_text_sha256": "f9d651763cedec1950563350dc0815a15185c682364fd85914efd5dd7f9f7a63",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbab7c",
        "00bbab9f"
      ]
    ],
    "bytes_sha256": "0ab4a1d440abd8e892a7273bbcfcc13bbf9e9a885cee7b2fd64f72326bb52d45",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bd6cd0](../00bd6/00bd6cd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 821 bytes

~~~c

void _ZSt15set_new_handlerPFvvE(undefined8 param_1)

{
                    /* catch() { ... } // from try @ 00bb42a8 with catch @ 00bbab80 */
                    /* catch() { ... } // from try @ 00bb3ebc with catch @ 00bbab84 */
                    /* catch() { ... } // from try @ 00bb3a9c with catch @ 00bbab88 */
                    /* catch() { ... } // from try @ 00bb7634 with catch @ 00bbab8c */
                    /* catch() { ... } // from try @ 00bb7284 with catch @ 00bbab90 */
  FUN_00bd6cd0(param_1,PTR___cxa_new_handler_00c1bf08);
                    /* catch() { ... } // from try @ 00bb6ed0 with catch @ 00bbab94 */
                    /* catch() { ... } // from try @ 00bb6b1c with catch @ 00bbab98 */
                    /* catch() { ... } // from try @ 00bb6768 with catch @ 00bbab9c */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbab7c"></a> `00bbab7c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbab80"></a> `00bbab80` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbab84"></a> `00bbab84` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbab88"></a> `00bbab88` | `01 03 00 b0` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbab8c"></a> `00bbab8c` | `21 84 47 f9` | ldr x1,[x1, #0xf08] | `FALL_THROUGH`
<a id="insn-00bbab90"></a> `00bbab90` | `50 70 00 94` | bl 0x00bd6cd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbab94"></a> `00bbab94` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bbab98"></a> `00bbab98` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbab9c"></a> `00bbab9c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbab7c`](#insn-00bbab7c) 範囲 `[['00bbab7c', '00bbab7f']]`
  - `FALL_THROUGH` [`00bbab7c`](#insn-00bbab7c) → [`00bbab80`](#insn-00bbab80)
- ブロック [`00bbab80`](#insn-00bbab80) 範囲 `[['00bbab80', '00bbab83']]`
  - `FALL_THROUGH` [`00bbab80`](#insn-00bbab80) → [`00bbab84`](#insn-00bbab84)
- ブロック [`00bbab84`](#insn-00bbab84) 範囲 `[['00bbab84', '00bbab87']]`
  - `FALL_THROUGH` [`00bbab84`](#insn-00bbab84) → [`00bbab88`](#insn-00bbab88)
- ブロック [`00bbab88`](#insn-00bbab88) 範囲 `[['00bbab88', '00bbab8b']]`
  - `FALL_THROUGH` [`00bbab88`](#insn-00bbab88) → [`00bbab8c`](#insn-00bbab8c)
- ブロック [`00bbab8c`](#insn-00bbab8c) 範囲 `[['00bbab8c', '00bbab8f']]`
  - `FALL_THROUGH` [`00bbab8c`](#insn-00bbab8c) → [`00bbab90`](#insn-00bbab90)
- ブロック [`00bbab90`](#insn-00bbab90) 範囲 `[['00bbab90', '00bbab93']]`
  - `FALL_THROUGH` [`00bbab90`](#insn-00bbab90) → [`00bbab94`](#insn-00bbab94)
- ブロック [`00bbab94`](#insn-00bbab94) 範囲 `[['00bbab94', '00bbab97']]`
  - `FALL_THROUGH` [`00bbab94`](#insn-00bbab94) → [`00bbab98`](#insn-00bbab98)
- ブロック [`00bbab98`](#insn-00bbab98) 範囲 `[['00bbab98', '00bbab9b']]`
  - `FALL_THROUGH` [`00bbab98`](#insn-00bbab98) → [`00bbab9c`](#insn-00bbab9c)
- ブロック [`00bbab9c`](#insn-00bbab9c) 範囲 `[['00bbab9c', '00bbab9f']]`

## 命令位置別の参照

- [`00bbab80`](#insn-00bbab80) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab8c`](#insn-00bbab8c) → `00c1bf08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbab8c`](#insn-00bbab8c) → `010a3658`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `__cxa_new_handler` · 推定型 `undefined8`
- [`00bbab90`](#insn-00bbab90) → [`00bd6cd0`](../00bd6/00bd6cd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6cd0` · 推定シンボル `None` · 推定型 `None`
- [`00bbab94`](#insn-00bbab94) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbab80`](#insn-00bbab80)

~~~json
{
  "source": "00bbab80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab8c`](#insn-00bbab8c)

~~~json
{
  "source": "00bbab8c",
  "target": "00c1bf08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bf08",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbab8c`](#insn-00bbab8c)

~~~json
{
  "source": "00bbab8c",
  "target": "010a3658",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3658",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbab90`](#insn-00bbab90)

~~~json
{
  "source": "00bbab90",
  "target": "00bd6cd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbab94`](#insn-00bbab94)

~~~json
{
  "source": "00bbab94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
