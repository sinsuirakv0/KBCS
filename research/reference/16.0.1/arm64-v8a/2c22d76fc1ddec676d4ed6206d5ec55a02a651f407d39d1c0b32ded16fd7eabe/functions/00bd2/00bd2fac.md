# 00bd2fac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bd2b84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2b84.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0083.md#compare-ea781ac4af985b6baf4be334f126f2fe)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd3048`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd3/00bd3048.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0083.md#compare-8723b4b1947682a62d19e4e6780459bd)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd2fac",
  "name": "_ZN8firebase4auth26firebase_network_exception12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42326f7db351c1203a2cf55d3185f9777311d7bd6af762015b6255a90d5af255",
  "source_text_sha256": "42326f7db351c1203a2cf55d3185f9777311d7bd6af762015b6255a90d5af255",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd2fac",
        "00bd301b"
      ]
    ],
    "bytes_sha256": "f89e7379aa91b44e7a18ecea2e167d4376204407d0976bb1ad2efd99eb60b0a5",
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

- [00c5af60](../00c5a/00c5af60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 401 bytes

~~~c

void _ZN8firebase4auth26firebase_network_exception12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_011269e8 != 0) {
    if (DAT_011269f0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011269f0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011269e8);
    DAT_011269e8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd2fac"></a> `00bd2fac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd2fb0"></a> `00bd2fb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2fb4"></a> `00bd2fb4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd2fb8"></a> `00bd2fb8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd2fbc"></a> `00bd2fbc` | `b4 2a 00 90` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd2fc0"></a> `00bd2fc0` | `81 f6 44 f9` | ldr x1,[x20, #0x9e8] | `FALL_THROUGH`
<a id="insn-00bd2fc4"></a> `00bd2fc4` | `41 02 00 b4` | cbz x1,0x00bd300c | `CONDITIONAL_JUMP`
<a id="insn-00bd2fc8"></a> `00bd2fc8` | `b5 2a 00 90` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd2fcc"></a> `00bd2fcc` | `a8 c2 67 39` | ldrb w8,[x21, #0x9f0] | `FALL_THROUGH`
<a id="insn-00bd2fd0"></a> `00bd2fd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd2fd4"></a> `00bd2fd4` | `c8 00 00 34` | cbz w8,0x00bd2fec | `CONDITIONAL_JUMP`
<a id="insn-00bd2fd8"></a> `00bd2fd8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd2fdc"></a> `00bd2fdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd2fe0"></a> `00bd2fe0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd2fe4"></a> `00bd2fe4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd2fe8"></a> `00bd2fe8` | `bf c2 27 39` | strb wzr,[x21, #0x9f0] | `FALL_THROUGH`
<a id="insn-00bd2fec"></a> `00bd2fec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd2ff0"></a> `00bd2ff0` | `dc 1f 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2ff4"></a> `00bd2ff4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd2ff8"></a> `00bd2ff8` | `81 f6 44 f9` | ldr x1,[x20, #0x9e8] | `FALL_THROUGH`
<a id="insn-00bd2ffc"></a> `00bd2ffc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3000"></a> `00bd3000` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd3004"></a> `00bd3004` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3008"></a> `00bd3008` | `9f f6 04 f9` | str xzr,[x20, #0x9e8] | `FALL_THROUGH`
<a id="insn-00bd300c"></a> `00bd300c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd3010"></a> `00bd3010` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3014"></a> `00bd3014` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd3018"></a> `00bd3018` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd2fac`](#insn-00bd2fac) 範囲 `[['00bd2fac', '00bd2fc7']]`
  - `CONDITIONAL_JUMP` [`00bd2fc4`](#insn-00bd2fc4) → [`00bd300c`](#insn-00bd300c)
  - `FALL_THROUGH` [`00bd2fc4`](#insn-00bd2fc4) → [`00bd2fc8`](#insn-00bd2fc8)
- ブロック [`00bd2fc8`](#insn-00bd2fc8) 範囲 `[['00bd2fc8', '00bd2fd7']]`
  - `CONDITIONAL_JUMP` [`00bd2fd4`](#insn-00bd2fd4) → [`00bd2fec`](#insn-00bd2fec)
  - `FALL_THROUGH` [`00bd2fd4`](#insn-00bd2fd4) → [`00bd2fd8`](#insn-00bd2fd8)
- ブロック [`00bd2fd8`](#insn-00bd2fd8) 範囲 `[['00bd2fd8', '00bd2feb']]`
  - `FALL_THROUGH` [`00bd2fe8`](#insn-00bd2fe8) → [`00bd2fec`](#insn-00bd2fec)
- ブロック [`00bd2fec`](#insn-00bd2fec) 範囲 `[['00bd2fec', '00bd300b']]`
  - `FALL_THROUGH` [`00bd3008`](#insn-00bd3008) → [`00bd300c`](#insn-00bd300c)
- ブロック [`00bd300c`](#insn-00bd300c) 範囲 `[['00bd300c', '00bd301b']]`

## 命令位置別の参照

- [`00bd2fac`](#insn-00bd2fac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fb0`](#insn-00bd2fb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fb4`](#insn-00bd2fb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fc0`](#insn-00bd2fc0) → `011269e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd2fc4`](#insn-00bd2fc4) → [`00bd300c`](#insn-00bd300c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fcc`](#insn-00bd2fcc) → `011269f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd2fd4`](#insn-00bd2fd4) → [`00bd2fec`](#insn-00bd2fec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fe8`](#insn-00bd2fe8) → `011269f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd2ff0`](#insn-00bd2ff0) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bd2ff8`](#insn-00bd2ff8) → `011269e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3008`](#insn-00bd3008) → `011269e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd300c`](#insn-00bd300c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3010`](#insn-00bd3010) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd2fac`](#insn-00bd2fac)

~~~json
{
  "source": "00bd2fac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2fb0`](#insn-00bd2fb0)

~~~json
{
  "source": "00bd2fb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2fb4`](#insn-00bd2fb4)

~~~json
{
  "source": "00bd2fb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2fc0`](#insn-00bd2fc0)

~~~json
{
  "source": "00bd2fc0",
  "target": "011269e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd2fc4`](#insn-00bd2fc4)

~~~json
{
  "source": "00bd2fc4",
  "target": "00bd300c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2fcc`](#insn-00bd2fcc)

~~~json
{
  "source": "00bd2fcc",
  "target": "011269f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269f0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd2fd4`](#insn-00bd2fd4)

~~~json
{
  "source": "00bd2fd4",
  "target": "00bd2fec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2fe8`](#insn-00bd2fe8)

~~~json
{
  "source": "00bd2fe8",
  "target": "011269f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269f0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd2ff0`](#insn-00bd2ff0)

~~~json
{
  "source": "00bd2ff0",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2ff8`](#insn-00bd2ff8)

~~~json
{
  "source": "00bd2ff8",
  "target": "011269e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3008`](#insn-00bd3008)

~~~json
{
  "source": "00bd3008",
  "target": "011269e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd300c`](#insn-00bd300c)

~~~json
{
  "source": "00bd300c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3010`](#insn-00bd3010)

~~~json
{
  "source": "00bd3010",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
