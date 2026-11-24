# 00bddce8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bddc4c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddc4c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-c307cbe4bd1f7d2a3f3cc0fe4bf6942d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bdecdc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdecdc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-e1c298f82c8d9d45ef8d47f07bfa84b5)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddce8",
  "name": "_ZN8firebase4auth18userprofilebuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8994957b66db97bfd652ad8db6fa756f64747d29419c3a84aac45eaf9ebc6e3f",
  "source_text_sha256": "8994957b66db97bfd652ad8db6fa756f64747d29419c3a84aac45eaf9ebc6e3f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddce8",
        "00bddd53"
      ]
    ],
    "bytes_sha256": "0dbcdbc0ed49d4439b5eeb9ec1fb0d01a002390079152e50d473bb2ab7b374cd",
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

- [00c5b030](../00c5b/00c5b030.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 494 bytes

~~~c

bool _ZN8firebase4auth18userprofilebuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01126f30 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126f28,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126f30 = iVar2 == 0;
    bVar1 = (bool)DAT_01126f30;
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
<a id="insn-00bddce8"></a> `00bddce8` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bddcec"></a> `00bddcec` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddcf0"></a> `00bddcf0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddcf4"></a> `00bddcf4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bddcf8"></a> `00bddcf8` | `55 2a 00 b0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddcfc"></a> `00bddcfc` | `a8 c2 7c 39` | ldrb w8,[x21, #0xf30] | `FALL_THROUGH`
<a id="insn-00bddd00"></a> `00bddd00` | `68 00 00 34` | cbz w8,0x00bddd0c | `CONDITIONAL_JUMP`
<a id="insn-00bddd04"></a> `00bddd04` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bddd08"></a> `00bddd08` | `0f 00 00 14` | b 0x00bddd44 | `UNCONDITIONAL_JUMP`
<a id="insn-00bddd0c"></a> `00bddd0c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bddd10"></a> `00bddd10` | `49 2a 00 b0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddd14"></a> `00bddd14` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bddd18"></a> `00bddd18` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bddd1c"></a> `00bddd1c` | `21 95 47 f9` | ldr x1,[x9, #0xf28] | `FALL_THROUGH`
<a id="insn-00bddd20"></a> `00bddd20` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bddd24"></a> `00bddd24` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bddd28"></a> `00bddd28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bddd2c"></a> `00bddd2c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bddd30"></a> `00bddd30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddd34"></a> `00bddd34` | `bf f4 01 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bddd38"></a> `00bddd38` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bddd3c"></a> `00bddd3c` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bddd40"></a> `00bddd40` | `a0 c2 3c 39` | strb w0,[x21, #0xf30] | `FALL_THROUGH`
<a id="insn-00bddd44"></a> `00bddd44` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddd48"></a> `00bddd48` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddd4c"></a> `00bddd4c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bddd50"></a> `00bddd50` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddce8`](#insn-00bddce8) 範囲 `[['00bddce8', '00bddd03']]`
  - `CONDITIONAL_JUMP` [`00bddd00`](#insn-00bddd00) → [`00bddd0c`](#insn-00bddd0c)
  - `FALL_THROUGH` [`00bddd00`](#insn-00bddd00) → [`00bddd04`](#insn-00bddd04)
- ブロック [`00bddd04`](#insn-00bddd04) 範囲 `[['00bddd04', '00bddd0b']]`
  - `UNCONDITIONAL_JUMP` [`00bddd08`](#insn-00bddd08) → [`00bddd44`](#insn-00bddd44)
- ブロック [`00bddd0c`](#insn-00bddd0c) 範囲 `[['00bddd0c', '00bddd43']]`
  - `FALL_THROUGH` [`00bddd40`](#insn-00bddd40) → [`00bddd44`](#insn-00bddd44)
- ブロック [`00bddd44`](#insn-00bddd44) 範囲 `[['00bddd44', '00bddd53']]`

## 命令位置別の参照

- [`00bddce8`](#insn-00bddce8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcec`](#insn-00bddcec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcf0`](#insn-00bddcf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcfc`](#insn-00bddcfc) → `01126f30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bddd00`](#insn-00bddd00) → [`00bddd0c`](#insn-00bddd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddd08`](#insn-00bddd08) → [`00bddd44`](#insn-00bddd44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddd1c`](#insn-00bddd1c) → `01126f28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddd34`](#insn-00bddd34) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bddd40`](#insn-00bddd40) → `01126f30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bddd44`](#insn-00bddd44) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddd48`](#insn-00bddd48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddce8`](#insn-00bddce8)

~~~json
{
  "source": "00bddce8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcec`](#insn-00bddcec)

~~~json
{
  "source": "00bddcec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcf0`](#insn-00bddcf0)

~~~json
{
  "source": "00bddcf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcfc`](#insn-00bddcfc)

~~~json
{
  "source": "00bddcfc",
  "target": "01126f30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddd00`](#insn-00bddd00)

~~~json
{
  "source": "00bddd00",
  "target": "00bddd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddd08`](#insn-00bddd08)

~~~json
{
  "source": "00bddd08",
  "target": "00bddd44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddd1c`](#insn-00bddd1c)

~~~json
{
  "source": "00bddd1c",
  "target": "01126f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddd34`](#insn-00bddd34)

~~~json
{
  "source": "00bddd34",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddd40`](#insn-00bddd40)

~~~json
{
  "source": "00bddd40",
  "target": "01126f30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddd44`](#insn-00bddd44)

~~~json
{
  "source": "00bddd44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddd48`](#insn-00bddd48)

~~~json
{
  "source": "00bddd48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
