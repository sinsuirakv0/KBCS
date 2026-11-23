# 00ae8fbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ae8ef4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8ef4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-34c98597aa57630cde69083508cadbc8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ae9000`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9000.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0063.md#compare-84783820ba03d538e071c6db51d50956)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae8fbc",
  "name": "_ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "afd278ceab4fe7bea908ff490e1acf86c120fd74b87594e6a7752c6bf656682d",
  "source_text_sha256": "afd278ceab4fe7bea908ff490e1acf86c120fd74b87594e6a7752c6bf656682d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae8fbc",
        "00ae8fff"
      ]
    ],
    "bytes_sha256": "df7249ffcc4a7eb98256fc7eda1f629bdecc7836759ffd29f17e9a4946a467bc",
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

- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"android/content/ContentResolver"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1014 bytes

~~~c

long _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
                    /* catch() { ... } // from try @ 00ae7084 with catch @ 00ae8fd0 */
  if (DAT_010a0680 == 0) {
                    /* catch() { ... } // from try @ 00ae8530 with catch @ 00ae8fd8 */
                    /* catch() { ... } // from try @ 00ae70b8 with catch @ 00ae8fdc */
                    /* catch() { ... } // from try @ 00ae7158 with catch @ 00ae8fe4 */
    DAT_010a0680 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/content/ContentResolver",param_3);
  }
                    /* catch() { ... } // from try @ 00ae70c8 with catch @ 00ae8ff0 */
                    /* catch() { ... } // from try @ 00ae7198 with catch @ 00ae8ff8 */
  return DAT_010a0680;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae8fbc"></a> `00ae8fbc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae8fc0"></a> `00ae8fc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae8fc4"></a> `00ae8fc4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae8fc8"></a> `00ae8fc8` | `d3 2d 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae8fcc"></a> `00ae8fcc` | `68 42 43 f9` | ldr x8,[x19, #0x680] | `FALL_THROUGH`
<a id="insn-00ae8fd0"></a> `00ae8fd0` | `08 01 00 b5` | cbnz x8,0x00ae8ff0 | `CONDITIONAL_JUMP`
<a id="insn-00ae8fd4"></a> `00ae8fd4` | `a3 bd ff d0` | adrp x3,0x29e000 | `FALL_THROUGH`
<a id="insn-00ae8fd8"></a> `00ae8fd8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00ae8fdc"></a> `00ae8fdc` | `63 44 39 91` | add x3,x3,#0xe51 | `FALL_THROUGH`
<a id="insn-00ae8fe0"></a> `00ae8fe0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ae8fe4"></a> `00ae8fe4` | `17 d4 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00ae8fe8"></a> `00ae8fe8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ae8fec"></a> `00ae8fec` | `60 42 03 f9` | str x0,[x19, #0x680] | `FALL_THROUGH`
<a id="insn-00ae8ff0"></a> `00ae8ff0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae8ff4"></a> `00ae8ff4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00ae8ff8"></a> `00ae8ff8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae8ffc"></a> `00ae8ffc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae8fbc`](#insn-00ae8fbc) 範囲 `[['00ae8fbc', '00ae8fcf']]`
  - `FALL_THROUGH` [`00ae8fcc`](#insn-00ae8fcc) → [`00ae8fd0`](#insn-00ae8fd0)
- ブロック [`00ae8fd0`](#insn-00ae8fd0) 範囲 `[['00ae8fd0', '00ae8fd3']]`
  - `CONDITIONAL_JUMP` [`00ae8fd0`](#insn-00ae8fd0) → [`00ae8ff0`](#insn-00ae8ff0)
  - `FALL_THROUGH` [`00ae8fd0`](#insn-00ae8fd0) → [`00ae8fd4`](#insn-00ae8fd4)
- ブロック [`00ae8fd4`](#insn-00ae8fd4) 範囲 `[['00ae8fd4', '00ae8fd7']]`
  - `FALL_THROUGH` [`00ae8fd4`](#insn-00ae8fd4) → [`00ae8fd8`](#insn-00ae8fd8)
- ブロック [`00ae8fd8`](#insn-00ae8fd8) 範囲 `[['00ae8fd8', '00ae8fdb']]`
  - `FALL_THROUGH` [`00ae8fd8`](#insn-00ae8fd8) → [`00ae8fdc`](#insn-00ae8fdc)
- ブロック [`00ae8fdc`](#insn-00ae8fdc) 範囲 `[['00ae8fdc', '00ae8fe3']]`
  - `FALL_THROUGH` [`00ae8fe0`](#insn-00ae8fe0) → [`00ae8fe4`](#insn-00ae8fe4)
- ブロック [`00ae8fe4`](#insn-00ae8fe4) 範囲 `[['00ae8fe4', '00ae8fef']]`
  - `FALL_THROUGH` [`00ae8fec`](#insn-00ae8fec) → [`00ae8ff0`](#insn-00ae8ff0)
- ブロック [`00ae8ff0`](#insn-00ae8ff0) 範囲 `[['00ae8ff0', '00ae8ff7']]`
  - `FALL_THROUGH` [`00ae8ff4`](#insn-00ae8ff4) → [`00ae8ff8`](#insn-00ae8ff8)
- ブロック [`00ae8ff8`](#insn-00ae8ff8) 範囲 `[['00ae8ff8', '00ae8fff']]`

## 命令位置別の参照

- [`00ae8fbc`](#insn-00ae8fbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae8fc0`](#insn-00ae8fc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae8fcc`](#insn-00ae8fcc) → `010a0680`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae8fd0`](#insn-00ae8fd0) → [`00ae8ff0`](#insn-00ae8ff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae8fdc`](#insn-00ae8fdc) → `0029ee51`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae8fe4`](#insn-00ae8fe4) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00ae8fec`](#insn-00ae8fec) → `010a0680`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae8ff0`](#insn-00ae8ff0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae8fbc`](#insn-00ae8fbc)

~~~json
{
  "source": "00ae8fbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae8fc0`](#insn-00ae8fc0)

~~~json
{
  "source": "00ae8fc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae8fcc`](#insn-00ae8fcc)

~~~json
{
  "source": "00ae8fcc",
  "target": "010a0680",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0680",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae8fd0`](#insn-00ae8fd0)

~~~json
{
  "source": "00ae8fd0",
  "target": "00ae8ff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae8fdc`](#insn-00ae8fdc)

~~~json
{
  "source": "00ae8fdc",
  "target": "0029ee51",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ee51",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "616e64726f69642f636f6e74656e742f436f6e74656e745265736f6c76657200",
  "capture_start": "0029ee51",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae8fe4`](#insn-00ae8fe4)

~~~json
{
  "source": "00ae8fe4",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae8fec`](#insn-00ae8fec)

~~~json
{
  "source": "00ae8fec",
  "target": "010a0680",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0680",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae8ff0`](#insn-00ae8ff0)

~~~json
{
  "source": "00ae8ff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
