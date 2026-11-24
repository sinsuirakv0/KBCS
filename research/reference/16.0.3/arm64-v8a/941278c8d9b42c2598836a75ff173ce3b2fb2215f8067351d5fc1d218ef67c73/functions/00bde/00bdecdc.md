# 00bdecdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bddce8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddce8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-e1c298f82c8d9d45ef8d47f07bfa84b5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdecdc",
  "name": "_ZN8firebase4auth18userprofilebuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d705af341764b74399145468dcd2c3a2fbe50aaf9118d658ae973c25526cd111",
  "source_text_sha256": "d705af341764b74399145468dcd2c3a2fbe50aaf9118d658ae973c25526cd111",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdecdc",
        "00bded47"
      ]
    ],
    "bytes_sha256": "b3c92e3d4f99ee2df60fa1deb8363a585683c0a6ab667aa477149197ddc1c5c1",
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

## 疑似コード / UTF-8 494 bytes

~~~c

bool _ZN8firebase4auth18userprofilebuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01127ef0 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01127ee8,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01127ef0 = iVar2 == 0;
    bVar1 = (bool)DAT_01127ef0;
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
<a id="insn-00bdecdc"></a> `00bdecdc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdece0"></a> `00bdece0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdece4"></a> `00bdece4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdece8"></a> `00bdece8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdecec"></a> `00bdecec` | `55 2a 00 b0` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdecf0"></a> `00bdecf0` | `a8 c2 7b 39` | ldrb w8,[x21, #0xef0] | `FALL_THROUGH`
<a id="insn-00bdecf4"></a> `00bdecf4` | `68 00 00 34` | cbz w8,0x00bded00 | `CONDITIONAL_JUMP`
<a id="insn-00bdecf8"></a> `00bdecf8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bdecfc"></a> `00bdecfc` | `0f 00 00 14` | b 0x00bded38 | `UNCONDITIONAL_JUMP`
<a id="insn-00bded00"></a> `00bded00` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bded04"></a> `00bded04` | `49 2a 00 b0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bded08"></a> `00bded08` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bded0c"></a> `00bded0c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bded10"></a> `00bded10` | `21 75 47 f9` | ldr x1,[x9, #0xee8] | `FALL_THROUGH`
<a id="insn-00bded14"></a> `00bded14` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bded18"></a> `00bded18` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bded1c"></a> `00bded1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bded20"></a> `00bded20` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bded24"></a> `00bded24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bded28"></a> `00bded28` | `b6 f4 01 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bded2c"></a> `00bded2c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bded30"></a> `00bded30` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bded34"></a> `00bded34` | `a0 c2 3b 39` | strb w0,[x21, #0xef0] | `FALL_THROUGH`
<a id="insn-00bded38"></a> `00bded38` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bded3c"></a> `00bded3c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bded40"></a> `00bded40` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bded44"></a> `00bded44` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdecdc`](#insn-00bdecdc) 範囲 `[['00bdecdc', '00bdecf7']]`
  - `CONDITIONAL_JUMP` [`00bdecf4`](#insn-00bdecf4) → [`00bded00`](#insn-00bded00)
  - `FALL_THROUGH` [`00bdecf4`](#insn-00bdecf4) → [`00bdecf8`](#insn-00bdecf8)
- ブロック [`00bdecf8`](#insn-00bdecf8) 範囲 `[['00bdecf8', '00bdecff']]`
  - `UNCONDITIONAL_JUMP` [`00bdecfc`](#insn-00bdecfc) → [`00bded38`](#insn-00bded38)
- ブロック [`00bded00`](#insn-00bded00) 範囲 `[['00bded00', '00bded37']]`
  - `FALL_THROUGH` [`00bded34`](#insn-00bded34) → [`00bded38`](#insn-00bded38)
- ブロック [`00bded38`](#insn-00bded38) 範囲 `[['00bded38', '00bded47']]`

## 命令位置別の参照

- [`00bdecdc`](#insn-00bdecdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdece0`](#insn-00bdece0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdece4`](#insn-00bdece4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdecf0`](#insn-00bdecf0) → `01127ef0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdecf4`](#insn-00bdecf4) → [`00bded00`](#insn-00bded00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdecfc`](#insn-00bdecfc) → [`00bded38`](#insn-00bded38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded10`](#insn-00bded10) → `01127ee8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bded28`](#insn-00bded28) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bded34`](#insn-00bded34) → `01127ef0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bded38`](#insn-00bded38) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded3c`](#insn-00bded3c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdecdc`](#insn-00bdecdc)

~~~json
{
  "source": "00bdecdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdece0`](#insn-00bdece0)

~~~json
{
  "source": "00bdece0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdece4`](#insn-00bdece4)

~~~json
{
  "source": "00bdece4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdecf0`](#insn-00bdecf0)

~~~json
{
  "source": "00bdecf0",
  "target": "01127ef0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ef0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdecf4`](#insn-00bdecf4)

~~~json
{
  "source": "00bdecf4",
  "target": "00bded00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdecfc`](#insn-00bdecfc)

~~~json
{
  "source": "00bdecfc",
  "target": "00bded38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded10`](#insn-00bded10)

~~~json
{
  "source": "00bded10",
  "target": "01127ee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bded28`](#insn-00bded28)

~~~json
{
  "source": "00bded28",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bded34`](#insn-00bded34)

~~~json
{
  "source": "00bded34",
  "target": "01127ef0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ef0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bded38`](#insn-00bded38)

~~~json
{
  "source": "00bded38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded3c`](#insn-00bded3c)

~~~json
{
  "source": "00bded3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
