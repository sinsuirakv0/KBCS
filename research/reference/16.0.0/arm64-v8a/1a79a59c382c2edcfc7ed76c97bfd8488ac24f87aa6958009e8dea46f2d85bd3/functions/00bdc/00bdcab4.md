# 00bdcab4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6d5b4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d5b4.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-1435fa2877552ab445488efd2041120d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdcedc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcedc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-685dcfe59129378f2fd3ae8701bad053)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcab4",
  "name": "_ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a24bc387d213ac2c9d0435bad669f4544fe0ded83f5ad061c6e1ef928a409fce",
  "source_text_sha256": "a24bc387d213ac2c9d0435bad669f4544fe0ded83f5ad061c6e1ef928a409fce",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcab4",
        "00bdcaf7"
      ]
    ],
    "bytes_sha256": "950cbe8ffe5b48d8dcf9fa6f7265ec1eb349f06e8afc319bb44707d8acac193b",
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
"%PG%com/google/firebase/auth/GetTokenResult"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 738 bytes

~~~c

long _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00bdcab4 to 00cdcabf has its CatchHandler @ 00bde9d0 */
                    /* try { // try from 00bdcac0 to 00cdcad7 has its CatchHandler @ 00bde9cc */
  if (DAT_01126900 == 0) {
                    /* try { // try from 00bdcad8 to 00cdd4f3 has its CatchHandler @ 00bd6d50 */
    DAT_01126900 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/GetTokenResult",0);
  }
  return DAT_01126900;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcab4"></a> `00bdcab4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdcab8"></a> `00bdcab8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcabc"></a> `00bdcabc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdcac0"></a> `00bdcac0` | `53 2a 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdcac4"></a> `00bdcac4` | `68 82 44 f9` | ldr x8,[x19, #0x900] | `FALL_THROUGH`
<a id="insn-00bdcac8"></a> `00bdcac8` | `08 01 00 b5` | cbnz x8,0x00bdcae8 | `CONDITIONAL_JUMP`
<a id="insn-00bdcacc"></a> `00bdcacc` | `03 b7 ff 90` | adrp x3,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bdcad0"></a> `00bdcad0` | `63 40 08 91` | add x3,x3,#0x210 | `FALL_THROUGH`
<a id="insn-00bdcad4"></a> `00bdcad4` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdcad8"></a> `00bdcad8` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdcadc"></a> `00bdcadc` | `0d f8 01 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcae0"></a> `00bdcae0` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bdcae4"></a> `00bdcae4` | `60 82 04 f9` | str x0,[x19, #0x900] | `FALL_THROUGH`
<a id="insn-00bdcae8"></a> `00bdcae8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcaec"></a> `00bdcaec` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bdcaf0"></a> `00bdcaf0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdcaf4"></a> `00bdcaf4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcab4`](#insn-00bdcab4) 範囲 `[['00bdcab4', '00bdcabf']]`
  - `FALL_THROUGH` [`00bdcabc`](#insn-00bdcabc) → [`00bdcac0`](#insn-00bdcac0)
- ブロック [`00bdcac0`](#insn-00bdcac0) 範囲 `[['00bdcac0', '00bdcacb']]`
  - `CONDITIONAL_JUMP` [`00bdcac8`](#insn-00bdcac8) → [`00bdcae8`](#insn-00bdcae8)
  - `FALL_THROUGH` [`00bdcac8`](#insn-00bdcac8) → [`00bdcacc`](#insn-00bdcacc)
- ブロック [`00bdcacc`](#insn-00bdcacc) 範囲 `[['00bdcacc', '00bdcad7']]`
  - `FALL_THROUGH` [`00bdcad4`](#insn-00bdcad4) → [`00bdcad8`](#insn-00bdcad8)
- ブロック [`00bdcad8`](#insn-00bdcad8) 範囲 `[['00bdcad8', '00bdcae7']]`
  - `FALL_THROUGH` [`00bdcae4`](#insn-00bdcae4) → [`00bdcae8`](#insn-00bdcae8)
- ブロック [`00bdcae8`](#insn-00bdcae8) 範囲 `[['00bdcae8', '00bdcaf7']]`

## 命令位置別の参照

- [`00bdcab4`](#insn-00bdcab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcab8`](#insn-00bdcab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcac4`](#insn-00bdcac4) → `01126900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcac8`](#insn-00bdcac8) → [`00bdcae8`](#insn-00bdcae8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcad0`](#insn-00bdcad0) → `002bc210`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdcadc`](#insn-00bdcadc) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bdcae4`](#insn-00bdcae4) → `01126900`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcae8`](#insn-00bdcae8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcab4`](#insn-00bdcab4)

~~~json
{
  "source": "00bdcab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcab8`](#insn-00bdcab8)

~~~json
{
  "source": "00bdcab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcac4`](#insn-00bdcac4)

~~~json
{
  "source": "00bdcac4",
  "target": "01126900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126900",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcac8`](#insn-00bdcac8)

~~~json
{
  "source": "00bdcac8",
  "target": "00bdcae8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcad0`](#insn-00bdcad0)

~~~json
{
  "source": "00bdcad0",
  "target": "002bc210",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc20c",
  "offset": 4,
  "size": 44,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f476574",
  "capture_start": "002bc20c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdcadc`](#insn-00bdcadc)

~~~json
{
  "source": "00bdcadc",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcae4`](#insn-00bdcae4)

~~~json
{
  "source": "00bdcae4",
  "target": "01126900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126900",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcae8`](#insn-00bdcae8)

~~~json
{
  "source": "00bdcae8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
