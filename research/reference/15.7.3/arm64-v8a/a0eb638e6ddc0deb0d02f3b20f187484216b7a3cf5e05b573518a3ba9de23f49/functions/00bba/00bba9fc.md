# 00bba9fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bba934`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba934.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-3e6ac1004a077c67cc47c095b4392c18)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbaa40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-92451a2eec26322cb80887838f51e7eb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bba9fc",
  "name": "_ZSt10unexpectedv",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "43635d2ec0a2edc94267a5b96bf85e34d4f74cc1d16010853b6b087df98289fe",
  "source_text_sha256": "43635d2ec0a2edc94267a5b96bf85e34d4f74cc1d16010853b6b087df98289fe",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bba9fc",
        "00bbaa17"
      ]
    ],
    "bytes_sha256": "eb2cd3f7ec9c6ce6f074adb4652edd0b75486a1c10fb4feee0c241fd100fef80",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bba9e0](../00bba/00bba9e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 348 bytes

~~~c

undefined8 _ZSt10unexpectedv(void)

{
                    /* catch() { ... } // from try @ 00bb3cd0 with catch @ 00bbaa00 */
                    /* catch() { ... } // from try @ 00bb3930 with catch @ 00bbaa04 */
  FUN_00bba9e0(*(undefined8 *)PTR___cxa_unexpected_handler_00c1bfa8);
  return *(undefined8 *)PTR___cxa_terminate_handler_00c1bfb0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bba9fc"></a> `00bba9fc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbaa00"></a> `00bbaa00` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbaa04"></a> `00bbaa04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbaa08"></a> `00bbaa08` | `08 03 00 b0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbaa0c"></a> `00bbaa0c` | `08 d5 47 f9` | ldr x8,[x8, #0xfa8] | `FALL_THROUGH`
<a id="insn-00bbaa10"></a> `00bbaa10` | `00 fd df c8` | ldar x0,[x8] | `FALL_THROUGH`
<a id="insn-00bbaa14"></a> `00bbaa14` | `f3 ff ff 97` | bl 0x00bba9e0 | `UNCONDITIONAL_CALL`

## 基本ブロックと分岐先

- ブロック [`00bba9fc`](#insn-00bba9fc) 範囲 `[['00bba9fc', '00bba9ff']]`
  - `FALL_THROUGH` [`00bba9fc`](#insn-00bba9fc) → [`00bbaa00`](#insn-00bbaa00)
- ブロック [`00bbaa00`](#insn-00bbaa00) 範囲 `[['00bbaa00', '00bbaa03']]`
  - `FALL_THROUGH` [`00bbaa00`](#insn-00bbaa00) → [`00bbaa04`](#insn-00bbaa04)
- ブロック [`00bbaa04`](#insn-00bbaa04) 範囲 `[['00bbaa04', '00bbaa17']]`
  - `FALL_THROUGH` [`00bbaa14`](#insn-00bbaa14) → [`00bbaa18`](00bbaa18.md)

## 命令位置別の参照

- [`00bbaa00`](#insn-00bbaa00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaa0c`](#insn-00bbaa0c) → `00c1bfa8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbaa10`](#insn-00bbaa10) → `00c24948`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `__cxa_unexpected_handler` · 推定型 `pointer`
- [`00bbaa10`](#insn-00bbaa10) → [`00bbabbc`](00bbabbc.md) · `PARAM` · `ANALYSIS` · 関数 `00bbabbc` · 推定シンボル `None` · 推定型 `None`
- [`00bbaa14`](#insn-00bbaa14) → [`00bba9e0`](00bba9e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bba9e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaa00`](#insn-00bbaa00)

~~~json
{
  "source": "00bbaa00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaa0c`](#insn-00bbaa0c)

~~~json
{
  "source": "00bbaa0c",
  "target": "00c1bfa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bfa8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbaa10`](#insn-00bbaa10)

~~~json
{
  "source": "00bbaa10",
  "target": "00c24948",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24948",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbaa10`](#insn-00bbaa10)

~~~json
{
  "source": "00bbaa10",
  "target": "00bbabbc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaa14`](#insn-00bbaa14)

~~~json
{
  "source": "00bbaa14",
  "target": "00bba9e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
