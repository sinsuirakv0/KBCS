# 00ae0cec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ae0c24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0c24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-e798c383bd623e499ae5d84005fca5cf)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ae0d30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0d30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0061.md#compare-335d3b9d0cbd0a50b236a6d5705e3827)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae0cec",
  "name": "_ZN8firebase9analytics24analytics_consent_status10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "60190da88929e560b7d32ef305749b420f6ea0c80426412ea20299c0ade3cdd8",
  "source_text_sha256": "60190da88929e560b7d32ef305749b420f6ea0c80426412ea20299c0ade3cdd8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae0cec",
        "00ae0d2f"
      ]
    ],
    "bytes_sha256": "76ac6df3bfc2d8628110a3c49841746bd2349f24a1cbf7675d3bcf3129fc0c3c",
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
"%PG%com/google/firebase/analytics/FirebaseAnalytics$ConsentStatus"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 951 bytes

~~~c

long _ZN8firebase9analytics24analytics_consent_status10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a00d8 == 0) {
    DAT_010a00d8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/analytics/FirebaseAnalytics$ConsentStatus",0);
  }
                    /* try { // try from 00ae0d20 to 00be0f0b has its CatchHandler @ 00ae0d20
                       catch() { ... } // from try @ 00ae0d20 with catch @ 00ae0d20
                       catch() { ... } // from try @ 00ae0f14 with catch @ 00ae0d20
                       catch() { ... } // from try @ 00ae0f98 with catch @ 00ae0d20
                       catch() { ... } // from try @ 00ae1004 with catch @ 00ae0d20 */
  return DAT_010a00d8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae0cec"></a> `00ae0cec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae0cf0"></a> `00ae0cf0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae0cf4"></a> `00ae0cf4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae0cf8"></a> `00ae0cf8` | `13 2e 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae0cfc"></a> `00ae0cfc` | `68 6e 40 f9` | ldr x8,[x19, #0xd8] | `FALL_THROUGH`
<a id="insn-00ae0d00"></a> `00ae0d00` | `08 01 00 b5` | cbnz x8,0x00ae0d20 | `CONDITIONAL_JUMP`
<a id="insn-00ae0d04"></a> `00ae0d04` | `a3 bd ff 90` | adrp x3,0x294000 | `FALL_THROUGH`
<a id="insn-00ae0d08"></a> `00ae0d08` | `63 98 05 91` | add x3,x3,#0x166 | `FALL_THROUGH`
<a id="insn-00ae0d0c"></a> `00ae0d0c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ae0d10"></a> `00ae0d10` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00ae0d14"></a> `00ae0d14` | `cb f4 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00ae0d18"></a> `00ae0d18` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ae0d1c"></a> `00ae0d1c` | `60 6e 00 f9` | str x0,[x19, #0xd8] | `FALL_THROUGH`
<a id="insn-00ae0d20"></a> `00ae0d20` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae0d24"></a> `00ae0d24` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00ae0d28"></a> `00ae0d28` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae0d2c"></a> `00ae0d2c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae0cec`](#insn-00ae0cec) 範囲 `[['00ae0cec', '00ae0d03']]`
  - `CONDITIONAL_JUMP` [`00ae0d00`](#insn-00ae0d00) → [`00ae0d20`](#insn-00ae0d20)
  - `FALL_THROUGH` [`00ae0d00`](#insn-00ae0d00) → [`00ae0d04`](#insn-00ae0d04)
- ブロック [`00ae0d04`](#insn-00ae0d04) 範囲 `[['00ae0d04', '00ae0d1f']]`
  - `FALL_THROUGH` [`00ae0d1c`](#insn-00ae0d1c) → [`00ae0d20`](#insn-00ae0d20)
- ブロック [`00ae0d20`](#insn-00ae0d20) 範囲 `[['00ae0d20', '00ae0d2f']]`

## 命令位置別の参照

- [`00ae0cec`](#insn-00ae0cec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0cf0`](#insn-00ae0cf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0cfc`](#insn-00ae0cfc) → `010a00d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae0d00`](#insn-00ae0d00) → [`00ae0d20`](#insn-00ae0d20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0d08`](#insn-00ae0d08) → `00294166`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae0d14`](#insn-00ae0d14) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00ae0d1c`](#insn-00ae0d1c) → `010a00d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae0d20`](#insn-00ae0d20) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae0cec`](#insn-00ae0cec)

~~~json
{
  "source": "00ae0cec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0cf0`](#insn-00ae0cf0)

~~~json
{
  "source": "00ae0cf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0cfc`](#insn-00ae0cfc)

~~~json
{
  "source": "00ae0cfc",
  "target": "010a00d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a00d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae0d00`](#insn-00ae0d00)

~~~json
{
  "source": "00ae0d00",
  "target": "00ae0d20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0d08`](#insn-00ae0d08)

~~~json
{
  "source": "00ae0d08",
  "target": "00294166",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00294162",
  "offset": 4,
  "size": 66,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f616e616c79746963",
  "capture_start": "00294162",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ae0d14`](#insn-00ae0d14)

~~~json
{
  "source": "00ae0d14",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae0d1c`](#insn-00ae0d1c)

~~~json
{
  "source": "00ae0d1c",
  "target": "010a00d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a00d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae0d20`](#insn-00ae0d20)

~~~json
{
  "source": "00ae0d20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
