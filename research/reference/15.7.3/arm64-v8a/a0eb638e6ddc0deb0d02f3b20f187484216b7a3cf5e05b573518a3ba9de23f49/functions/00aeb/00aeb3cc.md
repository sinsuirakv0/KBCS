# 00aeb3cc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aeb304`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb304.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-21ea23306575bfd2264d420629e79faa)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeb410`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb410.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-d92e264944b8dac2374d09e1e5e62187)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeb3cc",
  "name": "_ZN8firebase4util6intent19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e1daaba76ddcdf1f841e00d5dfdd896dd46968120c003a852c7d25d343ead70a",
  "source_text_sha256": "e1daaba76ddcdf1f841e00d5dfdd896dd46968120c003a852c7d25d343ead70a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeb3cc",
        "00aeb40b"
      ]
    ],
    "bytes_sha256": "2e4d7d90230bfc5eeb45aa87ed210c1edf74cd4b327a0895af3986d0f949cd04",
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
"android/content/Intent"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 448 bytes

~~~c

long _ZN8firebase4util6intent19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a0858 == 0) {
    DAT_010a0858 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0858;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeb3cc"></a> `00aeb3cc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeb3d0"></a> `00aeb3d0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeb3d4"></a> `00aeb3d4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeb3d8"></a> `00aeb3d8` | `b3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeb3dc"></a> `00aeb3dc` | `68 2e 44 f9` | ldr x8,[x19, #0x858] | `FALL_THROUGH`
<a id="insn-00aeb3e0"></a> `00aeb3e0` | `e8 00 00 b5` | cbnz x8,0x00aeb3fc | `CONDITIONAL_JUMP`
<a id="insn-00aeb3e4"></a> `00aeb3e4` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00aeb3e8"></a> `00aeb3e8` | `43 bd ff 90` | adrp x3,0x293000 | `FALL_THROUGH`
<a id="insn-00aeb3ec"></a> `00aeb3ec` | `63 24 0a 91` | add x3,x3,#0x289 | `FALL_THROUGH`
<a id="insn-00aeb3f0"></a> `00aeb3f0` | `14 cb 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aeb3f4"></a> `00aeb3f4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aeb3f8"></a> `00aeb3f8` | `60 2e 04 f9` | str x0,[x19, #0x858] | `FALL_THROUGH`
<a id="insn-00aeb3fc"></a> `00aeb3fc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeb400"></a> `00aeb400` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aeb404"></a> `00aeb404` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeb408"></a> `00aeb408` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeb3cc`](#insn-00aeb3cc) 範囲 `[['00aeb3cc', '00aeb3e3']]`
  - `CONDITIONAL_JUMP` [`00aeb3e0`](#insn-00aeb3e0) → [`00aeb3fc`](#insn-00aeb3fc)
  - `FALL_THROUGH` [`00aeb3e0`](#insn-00aeb3e0) → [`00aeb3e4`](#insn-00aeb3e4)
- ブロック [`00aeb3e4`](#insn-00aeb3e4) 範囲 `[['00aeb3e4', '00aeb3fb']]`
  - `FALL_THROUGH` [`00aeb3f8`](#insn-00aeb3f8) → [`00aeb3fc`](#insn-00aeb3fc)
- ブロック [`00aeb3fc`](#insn-00aeb3fc) 範囲 `[['00aeb3fc', '00aeb40b']]`

## 命令位置別の参照

- [`00aeb3cc`](#insn-00aeb3cc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb3d0`](#insn-00aeb3d0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb3dc`](#insn-00aeb3dc) → `010a0858`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeb3e0`](#insn-00aeb3e0) → [`00aeb3fc`](#insn-00aeb3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb3ec`](#insn-00aeb3ec) → `00293289`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeb3f0`](#insn-00aeb3f0) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aeb3f8`](#insn-00aeb3f8) → `010a0858`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeb3fc`](#insn-00aeb3fc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeb3cc`](#insn-00aeb3cc)

~~~json
{
  "source": "00aeb3cc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb3d0`](#insn-00aeb3d0)

~~~json
{
  "source": "00aeb3d0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb3dc`](#insn-00aeb3dc)

~~~json
{
  "source": "00aeb3dc",
  "target": "010a0858",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0858",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeb3e0`](#insn-00aeb3e0)

~~~json
{
  "source": "00aeb3e0",
  "target": "00aeb3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb3ec`](#insn-00aeb3ec)

~~~json
{
  "source": "00aeb3ec",
  "target": "00293289",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00293289",
  "offset": 0,
  "size": 23,
  "datatype": "string",
  "bytes": "616e64726f69642f636f6e74656e742f496e74656e7400",
  "capture_start": "00293289",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeb3f0`](#insn-00aeb3f0)

~~~json
{
  "source": "00aeb3f0",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeb3f8`](#insn-00aeb3f8)

~~~json
{
  "source": "00aeb3f8",
  "target": "010a0858",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0858",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeb3fc`](#insn-00aeb3fc)

~~~json
{
  "source": "00aeb3fc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
