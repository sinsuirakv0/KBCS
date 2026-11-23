# 00ae7cac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae7d74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7d74.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0059.md#compare-9e5f8d508abe0e9f7716ab27bcaedb75)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae7cac",
  "name": "_ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "20aedbcdd840631dc89cb6100e882e4a166023c8198884646e429365434d0316",
  "source_text_sha256": "20aedbcdd840631dc89cb6100e882e4a166023c8198884646e429365434d0316",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae7cac",
        "00ae7cef"
      ]
    ],
    "bytes_sha256": "110ce1bd4c5a87b04e54a21f9176ca137e6c831a6e0221bd1ca3b0c64f665a5d",
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

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Boolean"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 475 bytes

~~~c

long _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a04c0 == 0) {
    DAT_010a04c0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Boolean",param_3);
  }
  return DAT_010a04c0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae7cac"></a> `00ae7cac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae7cb0"></a> `00ae7cb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae7cb4"></a> `00ae7cb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae7cb8"></a> `00ae7cb8` | `d3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae7cbc"></a> `00ae7cbc` | `68 62 42 f9` | ldr x8,[x19, #0x4c0] | `FALL_THROUGH`
<a id="insn-00ae7cc0"></a> `00ae7cc0` | `08 01 00 b5` | cbnz x8,0x00ae7ce0 | `CONDITIONAL_JUMP`
<a id="insn-00ae7cc4"></a> `00ae7cc4` | `83 bd ff b0` | adrp x3,0x298000 | `FALL_THROUGH`
<a id="insn-00ae7cc8"></a> `00ae7cc8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00ae7ccc"></a> `00ae7ccc` | `63 70 17 91` | add x3,x3,#0x5dc | `FALL_THROUGH`
<a id="insn-00ae7cd0"></a> `00ae7cd0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ae7cd4"></a> `00ae7cd4` | `af d8 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00ae7cd8"></a> `00ae7cd8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ae7cdc"></a> `00ae7cdc` | `60 62 02 f9` | str x0,[x19, #0x4c0] | `FALL_THROUGH`
<a id="insn-00ae7ce0"></a> `00ae7ce0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae7ce4"></a> `00ae7ce4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00ae7ce8"></a> `00ae7ce8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae7cec"></a> `00ae7cec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae7cac`](#insn-00ae7cac) 範囲 `[['00ae7cac', '00ae7cc3']]`
  - `CONDITIONAL_JUMP` [`00ae7cc0`](#insn-00ae7cc0) → [`00ae7ce0`](#insn-00ae7ce0)
  - `FALL_THROUGH` [`00ae7cc0`](#insn-00ae7cc0) → [`00ae7cc4`](#insn-00ae7cc4)
- ブロック [`00ae7cc4`](#insn-00ae7cc4) 範囲 `[['00ae7cc4', '00ae7cdf']]`
  - `FALL_THROUGH` [`00ae7cdc`](#insn-00ae7cdc) → [`00ae7ce0`](#insn-00ae7ce0)
- ブロック [`00ae7ce0`](#insn-00ae7ce0) 範囲 `[['00ae7ce0', '00ae7cef']]`

## 命令位置別の参照

- [`00ae7cac`](#insn-00ae7cac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7cb0`](#insn-00ae7cb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7cbc`](#insn-00ae7cbc) → `010a04c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae7cc0`](#insn-00ae7cc0) → [`00ae7ce0`](#insn-00ae7ce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7ccc`](#insn-00ae7ccc) → `002985dc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae7cd4`](#insn-00ae7cd4) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00ae7cdc`](#insn-00ae7cdc) → `010a04c0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae7ce0`](#insn-00ae7ce0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae7cac`](#insn-00ae7cac)

~~~json
{
  "source": "00ae7cac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7cb0`](#insn-00ae7cb0)

~~~json
{
  "source": "00ae7cb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7cbc`](#insn-00ae7cbc)

~~~json
{
  "source": "00ae7cbc",
  "target": "010a04c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a04c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7cc0`](#insn-00ae7cc0)

~~~json
{
  "source": "00ae7cc0",
  "target": "00ae7ce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7ccc`](#insn-00ae7ccc)

~~~json
{
  "source": "00ae7ccc",
  "target": "002985dc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002985dc",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f426f6f6c65616e00",
  "capture_start": "002985dc",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae7cd4`](#insn-00ae7cd4)

~~~json
{
  "source": "00ae7cd4",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae7cdc`](#insn-00ae7cdc)

~~~json
{
  "source": "00ae7cdc",
  "target": "010a04c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a04c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7ce0`](#insn-00ae7ce0)

~~~json
{
  "source": "00ae7ce0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
