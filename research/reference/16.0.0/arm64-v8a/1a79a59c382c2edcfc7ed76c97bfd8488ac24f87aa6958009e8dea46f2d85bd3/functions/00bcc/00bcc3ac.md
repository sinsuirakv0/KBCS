# 00bcc3ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5ceac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ceac.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-1af1b57bddb23032aa3d5c20e10d9898)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcc7d4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc7d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-5e38805e7ab86e2192b78cfab68df2d0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcc3ac",
  "name": "_ZN8firebase4auth17signinmethodquery12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2b6fcbb7167ff29f2696e9a243b1fc681f393d9240e8133ae0f0a7684b7efa26",
  "source_text_sha256": "2b6fcbb7167ff29f2696e9a243b1fc681f393d9240e8133ae0f0a7684b7efa26",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcc3ac",
        "00bcc41b"
      ]
    ],
    "bytes_sha256": "6b8390ec28ba4505fd54bbe63456ca6966779a7fb6f54db10da8ce9860d086c8",
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

- [00c5ab60](../00c5a/00c5ab60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2589 bytes

~~~c

void _ZN8firebase4auth17signinmethodquery12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_011263d0 != 0) {
                    /* try { // try from 00bcc3d4 to 00ccc53b has its CatchHandler @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc3d4 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc560 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc5c8 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc6a4 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc770 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc840 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc90c with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc9d8 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcca40 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bccb1c with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bccbe8 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcccac with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bccd7c with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcce98 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bccf70 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcd140 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcd208 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcd368 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcd71c with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcd9c0 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcdcb8 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcddc4 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcdec4 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcdfd4 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bce040 with catch @ 00bcc3d4 */
    if (DAT_011263d8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011263d8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011263d0);
    DAT_011263d0 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcc3ac"></a> `00bcc3ac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcc3b0"></a> `00bcc3b0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc3b4"></a> `00bcc3b4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcc3b8"></a> `00bcc3b8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcc3bc"></a> `00bcc3bc` | `d4 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcc3c0"></a> `00bcc3c0` | `81 ea 41 f9` | ldr x1,[x20, #0x3d0] | `FALL_THROUGH`
<a id="insn-00bcc3c4"></a> `00bcc3c4` | `41 02 00 b4` | cbz x1,0x00bcc40c | `CONDITIONAL_JUMP`
<a id="insn-00bcc3c8"></a> `00bcc3c8` | `d5 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcc3cc"></a> `00bcc3cc` | `a8 62 4f 39` | ldrb w8,[x21, #0x3d8] | `FALL_THROUGH`
<a id="insn-00bcc3d0"></a> `00bcc3d0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcc3d4"></a> `00bcc3d4` | `c8 00 00 34` | cbz w8,0x00bcc3ec | `CONDITIONAL_JUMP`
<a id="insn-00bcc3d8"></a> `00bcc3d8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcc3dc"></a> `00bcc3dc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcc3e0"></a> `00bcc3e0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bcc3e4"></a> `00bcc3e4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcc3e8"></a> `00bcc3e8` | `bf 62 0f 39` | strb wzr,[x21, #0x3d8] | `FALL_THROUGH`
<a id="insn-00bcc3ec"></a> `00bcc3ec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcc3f0"></a> `00bcc3f0` | `dc 39 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc3f4"></a> `00bcc3f4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcc3f8"></a> `00bcc3f8` | `81 ea 41 f9` | ldr x1,[x20, #0x3d0] | `FALL_THROUGH`
<a id="insn-00bcc3fc"></a> `00bcc3fc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcc400"></a> `00bcc400` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bcc404"></a> `00bcc404` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcc408"></a> `00bcc408` | `9f ea 01 f9` | str xzr,[x20, #0x3d0] | `FALL_THROUGH`
<a id="insn-00bcc40c"></a> `00bcc40c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcc410"></a> `00bcc410` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc414"></a> `00bcc414` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcc418"></a> `00bcc418` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcc3ac`](#insn-00bcc3ac) 範囲 `[['00bcc3ac', '00bcc3c7']]`
  - `CONDITIONAL_JUMP` [`00bcc3c4`](#insn-00bcc3c4) → [`00bcc40c`](#insn-00bcc40c)
  - `FALL_THROUGH` [`00bcc3c4`](#insn-00bcc3c4) → [`00bcc3c8`](#insn-00bcc3c8)
- ブロック [`00bcc3c8`](#insn-00bcc3c8) 範囲 `[['00bcc3c8', '00bcc3d3']]`
  - `FALL_THROUGH` [`00bcc3d0`](#insn-00bcc3d0) → [`00bcc3d4`](#insn-00bcc3d4)
- ブロック [`00bcc3d4`](#insn-00bcc3d4) 範囲 `[['00bcc3d4', '00bcc3d7']]`
  - `CONDITIONAL_JUMP` [`00bcc3d4`](#insn-00bcc3d4) → [`00bcc3ec`](#insn-00bcc3ec)
  - `FALL_THROUGH` [`00bcc3d4`](#insn-00bcc3d4) → [`00bcc3d8`](#insn-00bcc3d8)
- ブロック [`00bcc3d8`](#insn-00bcc3d8) 範囲 `[['00bcc3d8', '00bcc3eb']]`
  - `FALL_THROUGH` [`00bcc3e8`](#insn-00bcc3e8) → [`00bcc3ec`](#insn-00bcc3ec)
- ブロック [`00bcc3ec`](#insn-00bcc3ec) 範囲 `[['00bcc3ec', '00bcc40b']]`
  - `FALL_THROUGH` [`00bcc408`](#insn-00bcc408) → [`00bcc40c`](#insn-00bcc40c)
- ブロック [`00bcc40c`](#insn-00bcc40c) 範囲 `[['00bcc40c', '00bcc41b']]`

## 命令位置別の参照

- [`00bcc3ac`](#insn-00bcc3ac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc3b0`](#insn-00bcc3b0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc3b4`](#insn-00bcc3b4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc3c0`](#insn-00bcc3c0) → `011263d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcc3c4`](#insn-00bcc3c4) → [`00bcc40c`](#insn-00bcc40c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc3cc`](#insn-00bcc3cc) → `011263d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcc3d4`](#insn-00bcc3d4) → [`00bcc3ec`](#insn-00bcc3ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc3e8`](#insn-00bcc3e8) → `011263d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcc3f0`](#insn-00bcc3f0) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcc3f8`](#insn-00bcc3f8) → `011263d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcc408`](#insn-00bcc408) → `011263d0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcc40c`](#insn-00bcc40c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc410`](#insn-00bcc410) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcc3ac`](#insn-00bcc3ac)

~~~json
{
  "source": "00bcc3ac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc3b0`](#insn-00bcc3b0)

~~~json
{
  "source": "00bcc3b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc3b4`](#insn-00bcc3b4)

~~~json
{
  "source": "00bcc3b4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc3c0`](#insn-00bcc3c0)

~~~json
{
  "source": "00bcc3c0",
  "target": "011263d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc3c4`](#insn-00bcc3c4)

~~~json
{
  "source": "00bcc3c4",
  "target": "00bcc40c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc3cc`](#insn-00bcc3cc)

~~~json
{
  "source": "00bcc3cc",
  "target": "011263d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263d8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc3d4`](#insn-00bcc3d4)

~~~json
{
  "source": "00bcc3d4",
  "target": "00bcc3ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc3e8`](#insn-00bcc3e8)

~~~json
{
  "source": "00bcc3e8",
  "target": "011263d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263d8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc3f0`](#insn-00bcc3f0)

~~~json
{
  "source": "00bcc3f0",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc3f8`](#insn-00bcc3f8)

~~~json
{
  "source": "00bcc3f8",
  "target": "011263d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc408`](#insn-00bcc408)

~~~json
{
  "source": "00bcc408",
  "target": "011263d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc40c`](#insn-00bcc40c)

~~~json
{
  "source": "00bcc40c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc410`](#insn-00bcc410)

~~~json
{
  "source": "00bcc410",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
