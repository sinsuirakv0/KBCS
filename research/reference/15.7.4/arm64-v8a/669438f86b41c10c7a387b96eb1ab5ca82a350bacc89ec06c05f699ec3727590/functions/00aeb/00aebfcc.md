# 00aebfcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aebf88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-4a34635b7048c75cc5dbbb6e820d82dd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4bd50`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bd50.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-887f5a5a7a3911e6599c23bafb94442d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebfcc",
  "name": "_ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d3de7de21217c2807f9b01a365e70d5782805fc99550bcfff5a19e3b1beefb9",
  "source_text_sha256": "7d3de7de21217c2807f9b01a365e70d5782805fc99550bcfff5a19e3b1beefb9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebfcc",
        "00aec00f"
      ]
    ],
    "bytes_sha256": "a48f5ccd9991a1d344ae27e464d129fed23facf48e71a513006cfd9b1d5211ea",
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
"java/util/List"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 398 bytes

~~~c

long _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0920 == 0) {
    DAT_010a0920 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/List",0);
  }
  return DAT_010a0920;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebfcc"></a> `00aebfcc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebfd0"></a> `00aebfd0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebfd4"></a> `00aebfd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebfd8"></a> `00aebfd8` | `b3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebfdc"></a> `00aebfdc` | `68 92 44 f9` | ldr x8,[x19, #0x920] | `FALL_THROUGH`
<a id="insn-00aebfe0"></a> `00aebfe0` | `08 01 00 b5` | cbnz x8,0x00aec000 | `CONDITIONAL_JUMP`
<a id="insn-00aebfe4"></a> `00aebfe4` | `23 bd ff b0` | adrp x3,0x290000 | `FALL_THROUGH`
<a id="insn-00aebfe8"></a> `00aebfe8` | `63 14 0e 91` | add x3,x3,#0x385 | `FALL_THROUGH`
<a id="insn-00aebfec"></a> `00aebfec` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aebff0"></a> `00aebff0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aebff4"></a> `00aebff4` | `27 c8 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aebff8"></a> `00aebff8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aebffc"></a> `00aebffc` | `60 92 04 f9` | str x0,[x19, #0x920] | `FALL_THROUGH`
<a id="insn-00aec000"></a> `00aec000` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec004"></a> `00aec004` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aec008"></a> `00aec008` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aec00c"></a> `00aec00c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebfcc`](#insn-00aebfcc) 範囲 `[['00aebfcc', '00aebfe3']]`
  - `CONDITIONAL_JUMP` [`00aebfe0`](#insn-00aebfe0) → [`00aec000`](#insn-00aec000)
  - `FALL_THROUGH` [`00aebfe0`](#insn-00aebfe0) → [`00aebfe4`](#insn-00aebfe4)
- ブロック [`00aebfe4`](#insn-00aebfe4) 範囲 `[['00aebfe4', '00aebfff']]`
  - `FALL_THROUGH` [`00aebffc`](#insn-00aebffc) → [`00aec000`](#insn-00aec000)
- ブロック [`00aec000`](#insn-00aec000) 範囲 `[['00aec000', '00aec00f']]`

## 命令位置別の参照

- [`00aebfcc`](#insn-00aebfcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebfd0`](#insn-00aebfd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebfdc`](#insn-00aebfdc) → `010a0920`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebfe0`](#insn-00aebfe0) → [`00aec000`](#insn-00aec000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebfe8`](#insn-00aebfe8) → `00290385`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebff4`](#insn-00aebff4) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aebffc`](#insn-00aebffc) → `010a0920`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec000`](#insn-00aec000) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebfcc`](#insn-00aebfcc)

~~~json
{
  "source": "00aebfcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebfd0`](#insn-00aebfd0)

~~~json
{
  "source": "00aebfd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebfdc`](#insn-00aebfdc)

~~~json
{
  "source": "00aebfdc",
  "target": "010a0920",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0920",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebfe0`](#insn-00aebfe0)

~~~json
{
  "source": "00aebfe0",
  "target": "00aec000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebfe8`](#insn-00aebfe8)

~~~json
{
  "source": "00aebfe8",
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
- 参照命令 [`00aebff4`](#insn-00aebff4)

~~~json
{
  "source": "00aebff4",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebffc`](#insn-00aebffc)

~~~json
{
  "source": "00aebffc",
  "target": "010a0920",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0920",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec000`](#insn-00aec000)

~~~json
{
  "source": "00aec000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
