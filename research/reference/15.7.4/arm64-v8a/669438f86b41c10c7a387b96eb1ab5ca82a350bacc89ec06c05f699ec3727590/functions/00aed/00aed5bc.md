# 00aed5bc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aed578`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed578.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-1ea9de5d2dd31a492bb31c0de0c77009)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4d340`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d340.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-5a5b82c85ed685064c6d0b5b2eccfbd4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aed5bc",
  "name": "_ZN8firebase4util6string10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "29f3f1c4209129c0b249cf0cb4d272734282fc008f65d7bb09ad4f8ac968ed78",
  "source_text_sha256": "29f3f1c4209129c0b249cf0cb4d272734282fc008f65d7bb09ad4f8ac968ed78",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aed5bc",
        "00aed5ff"
      ]
    ],
    "bytes_sha256": "be05c0a7c5b5f5bd9fa6397ffe191b2373aac46d4bf3dbdf94c539cc42478a77",
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

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/String"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 402 bytes

~~~c

long _ZN8firebase4util6string10CacheClassEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0a10 == 0) {
    DAT_010a0a10 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/String",0);
  }
  return DAT_010a0a10;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aed5bc"></a> `00aed5bc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aed5c0"></a> `00aed5c0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed5c4"></a> `00aed5c4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aed5c8"></a> `00aed5c8` | `93 2d 00 f0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aed5cc"></a> `00aed5cc` | `68 0a 45 f9` | ldr x8,[x19, #0xa10] | `FALL_THROUGH`
<a id="insn-00aed5d0"></a> `00aed5d0` | `08 01 00 b5` | cbnz x8,0x00aed5f0 | `CONDITIONAL_JUMP`
<a id="insn-00aed5d4"></a> `00aed5d4` | `83 bd ff b0` | adrp x3,0x29e000 | `FALL_THROUGH`
<a id="insn-00aed5d8"></a> `00aed5d8` | `63 6c 1b 91` | add x3,x3,#0x6db | `FALL_THROUGH`
<a id="insn-00aed5dc"></a> `00aed5dc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aed5e0"></a> `00aed5e0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aed5e4"></a> `00aed5e4` | `ab c2 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aed5e8"></a> `00aed5e8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aed5ec"></a> `00aed5ec` | `60 0a 05 f9` | str x0,[x19, #0xa10] | `FALL_THROUGH`
<a id="insn-00aed5f0"></a> `00aed5f0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed5f4"></a> `00aed5f4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aed5f8"></a> `00aed5f8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aed5fc"></a> `00aed5fc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aed5bc`](#insn-00aed5bc) 範囲 `[['00aed5bc', '00aed5d3']]`
  - `CONDITIONAL_JUMP` [`00aed5d0`](#insn-00aed5d0) → [`00aed5f0`](#insn-00aed5f0)
  - `FALL_THROUGH` [`00aed5d0`](#insn-00aed5d0) → [`00aed5d4`](#insn-00aed5d4)
- ブロック [`00aed5d4`](#insn-00aed5d4) 範囲 `[['00aed5d4', '00aed5ef']]`
  - `FALL_THROUGH` [`00aed5ec`](#insn-00aed5ec) → [`00aed5f0`](#insn-00aed5f0)
- ブロック [`00aed5f0`](#insn-00aed5f0) 範囲 `[['00aed5f0', '00aed5ff']]`

## 命令位置別の参照

- [`00aed5bc`](#insn-00aed5bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed5c0`](#insn-00aed5c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed5cc`](#insn-00aed5cc) → `010a0a10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aed5d0`](#insn-00aed5d0) → [`00aed5f0`](#insn-00aed5f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed5d8`](#insn-00aed5d8) → `0029e6db`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aed5e4`](#insn-00aed5e4) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aed5ec`](#insn-00aed5ec) → `010a0a10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aed5f0`](#insn-00aed5f0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aed5bc`](#insn-00aed5bc)

~~~json
{
  "source": "00aed5bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed5c0`](#insn-00aed5c0)

~~~json
{
  "source": "00aed5c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed5cc`](#insn-00aed5cc)

~~~json
{
  "source": "00aed5cc",
  "target": "010a0a10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed5d0`](#insn-00aed5d0)

~~~json
{
  "source": "00aed5d0",
  "target": "00aed5f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed5d8`](#insn-00aed5d8)

~~~json
{
  "source": "00aed5d8",
  "target": "0029e6db",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029e6db",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f537472696e6700",
  "capture_start": "0029e6db",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aed5e4`](#insn-00aed5e4)

~~~json
{
  "source": "00aed5e4",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed5ec`](#insn-00aed5ec)

~~~json
{
  "source": "00aed5ec",
  "target": "010a0a10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed5f0`](#insn-00aed5f0)

~~~json
{
  "source": "00aed5f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
