# 00bd0edc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bd0ab4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0ab4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0082.md#compare-096f28787689f6e3d2d4c3950512c0dd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd0f78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd0f78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0082.md#compare-eb179f652be9d0f2ff37a488561af2ab)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd0edc",
  "name": "_ZN8firebase4auth27api_not_available_exception12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e12f77748a9b9e1e09a16306b075bb4296727f30fbe83b9aac4e3a48f92517d8",
  "source_text_sha256": "e12f77748a9b9e1e09a16306b075bb4296727f30fbe83b9aac4e3a48f92517d8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd0edc",
        "00bd0f4b"
      ]
    ],
    "bytes_sha256": "a25e866b0a0f553d7bfd6fde2d48763daefaaa07b12b823e9ee46b697a34add5",
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

## 疑似コード / UTF-8 499 bytes

~~~c

void _ZN8firebase4auth27api_not_available_exception12ReleaseClassEP7_JNIEnv(long *param_1)

{
                    /* try { // try from 00bd0ee4 to 00cd0f7b has its CatchHandler @ 00bd0958 */
  if (DAT_011268a8 != 0) {
    if (DAT_011268b0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011268b0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011268a8);
    DAT_011268a8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd0edc"></a> `00bd0edc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd0ee0"></a> `00bd0ee0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0ee4"></a> `00bd0ee4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd0ee8"></a> `00bd0ee8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd0eec"></a> `00bd0eec` | `b4 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd0ef0"></a> `00bd0ef0` | `81 56 44 f9` | ldr x1,[x20, #0x8a8] | `FALL_THROUGH`
<a id="insn-00bd0ef4"></a> `00bd0ef4` | `41 02 00 b4` | cbz x1,0x00bd0f3c | `CONDITIONAL_JUMP`
<a id="insn-00bd0ef8"></a> `00bd0ef8` | `b5 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd0efc"></a> `00bd0efc` | `a8 c2 62 39` | ldrb w8,[x21, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bd0f00"></a> `00bd0f00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd0f04"></a> `00bd0f04` | `c8 00 00 34` | cbz w8,0x00bd0f1c | `CONDITIONAL_JUMP`
<a id="insn-00bd0f08"></a> `00bd0f08` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd0f0c"></a> `00bd0f0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd0f10"></a> `00bd0f10` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd0f14"></a> `00bd0f14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd0f18"></a> `00bd0f18` | `bf c2 22 39` | strb wzr,[x21, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bd0f1c"></a> `00bd0f1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd0f20"></a> `00bd0f20` | `10 28 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0f24"></a> `00bd0f24` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd0f28"></a> `00bd0f28` | `81 56 44 f9` | ldr x1,[x20, #0x8a8] | `FALL_THROUGH`
<a id="insn-00bd0f2c"></a> `00bd0f2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd0f30"></a> `00bd0f30` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd0f34"></a> `00bd0f34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd0f38"></a> `00bd0f38` | `9f 56 04 f9` | str xzr,[x20, #0x8a8] | `FALL_THROUGH`
<a id="insn-00bd0f3c"></a> `00bd0f3c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd0f40"></a> `00bd0f40` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0f44"></a> `00bd0f44` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd0f48"></a> `00bd0f48` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd0edc`](#insn-00bd0edc) 範囲 `[['00bd0edc', '00bd0ee3']]`
  - `FALL_THROUGH` [`00bd0ee0`](#insn-00bd0ee0) → [`00bd0ee4`](#insn-00bd0ee4)
- ブロック [`00bd0ee4`](#insn-00bd0ee4) 範囲 `[['00bd0ee4', '00bd0ef7']]`
  - `CONDITIONAL_JUMP` [`00bd0ef4`](#insn-00bd0ef4) → [`00bd0f3c`](#insn-00bd0f3c)
  - `FALL_THROUGH` [`00bd0ef4`](#insn-00bd0ef4) → [`00bd0ef8`](#insn-00bd0ef8)
- ブロック [`00bd0ef8`](#insn-00bd0ef8) 範囲 `[['00bd0ef8', '00bd0f07']]`
  - `CONDITIONAL_JUMP` [`00bd0f04`](#insn-00bd0f04) → [`00bd0f1c`](#insn-00bd0f1c)
  - `FALL_THROUGH` [`00bd0f04`](#insn-00bd0f04) → [`00bd0f08`](#insn-00bd0f08)
- ブロック [`00bd0f08`](#insn-00bd0f08) 範囲 `[['00bd0f08', '00bd0f1b']]`
  - `FALL_THROUGH` [`00bd0f18`](#insn-00bd0f18) → [`00bd0f1c`](#insn-00bd0f1c)
- ブロック [`00bd0f1c`](#insn-00bd0f1c) 範囲 `[['00bd0f1c', '00bd0f3b']]`
  - `FALL_THROUGH` [`00bd0f38`](#insn-00bd0f38) → [`00bd0f3c`](#insn-00bd0f3c)
- ブロック [`00bd0f3c`](#insn-00bd0f3c) 範囲 `[['00bd0f3c', '00bd0f4b']]`

## 命令位置別の参照

- [`00bd0edc`](#insn-00bd0edc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0ee0`](#insn-00bd0ee0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0ee4`](#insn-00bd0ee4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0ef0`](#insn-00bd0ef0) → `011268a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd0ef4`](#insn-00bd0ef4) → [`00bd0f3c`](#insn-00bd0f3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0efc`](#insn-00bd0efc) → `011268b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd0f04`](#insn-00bd0f04) → [`00bd0f1c`](#insn-00bd0f1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0f18`](#insn-00bd0f18) → `011268b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd0f20`](#insn-00bd0f20) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bd0f28`](#insn-00bd0f28) → `011268a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd0f38`](#insn-00bd0f38) → `011268a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd0f3c`](#insn-00bd0f3c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0f40`](#insn-00bd0f40) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd0edc`](#insn-00bd0edc)

~~~json
{
  "source": "00bd0edc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0ee0`](#insn-00bd0ee0)

~~~json
{
  "source": "00bd0ee0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0ee4`](#insn-00bd0ee4)

~~~json
{
  "source": "00bd0ee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0ef0`](#insn-00bd0ef0)

~~~json
{
  "source": "00bd0ef0",
  "target": "011268a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0ef4`](#insn-00bd0ef4)

~~~json
{
  "source": "00bd0ef4",
  "target": "00bd0f3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0efc`](#insn-00bd0efc)

~~~json
{
  "source": "00bd0efc",
  "target": "011268b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0f04`](#insn-00bd0f04)

~~~json
{
  "source": "00bd0f04",
  "target": "00bd0f1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0f18`](#insn-00bd0f18)

~~~json
{
  "source": "00bd0f18",
  "target": "011268b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0f20`](#insn-00bd0f20)

~~~json
{
  "source": "00bd0f20",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0f28`](#insn-00bd0f28)

~~~json
{
  "source": "00bd0f28",
  "target": "011268a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0f38`](#insn-00bd0f38)

~~~json
{
  "source": "00bd0f38",
  "target": "011268a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0f3c`](#insn-00bd0f3c)

~~~json
{
  "source": "00bd0f3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0f40`](#insn-00bd0f40)

~~~json
{
  "source": "00bd0f40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
