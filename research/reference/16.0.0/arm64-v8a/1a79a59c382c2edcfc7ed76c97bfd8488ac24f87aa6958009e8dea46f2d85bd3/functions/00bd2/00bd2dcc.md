# 00bd2dcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b638cc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b638cc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0068.md#compare-8d9d6c7fd09916f91e80e2fb409aaa3f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd31f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd31f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0083.md#compare-7d8c8693944206a57cfb355f4173bf59)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd2dcc",
  "name": "_ZN8firebase4auth27too_many_requests_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c4a31b6ea4176278548fcaabe8292b15b685ea70bef9cc3f7dd2d855f8516e0d",
  "source_text_sha256": "c4a31b6ea4176278548fcaabe8292b15b685ea70bef9cc3f7dd2d855f8516e0d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd2dcc",
        "00bd2e0f"
      ]
    ],
    "bytes_sha256": "632f67819e71667160dda41e982e7179a72bff45b6f33aa27db6cc2f8b5714e0",
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

- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/FirebaseTooManyRequestsException"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 559 bytes

~~~c

long _ZN8firebase4auth27too_many_requests_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_01126608 == 0) {
    DAT_01126608 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/FirebaseTooManyRequestsException",param_3);
  }
  return DAT_01126608;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd2dcc"></a> `00bd2dcc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd2dd0"></a> `00bd2dd0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2dd4"></a> `00bd2dd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd2dd8"></a> `00bd2dd8` | `b3 2a 00 90` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd2ddc"></a> `00bd2ddc` | `68 06 43 f9` | ldr x8,[x19, #0x608] | `FALL_THROUGH`
<a id="insn-00bd2de0"></a> `00bd2de0` | `08 01 00 b5` | cbnz x8,0x00bd2e00 | `CONDITIONAL_JUMP`
<a id="insn-00bd2de4"></a> `00bd2de4` | `03 b7 ff f0` | adrp x3,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bd2de8"></a> `00bd2de8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00bd2dec"></a> `00bd2dec` | `63 64 2f 91` | add x3,x3,#0xbd9 | `FALL_THROUGH`
<a id="insn-00bd2df0"></a> `00bd2df0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bd2df4"></a> `00bd2df4` | `47 1f 02 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2df8"></a> `00bd2df8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bd2dfc"></a> `00bd2dfc` | `60 06 03 f9` | str x0,[x19, #0x608] | `FALL_THROUGH`
<a id="insn-00bd2e00"></a> `00bd2e00` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2e04"></a> `00bd2e04` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bd2e08"></a> `00bd2e08` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd2e0c"></a> `00bd2e0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd2dcc`](#insn-00bd2dcc) 範囲 `[['00bd2dcc', '00bd2de3']]`
  - `CONDITIONAL_JUMP` [`00bd2de0`](#insn-00bd2de0) → [`00bd2e00`](#insn-00bd2e00)
  - `FALL_THROUGH` [`00bd2de0`](#insn-00bd2de0) → [`00bd2de4`](#insn-00bd2de4)
- ブロック [`00bd2de4`](#insn-00bd2de4) 範囲 `[['00bd2de4', '00bd2dff']]`
  - `FALL_THROUGH` [`00bd2dfc`](#insn-00bd2dfc) → [`00bd2e00`](#insn-00bd2e00)
- ブロック [`00bd2e00`](#insn-00bd2e00) 範囲 `[['00bd2e00', '00bd2e0f']]`

## 命令位置別の参照

- [`00bd2dcc`](#insn-00bd2dcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2dd0`](#insn-00bd2dd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2ddc`](#insn-00bd2ddc) → `01126608`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd2de0`](#insn-00bd2de0) → [`00bd2e00`](#insn-00bd2e00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2dec`](#insn-00bd2dec) → `002b5bd9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd2df4`](#insn-00bd2df4) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bd2dfc`](#insn-00bd2dfc) → `01126608`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd2e00`](#insn-00bd2e00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd2dcc`](#insn-00bd2dcc)

~~~json
{
  "source": "00bd2dcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2dd0`](#insn-00bd2dd0)

~~~json
{
  "source": "00bd2dd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2ddc`](#insn-00bd2ddc)

~~~json
{
  "source": "00bd2ddc",
  "target": "01126608",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126608",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd2de0`](#insn-00bd2de0)

~~~json
{
  "source": "00bd2de0",
  "target": "00bd2e00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2dec`](#insn-00bd2dec)

~~~json
{
  "source": "00bd2dec",
  "target": "002b5bd9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5bd5",
  "offset": 4,
  "size": 57,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f4669726562617365",
  "capture_start": "002b5bd5",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd2df4`](#insn-00bd2df4)

~~~json
{
  "source": "00bd2df4",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2dfc`](#insn-00bd2dfc)

~~~json
{
  "source": "00bd2dfc",
  "target": "01126608",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126608",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd2e00`](#insn-00bd2e00)

~~~json
{
  "source": "00bd2e00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
