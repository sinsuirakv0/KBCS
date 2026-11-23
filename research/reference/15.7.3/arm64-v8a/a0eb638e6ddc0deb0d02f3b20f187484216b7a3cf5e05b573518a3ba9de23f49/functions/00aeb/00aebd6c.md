# 00aebd6c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aebca4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebca4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-a5a2174ccaeb00e99dd3c05601fd8b82)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aebdb0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebdb0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-72c609ae4c6259c464a072b538e40051)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebd6c",
  "name": "_ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "69f446d3ee61c918e186657eac8fb03a53e1f76b5c131d1c89b0b297881c4c13",
  "source_text_sha256": "69f446d3ee61c918e186657eac8fb03a53e1f76b5c131d1c89b0b297881c4c13",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebd6c",
        "00aebddb"
      ]
    ],
    "bytes_sha256": "a57160fc19872316eb53a4a1efbb05fc227153b32faf8a9c4557799b5ffcb108",
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

- [00bde040](../00bde/00bde040.md)
- [00bde060](../00bde/00bde060.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Iterator"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 612 bytes

~~~c

void _ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a08b8 == 0) {
    DAT_010a08b8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Iterator",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a08b8,&PTR_s_hasNext_00c10440,2,&DAT_010a08c8,"java/util/Iterator");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebd6c"></a> `00aebd6c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebd70"></a> `00aebd70` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebd74"></a> `00aebd74` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebd78"></a> `00aebd78` | `b4 2d 00 b0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebd7c"></a> `00aebd7c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aebd80"></a> `00aebd80` | `81 5e 44 f9` | ldr x1,[x20, #0x8b8] | `FALL_THROUGH`
<a id="insn-00aebd84"></a> `00aebd84` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aebd88"></a> `00aebd88` | `41 01 00 b5` | cbnz x1,0x00aebdb0 | `CONDITIONAL_JUMP`
<a id="insn-00aebd8c"></a> `00aebd8c` | `63 bd ff 90` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aebd90"></a> `00aebd90` | `63 9c 15 91` | add x3,x3,#0x567 | `FALL_THROUGH`
<a id="insn-00aebd94"></a> `00aebd94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebd98"></a> `00aebd98` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aebd9c"></a> `00aebd9c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aebda0"></a> `00aebda0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aebda4"></a> `00aebda4` | `a7 c8 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aebda8"></a> `00aebda8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aebdac"></a> `00aebdac` | `80 5e 04 f9` | str x0,[x20, #0x8b8] | `FALL_THROUGH`
<a id="insn-00aebdb0"></a> `00aebdb0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebdb4"></a> `00aebdb4` | `22 09 00 b0` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aebdb8"></a> `00aebdb8` | `a4 2d 00 b0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebdbc"></a> `00aebdbc` | `65 bd ff 90` | adrp x5,0x297000 | `FALL_THROUGH`
<a id="insn-00aebdc0"></a> `00aebdc0` | `42 00 11 91` | add x2,x2,#0x440 | `FALL_THROUGH`
<a id="insn-00aebdc4"></a> `00aebdc4` | `84 20 23 91` | add x4,x4,#0x8c8 | `FALL_THROUGH`
<a id="insn-00aebdc8"></a> `00aebdc8` | `a5 9c 15 91` | add x5,x5,#0x567 | `FALL_THROUGH`
<a id="insn-00aebdcc"></a> `00aebdcc` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00aebdd0"></a> `00aebdd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebdd4"></a> `00aebdd4` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebdd8"></a> `00aebdd8` | `a2 c8 03 14` | b 0x00bde060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebd6c`](#insn-00aebd6c) 範囲 `[['00aebd6c', '00aebd8b']]`
  - `CONDITIONAL_JUMP` [`00aebd88`](#insn-00aebd88) → [`00aebdb0`](#insn-00aebdb0)
  - `FALL_THROUGH` [`00aebd88`](#insn-00aebd88) → [`00aebd8c`](#insn-00aebd8c)
- ブロック [`00aebd8c`](#insn-00aebd8c) 範囲 `[['00aebd8c', '00aebdaf']]`
  - `FALL_THROUGH` [`00aebdac`](#insn-00aebdac) → [`00aebdb0`](#insn-00aebdb0)
- ブロック [`00aebdb0`](#insn-00aebdb0) 範囲 `[['00aebdb0', '00aebddb']]`

## 命令位置別の参照

- [`00aebd6c`](#insn-00aebd6c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebd70`](#insn-00aebd70) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebd80`](#insn-00aebd80) → `010a08b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebd88`](#insn-00aebd88) → [`00aebdb0`](#insn-00aebdb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebd90`](#insn-00aebd90) → `00297567`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebda4`](#insn-00aebda4) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aebdac`](#insn-00aebdac) → `010a08b8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebdb0`](#insn-00aebdb0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebdc0`](#insn-00aebdc0) → `00c10440`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aebdc4`](#insn-00aebdc4) → `010a08c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebdc8`](#insn-00aebdc8) → `00297567`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebdd8`](#insn-00aebdd8) → [`00bde060`](../00bde/00bde060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebd6c`](#insn-00aebd6c)

~~~json
{
  "source": "00aebd6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebd70`](#insn-00aebd70)

~~~json
{
  "source": "00aebd70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebd80`](#insn-00aebd80)

~~~json
{
  "source": "00aebd80",
  "target": "010a08b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebd88`](#insn-00aebd88)

~~~json
{
  "source": "00aebd88",
  "target": "00aebdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebd90`](#insn-00aebd90)

~~~json
{
  "source": "00aebd90",
  "target": "00297567",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00297567",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4974657261746f7200",
  "capture_start": "00297567",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebda4`](#insn-00aebda4)

~~~json
{
  "source": "00aebda4",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebdac`](#insn-00aebdac)

~~~json
{
  "source": "00aebdac",
  "target": "010a08b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebdb0`](#insn-00aebdb0)

~~~json
{
  "source": "00aebdb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebdc0`](#insn-00aebdc0)

~~~json
{
  "source": "00aebdc0",
  "target": "00c10440",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10440",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aebdc4`](#insn-00aebdc4)

~~~json
{
  "source": "00aebdc4",
  "target": "010a08c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebdc8`](#insn-00aebdc8)

~~~json
{
  "source": "00aebdc8",
  "target": "00297567",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00297567",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4974657261746f7200",
  "capture_start": "00297567",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebdd8`](#insn-00aebdd8)

~~~json
{
  "source": "00aebdd8",
  "target": "00bde060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
