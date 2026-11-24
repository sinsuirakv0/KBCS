# 00bd6adc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd6a40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6a40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0084.md#compare-b9f5dfc2dae8b86c5231076266f30947)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd7ad0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7ad0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0084.md#compare-febae04fda6ccb6dda88f444f2976e4f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd6adc",
  "name": "_ZN8firebase4auth8timeunit12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "50c150900e6c3ee0a4ae5e6eb115c4f968c6c873fd4ef8cda1d5832fa440f239",
  "source_text_sha256": "50c150900e6c3ee0a4ae5e6eb115c4f968c6c873fd4ef8cda1d5832fa440f239",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd6adc",
        "00bd6b4b"
      ]
    ],
    "bytes_sha256": "25c46d9ce38cca0786127dff42028e60de6eb616fa1aa9c61c4df1bf4cf4ea24",
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

- [00c5b030](../00c5b/00c5b030.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 382 bytes

~~~c

void _ZN8firebase4auth8timeunit12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_01126c58 != 0) {
    if (DAT_01126c60 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126c60 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126c58);
    DAT_01126c58 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd6adc"></a> `00bd6adc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd6ae0"></a> `00bd6ae0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd6ae4"></a> `00bd6ae4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd6ae8"></a> `00bd6ae8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd6aec"></a> `00bd6aec` | `94 2a 00 90` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd6af0"></a> `00bd6af0` | `81 2e 46 f9` | ldr x1,[x20, #0xc58] | `FALL_THROUGH`
<a id="insn-00bd6af4"></a> `00bd6af4` | `41 02 00 b4` | cbz x1,0x00bd6b3c | `CONDITIONAL_JUMP`
<a id="insn-00bd6af8"></a> `00bd6af8` | `95 2a 00 90` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd6afc"></a> `00bd6afc` | `a8 82 71 39` | ldrb w8,[x21, #0xc60] | `FALL_THROUGH`
<a id="insn-00bd6b00"></a> `00bd6b00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd6b04"></a> `00bd6b04` | `c8 00 00 34` | cbz w8,0x00bd6b1c | `CONDITIONAL_JUMP`
<a id="insn-00bd6b08"></a> `00bd6b08` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd6b0c"></a> `00bd6b0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd6b10"></a> `00bd6b10` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd6b14"></a> `00bd6b14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd6b18"></a> `00bd6b18` | `bf 82 31 39` | strb wzr,[x21, #0xc60] | `FALL_THROUGH`
<a id="insn-00bd6b1c"></a> `00bd6b1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd6b20"></a> `00bd6b20` | `44 11 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd6b24"></a> `00bd6b24` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd6b28"></a> `00bd6b28` | `81 2e 46 f9` | ldr x1,[x20, #0xc58] | `FALL_THROUGH`
<a id="insn-00bd6b2c"></a> `00bd6b2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd6b30"></a> `00bd6b30` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd6b34"></a> `00bd6b34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd6b38"></a> `00bd6b38` | `9f 2e 06 f9` | str xzr,[x20, #0xc58] | `FALL_THROUGH`
<a id="insn-00bd6b3c"></a> `00bd6b3c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd6b40"></a> `00bd6b40` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd6b44"></a> `00bd6b44` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd6b48"></a> `00bd6b48` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd6adc`](#insn-00bd6adc) 範囲 `[['00bd6adc', '00bd6af7']]`
  - `CONDITIONAL_JUMP` [`00bd6af4`](#insn-00bd6af4) → [`00bd6b3c`](#insn-00bd6b3c)
  - `FALL_THROUGH` [`00bd6af4`](#insn-00bd6af4) → [`00bd6af8`](#insn-00bd6af8)
- ブロック [`00bd6af8`](#insn-00bd6af8) 範囲 `[['00bd6af8', '00bd6b07']]`
  - `CONDITIONAL_JUMP` [`00bd6b04`](#insn-00bd6b04) → [`00bd6b1c`](#insn-00bd6b1c)
  - `FALL_THROUGH` [`00bd6b04`](#insn-00bd6b04) → [`00bd6b08`](#insn-00bd6b08)
- ブロック [`00bd6b08`](#insn-00bd6b08) 範囲 `[['00bd6b08', '00bd6b1b']]`
  - `FALL_THROUGH` [`00bd6b18`](#insn-00bd6b18) → [`00bd6b1c`](#insn-00bd6b1c)
- ブロック [`00bd6b1c`](#insn-00bd6b1c) 範囲 `[['00bd6b1c', '00bd6b3b']]`
  - `FALL_THROUGH` [`00bd6b38`](#insn-00bd6b38) → [`00bd6b3c`](#insn-00bd6b3c)
- ブロック [`00bd6b3c`](#insn-00bd6b3c) 範囲 `[['00bd6b3c', '00bd6b4b']]`

## 命令位置別の参照

- [`00bd6adc`](#insn-00bd6adc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6ae0`](#insn-00bd6ae0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6ae4`](#insn-00bd6ae4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6af0`](#insn-00bd6af0) → `01126c58`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd6af4`](#insn-00bd6af4) → [`00bd6b3c`](#insn-00bd6b3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6afc`](#insn-00bd6afc) → `01126c60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd6b04`](#insn-00bd6b04) → [`00bd6b1c`](#insn-00bd6b1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6b18`](#insn-00bd6b18) → `01126c60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd6b20`](#insn-00bd6b20) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd6b28`](#insn-00bd6b28) → `01126c58`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd6b38`](#insn-00bd6b38) → `01126c58`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd6b3c`](#insn-00bd6b3c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6b40`](#insn-00bd6b40) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd6adc`](#insn-00bd6adc)

~~~json
{
  "source": "00bd6adc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6ae0`](#insn-00bd6ae0)

~~~json
{
  "source": "00bd6ae0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6ae4`](#insn-00bd6ae4)

~~~json
{
  "source": "00bd6ae4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6af0`](#insn-00bd6af0)

~~~json
{
  "source": "00bd6af0",
  "target": "01126c58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126c58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd6af4`](#insn-00bd6af4)

~~~json
{
  "source": "00bd6af4",
  "target": "00bd6b3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6afc`](#insn-00bd6afc)

~~~json
{
  "source": "00bd6afc",
  "target": "01126c60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126c60",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd6b04`](#insn-00bd6b04)

~~~json
{
  "source": "00bd6b04",
  "target": "00bd6b1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6b18`](#insn-00bd6b18)

~~~json
{
  "source": "00bd6b18",
  "target": "01126c60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126c60",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd6b20`](#insn-00bd6b20)

~~~json
{
  "source": "00bd6b20",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd6b28`](#insn-00bd6b28)

~~~json
{
  "source": "00bd6b28",
  "target": "01126c58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126c58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd6b38`](#insn-00bd6b38)

~~~json
{
  "source": "00bd6b38",
  "target": "01126c58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126c58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd6b3c`](#insn-00bd6b3c)

~~~json
{
  "source": "00bd6b3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6b40`](#insn-00bd6b40)

~~~json
{
  "source": "00bd6b40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
