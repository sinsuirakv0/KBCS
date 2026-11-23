# 00b4aedc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b4ae14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ae14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0067.md#compare-5088843bf4930a5130a3c6e470c9399a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b4af20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4af20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0068.md#compare-a27eb4d450cad2f10090bc90b4df768d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4aedc",
  "name": "_ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e537aa33ca5a87f6e85f5d4f62501a622c77413f88ec28b6b4f98259c496a1d9",
  "source_text_sha256": "e537aa33ca5a87f6e85f5d4f62501a622c77413f88ec28b6b4f98259c496a1d9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4aedc",
        "00b4af1f"
      ]
    ],
    "bytes_sha256": "c3f8717de4284476e7abf9f568191c11c891b2dbe4aa14e5439f1431e3d7f8bd",
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
"%PG%com/google/firebase/messaging/cpp/RegistrationIntentService"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 519 bytes

~~~c

long _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a1018 == 0) {
    DAT_010a1018 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/messaging/cpp/RegistrationIntentService",0);
  }
  return DAT_010a1018;
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
<a id="insn-00b4aeec"></a> `00b4aeec` | `68 0e 40 f9` | ldr x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b4aef0"></a> `00b4aef0` | `08 01 00 b5` | cbnz x8,0x00b4af10 | `CONDITIONAL_JUMP`
<a id="insn-00b4aef4"></a> `00b4aef4` | `e3 ba ff d0` | adrp x3,0x2a8000 | `FALL_THROUGH`
<a id="insn-00b4aef8"></a> `00b4aef8` | `63 18 38 91` | add x3,x3,#0xe06 | `FALL_THROUGH`
<a id="insn-00b4aefc"></a> `00b4aefc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b4af00"></a> `00b4af00` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b4af04"></a> `00b4af04` | `4f 4c 02 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00b4af08"></a> `00b4af08` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b4af0c"></a> `00b4af0c` | `60 0e 00 f9` | str x0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b4af10"></a> `00b4af10` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4af14"></a> `00b4af14` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4af18"></a> `00b4af18` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4af1c"></a> `00b4af1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4aedc`](#insn-00b4aedc) 範囲 `[['00b4aedc', '00b4aef3']]`
  - `CONDITIONAL_JUMP` [`00b4aef0`](#insn-00b4aef0) → [`00b4af10`](#insn-00b4af10)
  - `FALL_THROUGH` [`00b4aef0`](#insn-00b4aef0) → [`00b4aef4`](#insn-00b4aef4)
- ブロック [`00b4aef4`](#insn-00b4aef4) 範囲 `[['00b4aef4', '00b4af0f']]`
  - `FALL_THROUGH` [`00b4af0c`](#insn-00b4af0c) → [`00b4af10`](#insn-00b4af10)
- ブロック [`00b4af10`](#insn-00b4af10) 範囲 `[['00b4af10', '00b4af1f']]`

## 命令位置別の参照

- [`00b4aedc`](#insn-00b4aedc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aee0`](#insn-00b4aee0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aeec`](#insn-00b4aeec) → `010a1018`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4aef0`](#insn-00b4aef0) → [`00b4af10`](#insn-00b4af10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aef8`](#insn-00b4aef8) → `002a8e06`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4af04`](#insn-00b4af04) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00b4af0c`](#insn-00b4af0c) → `010a1018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
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
  "target": "010a1018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1018",
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
- 参照命令 [`00b4aef8`](#insn-00b4aef8)

~~~json
{
  "source": "00b4aef8",
  "target": "002a8e06",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8e02",
  "offset": 4,
  "size": 64,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f6d6573736167696e",
  "capture_start": "002a8e02",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b4af04`](#insn-00b4af04)

~~~json
{
  "source": "00b4af04",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4af0c`](#insn-00b4af0c)

~~~json
{
  "source": "00b4af0c",
  "target": "010a1018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1018",
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
