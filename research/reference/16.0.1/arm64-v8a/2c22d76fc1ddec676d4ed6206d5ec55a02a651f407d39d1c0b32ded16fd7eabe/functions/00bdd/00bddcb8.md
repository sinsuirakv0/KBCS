# 00bddcb8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdd890`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd890.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-54b02a49ee2c33f1b7498c96487767bd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bddd54`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddd54.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-f032155871d00122734dfbe94817759a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddcb8",
  "name": "_ZN8firebase4auth18userprofilebuilder12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "52cf5ef26b879e371e7b6ac9c07303a986176badc92a2e47b370e397cf0ee899",
  "source_text_sha256": "52cf5ef26b879e371e7b6ac9c07303a986176badc92a2e47b370e397cf0ee899",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddcb8",
        "00bddd27"
      ]
    ],
    "bytes_sha256": "3db708c93bc6015a0715bce7774617bbe16a2f123aaa53ad7f56c201ffa6dd6a",
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

## 疑似コード / UTF-8 393 bytes

~~~c

void _ZN8firebase4auth18userprofilebuilder12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_01126e28 != 0) {
    if (DAT_01126e30 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126e30 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126e28);
    DAT_01126e28 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddcb8"></a> `00bddcb8` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bddcbc"></a> `00bddcbc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddcc0"></a> `00bddcc0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddcc4"></a> `00bddcc4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bddcc8"></a> `00bddcc8` | `54 2a 00 b0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddccc"></a> `00bddccc` | `81 16 47 f9` | ldr x1,[x20, #0xe28] | `FALL_THROUGH`
<a id="insn-00bddcd0"></a> `00bddcd0` | `41 02 00 b4` | cbz x1,0x00bddd18 | `CONDITIONAL_JUMP`
<a id="insn-00bddcd4"></a> `00bddcd4` | `55 2a 00 b0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddcd8"></a> `00bddcd8` | `a8 c2 78 39` | ldrb w8,[x21, #0xe30] | `FALL_THROUGH`
<a id="insn-00bddcdc"></a> `00bddcdc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bddce0"></a> `00bddce0` | `c8 00 00 34` | cbz w8,0x00bddcf8 | `CONDITIONAL_JUMP`
<a id="insn-00bddce4"></a> `00bddce4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bddce8"></a> `00bddce8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddcec"></a> `00bddcec` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bddcf0"></a> `00bddcf0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bddcf4"></a> `00bddcf4` | `bf c2 38 39` | strb wzr,[x21, #0xe30] | `FALL_THROUGH`
<a id="insn-00bddcf8"></a> `00bddcf8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddcfc"></a> `00bddcfc` | `99 f4 01 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bddd00"></a> `00bddd00` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bddd04"></a> `00bddd04` | `81 16 47 f9` | ldr x1,[x20, #0xe28] | `FALL_THROUGH`
<a id="insn-00bddd08"></a> `00bddd08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddd0c"></a> `00bddd0c` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bddd10"></a> `00bddd10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bddd14"></a> `00bddd14` | `9f 16 07 f9` | str xzr,[x20, #0xe28] | `FALL_THROUGH`
<a id="insn-00bddd18"></a> `00bddd18` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddd1c"></a> `00bddd1c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddd20"></a> `00bddd20` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bddd24"></a> `00bddd24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddcb8`](#insn-00bddcb8) 範囲 `[['00bddcb8', '00bddcd3']]`
  - `CONDITIONAL_JUMP` [`00bddcd0`](#insn-00bddcd0) → [`00bddd18`](#insn-00bddd18)
  - `FALL_THROUGH` [`00bddcd0`](#insn-00bddcd0) → [`00bddcd4`](#insn-00bddcd4)
- ブロック [`00bddcd4`](#insn-00bddcd4) 範囲 `[['00bddcd4', '00bddce3']]`
  - `CONDITIONAL_JUMP` [`00bddce0`](#insn-00bddce0) → [`00bddcf8`](#insn-00bddcf8)
  - `FALL_THROUGH` [`00bddce0`](#insn-00bddce0) → [`00bddce4`](#insn-00bddce4)
- ブロック [`00bddce4`](#insn-00bddce4) 範囲 `[['00bddce4', '00bddcf7']]`
  - `FALL_THROUGH` [`00bddcf4`](#insn-00bddcf4) → [`00bddcf8`](#insn-00bddcf8)
- ブロック [`00bddcf8`](#insn-00bddcf8) 範囲 `[['00bddcf8', '00bddd17']]`
  - `FALL_THROUGH` [`00bddd14`](#insn-00bddd14) → [`00bddd18`](#insn-00bddd18)
- ブロック [`00bddd18`](#insn-00bddd18) 範囲 `[['00bddd18', '00bddd27']]`

## 命令位置別の参照

- [`00bddcb8`](#insn-00bddcb8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcbc`](#insn-00bddcbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcc0`](#insn-00bddcc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddccc`](#insn-00bddccc) → `01126e28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddcd0`](#insn-00bddcd0) → [`00bddd18`](#insn-00bddd18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcd8`](#insn-00bddcd8) → `01126e30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bddce0`](#insn-00bddce0) → [`00bddcf8`](#insn-00bddcf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcf4`](#insn-00bddcf4) → `01126e30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bddcfc`](#insn-00bddcfc) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bddd04`](#insn-00bddd04) → `01126e28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddd14`](#insn-00bddd14) → `01126e28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddd18`](#insn-00bddd18) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddd1c`](#insn-00bddd1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddcb8`](#insn-00bddcb8)

~~~json
{
  "source": "00bddcb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcbc`](#insn-00bddcbc)

~~~json
{
  "source": "00bddcbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcc0`](#insn-00bddcc0)

~~~json
{
  "source": "00bddcc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddccc`](#insn-00bddccc)

~~~json
{
  "source": "00bddccc",
  "target": "01126e28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddcd0`](#insn-00bddcd0)

~~~json
{
  "source": "00bddcd0",
  "target": "00bddd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcd8`](#insn-00bddcd8)

~~~json
{
  "source": "00bddcd8",
  "target": "01126e30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddce0`](#insn-00bddce0)

~~~json
{
  "source": "00bddce0",
  "target": "00bddcf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcf4`](#insn-00bddcf4)

~~~json
{
  "source": "00bddcf4",
  "target": "01126e30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddcfc`](#insn-00bddcfc)

~~~json
{
  "source": "00bddcfc",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddd04`](#insn-00bddd04)

~~~json
{
  "source": "00bddd04",
  "target": "01126e28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddd14`](#insn-00bddd14)

~~~json
{
  "source": "00bddd14",
  "target": "01126e28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddd18`](#insn-00bddd18)

~~~json
{
  "source": "00bddd18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddd1c`](#insn-00bddd1c)

~~~json
{
  "source": "00bddd1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
