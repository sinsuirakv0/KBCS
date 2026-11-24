# 00b4afdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b4af98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af98.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0068.md#compare-bc30a8625b63d55fec868b5605b828d3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bb8d00`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8d00.md) · 移動量 `+0x6dd24`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0016.md#compare-76ccd7a8521d170d5a00978fb20c9da1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4afdc",
  "name": "_ZN8firebase9messaging27registration_intent_service12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8b2d0a43dd972d7b1a1517f60d1c783eaa6cf9a07d9351aa6007044503a60bd3",
  "source_text_sha256": "8b2d0a43dd972d7b1a1517f60d1c783eaa6cf9a07d9351aa6007044503a60bd3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4afdc",
        "00b4b04b"
      ]
    ],
    "bytes_sha256": "147469034e28df58362b338d5832fd0ccc9149647bd2262a27ef9642a104d641",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde0e0](../00bde/00bde0e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 698 bytes

~~~c

void _ZN8firebase9messaging27registration_intent_service12ReleaseClassEP7_JNIEnv(long *param_1)

{
                    /* try { // try from 00b4aff4 to 00c4afff has its CatchHandler @ 00b4b1b0 */
  if (DAT_010a1058 != 0) {
    if (DAT_010a1060 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a1060 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
                    /* try { // try from 00b4b024 to 00c4b02f has its CatchHandler @ 00b4b188 */
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a1058);
    DAT_010a1058 = 0;
  }
                    /* try { // try from 00b4b044 to 00c4b04f has its CatchHandler @ 00b4b184 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4afdc"></a> `00b4afdc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b4afe0"></a> `00b4afe0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4afe4"></a> `00b4afe4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4afe8"></a> `00b4afe8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b4afec"></a> `00b4afec` | `b4 2a 00 f0` | adrp x20,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b4aff0"></a> `00b4aff0` | `81 2e 40 f9` | ldr x1,[x20, #0x58] | `FALL_THROUGH`
<a id="insn-00b4aff4"></a> `00b4aff4` | `41 02 00 b4` | cbz x1,0x00b4b03c | `CONDITIONAL_JUMP`
<a id="insn-00b4aff8"></a> `00b4aff8` | `b5 2a 00 f0` | adrp x21,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b4affc"></a> `00b4affc` | `a8 82 41 39` | ldrb w8,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00b4b000"></a> `00b4b000` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b4b004"></a> `00b4b004` | `c8 00 00 34` | cbz w8,0x00b4b01c | `CONDITIONAL_JUMP`
<a id="insn-00b4b008"></a> `00b4b008` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4b00c"></a> `00b4b00c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4b010"></a> `00b4b010` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00b4b014"></a> `00b4b014` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4b018"></a> `00b4b018` | `bf 82 01 39` | strb wzr,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00b4b01c"></a> `00b4b01c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4b020"></a> `00b4b020` | `30 4c 02 94` | bl 0x00bde0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4b024"></a> `00b4b024` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4b028"></a> `00b4b028` | `81 2e 40 f9` | ldr x1,[x20, #0x58] | `FALL_THROUGH`
<a id="insn-00b4b02c"></a> `00b4b02c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4b030"></a> `00b4b030` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00b4b034"></a> `00b4b034` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4b038"></a> `00b4b038` | `9f 2e 00 f9` | str xzr,[x20, #0x58] | `FALL_THROUGH`
<a id="insn-00b4b03c"></a> `00b4b03c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4b040"></a> `00b4b040` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4b044"></a> `00b4b044` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b4b048"></a> `00b4b048` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4afdc`](#insn-00b4afdc) 範囲 `[['00b4afdc', '00b4aff3']]`
  - `FALL_THROUGH` [`00b4aff0`](#insn-00b4aff0) → [`00b4aff4`](#insn-00b4aff4)
- ブロック [`00b4aff4`](#insn-00b4aff4) 範囲 `[['00b4aff4', '00b4aff7']]`
  - `CONDITIONAL_JUMP` [`00b4aff4`](#insn-00b4aff4) → [`00b4b03c`](#insn-00b4b03c)
  - `FALL_THROUGH` [`00b4aff4`](#insn-00b4aff4) → [`00b4aff8`](#insn-00b4aff8)
- ブロック [`00b4aff8`](#insn-00b4aff8) 範囲 `[['00b4aff8', '00b4b007']]`
  - `CONDITIONAL_JUMP` [`00b4b004`](#insn-00b4b004) → [`00b4b01c`](#insn-00b4b01c)
  - `FALL_THROUGH` [`00b4b004`](#insn-00b4b004) → [`00b4b008`](#insn-00b4b008)
- ブロック [`00b4b008`](#insn-00b4b008) 範囲 `[['00b4b008', '00b4b01b']]`
  - `FALL_THROUGH` [`00b4b018`](#insn-00b4b018) → [`00b4b01c`](#insn-00b4b01c)
- ブロック [`00b4b01c`](#insn-00b4b01c) 範囲 `[['00b4b01c', '00b4b023']]`
  - `FALL_THROUGH` [`00b4b020`](#insn-00b4b020) → [`00b4b024`](#insn-00b4b024)
- ブロック [`00b4b024`](#insn-00b4b024) 範囲 `[['00b4b024', '00b4b03b']]`
  - `FALL_THROUGH` [`00b4b038`](#insn-00b4b038) → [`00b4b03c`](#insn-00b4b03c)
- ブロック [`00b4b03c`](#insn-00b4b03c) 範囲 `[['00b4b03c', '00b4b043']]`
  - `FALL_THROUGH` [`00b4b040`](#insn-00b4b040) → [`00b4b044`](#insn-00b4b044)
- ブロック [`00b4b044`](#insn-00b4b044) 範囲 `[['00b4b044', '00b4b04b']]`

## 命令位置別の参照

- [`00b4afdc`](#insn-00b4afdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4afe0`](#insn-00b4afe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4afe4`](#insn-00b4afe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aff0`](#insn-00b4aff0) → `010a1058`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4aff4`](#insn-00b4aff4) → [`00b4b03c`](#insn-00b4b03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4affc`](#insn-00b4affc) → `010a1060`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4b004`](#insn-00b4b004) → [`00b4b01c`](#insn-00b4b01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4b018`](#insn-00b4b018) → `010a1060`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4b020`](#insn-00b4b020) → [`00bde0e0`](../00bde/00bde0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0e0` · 推定シンボル `None` · 推定型 `None`
- [`00b4b028`](#insn-00b4b028) → `010a1058`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4b038`](#insn-00b4b038) → `010a1058`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4b03c`](#insn-00b4b03c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4b040`](#insn-00b4b040) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4afdc`](#insn-00b4afdc)

~~~json
{
  "source": "00b4afdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4afe0`](#insn-00b4afe0)

~~~json
{
  "source": "00b4afe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4afe4`](#insn-00b4afe4)

~~~json
{
  "source": "00b4afe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aff0`](#insn-00b4aff0)

~~~json
{
  "source": "00b4aff0",
  "target": "010a1058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1058",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4aff4`](#insn-00b4aff4)

~~~json
{
  "source": "00b4aff4",
  "target": "00b4b03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4affc`](#insn-00b4affc)

~~~json
{
  "source": "00b4affc",
  "target": "010a1060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1060",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4b004`](#insn-00b4b004)

~~~json
{
  "source": "00b4b004",
  "target": "00b4b01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4b018`](#insn-00b4b018)

~~~json
{
  "source": "00b4b018",
  "target": "010a1060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1060",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4b020`](#insn-00b4b020)

~~~json
{
  "source": "00b4b020",
  "target": "00bde0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4b028`](#insn-00b4b028)

~~~json
{
  "source": "00b4b028",
  "target": "010a1058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1058",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4b038`](#insn-00b4b038)

~~~json
{
  "source": "00b4b038",
  "target": "010a1058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1058",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4b03c`](#insn-00b4b03c)

~~~json
{
  "source": "00b4b03c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4b040`](#insn-00b4b040)

~~~json
{
  "source": "00b4b040",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
