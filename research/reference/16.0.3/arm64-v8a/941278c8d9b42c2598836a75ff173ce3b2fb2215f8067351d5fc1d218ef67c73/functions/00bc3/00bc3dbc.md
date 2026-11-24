# 00bc3dbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc2dc8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2dc8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0080.md#compare-cec32d3b12656f5a9076018849dd03fb)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc3dbc",
  "name": "_ZN8firebase13remote_config8internal22custom_signals_builder12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "99874e3e67582ce47a28e281c1c824b1b1562c0e5f9eb04e27053b884b57684f",
  "source_text_sha256": "99874e3e67582ce47a28e281c1c824b1b1562c0e5f9eb04e27053b884b57684f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc3dbc",
        "00bc3e2b"
      ]
    ],
    "bytes_sha256": "5acb0ebbe94b4e3bb9f46649b6036c9feba115a57989e6a230e4a2bf0095c08f",
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

- [00c5c000](../00c5c/00c5c000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 432 bytes

~~~c

void _ZN8firebase13remote_config8internal22custom_signals_builder12ReleaseClassEP7_JNIEnv
               (long *param_1)

{
  if (DAT_011276b8 != 0) {
    if (DAT_011276c0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011276c0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011276b8);
    DAT_011276b8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc3dbc"></a> `00bc3dbc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bc3dc0"></a> `00bc3dc0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc3dc4"></a> `00bc3dc4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc3dc8"></a> `00bc3dc8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bc3dcc"></a> `00bc3dcc` | `34 2b 00 90` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc3dd0"></a> `00bc3dd0` | `81 5e 43 f9` | ldr x1,[x20, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bc3dd4"></a> `00bc3dd4` | `41 02 00 b4` | cbz x1,0x00bc3e1c | `CONDITIONAL_JUMP`
<a id="insn-00bc3dd8"></a> `00bc3dd8` | `35 2b 00 90` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc3ddc"></a> `00bc3ddc` | `a8 02 5b 39` | ldrb w8,[x21, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc3de0"></a> `00bc3de0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc3de4"></a> `00bc3de4` | `c8 00 00 34` | cbz w8,0x00bc3dfc | `CONDITIONAL_JUMP`
<a id="insn-00bc3de8"></a> `00bc3de8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc3dec"></a> `00bc3dec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc3df0"></a> `00bc3df0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc3df4"></a> `00bc3df4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc3df8"></a> `00bc3df8` | `bf 02 1b 39` | strb wzr,[x21, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc3dfc"></a> `00bc3dfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc3e00"></a> `00bc3e00` | `80 60 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc3e04"></a> `00bc3e04` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc3e08"></a> `00bc3e08` | `81 5e 43 f9` | ldr x1,[x20, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bc3e0c"></a> `00bc3e0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc3e10"></a> `00bc3e10` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bc3e14"></a> `00bc3e14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc3e18"></a> `00bc3e18` | `9f 5e 03 f9` | str xzr,[x20, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bc3e1c"></a> `00bc3e1c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc3e20"></a> `00bc3e20` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc3e24"></a> `00bc3e24` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bc3e28"></a> `00bc3e28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc3dbc`](#insn-00bc3dbc) 範囲 `[['00bc3dbc', '00bc3dd7']]`
  - `CONDITIONAL_JUMP` [`00bc3dd4`](#insn-00bc3dd4) → [`00bc3e1c`](#insn-00bc3e1c)
  - `FALL_THROUGH` [`00bc3dd4`](#insn-00bc3dd4) → [`00bc3dd8`](#insn-00bc3dd8)
- ブロック [`00bc3dd8`](#insn-00bc3dd8) 範囲 `[['00bc3dd8', '00bc3de7']]`
  - `CONDITIONAL_JUMP` [`00bc3de4`](#insn-00bc3de4) → [`00bc3dfc`](#insn-00bc3dfc)
  - `FALL_THROUGH` [`00bc3de4`](#insn-00bc3de4) → [`00bc3de8`](#insn-00bc3de8)
- ブロック [`00bc3de8`](#insn-00bc3de8) 範囲 `[['00bc3de8', '00bc3dfb']]`
  - `FALL_THROUGH` [`00bc3df8`](#insn-00bc3df8) → [`00bc3dfc`](#insn-00bc3dfc)
- ブロック [`00bc3dfc`](#insn-00bc3dfc) 範囲 `[['00bc3dfc', '00bc3e1b']]`
  - `FALL_THROUGH` [`00bc3e18`](#insn-00bc3e18) → [`00bc3e1c`](#insn-00bc3e1c)
- ブロック [`00bc3e1c`](#insn-00bc3e1c) 範囲 `[['00bc3e1c', '00bc3e2b']]`

## 命令位置別の参照

- [`00bc3dbc`](#insn-00bc3dbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc3dc0`](#insn-00bc3dc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc3dc4`](#insn-00bc3dc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc3dd0`](#insn-00bc3dd0) → `011276b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc3dd4`](#insn-00bc3dd4) → [`00bc3e1c`](#insn-00bc3e1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc3ddc`](#insn-00bc3ddc) → `011276c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc3de4`](#insn-00bc3de4) → [`00bc3dfc`](#insn-00bc3dfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc3df8`](#insn-00bc3df8) → `011276c0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc3e00`](#insn-00bc3e00) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc3e08`](#insn-00bc3e08) → `011276b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc3e18`](#insn-00bc3e18) → `011276b8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc3e1c`](#insn-00bc3e1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc3e20`](#insn-00bc3e20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc3dbc`](#insn-00bc3dbc)

~~~json
{
  "source": "00bc3dbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc3dc0`](#insn-00bc3dc0)

~~~json
{
  "source": "00bc3dc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc3dc4`](#insn-00bc3dc4)

~~~json
{
  "source": "00bc3dc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc3dd0`](#insn-00bc3dd0)

~~~json
{
  "source": "00bc3dd0",
  "target": "011276b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011276b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc3dd4`](#insn-00bc3dd4)

~~~json
{
  "source": "00bc3dd4",
  "target": "00bc3e1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc3ddc`](#insn-00bc3ddc)

~~~json
{
  "source": "00bc3ddc",
  "target": "011276c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011276c0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc3de4`](#insn-00bc3de4)

~~~json
{
  "source": "00bc3de4",
  "target": "00bc3dfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc3df8`](#insn-00bc3df8)

~~~json
{
  "source": "00bc3df8",
  "target": "011276c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011276c0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc3e00`](#insn-00bc3e00)

~~~json
{
  "source": "00bc3e00",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc3e08`](#insn-00bc3e08)

~~~json
{
  "source": "00bc3e08",
  "target": "011276b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011276b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc3e18`](#insn-00bc3e18)

~~~json
{
  "source": "00bc3e18",
  "target": "011276b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011276b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc3e1c`](#insn-00bc3e1c)

~~~json
{
  "source": "00bc3e1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc3e20`](#insn-00bc3e20)

~~~json
{
  "source": "00bc3e20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
