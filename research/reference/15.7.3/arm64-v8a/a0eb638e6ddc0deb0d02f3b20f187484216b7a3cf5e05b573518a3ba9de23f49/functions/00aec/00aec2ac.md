# 00aec2ac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aec1e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec1e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-0a8bed3c4165d40d6aafd0e7272f47a4)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aec2f0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2f0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-d5f89b09a3719943846c184fdacdce76)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aec2ac",
  "name": "_ZN8firebase4util10long_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6dba2088dcc5dcbcad51580779941ca699e3adaf355fa4e89d3b720a208f8aac",
  "source_text_sha256": "6dba2088dcc5dcbcad51580779941ca699e3adaf355fa4e89d3b720a208f8aac",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aec2ac",
        "00aec2eb"
      ]
    ],
    "bytes_sha256": "5ad23dc94822602ee7c8cbb9b4772ecedb13237b7d57e93720a95ff0724de4ba",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
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

## 疑似コード / UTF-8 430 bytes

~~~c

long _ZN8firebase4util10long_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a0910 == 0) {
    DAT_010a0910 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0910;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aec2ac"></a> `00aec2ac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aec2b0"></a> `00aec2b0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec2b4"></a> `00aec2b4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aec2b8"></a> `00aec2b8` | `b3 2d 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aec2bc"></a> `00aec2bc` | `68 8a 44 f9` | ldr x8,[x19, #0x910] | `FALL_THROUGH`
<a id="insn-00aec2c0"></a> `00aec2c0` | `e8 00 00 b5` | cbnz x8,0x00aec2dc | `CONDITIONAL_JUMP`
<a id="insn-00aec2c4"></a> `00aec2c4` | `c3 bd ff f0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aec2c8"></a> `00aec2c8` | `63 58 35 91` | add x3,x3,#0xd56 | `FALL_THROUGH`
<a id="insn-00aec2cc"></a> `00aec2cc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aec2d0"></a> `00aec2d0` | `5c c7 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aec2d4"></a> `00aec2d4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aec2d8"></a> `00aec2d8` | `60 8a 04 f9` | str x0,[x19, #0x910] | `FALL_THROUGH`
<a id="insn-00aec2dc"></a> `00aec2dc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec2e0"></a> `00aec2e0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aec2e4"></a> `00aec2e4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aec2e8"></a> `00aec2e8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aec2ac`](#insn-00aec2ac) 範囲 `[['00aec2ac', '00aec2c3']]`
  - `CONDITIONAL_JUMP` [`00aec2c0`](#insn-00aec2c0) → [`00aec2dc`](#insn-00aec2dc)
  - `FALL_THROUGH` [`00aec2c0`](#insn-00aec2c0) → [`00aec2c4`](#insn-00aec2c4)
- ブロック [`00aec2c4`](#insn-00aec2c4) 範囲 `[['00aec2c4', '00aec2db']]`
  - `FALL_THROUGH` [`00aec2d8`](#insn-00aec2d8) → [`00aec2dc`](#insn-00aec2dc)
- ブロック [`00aec2dc`](#insn-00aec2dc) 範囲 `[['00aec2dc', '00aec2eb']]`

## 命令位置別の参照

- [`00aec2ac`](#insn-00aec2ac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec2b0`](#insn-00aec2b0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec2bc`](#insn-00aec2bc) → `010a0910`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec2c0`](#insn-00aec2c0) → [`00aec2dc`](#insn-00aec2dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec2c8`](#insn-00aec2c8) → `002a7d56`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aec2d0`](#insn-00aec2d0) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aec2d8`](#insn-00aec2d8) → `010a0910`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec2dc`](#insn-00aec2dc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aec2ac`](#insn-00aec2ac)

~~~json
{
  "source": "00aec2ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec2b0`](#insn-00aec2b0)

~~~json
{
  "source": "00aec2b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec2bc`](#insn-00aec2bc)

~~~json
{
  "source": "00aec2bc",
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
- 参照命令 [`00aec2c0`](#insn-00aec2c0)

~~~json
{
  "source": "00aec2c0",
  "target": "00aec2dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec2c8`](#insn-00aec2c8)

~~~json
{
  "source": "00aec2c8",
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
- 参照命令 [`00aec2d0`](#insn-00aec2d0)

~~~json
{
  "source": "00aec2d0",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec2d8`](#insn-00aec2d8)

~~~json
{
  "source": "00aec2d8",
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
- 参照命令 [`00aec2dc`](#insn-00aec2dc)

~~~json
{
  "source": "00aec2dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
