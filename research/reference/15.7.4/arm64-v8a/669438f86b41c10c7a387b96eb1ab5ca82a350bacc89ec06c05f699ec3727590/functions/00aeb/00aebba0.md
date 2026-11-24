# 00aebba0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aebb5c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb5c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-e9dce1394f1f23555a981b5886c81af7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4b924`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b924.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-e802d441b92894cc347ff3aa4024adcc)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebba0",
  "name": "_ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "704c91a710f8dd523f7fcf7922c8b587f481528856e83e25d186a923c465a1e7",
  "source_text_sha256": "704c91a710f8dd523f7fcf7922c8b587f481528856e83e25d186a923c465a1e7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebba0",
        "00aebbdf"
      ]
    ],
    "bytes_sha256": "1aed14b81547c970807d5226db07d00a206179b8a2d8069c02db01dae116eb4c",
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
"java/util/Iterator"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 427 bytes

~~~c

long _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a08f8 == 0) {
    DAT_010a08f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a08f8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebba0"></a> `00aebba0` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebba4"></a> `00aebba4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebba8"></a> `00aebba8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebbac"></a> `00aebbac` | `b3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebbb0"></a> `00aebbb0` | `68 7e 44 f9` | ldr x8,[x19, #0x8f8] | `FALL_THROUGH`
<a id="insn-00aebbb4"></a> `00aebbb4` | `e8 00 00 b5` | cbnz x8,0x00aebbd0 | `CONDITIONAL_JUMP`
<a id="insn-00aebbb8"></a> `00aebbb8` | `63 bd ff 90` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aebbbc"></a> `00aebbbc` | `63 68 13 91` | add x3,x3,#0x4da | `FALL_THROUGH`
<a id="insn-00aebbc0"></a> `00aebbc0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aebbc4"></a> `00aebbc4` | `33 c9 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aebbc8"></a> `00aebbc8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aebbcc"></a> `00aebbcc` | `60 7e 04 f9` | str x0,[x19, #0x8f8] | `FALL_THROUGH`
<a id="insn-00aebbd0"></a> `00aebbd0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebbd4"></a> `00aebbd4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aebbd8"></a> `00aebbd8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebbdc"></a> `00aebbdc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebba0`](#insn-00aebba0) 範囲 `[['00aebba0', '00aebbb7']]`
  - `CONDITIONAL_JUMP` [`00aebbb4`](#insn-00aebbb4) → [`00aebbd0`](#insn-00aebbd0)
  - `FALL_THROUGH` [`00aebbb4`](#insn-00aebbb4) → [`00aebbb8`](#insn-00aebbb8)
- ブロック [`00aebbb8`](#insn-00aebbb8) 範囲 `[['00aebbb8', '00aebbcf']]`
  - `FALL_THROUGH` [`00aebbcc`](#insn-00aebbcc) → [`00aebbd0`](#insn-00aebbd0)
- ブロック [`00aebbd0`](#insn-00aebbd0) 範囲 `[['00aebbd0', '00aebbdf']]`

## 命令位置別の参照

- [`00aebba0`](#insn-00aebba0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebba4`](#insn-00aebba4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebbb0`](#insn-00aebbb0) → `010a08f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebbb4`](#insn-00aebbb4) → [`00aebbd0`](#insn-00aebbd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebbbc`](#insn-00aebbbc) → `002974da`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebbc4`](#insn-00aebbc4) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aebbcc`](#insn-00aebbcc) → `010a08f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebbd0`](#insn-00aebbd0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebba0`](#insn-00aebba0)

~~~json
{
  "source": "00aebba0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebba4`](#insn-00aebba4)

~~~json
{
  "source": "00aebba4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebbb0`](#insn-00aebbb0)

~~~json
{
  "source": "00aebbb0",
  "target": "010a08f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebbb4`](#insn-00aebbb4)

~~~json
{
  "source": "00aebbb4",
  "target": "00aebbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebbbc`](#insn-00aebbbc)

~~~json
{
  "source": "00aebbbc",
  "target": "002974da",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002974da",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4974657261746f7200",
  "capture_start": "002974da",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebbc4`](#insn-00aebbc4)

~~~json
{
  "source": "00aebbc4",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebbcc`](#insn-00aebbcc)

~~~json
{
  "source": "00aebbcc",
  "target": "010a08f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebbd0`](#insn-00aebbd0)

~~~json
{
  "source": "00aebbd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
