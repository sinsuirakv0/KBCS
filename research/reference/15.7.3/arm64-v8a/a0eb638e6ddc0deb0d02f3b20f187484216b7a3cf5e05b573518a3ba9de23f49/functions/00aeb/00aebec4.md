# 00aebec4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aebdfc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebdfc.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-866755f86d2235d45bb96c497792dfc1)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aebf08`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf08.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-221095e702f65960a28f760f4a04bdd0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebec4",
  "name": "_ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5b27075d0de3a83b92ac9c9a355d8907a917a5fdb49ef909bda9947dbf0c5f08",
  "source_text_sha256": "5b27075d0de3a83b92ac9c9a355d8907a917a5fdb49ef909bda9947dbf0c5f08",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebec4",
        "00aebf03"
      ]
    ],
    "bytes_sha256": "b197b86481d47e760e1feb9403c15d1bb62444a501b0b3ea4bdf2c25e6cd38ba",
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
"java/util/List"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 446 bytes

~~~c

long _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a08e0 == 0) {
    DAT_010a08e0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a08e0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebec4"></a> `00aebec4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebec8"></a> `00aebec8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebecc"></a> `00aebecc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebed0"></a> `00aebed0` | `b3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebed4"></a> `00aebed4` | `68 72 44 f9` | ldr x8,[x19, #0x8e0] | `FALL_THROUGH`
<a id="insn-00aebed8"></a> `00aebed8` | `e8 00 00 b5` | cbnz x8,0x00aebef4 | `CONDITIONAL_JUMP`
<a id="insn-00aebedc"></a> `00aebedc` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00aebee0"></a> `00aebee0` | `23 bd ff b0` | adrp x3,0x290000 | `FALL_THROUGH`
<a id="insn-00aebee4"></a> `00aebee4` | `63 14 0e 91` | add x3,x3,#0x385 | `FALL_THROUGH`
<a id="insn-00aebee8"></a> `00aebee8` | `56 c8 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aebeec"></a> `00aebeec` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aebef0"></a> `00aebef0` | `60 72 04 f9` | str x0,[x19, #0x8e0] | `FALL_THROUGH`
<a id="insn-00aebef4"></a> `00aebef4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebef8"></a> `00aebef8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aebefc"></a> `00aebefc` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebf00"></a> `00aebf00` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebec4`](#insn-00aebec4) 範囲 `[['00aebec4', '00aebedb']]`
  - `CONDITIONAL_JUMP` [`00aebed8`](#insn-00aebed8) → [`00aebef4`](#insn-00aebef4)
  - `FALL_THROUGH` [`00aebed8`](#insn-00aebed8) → [`00aebedc`](#insn-00aebedc)
- ブロック [`00aebedc`](#insn-00aebedc) 範囲 `[['00aebedc', '00aebef3']]`
  - `FALL_THROUGH` [`00aebef0`](#insn-00aebef0) → [`00aebef4`](#insn-00aebef4)
- ブロック [`00aebef4`](#insn-00aebef4) 範囲 `[['00aebef4', '00aebf03']]`

## 命令位置別の参照

- [`00aebec4`](#insn-00aebec4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebec8`](#insn-00aebec8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebed4`](#insn-00aebed4) → `010a08e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebed8`](#insn-00aebed8) → [`00aebef4`](#insn-00aebef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebee4`](#insn-00aebee4) → `00290385`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebee8`](#insn-00aebee8) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aebef0`](#insn-00aebef0) → `010a08e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebef4`](#insn-00aebef4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebec4`](#insn-00aebec4)

~~~json
{
  "source": "00aebec4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebec8`](#insn-00aebec8)

~~~json
{
  "source": "00aebec8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebed4`](#insn-00aebed4)

~~~json
{
  "source": "00aebed4",
  "target": "010a08e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebed8`](#insn-00aebed8)

~~~json
{
  "source": "00aebed8",
  "target": "00aebef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebee4`](#insn-00aebee4)

~~~json
{
  "source": "00aebee4",
  "target": "00290385",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290385",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4c69737400",
  "capture_start": "00290385",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebee8`](#insn-00aebee8)

~~~json
{
  "source": "00aebee8",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebef0`](#insn-00aebef0)

~~~json
{
  "source": "00aebef0",
  "target": "010a08e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebef4`](#insn-00aebef4)

~~~json
{
  "source": "00aebef4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
