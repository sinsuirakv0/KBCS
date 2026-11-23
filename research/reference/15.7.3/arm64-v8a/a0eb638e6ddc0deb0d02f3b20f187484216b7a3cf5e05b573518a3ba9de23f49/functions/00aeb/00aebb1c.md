# 00aebb1c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aeba54`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba54.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-c96f61fb806ee89aa644929496e9513d)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aebb60`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb60.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-fdceb5d7bdadd731c7774430ee60418d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebb1c",
  "name": "_ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a298a5ea82c43337833e7208fadd2a221c97aa5210175a41f51942fe2ed47922",
  "source_text_sha256": "a298a5ea82c43337833e7208fadd2a221c97aa5210175a41f51942fe2ed47922",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebb1c",
        "00aebb5b"
      ]
    ],
    "bytes_sha256": "d921b0a35b4c102e8c75ea73ce3e2eb050c9157c2949a63256fced20a2f984dd",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Iterator"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 547 bytes

~~~c

long _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a08b8 == 0) {
    DAT_010a08b8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
                    /* try { // try from 00aebb54 to 00bebb6f has its CatchHandler @ 00af1ac0 */
  return DAT_010a08b8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebb1c"></a> `00aebb1c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebb20"></a> `00aebb20` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebb24"></a> `00aebb24` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebb28"></a> `00aebb28` | `b3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebb2c"></a> `00aebb2c` | `68 5e 44 f9` | ldr x8,[x19, #0x8b8] | `FALL_THROUGH`
<a id="insn-00aebb30"></a> `00aebb30` | `e8 00 00 b5` | cbnz x8,0x00aebb4c | `CONDITIONAL_JUMP`
<a id="insn-00aebb34"></a> `00aebb34` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00aebb38"></a> `00aebb38` | `63 bd ff 90` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aebb3c"></a> `00aebb3c` | `63 9c 15 91` | add x3,x3,#0x567 | `FALL_THROUGH`
<a id="insn-00aebb40"></a> `00aebb40` | `40 c9 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aebb44"></a> `00aebb44` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aebb48"></a> `00aebb48` | `60 5e 04 f9` | str x0,[x19, #0x8b8] | `FALL_THROUGH`
<a id="insn-00aebb4c"></a> `00aebb4c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebb50"></a> `00aebb50` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aebb54"></a> `00aebb54` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebb58"></a> `00aebb58` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebb1c`](#insn-00aebb1c) 範囲 `[['00aebb1c', '00aebb33']]`
  - `CONDITIONAL_JUMP` [`00aebb30`](#insn-00aebb30) → [`00aebb4c`](#insn-00aebb4c)
  - `FALL_THROUGH` [`00aebb30`](#insn-00aebb30) → [`00aebb34`](#insn-00aebb34)
- ブロック [`00aebb34`](#insn-00aebb34) 範囲 `[['00aebb34', '00aebb4b']]`
  - `FALL_THROUGH` [`00aebb48`](#insn-00aebb48) → [`00aebb4c`](#insn-00aebb4c)
- ブロック [`00aebb4c`](#insn-00aebb4c) 範囲 `[['00aebb4c', '00aebb53']]`
  - `FALL_THROUGH` [`00aebb50`](#insn-00aebb50) → [`00aebb54`](#insn-00aebb54)
- ブロック [`00aebb54`](#insn-00aebb54) 範囲 `[['00aebb54', '00aebb5b']]`

## 命令位置別の参照

- [`00aebb1c`](#insn-00aebb1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb20`](#insn-00aebb20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb2c`](#insn-00aebb2c) → `010a08b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebb30`](#insn-00aebb30) → [`00aebb4c`](#insn-00aebb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb3c`](#insn-00aebb3c) → `00297567`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebb40`](#insn-00aebb40) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aebb48`](#insn-00aebb48) → `010a08b8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebb4c`](#insn-00aebb4c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebb1c`](#insn-00aebb1c)

~~~json
{
  "source": "00aebb1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb20`](#insn-00aebb20)

~~~json
{
  "source": "00aebb20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb2c`](#insn-00aebb2c)

~~~json
{
  "source": "00aebb2c",
  "target": "010a08b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebb30`](#insn-00aebb30)

~~~json
{
  "source": "00aebb30",
  "target": "00aebb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb3c`](#insn-00aebb3c)

~~~json
{
  "source": "00aebb3c",
  "target": "00297567",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00297567",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4974657261746f7200",
  "capture_start": "00297567",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebb40`](#insn-00aebb40)

~~~json
{
  "source": "00aebb40",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebb48`](#insn-00aebb48)

~~~json
{
  "source": "00aebb48",
  "target": "010a08b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebb4c`](#insn-00aebb4c)

~~~json
{
  "source": "00aebb4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
