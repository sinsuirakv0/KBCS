# 00aec2ec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aec224`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec224.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-75dec754d4df6e4d494357d79816238e)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aec330`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec330.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-b84e1d130a5ba882ccf7dc9bf85a9cb2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aec2ec",
  "name": "_ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "52b602d034f5cbc90bcc157782cf7c7dfa1d1ad50dd9c60524dcad0efaeb03f5",
  "source_text_sha256": "52b602d034f5cbc90bcc157782cf7c7dfa1d1ad50dd9c60524dcad0efaeb03f5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aec2ec",
        "00aec32f"
      ]
    ],
    "bytes_sha256": "88ce7a894a1dcdae7fbb605a49e9c5b30c3c62cf8cdb8ce3148187dbf59cc18b",
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
"java/lang/Long"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 469 bytes

~~~c

long _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a0910 == 0) {
    DAT_010a0910 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Long",param_3);
  }
  return DAT_010a0910;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aec2ec"></a> `00aec2ec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aec2f0"></a> `00aec2f0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec2f4"></a> `00aec2f4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aec2f8"></a> `00aec2f8` | `b3 2d 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aec2fc"></a> `00aec2fc` | `68 8a 44 f9` | ldr x8,[x19, #0x910] | `FALL_THROUGH`
<a id="insn-00aec300"></a> `00aec300` | `08 01 00 b5` | cbnz x8,0x00aec320 | `CONDITIONAL_JUMP`
<a id="insn-00aec304"></a> `00aec304` | `c3 bd ff f0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aec308"></a> `00aec308` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00aec30c"></a> `00aec30c` | `63 58 35 91` | add x3,x3,#0xd56 | `FALL_THROUGH`
<a id="insn-00aec310"></a> `00aec310` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aec314"></a> `00aec314` | `4b c7 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aec318"></a> `00aec318` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aec31c"></a> `00aec31c` | `60 8a 04 f9` | str x0,[x19, #0x910] | `FALL_THROUGH`
<a id="insn-00aec320"></a> `00aec320` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec324"></a> `00aec324` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aec328"></a> `00aec328` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aec32c"></a> `00aec32c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aec2ec`](#insn-00aec2ec) 範囲 `[['00aec2ec', '00aec303']]`
  - `CONDITIONAL_JUMP` [`00aec300`](#insn-00aec300) → [`00aec320`](#insn-00aec320)
  - `FALL_THROUGH` [`00aec300`](#insn-00aec300) → [`00aec304`](#insn-00aec304)
- ブロック [`00aec304`](#insn-00aec304) 範囲 `[['00aec304', '00aec31f']]`
  - `FALL_THROUGH` [`00aec31c`](#insn-00aec31c) → [`00aec320`](#insn-00aec320)
- ブロック [`00aec320`](#insn-00aec320) 範囲 `[['00aec320', '00aec32f']]`

## 命令位置別の参照

- [`00aec2ec`](#insn-00aec2ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec2f0`](#insn-00aec2f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec2fc`](#insn-00aec2fc) → `010a0910`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec300`](#insn-00aec300) → [`00aec320`](#insn-00aec320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec30c`](#insn-00aec30c) → `002a7d56`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aec314`](#insn-00aec314) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aec31c`](#insn-00aec31c) → `010a0910`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec320`](#insn-00aec320) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aec2ec`](#insn-00aec2ec)

~~~json
{
  "source": "00aec2ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec2f0`](#insn-00aec2f0)

~~~json
{
  "source": "00aec2f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec2fc`](#insn-00aec2fc)

~~~json
{
  "source": "00aec2fc",
  "target": "010a0910",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0910",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec300`](#insn-00aec300)

~~~json
{
  "source": "00aec300",
  "target": "00aec320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec30c`](#insn-00aec30c)

~~~json
{
  "source": "00aec30c",
  "target": "002a7d56",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7d56",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4c6f6e6700",
  "capture_start": "002a7d56",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aec314`](#insn-00aec314)

~~~json
{
  "source": "00aec314",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec31c`](#insn-00aec31c)

~~~json
{
  "source": "00aec31c",
  "target": "010a0910",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0910",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec320`](#insn-00aec320)

~~~json
{
  "source": "00aec320",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
