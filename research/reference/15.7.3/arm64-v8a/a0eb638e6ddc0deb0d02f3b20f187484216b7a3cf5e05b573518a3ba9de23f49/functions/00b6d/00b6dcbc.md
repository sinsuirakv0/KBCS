# 00b6dcbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b6dbf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dbf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0073.md#compare-ac83b75dbe0d5eb9890714a839ec9bb2)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6dd00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0074.md#compare-10160c76f3dd2597e6c36d4d99868d11)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6dcbc",
  "name": "_ZN8firebase4auth8userinfo12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df05ed018abb53657572f276326b55acf02e43aae0a64be9063215cbaed6a632",
  "source_text_sha256": "df05ed018abb53657572f276326b55acf02e43aae0a64be9063215cbaed6a632",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6dcbc",
        "00b6dd2b"
      ]
    ],
    "bytes_sha256": "a398f0f1397ab3cbf5e787132ad607c217f2b7c580b61787eae1b72aba52ebf8",
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

- [00bde090](../00bde/00bde090.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 382 bytes

~~~c

void _ZN8firebase4auth8userinfo12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_010a1a68 != 0) {
    if (DAT_010a1a70 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a1a70 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a1a68);
    DAT_010a1a68 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6dcbc"></a> `00b6dcbc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b6dcc0"></a> `00b6dcc0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6dcc4"></a> `00b6dcc4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6dcc8"></a> `00b6dcc8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b6dccc"></a> `00b6dccc` | `b4 29 00 90` | adrp x20,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6dcd0"></a> `00b6dcd0` | `81 36 45 f9` | ldr x1,[x20, #0xa68] | `FALL_THROUGH`
<a id="insn-00b6dcd4"></a> `00b6dcd4` | `41 02 00 b4` | cbz x1,0x00b6dd1c | `CONDITIONAL_JUMP`
<a id="insn-00b6dcd8"></a> `00b6dcd8` | `b5 29 00 90` | adrp x21,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6dcdc"></a> `00b6dcdc` | `a8 c2 69 39` | ldrb w8,[x21, #0xa70] | `FALL_THROUGH`
<a id="insn-00b6dce0"></a> `00b6dce0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b6dce4"></a> `00b6dce4` | `c8 00 00 34` | cbz w8,0x00b6dcfc | `CONDITIONAL_JUMP`
<a id="insn-00b6dce8"></a> `00b6dce8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b6dcec"></a> `00b6dcec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6dcf0"></a> `00b6dcf0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00b6dcf4"></a> `00b6dcf4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b6dcf8"></a> `00b6dcf8` | `bf c2 29 39` | strb wzr,[x21, #0xa70] | `FALL_THROUGH`
<a id="insn-00b6dcfc"></a> `00b6dcfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6dd00"></a> `00b6dd00` | `e4 c0 01 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00b6dd04"></a> `00b6dd04` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b6dd08"></a> `00b6dd08` | `81 36 45 f9` | ldr x1,[x20, #0xa68] | `FALL_THROUGH`
<a id="insn-00b6dd0c"></a> `00b6dd0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6dd10"></a> `00b6dd10` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00b6dd14"></a> `00b6dd14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b6dd18"></a> `00b6dd18` | `9f 36 05 f9` | str xzr,[x20, #0xa68] | `FALL_THROUGH`
<a id="insn-00b6dd1c"></a> `00b6dd1c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6dd20"></a> `00b6dd20` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6dd24"></a> `00b6dd24` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6dd28"></a> `00b6dd28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6dcbc`](#insn-00b6dcbc) 範囲 `[['00b6dcbc', '00b6dcd7']]`
  - `CONDITIONAL_JUMP` [`00b6dcd4`](#insn-00b6dcd4) → [`00b6dd1c`](#insn-00b6dd1c)
  - `FALL_THROUGH` [`00b6dcd4`](#insn-00b6dcd4) → [`00b6dcd8`](#insn-00b6dcd8)
- ブロック [`00b6dcd8`](#insn-00b6dcd8) 範囲 `[['00b6dcd8', '00b6dce7']]`
  - `CONDITIONAL_JUMP` [`00b6dce4`](#insn-00b6dce4) → [`00b6dcfc`](#insn-00b6dcfc)
  - `FALL_THROUGH` [`00b6dce4`](#insn-00b6dce4) → [`00b6dce8`](#insn-00b6dce8)
- ブロック [`00b6dce8`](#insn-00b6dce8) 範囲 `[['00b6dce8', '00b6dcfb']]`
  - `FALL_THROUGH` [`00b6dcf8`](#insn-00b6dcf8) → [`00b6dcfc`](#insn-00b6dcfc)
- ブロック [`00b6dcfc`](#insn-00b6dcfc) 範囲 `[['00b6dcfc', '00b6dd1b']]`
  - `FALL_THROUGH` [`00b6dd18`](#insn-00b6dd18) → [`00b6dd1c`](#insn-00b6dd1c)
- ブロック [`00b6dd1c`](#insn-00b6dd1c) 範囲 `[['00b6dd1c', '00b6dd2b']]`

## 命令位置別の参照

- [`00b6dcbc`](#insn-00b6dcbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dcc0`](#insn-00b6dcc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dcc4`](#insn-00b6dcc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dcd0`](#insn-00b6dcd0) → `010a1a68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6dcd4`](#insn-00b6dcd4) → [`00b6dd1c`](#insn-00b6dd1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dcdc`](#insn-00b6dcdc) → `010a1a70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b6dce4`](#insn-00b6dce4) → [`00b6dcfc`](#insn-00b6dcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dcf8`](#insn-00b6dcf8) → `010a1a70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b6dd00`](#insn-00b6dd00) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00b6dd08`](#insn-00b6dd08) → `010a1a68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6dd18`](#insn-00b6dd18) → `010a1a68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6dd1c`](#insn-00b6dd1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dd20`](#insn-00b6dd20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6dcbc`](#insn-00b6dcbc)

~~~json
{
  "source": "00b6dcbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dcc0`](#insn-00b6dcc0)

~~~json
{
  "source": "00b6dcc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dcc4`](#insn-00b6dcc4)

~~~json
{
  "source": "00b6dcc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dcd0`](#insn-00b6dcd0)

~~~json
{
  "source": "00b6dcd0",
  "target": "010a1a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6dcd4`](#insn-00b6dcd4)

~~~json
{
  "source": "00b6dcd4",
  "target": "00b6dd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dcdc`](#insn-00b6dcdc)

~~~json
{
  "source": "00b6dcdc",
  "target": "010a1a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1a70",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6dce4`](#insn-00b6dce4)

~~~json
{
  "source": "00b6dce4",
  "target": "00b6dcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dcf8`](#insn-00b6dcf8)

~~~json
{
  "source": "00b6dcf8",
  "target": "010a1a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1a70",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6dd00`](#insn-00b6dd00)

~~~json
{
  "source": "00b6dd00",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6dd08`](#insn-00b6dd08)

~~~json
{
  "source": "00b6dd08",
  "target": "010a1a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6dd18`](#insn-00b6dd18)

~~~json
{
  "source": "00b6dd18",
  "target": "010a1a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6dd1c`](#insn-00b6dd1c)

~~~json
{
  "source": "00b6dd1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dd20`](#insn-00b6dd20)

~~~json
{
  "source": "00b6dd20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
