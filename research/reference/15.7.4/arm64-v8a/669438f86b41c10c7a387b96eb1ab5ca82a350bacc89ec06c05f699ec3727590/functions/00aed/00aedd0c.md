# 00aedd0c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aedcc8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedcc8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-ed3d196d44faf28b9bbd930c1ee7360b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4da90`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da90.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-420be1f8d82646e771913ef87d54c2d0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedd0c",
  "name": "_ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "34330fcfe4bc5c2cfbc90a6a876cf9e8ed1369225e36abb7b8ee7ef0b6d2e055",
  "source_text_sha256": "34330fcfe4bc5c2cfbc90a6a876cf9e8ed1369225e36abb7b8ee7ef0b6d2e055",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedd0c",
        "00aedd4f"
      ]
    ],
    "bytes_sha256": "a39dc49f36d0408c602925da5171aedd7100033006a4497c1e9e43e4b9a9acf1",
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
"android/net/Uri"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 398 bytes

~~~c

long _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0a60 == 0) {
    DAT_010a0a60 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/net/Uri",0);
  }
  return DAT_010a0a60;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedd0c"></a> `00aedd0c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedd10"></a> `00aedd10` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedd14"></a> `00aedd14` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedd18"></a> `00aedd18` | `93 2d 00 f0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedd1c"></a> `00aedd1c` | `68 32 45 f9` | ldr x8,[x19, #0xa60] | `FALL_THROUGH`
<a id="insn-00aedd20"></a> `00aedd20` | `08 01 00 b5` | cbnz x8,0x00aedd40 | `CONDITIONAL_JUMP`
<a id="insn-00aedd24"></a> `00aedd24` | `43 bd ff d0` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aedd28"></a> `00aedd28` | `63 e0 13 91` | add x3,x3,#0x4f8 | `FALL_THROUGH`
<a id="insn-00aedd2c"></a> `00aedd2c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aedd30"></a> `00aedd30` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aedd34"></a> `00aedd34` | `d7 c0 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aedd38"></a> `00aedd38` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aedd3c"></a> `00aedd3c` | `60 32 05 f9` | str x0,[x19, #0xa60] | `FALL_THROUGH`
<a id="insn-00aedd40"></a> `00aedd40` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedd44"></a> `00aedd44` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aedd48"></a> `00aedd48` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aedd4c"></a> `00aedd4c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedd0c`](#insn-00aedd0c) 範囲 `[['00aedd0c', '00aedd23']]`
  - `CONDITIONAL_JUMP` [`00aedd20`](#insn-00aedd20) → [`00aedd40`](#insn-00aedd40)
  - `FALL_THROUGH` [`00aedd20`](#insn-00aedd20) → [`00aedd24`](#insn-00aedd24)
- ブロック [`00aedd24`](#insn-00aedd24) 範囲 `[['00aedd24', '00aedd3f']]`
  - `FALL_THROUGH` [`00aedd3c`](#insn-00aedd3c) → [`00aedd40`](#insn-00aedd40)
- ブロック [`00aedd40`](#insn-00aedd40) 範囲 `[['00aedd40', '00aedd4f']]`

## 命令位置別の参照

- [`00aedd0c`](#insn-00aedd0c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd10`](#insn-00aedd10) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd1c`](#insn-00aedd1c) → `010a0a60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedd20`](#insn-00aedd20) → [`00aedd40`](#insn-00aedd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd28`](#insn-00aedd28) → `002974f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedd34`](#insn-00aedd34) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aedd3c`](#insn-00aedd3c) → `010a0a60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedd40`](#insn-00aedd40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedd0c`](#insn-00aedd0c)

~~~json
{
  "source": "00aedd0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd10`](#insn-00aedd10)

~~~json
{
  "source": "00aedd10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd1c`](#insn-00aedd1c)

~~~json
{
  "source": "00aedd1c",
  "target": "010a0a60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedd20`](#insn-00aedd20)

~~~json
{
  "source": "00aedd20",
  "target": "00aedd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd28`](#insn-00aedd28)

~~~json
{
  "source": "00aedd28",
  "target": "002974f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002974f8",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "616e64726f69642f6e65742f55726900",
  "capture_start": "002974f8",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedd34`](#insn-00aedd34)

~~~json
{
  "source": "00aedd34",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedd3c`](#insn-00aedd3c)

~~~json
{
  "source": "00aedd3c",
  "target": "010a0a60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedd40`](#insn-00aedd40)

~~~json
{
  "source": "00aedd40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
