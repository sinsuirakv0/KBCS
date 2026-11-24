# 00aece6c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aece28`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece28.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-edbc96c902218b0b5643045a725867dd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4cbf0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cbf0.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-f2170dae78ab70e44ebc7b156b6d9604)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aece6c",
  "name": "_ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2d2a7a8d6d1a5e6137129af2d4a848570abd4aa4a7cdffd164217c6b00df862d",
  "source_text_sha256": "2d2a7a8d6d1a5e6137129af2d4a848570abd4aa4a7cdffd164217c6b00df862d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aece6c",
        "00aeceaf"
      ]
    ],
    "bytes_sha256": "8268329a46984d15b717f3bc65672d8581de6d065e0894b652150cc01851415d",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Set"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 396 bytes

~~~c

long _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a09c8 == 0) {
    DAT_010a09c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Set",0);
  }
  return DAT_010a09c8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aece6c"></a> `00aece6c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aece70"></a> `00aece70` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aece74"></a> `00aece74` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aece78"></a> `00aece78` | `b3 2d 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aece7c"></a> `00aece7c` | `68 e6 44 f9` | ldr x8,[x19, #0x9c8] | `FALL_THROUGH`
<a id="insn-00aece80"></a> `00aece80` | `08 01 00 b5` | cbnz x8,0x00aecea0 | `CONDITIONAL_JUMP`
<a id="insn-00aece84"></a> `00aece84` | `a3 bd ff 90` | adrp x3,0x2a0000 | `FALL_THROUGH`
<a id="insn-00aece88"></a> `00aece88` | `63 28 01 91` | add x3,x3,#0x4a | `FALL_THROUGH`
<a id="insn-00aece8c"></a> `00aece8c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aece90"></a> `00aece90` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aece94"></a> `00aece94` | `7f c4 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aece98"></a> `00aece98` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aece9c"></a> `00aece9c` | `60 e6 04 f9` | str x0,[x19, #0x9c8] | `FALL_THROUGH`
<a id="insn-00aecea0"></a> `00aecea0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecea4"></a> `00aecea4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aecea8"></a> `00aecea8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeceac"></a> `00aeceac` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aece6c`](#insn-00aece6c) 範囲 `[['00aece6c', '00aece83']]`
  - `CONDITIONAL_JUMP` [`00aece80`](#insn-00aece80) → [`00aecea0`](#insn-00aecea0)
  - `FALL_THROUGH` [`00aece80`](#insn-00aece80) → [`00aece84`](#insn-00aece84)
- ブロック [`00aece84`](#insn-00aece84) 範囲 `[['00aece84', '00aece9f']]`
  - `FALL_THROUGH` [`00aece9c`](#insn-00aece9c) → [`00aecea0`](#insn-00aecea0)
- ブロック [`00aecea0`](#insn-00aecea0) 範囲 `[['00aecea0', '00aeceaf']]`

## 命令位置別の参照

- [`00aece6c`](#insn-00aece6c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aece70`](#insn-00aece70) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aece7c`](#insn-00aece7c) → `010a09c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aece80`](#insn-00aece80) → [`00aecea0`](#insn-00aecea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aece88`](#insn-00aece88) → `002a004a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aece94`](#insn-00aece94) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aece9c`](#insn-00aece9c) → `010a09c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecea0`](#insn-00aecea0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aece6c`](#insn-00aece6c)

~~~json
{
  "source": "00aece6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aece70`](#insn-00aece70)

~~~json
{
  "source": "00aece70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aece7c`](#insn-00aece7c)

~~~json
{
  "source": "00aece7c",
  "target": "010a09c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aece80`](#insn-00aece80)

~~~json
{
  "source": "00aece80",
  "target": "00aecea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aece88`](#insn-00aece88)

~~~json
{
  "source": "00aece88",
  "target": "002a004a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a004a",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f53657400",
  "capture_start": "002a004a",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aece94`](#insn-00aece94)

~~~json
{
  "source": "00aece94",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aece9c`](#insn-00aece9c)

~~~json
{
  "source": "00aece9c",
  "target": "010a09c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecea0`](#insn-00aecea0)

~~~json
{
  "source": "00aecea0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
