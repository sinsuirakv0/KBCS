# 00aed8dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aed814`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed814.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-6f8d804cb93e98fe68c87a0275076684)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aed920`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed920.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-d89559accbfc9dbbed8b3c1134aa7d93)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aed8dc",
  "name": "_ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1bb1b8a783e100ff41dc7a417b18d95e120d89082472d74078c7ac112840cb9c",
  "source_text_sha256": "1bb1b8a783e100ff41dc7a417b18d95e120d89082472d74078c7ac112840cb9c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aed8dc",
        "00aed91f"
      ]
    ],
    "bytes_sha256": "ea562866472e6521d49eee6697d88e2206b9298b388e53fcf35680c77fca3a2b",
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
"java/lang/Throwable"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 472 bytes

~~~c

long _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a09f0 == 0) {
    DAT_010a09f0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Throwable",param_3);
  }
  return DAT_010a09f0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aed8dc"></a> `00aed8dc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aed8e0"></a> `00aed8e0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed8e4"></a> `00aed8e4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aed8e8"></a> `00aed8e8` | `93 2d 00 f0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aed8ec"></a> `00aed8ec` | `68 fa 44 f9` | ldr x8,[x19, #0x9f0] | `FALL_THROUGH`
<a id="insn-00aed8f0"></a> `00aed8f0` | `08 01 00 b5` | cbnz x8,0x00aed910 | `CONDITIONAL_JUMP`
<a id="insn-00aed8f4"></a> `00aed8f4` | `c3 bd ff f0` | adrp x3,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aed8f8"></a> `00aed8f8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00aed8fc"></a> `00aed8fc` | `63 28 30 91` | add x3,x3,#0xc0a | `FALL_THROUGH`
<a id="insn-00aed900"></a> `00aed900` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aed904"></a> `00aed904` | `cf c1 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aed908"></a> `00aed908` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aed90c"></a> `00aed90c` | `60 fa 04 f9` | str x0,[x19, #0x9f0] | `FALL_THROUGH`
<a id="insn-00aed910"></a> `00aed910` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed914"></a> `00aed914` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aed918"></a> `00aed918` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aed91c"></a> `00aed91c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aed8dc`](#insn-00aed8dc) 範囲 `[['00aed8dc', '00aed8f3']]`
  - `CONDITIONAL_JUMP` [`00aed8f0`](#insn-00aed8f0) → [`00aed910`](#insn-00aed910)
  - `FALL_THROUGH` [`00aed8f0`](#insn-00aed8f0) → [`00aed8f4`](#insn-00aed8f4)
- ブロック [`00aed8f4`](#insn-00aed8f4) 範囲 `[['00aed8f4', '00aed90f']]`
  - `FALL_THROUGH` [`00aed90c`](#insn-00aed90c) → [`00aed910`](#insn-00aed910)
- ブロック [`00aed910`](#insn-00aed910) 範囲 `[['00aed910', '00aed91f']]`

## 命令位置別の参照

- [`00aed8dc`](#insn-00aed8dc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed8e0`](#insn-00aed8e0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed8ec`](#insn-00aed8ec) → `010a09f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aed8f0`](#insn-00aed8f0) → [`00aed910`](#insn-00aed910) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed8fc`](#insn-00aed8fc) → `002a8c0a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aed904`](#insn-00aed904) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aed90c`](#insn-00aed90c) → `010a09f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aed910`](#insn-00aed910) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aed8dc`](#insn-00aed8dc)

~~~json
{
  "source": "00aed8dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed8e0`](#insn-00aed8e0)

~~~json
{
  "source": "00aed8e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed8ec`](#insn-00aed8ec)

~~~json
{
  "source": "00aed8ec",
  "target": "010a09f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed8f0`](#insn-00aed8f0)

~~~json
{
  "source": "00aed8f0",
  "target": "00aed910",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed8fc`](#insn-00aed8fc)

~~~json
{
  "source": "00aed8fc",
  "target": "002a8c0a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8c0a",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f5468726f7761626c6500",
  "capture_start": "002a8c0a",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aed904`](#insn-00aed904)

~~~json
{
  "source": "00aed904",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed90c`](#insn-00aed90c)

~~~json
{
  "source": "00aed90c",
  "target": "010a09f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed910`](#insn-00aed910)

~~~json
{
  "source": "00aed910",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
