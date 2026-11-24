# 00bd7dac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd6db8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6db8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0084.md#compare-0eb8fe25a44fa9d01f5aa1f8fd6c5bc7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd7dac",
  "name": "_ZN8firebase4auth26phone_auth_options_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "806effe6714c0086a58ddcb66b941885ae3c835fb0626436ef5d45148978a258",
  "source_text_sha256": "806effe6714c0086a58ddcb66b941885ae3c835fb0626436ef5d45148978a258",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd7dac",
        "00bd7e17"
      ]
    ],
    "bytes_sha256": "fae273aeb8762409b75027426a782a8ed14b35a22d2070cb6cbd3b20a1092cae",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5c000](../00c5c/00c5c000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 502 bytes

~~~c

bool _ZN8firebase4auth26phone_auth_options_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01127c40 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01127c38,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01127c40 = iVar2 == 0;
    bVar1 = (bool)DAT_01127c40;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd7dac"></a> `00bd7dac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd7db0"></a> `00bd7db0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd7db4"></a> `00bd7db4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd7db8"></a> `00bd7db8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd7dbc"></a> `00bd7dbc` | `95 2a 00 90` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd7dc0"></a> `00bd7dc0` | `a8 02 71 39` | ldrb w8,[x21, #0xc40] | `FALL_THROUGH`
<a id="insn-00bd7dc4"></a> `00bd7dc4` | `68 00 00 34` | cbz w8,0x00bd7dd0 | `CONDITIONAL_JUMP`
<a id="insn-00bd7dc8"></a> `00bd7dc8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bd7dcc"></a> `00bd7dcc` | `0f 00 00 14` | b 0x00bd7e08 | `UNCONDITIONAL_JUMP`
<a id="insn-00bd7dd0"></a> `00bd7dd0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd7dd4"></a> `00bd7dd4` | `89 2a 00 90` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd7dd8"></a> `00bd7dd8` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bd7ddc"></a> `00bd7ddc` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bd7de0"></a> `00bd7de0` | `21 1d 46 f9` | ldr x1,[x9, #0xc38] | `FALL_THROUGH`
<a id="insn-00bd7de4"></a> `00bd7de4` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bd7de8"></a> `00bd7de8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd7dec"></a> `00bd7dec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd7df0"></a> `00bd7df0` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bd7df4"></a> `00bd7df4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd7df8"></a> `00bd7df8` | `82 10 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bd7dfc"></a> `00bd7dfc` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bd7e00"></a> `00bd7e00` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bd7e04"></a> `00bd7e04` | `a0 02 31 39` | strb w0,[x21, #0xc40] | `FALL_THROUGH`
<a id="insn-00bd7e08"></a> `00bd7e08` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd7e0c"></a> `00bd7e0c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd7e10"></a> `00bd7e10` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd7e14"></a> `00bd7e14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd7dac`](#insn-00bd7dac) 範囲 `[['00bd7dac', '00bd7dc7']]`
  - `CONDITIONAL_JUMP` [`00bd7dc4`](#insn-00bd7dc4) → [`00bd7dd0`](#insn-00bd7dd0)
  - `FALL_THROUGH` [`00bd7dc4`](#insn-00bd7dc4) → [`00bd7dc8`](#insn-00bd7dc8)
- ブロック [`00bd7dc8`](#insn-00bd7dc8) 範囲 `[['00bd7dc8', '00bd7dcf']]`
  - `UNCONDITIONAL_JUMP` [`00bd7dcc`](#insn-00bd7dcc) → [`00bd7e08`](#insn-00bd7e08)
- ブロック [`00bd7dd0`](#insn-00bd7dd0) 範囲 `[['00bd7dd0', '00bd7e07']]`
  - `FALL_THROUGH` [`00bd7e04`](#insn-00bd7e04) → [`00bd7e08`](#insn-00bd7e08)
- ブロック [`00bd7e08`](#insn-00bd7e08) 範囲 `[['00bd7e08', '00bd7e17']]`

## 命令位置別の参照

- [`00bd7dac`](#insn-00bd7dac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7db0`](#insn-00bd7db0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7db4`](#insn-00bd7db4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7dc0`](#insn-00bd7dc0) → `01127c40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd7dc4`](#insn-00bd7dc4) → [`00bd7dd0`](#insn-00bd7dd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7dcc`](#insn-00bd7dcc) → [`00bd7e08`](#insn-00bd7e08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7de0`](#insn-00bd7de0) → `01127c38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd7df8`](#insn-00bd7df8) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bd7e04`](#insn-00bd7e04) → `01127c40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd7e08`](#insn-00bd7e08) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7e0c`](#insn-00bd7e0c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd7dac`](#insn-00bd7dac)

~~~json
{
  "source": "00bd7dac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7db0`](#insn-00bd7db0)

~~~json
{
  "source": "00bd7db0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7db4`](#insn-00bd7db4)

~~~json
{
  "source": "00bd7db4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7dc0`](#insn-00bd7dc0)

~~~json
{
  "source": "00bd7dc0",
  "target": "01127c40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c40",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd7dc4`](#insn-00bd7dc4)

~~~json
{
  "source": "00bd7dc4",
  "target": "00bd7dd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7dcc`](#insn-00bd7dcc)

~~~json
{
  "source": "00bd7dcc",
  "target": "00bd7e08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7de0`](#insn-00bd7de0)

~~~json
{
  "source": "00bd7de0",
  "target": "01127c38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd7df8`](#insn-00bd7df8)

~~~json
{
  "source": "00bd7df8",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd7e04`](#insn-00bd7e04)

~~~json
{
  "source": "00bd7e04",
  "target": "01127c40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c40",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd7e08`](#insn-00bd7e08)

~~~json
{
  "source": "00bd7e08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7e0c`](#insn-00bd7e0c)

~~~json
{
  "source": "00bd7e0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
