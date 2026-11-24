# 00bcca3c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5d53c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d53c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-328442f7b77a52e8f33bafc81606a261)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcce64`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcce64.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-674ad46d78d250bf33d5db7efe5ae280)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcca3c",
  "name": "_ZN8firebase4auth21jni_id_token_listener12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9677dc3e9f3b9fa04a5c464c9c08d3f26d01aa09d42f7fe390a0b34d2ad816e1",
  "source_text_sha256": "9677dc3e9f3b9fa04a5c464c9c08d3f26d01aa09d42f7fe390a0b34d2ad816e1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcca3c",
        "00bccaab"
      ]
    ],
    "bytes_sha256": "1e77f99ffff79f14594ae2290c314400cf64835ff60fa264bdbe3c3da7e346fa",
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

void _ZN8firebase4auth21jni_id_token_listener12ReleaseClassEP7_JNIEnv(long *param_1)

{
                    /* try { // try from 00bcca40 to 00cccb03 has its CatchHandler @ 00bcc3d4 */
  if (DAT_01126418 != 0) {
    if (DAT_01126420 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126420 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126418);
    DAT_01126418 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcca3c"></a> `00bcca3c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcca40"></a> `00bcca40` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcca44"></a> `00bcca44` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcca48"></a> `00bcca48` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcca4c"></a> `00bcca4c` | `d4 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcca50"></a> `00bcca50` | `81 0e 42 f9` | ldr x1,[x20, #0x418] | `FALL_THROUGH`
<a id="insn-00bcca54"></a> `00bcca54` | `41 02 00 b4` | cbz x1,0x00bcca9c | `CONDITIONAL_JUMP`
<a id="insn-00bcca58"></a> `00bcca58` | `d5 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcca5c"></a> `00bcca5c` | `a8 82 50 39` | ldrb w8,[x21, #0x420] | `FALL_THROUGH`
<a id="insn-00bcca60"></a> `00bcca60` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcca64"></a> `00bcca64` | `c8 00 00 34` | cbz w8,0x00bcca7c | `CONDITIONAL_JUMP`
<a id="insn-00bcca68"></a> `00bcca68` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcca6c"></a> `00bcca6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcca70"></a> `00bcca70` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bcca74"></a> `00bcca74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcca78"></a> `00bcca78` | `bf 82 10 39` | strb wzr,[x21, #0x420] | `FALL_THROUGH`
<a id="insn-00bcca7c"></a> `00bcca7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcca80"></a> `00bcca80` | `38 38 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcca84"></a> `00bcca84` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcca88"></a> `00bcca88` | `81 0e 42 f9` | ldr x1,[x20, #0x418] | `FALL_THROUGH`
<a id="insn-00bcca8c"></a> `00bcca8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcca90"></a> `00bcca90` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bcca94"></a> `00bcca94` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcca98"></a> `00bcca98` | `9f 0e 02 f9` | str xzr,[x20, #0x418] | `FALL_THROUGH`
<a id="insn-00bcca9c"></a> `00bcca9c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccaa0"></a> `00bccaa0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccaa4"></a> `00bccaa4` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bccaa8"></a> `00bccaa8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcca3c`](#insn-00bcca3c) 範囲 `[['00bcca3c', '00bcca3f']]`
  - `FALL_THROUGH` [`00bcca3c`](#insn-00bcca3c) → [`00bcca40`](#insn-00bcca40)
- ブロック [`00bcca40`](#insn-00bcca40) 範囲 `[['00bcca40', '00bcca57']]`
  - `CONDITIONAL_JUMP` [`00bcca54`](#insn-00bcca54) → [`00bcca9c`](#insn-00bcca9c)
  - `FALL_THROUGH` [`00bcca54`](#insn-00bcca54) → [`00bcca58`](#insn-00bcca58)
- ブロック [`00bcca58`](#insn-00bcca58) 範囲 `[['00bcca58', '00bcca67']]`
  - `CONDITIONAL_JUMP` [`00bcca64`](#insn-00bcca64) → [`00bcca7c`](#insn-00bcca7c)
  - `FALL_THROUGH` [`00bcca64`](#insn-00bcca64) → [`00bcca68`](#insn-00bcca68)
- ブロック [`00bcca68`](#insn-00bcca68) 範囲 `[['00bcca68', '00bcca7b']]`
  - `FALL_THROUGH` [`00bcca78`](#insn-00bcca78) → [`00bcca7c`](#insn-00bcca7c)
- ブロック [`00bcca7c`](#insn-00bcca7c) 範囲 `[['00bcca7c', '00bcca9b']]`
  - `FALL_THROUGH` [`00bcca98`](#insn-00bcca98) → [`00bcca9c`](#insn-00bcca9c)
- ブロック [`00bcca9c`](#insn-00bcca9c) 範囲 `[['00bcca9c', '00bccaab']]`

## 命令位置別の参照

- [`00bcca3c`](#insn-00bcca3c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcca40`](#insn-00bcca40) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcca44`](#insn-00bcca44) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcca50`](#insn-00bcca50) → `01126418`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcca54`](#insn-00bcca54) → [`00bcca9c`](#insn-00bcca9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcca5c`](#insn-00bcca5c) → `01126420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcca64`](#insn-00bcca64) → [`00bcca7c`](#insn-00bcca7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcca78`](#insn-00bcca78) → `01126420`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcca80`](#insn-00bcca80) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcca88`](#insn-00bcca88) → `01126418`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcca98`](#insn-00bcca98) → `01126418`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcca9c`](#insn-00bcca9c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccaa0`](#insn-00bccaa0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcca3c`](#insn-00bcca3c)

~~~json
{
  "source": "00bcca3c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcca40`](#insn-00bcca40)

~~~json
{
  "source": "00bcca40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcca44`](#insn-00bcca44)

~~~json
{
  "source": "00bcca44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcca50`](#insn-00bcca50)

~~~json
{
  "source": "00bcca50",
  "target": "01126418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcca54`](#insn-00bcca54)

~~~json
{
  "source": "00bcca54",
  "target": "00bcca9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcca5c`](#insn-00bcca5c)

~~~json
{
  "source": "00bcca5c",
  "target": "01126420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126420",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcca64`](#insn-00bcca64)

~~~json
{
  "source": "00bcca64",
  "target": "00bcca7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcca78`](#insn-00bcca78)

~~~json
{
  "source": "00bcca78",
  "target": "01126420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126420",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcca80`](#insn-00bcca80)

~~~json
{
  "source": "00bcca80",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcca88`](#insn-00bcca88)

~~~json
{
  "source": "00bcca88",
  "target": "01126418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcca98`](#insn-00bcca98)

~~~json
{
  "source": "00bcca98",
  "target": "01126418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcca9c`](#insn-00bcca9c)

~~~json
{
  "source": "00bcca9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccaa0`](#insn-00bccaa0)

~~~json
{
  "source": "00bccaa0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
