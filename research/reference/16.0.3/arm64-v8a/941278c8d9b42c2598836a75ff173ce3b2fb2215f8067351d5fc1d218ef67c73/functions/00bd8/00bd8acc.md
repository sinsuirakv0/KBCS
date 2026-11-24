# 00bd8acc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd7ad8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7ad8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0084.md#compare-bdedc4a3c1a4f6dc07e42aff8f81afcf)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd8acc",
  "name": "_ZN8firebase4auth8auth_idp15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cda1ef5c59ba9594ebeb7b1a504f10e0084dc6427945281d6b7e048261d64692",
  "source_text_sha256": "cda1ef5c59ba9594ebeb7b1a504f10e0084dc6427945281d6b7e048261d64692",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd8acc",
        "00bd8b37"
      ]
    ],
    "bytes_sha256": "23f0d87ecb8e852d2bd9f7a5ca07e55dec51bb4b5a862a6e1c64f6ec8ee4e139",
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

## 疑似コード / UTF-8 483 bytes

~~~c

bool _ZN8firebase4auth8auth_idp15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01127d30 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01127d28,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01127d30 = iVar2 == 0;
    bVar1 = (bool)DAT_01127d30;
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
<a id="insn-00bd8acc"></a> `00bd8acc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd8ad0"></a> `00bd8ad0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd8ad4"></a> `00bd8ad4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd8ad8"></a> `00bd8ad8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd8adc"></a> `00bd8adc` | `75 2a 00 f0` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd8ae0"></a> `00bd8ae0` | `a8 c2 74 39` | ldrb w8,[x21, #0xd30] | `FALL_THROUGH`
<a id="insn-00bd8ae4"></a> `00bd8ae4` | `68 00 00 34` | cbz w8,0x00bd8af0 | `CONDITIONAL_JUMP`
<a id="insn-00bd8ae8"></a> `00bd8ae8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bd8aec"></a> `00bd8aec` | `0f 00 00 14` | b 0x00bd8b28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bd8af0"></a> `00bd8af0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd8af4"></a> `00bd8af4` | `69 2a 00 f0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd8af8"></a> `00bd8af8` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bd8afc"></a> `00bd8afc` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bd8b00"></a> `00bd8b00` | `21 95 46 f9` | ldr x1,[x9, #0xd28] | `FALL_THROUGH`
<a id="insn-00bd8b04"></a> `00bd8b04` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bd8b08"></a> `00bd8b08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd8b0c"></a> `00bd8b0c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd8b10"></a> `00bd8b10` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bd8b14"></a> `00bd8b14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd8b18"></a> `00bd8b18` | `3a 0d 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bd8b1c"></a> `00bd8b1c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bd8b20"></a> `00bd8b20` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bd8b24"></a> `00bd8b24` | `a0 c2 34 39` | strb w0,[x21, #0xd30] | `FALL_THROUGH`
<a id="insn-00bd8b28"></a> `00bd8b28` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd8b2c"></a> `00bd8b2c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd8b30"></a> `00bd8b30` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd8b34"></a> `00bd8b34` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd8acc`](#insn-00bd8acc) 範囲 `[['00bd8acc', '00bd8ae7']]`
  - `CONDITIONAL_JUMP` [`00bd8ae4`](#insn-00bd8ae4) → [`00bd8af0`](#insn-00bd8af0)
  - `FALL_THROUGH` [`00bd8ae4`](#insn-00bd8ae4) → [`00bd8ae8`](#insn-00bd8ae8)
- ブロック [`00bd8ae8`](#insn-00bd8ae8) 範囲 `[['00bd8ae8', '00bd8aef']]`
  - `UNCONDITIONAL_JUMP` [`00bd8aec`](#insn-00bd8aec) → [`00bd8b28`](#insn-00bd8b28)
- ブロック [`00bd8af0`](#insn-00bd8af0) 範囲 `[['00bd8af0', '00bd8b27']]`
  - `FALL_THROUGH` [`00bd8b24`](#insn-00bd8b24) → [`00bd8b28`](#insn-00bd8b28)
- ブロック [`00bd8b28`](#insn-00bd8b28) 範囲 `[['00bd8b28', '00bd8b37']]`

## 命令位置別の参照

- [`00bd8acc`](#insn-00bd8acc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd8ad0`](#insn-00bd8ad0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd8ad4`](#insn-00bd8ad4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd8ae0`](#insn-00bd8ae0) → `01127d30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd8ae4`](#insn-00bd8ae4) → [`00bd8af0`](#insn-00bd8af0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd8aec`](#insn-00bd8aec) → [`00bd8b28`](#insn-00bd8b28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd8b00`](#insn-00bd8b00) → `01127d28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd8b18`](#insn-00bd8b18) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bd8b24`](#insn-00bd8b24) → `01127d30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd8b28`](#insn-00bd8b28) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd8b2c`](#insn-00bd8b2c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd8acc`](#insn-00bd8acc)

~~~json
{
  "source": "00bd8acc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd8ad0`](#insn-00bd8ad0)

~~~json
{
  "source": "00bd8ad0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd8ad4`](#insn-00bd8ad4)

~~~json
{
  "source": "00bd8ad4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd8ae0`](#insn-00bd8ae0)

~~~json
{
  "source": "00bd8ae0",
  "target": "01127d30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127d30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd8ae4`](#insn-00bd8ae4)

~~~json
{
  "source": "00bd8ae4",
  "target": "00bd8af0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd8aec`](#insn-00bd8aec)

~~~json
{
  "source": "00bd8aec",
  "target": "00bd8b28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd8b00`](#insn-00bd8b00)

~~~json
{
  "source": "00bd8b00",
  "target": "01127d28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127d28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd8b18`](#insn-00bd8b18)

~~~json
{
  "source": "00bd8b18",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd8b24`](#insn-00bd8b24)

~~~json
{
  "source": "00bd8b24",
  "target": "01127d30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127d30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd8b28`](#insn-00bd8b28)

~~~json
{
  "source": "00bd8b28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd8b2c`](#insn-00bd8b2c)

~~~json
{
  "source": "00bd8b2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
