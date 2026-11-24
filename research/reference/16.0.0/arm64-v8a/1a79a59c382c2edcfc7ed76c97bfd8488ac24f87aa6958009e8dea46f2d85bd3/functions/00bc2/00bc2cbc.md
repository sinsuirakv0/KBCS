# 00bc2cbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b54000`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54000.md) · 移動量 `+0x6ecbc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0065.md#compare-a92d1faa2f9fd55c452c162fd540881e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bc30e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc30e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0080.md#compare-0a00077019e23bbaeded8cc03fd033ea)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc2cbc",
  "name": "_ZN8firebase13remote_config8internal19throttled_exception14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ec068a24b5446fa88ec61216871c37703b9fa293f2fd5d4d40f459bfc9cfab4",
  "source_text_sha256": "9ec068a24b5446fa88ec61216871c37703b9fa293f2fd5d4d40f459bfc9cfab4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc2cbc",
        "00bc2d2b"
      ]
    ],
    "bytes_sha256": "574df1761f499f5910f51b072d601fdfde904d98d161262414ff6b6d9e9d2eb5",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab10](../00c5a/00c5ab10.md)
- [00c5ab30](../00c5a/00c5ab30.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1113 bytes

~~~c

void _ZN8firebase13remote_config8internal19throttled_exception14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126238 == 0) {
    DAT_01126238 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException"
                              ,0);
  }
                    /* catch() { ... } // from try @ 00bc299c with catch @ 00bc2d20 */
                    /* catch() { ... } // from try @ 00bc2890 with catch @ 00bc2d24 */
                    /* catch() { ... } // from try @ 00bc275c with catch @ 00bc2d28 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126238,&PTR_s_getThrottleEndTimeMillis_00c91388,1,&DAT_01126248,
             "com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc2cbc"></a> `00bc2cbc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bc2cc0"></a> `00bc2cc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2cc4"></a> `00bc2cc4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bc2cc8"></a> `00bc2cc8` | `34 2b 00 90` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bc2ccc"></a> `00bc2ccc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bc2cd0"></a> `00bc2cd0` | `81 1e 41 f9` | ldr x1,[x20, #0x238] | `FALL_THROUGH`
<a id="insn-00bc2cd4"></a> `00bc2cd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc2cd8"></a> `00bc2cd8` | `41 01 00 b5` | cbnz x1,0x00bc2d00 | `CONDITIONAL_JUMP`
<a id="insn-00bc2cdc"></a> `00bc2cdc` | `a3 b7 ff f0` | adrp x3,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bc2ce0"></a> `00bc2ce0` | `63 a0 2f 91` | add x3,x3,#0xbe8 | `FALL_THROUGH`
<a id="insn-00bc2ce4"></a> `00bc2ce4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc2ce8"></a> `00bc2ce8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bc2cec"></a> `00bc2cec` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bc2cf0"></a> `00bc2cf0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bc2cf4"></a> `00bc2cf4` | `87 5f 02 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bc2cf8"></a> `00bc2cf8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bc2cfc"></a> `00bc2cfc` | `80 1e 01 f9` | str x0,[x20, #0x238] | `FALL_THROUGH`
<a id="insn-00bc2d00"></a> `00bc2d00` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2d04"></a> `00bc2d04` | `62 06 00 f0` | adrp x2,0xc91000 | `FALL_THROUGH`
<a id="insn-00bc2d08"></a> `00bc2d08` | `24 2b 00 90` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bc2d0c"></a> `00bc2d0c` | `a5 b7 ff f0` | adrp x5,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bc2d10"></a> `00bc2d10` | `42 20 0e 91` | add x2,x2,#0x388 | `FALL_THROUGH`
<a id="insn-00bc2d14"></a> `00bc2d14` | `84 20 09 91` | add x4,x4,#0x248 | `FALL_THROUGH`
<a id="insn-00bc2d18"></a> `00bc2d18` | `a5 a0 2f 91` | add x5,x5,#0xbe8 | `FALL_THROUGH`
<a id="insn-00bc2d1c"></a> `00bc2d1c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bc2d20"></a> `00bc2d20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc2d24"></a> `00bc2d24` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bc2d28"></a> `00bc2d28` | `82 5f 02 14` | b 0x00c5ab30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc2cbc`](#insn-00bc2cbc) 範囲 `[['00bc2cbc', '00bc2cdb']]`
  - `CONDITIONAL_JUMP` [`00bc2cd8`](#insn-00bc2cd8) → [`00bc2d00`](#insn-00bc2d00)
  - `FALL_THROUGH` [`00bc2cd8`](#insn-00bc2cd8) → [`00bc2cdc`](#insn-00bc2cdc)
- ブロック [`00bc2cdc`](#insn-00bc2cdc) 範囲 `[['00bc2cdc', '00bc2cff']]`
  - `FALL_THROUGH` [`00bc2cfc`](#insn-00bc2cfc) → [`00bc2d00`](#insn-00bc2d00)
- ブロック [`00bc2d00`](#insn-00bc2d00) 範囲 `[['00bc2d00', '00bc2d1f']]`
  - `FALL_THROUGH` [`00bc2d1c`](#insn-00bc2d1c) → [`00bc2d20`](#insn-00bc2d20)
- ブロック [`00bc2d20`](#insn-00bc2d20) 範囲 `[['00bc2d20', '00bc2d23']]`
  - `FALL_THROUGH` [`00bc2d20`](#insn-00bc2d20) → [`00bc2d24`](#insn-00bc2d24)
- ブロック [`00bc2d24`](#insn-00bc2d24) 範囲 `[['00bc2d24', '00bc2d27']]`
  - `FALL_THROUGH` [`00bc2d24`](#insn-00bc2d24) → [`00bc2d28`](#insn-00bc2d28)
- ブロック [`00bc2d28`](#insn-00bc2d28) 範囲 `[['00bc2d28', '00bc2d2b']]`

## 命令位置別の参照

- [`00bc2cbc`](#insn-00bc2cbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2cc0`](#insn-00bc2cc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2cd0`](#insn-00bc2cd0) → `01126238`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc2cd8`](#insn-00bc2cd8) → [`00bc2d00`](#insn-00bc2d00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2ce0`](#insn-00bc2ce0) → `002b9be8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc2cf4`](#insn-00bc2cf4) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bc2cfc`](#insn-00bc2cfc) → `01126238`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc2d00`](#insn-00bc2d00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2d10`](#insn-00bc2d10) → `00c91388`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bc2d14`](#insn-00bc2d14) → `01126248`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc2d18`](#insn-00bc2d18) → `002b9be8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc2d28`](#insn-00bc2d28) → [`00c5ab30`](../00c5a/00c5ab30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc2cbc`](#insn-00bc2cbc)

~~~json
{
  "source": "00bc2cbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2cc0`](#insn-00bc2cc0)

~~~json
{
  "source": "00bc2cc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2cd0`](#insn-00bc2cd0)

~~~json
{
  "source": "00bc2cd0",
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
- 参照命令 [`00bc2cd8`](#insn-00bc2cd8)

~~~json
{
  "source": "00bc2cd8",
  "target": "00bc2d00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2ce0`](#insn-00bc2ce0)

~~~json
{
  "source": "00bc2ce0",
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
- 参照命令 [`00bc2cf4`](#insn-00bc2cf4)

~~~json
{
  "source": "00bc2cf4",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc2cfc`](#insn-00bc2cfc)

~~~json
{
  "source": "00bc2cfc",
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
- 参照命令 [`00bc2d00`](#insn-00bc2d00)

~~~json
{
  "source": "00bc2d00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2d10`](#insn-00bc2d10)

~~~json
{
  "source": "00bc2d10",
  "target": "00c91388",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91388",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc2d14`](#insn-00bc2d14)

~~~json
{
  "source": "00bc2d14",
  "target": "01126248",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126248",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc2d18`](#insn-00bc2d18)

~~~json
{
  "source": "00bc2d18",
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
- 参照命令 [`00bc2d28`](#insn-00bc2d28)

~~~json
{
  "source": "00bc2d28",
  "target": "00c5ab30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
