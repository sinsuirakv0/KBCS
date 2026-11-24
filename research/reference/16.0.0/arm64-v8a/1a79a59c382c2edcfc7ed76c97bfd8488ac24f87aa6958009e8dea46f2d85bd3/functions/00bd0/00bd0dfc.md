# 00bd0dfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b618fc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b618fc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0067.md#compare-d2bd39e546884b0c57c571d52fa58873)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd1224`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1224.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0082.md#compare-f6950b34652306e62ed2655a6cce44e9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd0dfc",
  "name": "_ZN8firebase4auth21action_code_exception12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8514e48819c18634b1a1c01969b5116d25e8b923bc152d18cc27b0a563ce6ce4",
  "source_text_sha256": "8514e48819c18634b1a1c01969b5116d25e8b923bc152d18cc27b0a563ce6ce4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd0dfc",
        "00bd0e6b"
      ]
    ],
    "bytes_sha256": "a9085d9c237971cdf79e6f0de05f331e0bcaf0931dacebe21cb6cf82dbc2414a",
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

## 疑似コード / UTF-8 493 bytes

~~~c

void _ZN8firebase4auth21action_code_exception12ReleaseClassEP7_JNIEnv(long *param_1)

{
                    /* try { // try from 00bd0e00 to 00cd0f07 has its CatchHandler @ 00bd075c */
  if (DAT_011264c8 != 0) {
    if (DAT_011264d0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011264d0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011264c8);
    DAT_011264c8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd0dfc"></a> `00bd0dfc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd0e00"></a> `00bd0e00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0e04"></a> `00bd0e04` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd0e08"></a> `00bd0e08` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd0e0c"></a> `00bd0e0c` | `b4 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd0e10"></a> `00bd0e10` | `81 66 42 f9` | ldr x1,[x20, #0x4c8] | `FALL_THROUGH`
<a id="insn-00bd0e14"></a> `00bd0e14` | `41 02 00 b4` | cbz x1,0x00bd0e5c | `CONDITIONAL_JUMP`
<a id="insn-00bd0e18"></a> `00bd0e18` | `b5 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd0e1c"></a> `00bd0e1c` | `a8 42 53 39` | ldrb w8,[x21, #0x4d0] | `FALL_THROUGH`
<a id="insn-00bd0e20"></a> `00bd0e20` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd0e24"></a> `00bd0e24` | `c8 00 00 34` | cbz w8,0x00bd0e3c | `CONDITIONAL_JUMP`
<a id="insn-00bd0e28"></a> `00bd0e28` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd0e2c"></a> `00bd0e2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd0e30"></a> `00bd0e30` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd0e34"></a> `00bd0e34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd0e38"></a> `00bd0e38` | `bf 42 13 39` | strb wzr,[x21, #0x4d0] | `FALL_THROUGH`
<a id="insn-00bd0e3c"></a> `00bd0e3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd0e40"></a> `00bd0e40` | `48 27 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0e44"></a> `00bd0e44` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd0e48"></a> `00bd0e48` | `81 66 42 f9` | ldr x1,[x20, #0x4c8] | `FALL_THROUGH`
<a id="insn-00bd0e4c"></a> `00bd0e4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd0e50"></a> `00bd0e50` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd0e54"></a> `00bd0e54` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd0e58"></a> `00bd0e58` | `9f 66 02 f9` | str xzr,[x20, #0x4c8] | `FALL_THROUGH`
<a id="insn-00bd0e5c"></a> `00bd0e5c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd0e60"></a> `00bd0e60` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0e64"></a> `00bd0e64` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd0e68"></a> `00bd0e68` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd0dfc`](#insn-00bd0dfc) 範囲 `[['00bd0dfc', '00bd0dff']]`
  - `FALL_THROUGH` [`00bd0dfc`](#insn-00bd0dfc) → [`00bd0e00`](#insn-00bd0e00)
- ブロック [`00bd0e00`](#insn-00bd0e00) 範囲 `[['00bd0e00', '00bd0e17']]`
  - `CONDITIONAL_JUMP` [`00bd0e14`](#insn-00bd0e14) → [`00bd0e5c`](#insn-00bd0e5c)
  - `FALL_THROUGH` [`00bd0e14`](#insn-00bd0e14) → [`00bd0e18`](#insn-00bd0e18)
- ブロック [`00bd0e18`](#insn-00bd0e18) 範囲 `[['00bd0e18', '00bd0e27']]`
  - `CONDITIONAL_JUMP` [`00bd0e24`](#insn-00bd0e24) → [`00bd0e3c`](#insn-00bd0e3c)
  - `FALL_THROUGH` [`00bd0e24`](#insn-00bd0e24) → [`00bd0e28`](#insn-00bd0e28)
- ブロック [`00bd0e28`](#insn-00bd0e28) 範囲 `[['00bd0e28', '00bd0e3b']]`
  - `FALL_THROUGH` [`00bd0e38`](#insn-00bd0e38) → [`00bd0e3c`](#insn-00bd0e3c)
- ブロック [`00bd0e3c`](#insn-00bd0e3c) 範囲 `[['00bd0e3c', '00bd0e5b']]`
  - `FALL_THROUGH` [`00bd0e58`](#insn-00bd0e58) → [`00bd0e5c`](#insn-00bd0e5c)
- ブロック [`00bd0e5c`](#insn-00bd0e5c) 範囲 `[['00bd0e5c', '00bd0e6b']]`

## 命令位置別の参照

- [`00bd0dfc`](#insn-00bd0dfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0e00`](#insn-00bd0e00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0e04`](#insn-00bd0e04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0e10`](#insn-00bd0e10) → `011264c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd0e14`](#insn-00bd0e14) → [`00bd0e5c`](#insn-00bd0e5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0e1c`](#insn-00bd0e1c) → `011264d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd0e24`](#insn-00bd0e24) → [`00bd0e3c`](#insn-00bd0e3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0e38`](#insn-00bd0e38) → `011264d0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd0e40`](#insn-00bd0e40) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bd0e48`](#insn-00bd0e48) → `011264c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd0e58`](#insn-00bd0e58) → `011264c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd0e5c`](#insn-00bd0e5c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0e60`](#insn-00bd0e60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd0dfc`](#insn-00bd0dfc)

~~~json
{
  "source": "00bd0dfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0e00`](#insn-00bd0e00)

~~~json
{
  "source": "00bd0e00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0e04`](#insn-00bd0e04)

~~~json
{
  "source": "00bd0e04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0e10`](#insn-00bd0e10)

~~~json
{
  "source": "00bd0e10",
  "target": "011264c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011264c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0e14`](#insn-00bd0e14)

~~~json
{
  "source": "00bd0e14",
  "target": "00bd0e5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0e1c`](#insn-00bd0e1c)

~~~json
{
  "source": "00bd0e1c",
  "target": "011264d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011264d0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0e24`](#insn-00bd0e24)

~~~json
{
  "source": "00bd0e24",
  "target": "00bd0e3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0e38`](#insn-00bd0e38)

~~~json
{
  "source": "00bd0e38",
  "target": "011264d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011264d0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0e40`](#insn-00bd0e40)

~~~json
{
  "source": "00bd0e40",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0e48`](#insn-00bd0e48)

~~~json
{
  "source": "00bd0e48",
  "target": "011264c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011264c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0e58`](#insn-00bd0e58)

~~~json
{
  "source": "00bd0e58",
  "target": "011264c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011264c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0e5c`](#insn-00bd0e5c)

~~~json
{
  "source": "00bd0e5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0e60`](#insn-00bd0e60)

~~~json
{
  "source": "00bd0e60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
