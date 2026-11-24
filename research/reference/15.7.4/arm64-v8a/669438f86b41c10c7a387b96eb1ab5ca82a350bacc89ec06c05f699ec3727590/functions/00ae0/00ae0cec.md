# 00ae0cec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae0ca8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0ca8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0061.md#compare-2ba36b734401f5425970577f5c17d67f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b406c4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b406c4.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0055.md#compare-34f07e1a2bb4733b522fea02750643b6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae0cec",
  "name": "_ZN8firebase9analytics24analytics_consent_status10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed0be5e167ff82a0386e9d26854e8c4b6d45539be7cb5392fb8cec6b90f41727",
  "source_text_sha256": "ed0be5e167ff82a0386e9d26854e8c4b6d45539be7cb5392fb8cec6b90f41727",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae0cec",
        "00ae0d2f"
      ]
    ],
    "bytes_sha256": "02d9da93ff6c4e6e8130622aecc782c9377c26bd669600bfc6399111f08c9fb6",
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
"%PG%com/google/firebase/analytics/FirebaseAnalytics$ConsentStatus"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 601 bytes

~~~c

long _ZN8firebase9analytics24analytics_consent_status10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a0118 == 0) {
    DAT_010a0118 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/analytics/FirebaseAnalytics$ConsentStatus",
                              param_3);
  }
  return DAT_010a0118;
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
<a id="insn-00ae0cfc"></a> `00ae0cfc` | `68 8e 40 f9` | ldr x8,[x19, #0x118] | `FALL_THROUGH`
<a id="insn-00ae0d00"></a> `00ae0d00` | `08 01 00 b5` | cbnz x8,0x00ae0d20 | `CONDITIONAL_JUMP`
<a id="insn-00ae0d04"></a> `00ae0d04` | `a3 bd ff 90` | adrp x3,0x294000 | `FALL_THROUGH`
<a id="insn-00ae0d08"></a> `00ae0d08` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00ae0d0c"></a> `00ae0d0c` | `63 64 03 91` | add x3,x3,#0xd9 | `FALL_THROUGH`
<a id="insn-00ae0d10"></a> `00ae0d10` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ae0d14"></a> `00ae0d14` | `df f4 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00ae0d18"></a> `00ae0d18` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ae0d1c"></a> `00ae0d1c` | `60 8e 00 f9` | str x0,[x19, #0x118] | `FALL_THROUGH`
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
- [`00ae0cfc`](#insn-00ae0cfc) → `010a0118`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae0d00`](#insn-00ae0d00) → [`00ae0d20`](#insn-00ae0d20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0d0c`](#insn-00ae0d0c) → `002940d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae0d14`](#insn-00ae0d14) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00ae0d1c`](#insn-00ae0d1c) → `010a0118`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
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
  "target": "010a0118",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0118",
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
- 参照命令 [`00ae0d0c`](#insn-00ae0d0c)

~~~json
{
  "source": "00ae0d0c",
  "target": "002940d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002940d5",
  "offset": 4,
  "size": 66,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f616e616c79746963",
  "capture_start": "002940d5",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ae0d14`](#insn-00ae0d14)

~~~json
{
  "source": "00ae0d14",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae0d1c`](#insn-00ae0d1c)

~~~json
{
  "source": "00ae0d1c",
  "target": "010a0118",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0118",
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
