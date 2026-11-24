# 00aedff0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aedfac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfac.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-d3e3f07bd416bf04def6c7b531e0827c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4dd74`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dd74.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-4d845c69d79a0846f4ab343a4cb2e507)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedff0",
  "name": "_ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5df0ac4785c72da4cbb49aaecfc9eaed3522ab4fa9ba714c25d856e9001e5422",
  "source_text_sha256": "5df0ac4785c72da4cbb49aaecfc9eaed3522ab4fa9ba714c25d856e9001e5422",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedff0",
        "00aee02f"
      ]
    ],
    "bytes_sha256": "fb6bdb25ff1ad393e28b896d264361b0cc23622b698335f78d2c9e217ac6952b",
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

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Object"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 448 bytes

~~~c

long _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a0a88 == 0) {
    DAT_010a0a88 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0a88;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedff0"></a> `00aedff0` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedff4"></a> `00aedff4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedff8"></a> `00aedff8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedffc"></a> `00aedffc` | `93 2d 00 f0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aee000"></a> `00aee000` | `68 46 45 f9` | ldr x8,[x19, #0xa88] | `FALL_THROUGH`
<a id="insn-00aee004"></a> `00aee004` | `e8 00 00 b5` | cbnz x8,0x00aee020 | `CONDITIONAL_JUMP`
<a id="insn-00aee008"></a> `00aee008` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00aee00c"></a> `00aee00c` | `63 bd ff f0` | adrp x3,0x29d000 | `FALL_THROUGH`
<a id="insn-00aee010"></a> `00aee010` | `63 dc 37 91` | add x3,x3,#0xdf7 | `FALL_THROUGH`
<a id="insn-00aee014"></a> `00aee014` | `1f c0 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aee018"></a> `00aee018` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aee01c"></a> `00aee01c` | `60 46 05 f9` | str x0,[x19, #0xa88] | `FALL_THROUGH`
<a id="insn-00aee020"></a> `00aee020` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aee024"></a> `00aee024` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aee028"></a> `00aee028` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aee02c"></a> `00aee02c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedff0`](#insn-00aedff0) 範囲 `[['00aedff0', '00aee007']]`
  - `CONDITIONAL_JUMP` [`00aee004`](#insn-00aee004) → [`00aee020`](#insn-00aee020)
  - `FALL_THROUGH` [`00aee004`](#insn-00aee004) → [`00aee008`](#insn-00aee008)
- ブロック [`00aee008`](#insn-00aee008) 範囲 `[['00aee008', '00aee01f']]`
  - `FALL_THROUGH` [`00aee01c`](#insn-00aee01c) → [`00aee020`](#insn-00aee020)
- ブロック [`00aee020`](#insn-00aee020) 範囲 `[['00aee020', '00aee02f']]`

## 命令位置別の参照

- [`00aedff0`](#insn-00aedff0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedff4`](#insn-00aedff4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee000`](#insn-00aee000) → `010a0a88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aee004`](#insn-00aee004) → [`00aee020`](#insn-00aee020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee010`](#insn-00aee010) → `0029ddf7`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aee014`](#insn-00aee014) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aee01c`](#insn-00aee01c) → `010a0a88`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aee020`](#insn-00aee020) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedff0`](#insn-00aedff0)

~~~json
{
  "source": "00aedff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedff4`](#insn-00aedff4)

~~~json
{
  "source": "00aedff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee000`](#insn-00aee000)

~~~json
{
  "source": "00aee000",
  "target": "010a0a88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aee004`](#insn-00aee004)

~~~json
{
  "source": "00aee004",
  "target": "00aee020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee010`](#insn-00aee010)

~~~json
{
  "source": "00aee010",
  "target": "0029ddf7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ddf7",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4f626a65637400",
  "capture_start": "0029ddf7",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aee014`](#insn-00aee014)

~~~json
{
  "source": "00aee014",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aee01c`](#insn-00aee01c)

~~~json
{
  "source": "00aee01c",
  "target": "010a0a88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aee020`](#insn-00aee020)

~~~json
{
  "source": "00aee020",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
