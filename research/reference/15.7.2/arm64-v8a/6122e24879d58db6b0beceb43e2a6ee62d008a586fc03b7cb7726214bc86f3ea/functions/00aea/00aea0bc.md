# 00aea0bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aea184`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea184.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-89faadfaec4308dee2a7b0126ede472d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aea0bc",
  "name": "_ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "79d41006d5befa847fe70b9ae60beef9eea03d30da5af284e3e00448697cfc0d",
  "source_text_sha256": "79d41006d5befa847fe70b9ae60beef9eea03d30da5af284e3e00448697cfc0d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aea0bc",
        "00aea0fb"
      ]
    ],
    "bytes_sha256": "40c39248744cba134be85d615f7b86591a2f1e3034065a70f188f716eb00616f",
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

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Enum"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 453 bytes

~~~c

long _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a06a8 == 0) {
    DAT_010a06a8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a06a8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aea0bc"></a> `00aea0bc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aea0c0"></a> `00aea0c0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea0c4"></a> `00aea0c4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aea0c8"></a> `00aea0c8` | `b3 2d 00 d0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aea0cc"></a> `00aea0cc` | `68 56 43 f9` | ldr x8,[x19, #0x6a8] | `FALL_THROUGH`
<a id="insn-00aea0d0"></a> `00aea0d0` | `e8 00 00 b5` | cbnz x8,0x00aea0ec | `CONDITIONAL_JUMP`
<a id="insn-00aea0d4"></a> `00aea0d4` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00aea0d8"></a> `00aea0d8` | `23 be ff d0` | adrp x3,0x2b0000 | `FALL_THROUGH`
<a id="insn-00aea0dc"></a> `00aea0dc` | `63 ec 12 91` | add x3,x3,#0x4bb | `FALL_THROUGH`
<a id="insn-00aea0e0"></a> `00aea0e0` | `ac cf 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aea0e4"></a> `00aea0e4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aea0e8"></a> `00aea0e8` | `60 56 03 f9` | str x0,[x19, #0x6a8] | `FALL_THROUGH`
<a id="insn-00aea0ec"></a> `00aea0ec` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea0f0"></a> `00aea0f0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aea0f4"></a> `00aea0f4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aea0f8"></a> `00aea0f8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aea0bc`](#insn-00aea0bc) 範囲 `[['00aea0bc', '00aea0d3']]`
  - `CONDITIONAL_JUMP` [`00aea0d0`](#insn-00aea0d0) → [`00aea0ec`](#insn-00aea0ec)
  - `FALL_THROUGH` [`00aea0d0`](#insn-00aea0d0) → [`00aea0d4`](#insn-00aea0d4)
- ブロック [`00aea0d4`](#insn-00aea0d4) 範囲 `[['00aea0d4', '00aea0eb']]`
  - `FALL_THROUGH` [`00aea0e8`](#insn-00aea0e8) → [`00aea0ec`](#insn-00aea0ec)
- ブロック [`00aea0ec`](#insn-00aea0ec) 範囲 `[['00aea0ec', '00aea0fb']]`

## 命令位置別の参照

- [`00aea0bc`](#insn-00aea0bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea0c0`](#insn-00aea0c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea0cc`](#insn-00aea0cc) → `010a06a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aea0d0`](#insn-00aea0d0) → [`00aea0ec`](#insn-00aea0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea0dc`](#insn-00aea0dc) → `002b04bb`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aea0e0`](#insn-00aea0e0) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aea0e8`](#insn-00aea0e8) → `010a06a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aea0ec`](#insn-00aea0ec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aea0bc`](#insn-00aea0bc)

~~~json
{
  "source": "00aea0bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea0c0`](#insn-00aea0c0)

~~~json
{
  "source": "00aea0c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea0cc`](#insn-00aea0cc)

~~~json
{
  "source": "00aea0cc",
  "target": "010a06a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a06a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea0d0`](#insn-00aea0d0)

~~~json
{
  "source": "00aea0d0",
  "target": "00aea0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea0dc`](#insn-00aea0dc)

~~~json
{
  "source": "00aea0dc",
  "target": "002b04bb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b04bb",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f456e756d00",
  "capture_start": "002b04bb",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea0e0`](#insn-00aea0e0)

~~~json
{
  "source": "00aea0e0",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea0e8`](#insn-00aea0e8)

~~~json
{
  "source": "00aea0e8",
  "target": "010a06a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a06a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea0ec`](#insn-00aea0ec)

~~~json
{
  "source": "00aea0ec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
