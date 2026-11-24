# 00b4aedc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b4ae98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae98.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0068.md#compare-a8fc8de37841f6b4b34928ac17c57a22)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bb8c00`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c00.md) · 移動量 `+0x6dd24`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0064.md#compare-2273979d204bbe35d1dfabe9492e18e3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4aedc",
  "name": "_ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c343783ae64d748d46c737facda25cfed08608f552bc9f3cbe4eaf2d43d93781",
  "source_text_sha256": "c343783ae64d748d46c737facda25cfed08608f552bc9f3cbe4eaf2d43d93781",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4aedc",
        "00b4af1f"
      ]
    ],
    "bytes_sha256": "43ff2e73de50eb9c1a3e03a2a5629c9376d2c77c759e25b8264a77b35213fbd8",
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
"%PG%com/google/firebase/messaging/cpp/RegistrationIntentService"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1344 bytes

~~~c

long _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00b4ae3c with catch @ 00b4aedc
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00b4ae1c with catch @ 00b4aee0
                        */
  if (DAT_010a1058 == 0) {
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00b4adf8 with catch @ 00b4aef8
                        */
    DAT_010a1058 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/messaging/cpp/RegistrationIntentService",param_3)
    ;
  }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00b4add4 with catch @ 00b4af10
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00b4ae84 with catch @ 00b4af18
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00b4ae54 with catch @ 00b4af1c
                        */
  return DAT_010a1058;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4aedc"></a> `00b4aedc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4aee0"></a> `00b4aee0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4aee4"></a> `00b4aee4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4aee8"></a> `00b4aee8` | `b3 2a 00 f0` | adrp x19,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b4aeec"></a> `00b4aeec` | `68 2e 40 f9` | ldr x8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00b4aef0"></a> `00b4aef0` | `08 01 00 b5` | cbnz x8,0x00b4af10 | `CONDITIONAL_JUMP`
<a id="insn-00b4aef4"></a> `00b4aef4` | `e3 ba ff d0` | adrp x3,0x2a8000 | `FALL_THROUGH`
<a id="insn-00b4aef8"></a> `00b4aef8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00b4aefc"></a> `00b4aefc` | `63 80 3a 91` | add x3,x3,#0xea0 | `FALL_THROUGH`
<a id="insn-00b4af00"></a> `00b4af00` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b4af04"></a> `00b4af04` | `63 4c 02 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4af08"></a> `00b4af08` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b4af0c"></a> `00b4af0c` | `60 2e 00 f9` | str x0,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00b4af10"></a> `00b4af10` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4af14"></a> `00b4af14` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4af18"></a> `00b4af18` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4af1c"></a> `00b4af1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4aedc`](#insn-00b4aedc) 範囲 `[['00b4aedc', '00b4aedf']]`
  - `FALL_THROUGH` [`00b4aedc`](#insn-00b4aedc) → [`00b4aee0`](#insn-00b4aee0)
- ブロック [`00b4aee0`](#insn-00b4aee0) 範囲 `[['00b4aee0', '00b4aef3']]`
  - `CONDITIONAL_JUMP` [`00b4aef0`](#insn-00b4aef0) → [`00b4af10`](#insn-00b4af10)
  - `FALL_THROUGH` [`00b4aef0`](#insn-00b4aef0) → [`00b4aef4`](#insn-00b4aef4)
- ブロック [`00b4aef4`](#insn-00b4aef4) 範囲 `[['00b4aef4', '00b4aef7']]`
  - `FALL_THROUGH` [`00b4aef4`](#insn-00b4aef4) → [`00b4aef8`](#insn-00b4aef8)
- ブロック [`00b4aef8`](#insn-00b4aef8) 範囲 `[['00b4aef8', '00b4af0f']]`
  - `FALL_THROUGH` [`00b4af0c`](#insn-00b4af0c) → [`00b4af10`](#insn-00b4af10)
- ブロック [`00b4af10`](#insn-00b4af10) 範囲 `[['00b4af10', '00b4af17']]`
  - `FALL_THROUGH` [`00b4af14`](#insn-00b4af14) → [`00b4af18`](#insn-00b4af18)
- ブロック [`00b4af18`](#insn-00b4af18) 範囲 `[['00b4af18', '00b4af1b']]`
  - `FALL_THROUGH` [`00b4af18`](#insn-00b4af18) → [`00b4af1c`](#insn-00b4af1c)
- ブロック [`00b4af1c`](#insn-00b4af1c) 範囲 `[['00b4af1c', '00b4af1f']]`

## 命令位置別の参照

- [`00b4aedc`](#insn-00b4aedc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aee0`](#insn-00b4aee0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aeec`](#insn-00b4aeec) → `010a1058`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4aef0`](#insn-00b4aef0) → [`00b4af10`](#insn-00b4af10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aefc`](#insn-00b4aefc) → `002a8ea0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4af04`](#insn-00b4af04) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00b4af0c`](#insn-00b4af0c) → `010a1058`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4af10`](#insn-00b4af10) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4aedc`](#insn-00b4aedc)

~~~json
{
  "source": "00b4aedc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aee0`](#insn-00b4aee0)

~~~json
{
  "source": "00b4aee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aeec`](#insn-00b4aeec)

~~~json
{
  "source": "00b4aeec",
  "target": "010a1058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1058",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4aef0`](#insn-00b4aef0)

~~~json
{
  "source": "00b4aef0",
  "target": "00b4af10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aefc`](#insn-00b4aefc)

~~~json
{
  "source": "00b4aefc",
  "target": "002a8ea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8e9c",
  "offset": 4,
  "size": 64,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f6d6573736167696e",
  "capture_start": "002a8e9c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b4af04`](#insn-00b4af04)

~~~json
{
  "source": "00b4af04",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4af0c`](#insn-00b4af0c)

~~~json
{
  "source": "00b4af0c",
  "target": "010a1058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1058",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4af10`](#insn-00b4af10)

~~~json
{
  "source": "00b4af10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
