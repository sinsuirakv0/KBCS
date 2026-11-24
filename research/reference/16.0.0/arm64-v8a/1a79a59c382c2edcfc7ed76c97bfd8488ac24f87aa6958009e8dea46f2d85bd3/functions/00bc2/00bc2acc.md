# 00bc2acc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b53e10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e10.md) · 移動量 `+0x6ecbc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0065.md#compare-9777272181caba58bcf2bf2910dbed74)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bc2ef4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2ef4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0080.md#compare-707808178157a1a2935557119ca39f71)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc2acc",
  "name": "_ZN8firebase13remote_config8internal19throttled_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "08ee88d3c06cd01d8ef1d47f55d540688b510aa06a2a52b146c47e6d60a083ea",
  "source_text_sha256": "08ee88d3c06cd01d8ef1d47f55d540688b510aa06a2a52b146c47e6d60a083ea",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc2acc",
        "00bc2b0b"
      ]
    ],
    "bytes_sha256": "0f80294387534235e7eae442cae4c9fa30ddc59133a8fb88b87efc0d6e85b778",
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
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 485 bytes

~~~c

long _ZN8firebase13remote_config8internal19throttled_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEENS_4util16ClassRequirementE
               (void)

{
  if (DAT_01126238 == 0) {
    DAT_01126238 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126238;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc2acc"></a> `00bc2acc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bc2ad0"></a> `00bc2ad0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2ad4"></a> `00bc2ad4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bc2ad8"></a> `00bc2ad8` | `33 2b 00 90` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bc2adc"></a> `00bc2adc` | `68 1e 41 f9` | ldr x8,[x19, #0x238] | `FALL_THROUGH`
<a id="insn-00bc2ae0"></a> `00bc2ae0` | `e8 00 00 b5` | cbnz x8,0x00bc2afc | `CONDITIONAL_JUMP`
<a id="insn-00bc2ae4"></a> `00bc2ae4` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00bc2ae8"></a> `00bc2ae8` | `a3 b7 ff f0` | adrp x3,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bc2aec"></a> `00bc2aec` | `63 a0 2f 91` | add x3,x3,#0xbe8 | `FALL_THROUGH`
<a id="insn-00bc2af0"></a> `00bc2af0` | `08 60 02 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bc2af4"></a> `00bc2af4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bc2af8"></a> `00bc2af8` | `60 1e 01 f9` | str x0,[x19, #0x238] | `FALL_THROUGH`
<a id="insn-00bc2afc"></a> `00bc2afc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2b00"></a> `00bc2b00` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bc2b04"></a> `00bc2b04` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bc2b08"></a> `00bc2b08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc2acc`](#insn-00bc2acc) 範囲 `[['00bc2acc', '00bc2ae3']]`
  - `CONDITIONAL_JUMP` [`00bc2ae0`](#insn-00bc2ae0) → [`00bc2afc`](#insn-00bc2afc)
  - `FALL_THROUGH` [`00bc2ae0`](#insn-00bc2ae0) → [`00bc2ae4`](#insn-00bc2ae4)
- ブロック [`00bc2ae4`](#insn-00bc2ae4) 範囲 `[['00bc2ae4', '00bc2afb']]`
  - `FALL_THROUGH` [`00bc2af8`](#insn-00bc2af8) → [`00bc2afc`](#insn-00bc2afc)
- ブロック [`00bc2afc`](#insn-00bc2afc) 範囲 `[['00bc2afc', '00bc2b0b']]`

## 命令位置別の参照

- [`00bc2acc`](#insn-00bc2acc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2ad0`](#insn-00bc2ad0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2adc`](#insn-00bc2adc) → `01126238`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc2ae0`](#insn-00bc2ae0) → [`00bc2afc`](#insn-00bc2afc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2aec`](#insn-00bc2aec) → `002b9be8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc2af0`](#insn-00bc2af0) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bc2af8`](#insn-00bc2af8) → `01126238`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc2afc`](#insn-00bc2afc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc2acc`](#insn-00bc2acc)

~~~json
{
  "source": "00bc2acc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2ad0`](#insn-00bc2ad0)

~~~json
{
  "source": "00bc2ad0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2adc`](#insn-00bc2adc)

~~~json
{
  "source": "00bc2adc",
  "target": "01126238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126238",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc2ae0`](#insn-00bc2ae0)

~~~json
{
  "source": "00bc2ae0",
  "target": "00bc2afc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2aec`](#insn-00bc2aec)

~~~json
{
  "source": "00bc2aec",
  "target": "002b9be8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9be4",
  "offset": 4,
  "size": 81,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f72656d6f7465636f",
  "capture_start": "002b9be4",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bc2af0`](#insn-00bc2af0)

~~~json
{
  "source": "00bc2af0",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc2af8`](#insn-00bc2af8)

~~~json
{
  "source": "00bc2af8",
  "target": "01126238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126238",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc2afc`](#insn-00bc2afc)

~~~json
{
  "source": "00bc2afc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
