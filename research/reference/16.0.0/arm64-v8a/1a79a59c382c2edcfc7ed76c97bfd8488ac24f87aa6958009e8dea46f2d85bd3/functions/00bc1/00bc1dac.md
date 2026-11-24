# 00bc1dac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b53438`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53438.md) · 移動量 `+0x6e974`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0065.md#compare-428b3725852043c51007d3693c9a3344)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bc21d4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc21d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0080.md#compare-073e96ea0c1cfe07ea9f5febf5bce565)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc1dac",
  "name": "_ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9465a188a9c9471b9f5a024b11e0c56084910f32958cccc8d0c81c15d2b2ffd9",
  "source_text_sha256": "9465a188a9c9471b9f5a024b11e0c56084910f32958cccc8d0c81c15d2b2ffd9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc1dac",
        "00bc1deb"
      ]
    ],
    "bytes_sha256": "b96e7f53fe3c96dd1512f2c1d390868dd706754b697543aa29fdcf0c0809098b",
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

- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 574 bytes

~~~c

long _ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEENS_4util16ClassRequirementE
               (void)

{
  if (DAT_01126168 == 0) {
    DAT_01126168 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
                    /* try { // try from 00bc1dd8 to 00cc1ddb has its CatchHandler @ 00bc1fe0 */
  }
  return DAT_01126168;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc1dac"></a> `00bc1dac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bc1db0"></a> `00bc1db0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc1db4"></a> `00bc1db4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bc1db8"></a> `00bc1db8` | `33 2b 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bc1dbc"></a> `00bc1dbc` | `68 b6 40 f9` | ldr x8,[x19, #0x168] | `FALL_THROUGH`
<a id="insn-00bc1dc0"></a> `00bc1dc0` | `e8 00 00 b5` | cbnz x8,0x00bc1ddc | `CONDITIONAL_JUMP`
<a id="insn-00bc1dc4"></a> `00bc1dc4` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00bc1dc8"></a> `00bc1dc8` | `23 b7 ff d0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bc1dcc"></a> `00bc1dcc` | `63 30 0c 91` | add x3,x3,#0x30c | `FALL_THROUGH`
<a id="insn-00bc1dd0"></a> `00bc1dd0` | `50 63 02 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bc1dd4"></a> `00bc1dd4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bc1dd8"></a> `00bc1dd8` | `60 b6 00 f9` | str x0,[x19, #0x168] | `FALL_THROUGH`
<a id="insn-00bc1ddc"></a> `00bc1ddc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc1de0"></a> `00bc1de0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bc1de4"></a> `00bc1de4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bc1de8"></a> `00bc1de8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc1dac`](#insn-00bc1dac) 範囲 `[['00bc1dac', '00bc1dc3']]`
  - `CONDITIONAL_JUMP` [`00bc1dc0`](#insn-00bc1dc0) → [`00bc1ddc`](#insn-00bc1ddc)
  - `FALL_THROUGH` [`00bc1dc0`](#insn-00bc1dc0) → [`00bc1dc4`](#insn-00bc1dc4)
- ブロック [`00bc1dc4`](#insn-00bc1dc4) 範囲 `[['00bc1dc4', '00bc1dd7']]`
  - `FALL_THROUGH` [`00bc1dd4`](#insn-00bc1dd4) → [`00bc1dd8`](#insn-00bc1dd8)
- ブロック [`00bc1dd8`](#insn-00bc1dd8) 範囲 `[['00bc1dd8', '00bc1ddb']]`
  - `FALL_THROUGH` [`00bc1dd8`](#insn-00bc1dd8) → [`00bc1ddc`](#insn-00bc1ddc)
- ブロック [`00bc1ddc`](#insn-00bc1ddc) 範囲 `[['00bc1ddc', '00bc1deb']]`

## 命令位置別の参照

- [`00bc1dac`](#insn-00bc1dac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1db0`](#insn-00bc1db0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1dbc`](#insn-00bc1dbc) → `01126168`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc1dc0`](#insn-00bc1dc0) → [`00bc1ddc`](#insn-00bc1ddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1dcc`](#insn-00bc1dcc) → `002a730c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc1dd0`](#insn-00bc1dd0) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bc1dd8`](#insn-00bc1dd8) → `01126168`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc1ddc`](#insn-00bc1ddc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc1dac`](#insn-00bc1dac)

~~~json
{
  "source": "00bc1dac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1db0`](#insn-00bc1db0)

~~~json
{
  "source": "00bc1db0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1dbc`](#insn-00bc1dbc)

~~~json
{
  "source": "00bc1dbc",
  "target": "01126168",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126168",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc1dc0`](#insn-00bc1dc0)

~~~json
{
  "source": "00bc1dc0",
  "target": "00bc1ddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1dcc`](#insn-00bc1dcc)

~~~json
{
  "source": "00bc1dcc",
  "target": "002a730c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7308",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f72656d6f7465636f",
  "capture_start": "002a7308",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bc1dd0`](#insn-00bc1dd0)

~~~json
{
  "source": "00bc1dd0",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc1dd8`](#insn-00bc1dd8)

~~~json
{
  "source": "00bc1dd8",
  "target": "01126168",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126168",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc1ddc`](#insn-00bc1ddc)

~~~json
{
  "source": "00bc1ddc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
