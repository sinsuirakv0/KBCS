# 00bdcf2c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdcb04`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcb04.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-a053efbf17efd8301c130d4691ee63a9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdcfc8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcfc8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-fe08098407ec6299e071fd17e4ec8427)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcf2c",
  "name": "_ZN8firebase4auth11tokenresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0f49097d49aa93a0922f898af7756e85af4663af8dd8d2a9fd87762ec6456e5a",
  "source_text_sha256": "0f49097d49aa93a0922f898af7756e85af4663af8dd8d2a9fd87762ec6456e5a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcf2c",
        "00bdcf97"
      ]
    ],
    "bytes_sha256": "b68d9fa9ecdcff39afad8675be0cd838e95960d7e93662dcd590a5a56583dcab",
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

- [00c5af60](../00c5a/00c5af60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 487 bytes

~~~c

bool _ZN8firebase4auth11tokenresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01126d08 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126d00,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126d08 = iVar2 == 0;
    bVar1 = (bool)DAT_01126d08;
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
<a id="insn-00bdcf2c"></a> `00bdcf2c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdcf30"></a> `00bdcf30` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcf34"></a> `00bdcf34` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdcf38"></a> `00bdcf38` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdcf3c"></a> `00bdcf3c` | `55 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdcf40"></a> `00bdcf40` | `a8 22 74 39` | ldrb w8,[x21, #0xd08] | `FALL_THROUGH`
<a id="insn-00bdcf44"></a> `00bdcf44` | `68 00 00 34` | cbz w8,0x00bdcf50 | `CONDITIONAL_JUMP`
<a id="insn-00bdcf48"></a> `00bdcf48` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bdcf4c"></a> `00bdcf4c` | `0f 00 00 14` | b 0x00bdcf88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdcf50"></a> `00bdcf50` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdcf54"></a> `00bdcf54` | `49 2a 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdcf58"></a> `00bdcf58` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bdcf5c"></a> `00bdcf5c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bdcf60"></a> `00bdcf60` | `21 81 46 f9` | ldr x1,[x9, #0xd00] | `FALL_THROUGH`
<a id="insn-00bdcf64"></a> `00bdcf64` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bdcf68"></a> `00bdcf68` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdcf6c"></a> `00bdcf6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcf70"></a> `00bdcf70` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bdcf74"></a> `00bdcf74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcf78"></a> `00bdcf78` | `fa f7 01 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcf7c"></a> `00bdcf7c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bdcf80"></a> `00bdcf80` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bdcf84"></a> `00bdcf84` | `a0 22 34 39` | strb w0,[x21, #0xd08] | `FALL_THROUGH`
<a id="insn-00bdcf88"></a> `00bdcf88` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdcf8c"></a> `00bdcf8c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcf90"></a> `00bdcf90` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdcf94"></a> `00bdcf94` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcf2c`](#insn-00bdcf2c) 範囲 `[['00bdcf2c', '00bdcf47']]`
  - `CONDITIONAL_JUMP` [`00bdcf44`](#insn-00bdcf44) → [`00bdcf50`](#insn-00bdcf50)
  - `FALL_THROUGH` [`00bdcf44`](#insn-00bdcf44) → [`00bdcf48`](#insn-00bdcf48)
- ブロック [`00bdcf48`](#insn-00bdcf48) 範囲 `[['00bdcf48', '00bdcf4f']]`
  - `UNCONDITIONAL_JUMP` [`00bdcf4c`](#insn-00bdcf4c) → [`00bdcf88`](#insn-00bdcf88)
- ブロック [`00bdcf50`](#insn-00bdcf50) 範囲 `[['00bdcf50', '00bdcf87']]`
  - `FALL_THROUGH` [`00bdcf84`](#insn-00bdcf84) → [`00bdcf88`](#insn-00bdcf88)
- ブロック [`00bdcf88`](#insn-00bdcf88) 範囲 `[['00bdcf88', '00bdcf97']]`

## 命令位置別の参照

- [`00bdcf2c`](#insn-00bdcf2c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcf30`](#insn-00bdcf30) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcf34`](#insn-00bdcf34) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcf40`](#insn-00bdcf40) → `01126d08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdcf44`](#insn-00bdcf44) → [`00bdcf50`](#insn-00bdcf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcf4c`](#insn-00bdcf4c) → [`00bdcf88`](#insn-00bdcf88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcf60`](#insn-00bdcf60) → `01126d00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcf78`](#insn-00bdcf78) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bdcf84`](#insn-00bdcf84) → `01126d08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdcf88`](#insn-00bdcf88) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcf8c`](#insn-00bdcf8c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcf2c`](#insn-00bdcf2c)

~~~json
{
  "source": "00bdcf2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcf30`](#insn-00bdcf30)

~~~json
{
  "source": "00bdcf30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcf34`](#insn-00bdcf34)

~~~json
{
  "source": "00bdcf34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcf40`](#insn-00bdcf40)

~~~json
{
  "source": "00bdcf40",
  "target": "01126d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d08",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcf44`](#insn-00bdcf44)

~~~json
{
  "source": "00bdcf44",
  "target": "00bdcf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcf4c`](#insn-00bdcf4c)

~~~json
{
  "source": "00bdcf4c",
  "target": "00bdcf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcf60`](#insn-00bdcf60)

~~~json
{
  "source": "00bdcf60",
  "target": "01126d00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcf78`](#insn-00bdcf78)

~~~json
{
  "source": "00bdcf78",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcf84`](#insn-00bdcf84)

~~~json
{
  "source": "00bdcf84",
  "target": "01126d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d08",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcf88`](#insn-00bdcf88)

~~~json
{
  "source": "00bdcf88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcf8c`](#insn-00bdcf8c)

~~~json
{
  "source": "00bdcf8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
