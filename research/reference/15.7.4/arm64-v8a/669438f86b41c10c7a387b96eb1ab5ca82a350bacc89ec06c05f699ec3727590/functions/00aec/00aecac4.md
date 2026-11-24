# 00aecac4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeca80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca80.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-1f0cbe5f240c435377777e35df328692)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4c848`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c848.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-dea1f423a830737a6fbefb020d17a777)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecac4",
  "name": "_ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "29fedad2ea84d35c71368be7c89650d678193ca76000341a569958b9a2545478",
  "source_text_sha256": "29fedad2ea84d35c71368be7c89650d678193ca76000341a569958b9a2545478",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecac4",
        "00aecb07"
      ]
    ],
    "bytes_sha256": "7cec2fe5b5ce481a535eb275efbd0e05957dfed36336f91ce1298a5aacbc8187",
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
"android/os/ParcelFileDescriptor"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 450 bytes

~~~c

long _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a09a8 == 0) {
    DAT_010a09a8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/os/ParcelFileDescriptor",0);
  }
  return DAT_010a09a8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecac4"></a> `00aecac4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aecac8"></a> `00aecac8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecacc"></a> `00aecacc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aecad0"></a> `00aecad0` | `b3 2d 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecad4"></a> `00aecad4` | `68 d6 44 f9` | ldr x8,[x19, #0x9a8] | `FALL_THROUGH`
<a id="insn-00aecad8"></a> `00aecad8` | `08 01 00 b5` | cbnz x8,0x00aecaf8 | `CONDITIONAL_JUMP`
<a id="insn-00aecadc"></a> `00aecadc` | `43 bd ff 90` | adrp x3,0x294000 | `FALL_THROUGH`
<a id="insn-00aecae0"></a> `00aecae0` | `63 4c 07 91` | add x3,x3,#0x1d3 | `FALL_THROUGH`
<a id="insn-00aecae4"></a> `00aecae4` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aecae8"></a> `00aecae8` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aecaec"></a> `00aecaec` | `69 c5 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aecaf0"></a> `00aecaf0` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aecaf4"></a> `00aecaf4` | `60 d6 04 f9` | str x0,[x19, #0x9a8] | `FALL_THROUGH`
<a id="insn-00aecaf8"></a> `00aecaf8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecafc"></a> `00aecafc` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aecb00"></a> `00aecb00` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aecb04"></a> `00aecb04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecac4`](#insn-00aecac4) 範囲 `[['00aecac4', '00aecadb']]`
  - `CONDITIONAL_JUMP` [`00aecad8`](#insn-00aecad8) → [`00aecaf8`](#insn-00aecaf8)
  - `FALL_THROUGH` [`00aecad8`](#insn-00aecad8) → [`00aecadc`](#insn-00aecadc)
- ブロック [`00aecadc`](#insn-00aecadc) 範囲 `[['00aecadc', '00aecaf7']]`
  - `FALL_THROUGH` [`00aecaf4`](#insn-00aecaf4) → [`00aecaf8`](#insn-00aecaf8)
- ブロック [`00aecaf8`](#insn-00aecaf8) 範囲 `[['00aecaf8', '00aecb07']]`

## 命令位置別の参照

- [`00aecac4`](#insn-00aecac4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecac8`](#insn-00aecac8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecad4`](#insn-00aecad4) → `010a09a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecad8`](#insn-00aecad8) → [`00aecaf8`](#insn-00aecaf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecae0`](#insn-00aecae0) → `002941d3`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecaec`](#insn-00aecaec) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aecaf4`](#insn-00aecaf4) → `010a09a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecaf8`](#insn-00aecaf8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecac4`](#insn-00aecac4)

~~~json
{
  "source": "00aecac4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecac8`](#insn-00aecac8)

~~~json
{
  "source": "00aecac8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecad4`](#insn-00aecad4)

~~~json
{
  "source": "00aecad4",
  "target": "010a09a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecad8`](#insn-00aecad8)

~~~json
{
  "source": "00aecad8",
  "target": "00aecaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecae0`](#insn-00aecae0)

~~~json
{
  "source": "00aecae0",
  "target": "002941d3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002941d3",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "616e64726f69642f6f732f50617263656c46696c6544657363726970746f7200",
  "capture_start": "002941d3",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecaec`](#insn-00aecaec)

~~~json
{
  "source": "00aecaec",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecaf4`](#insn-00aecaf4)

~~~json
{
  "source": "00aecaf4",
  "target": "010a09a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecaf8`](#insn-00aecaf8)

~~~json
{
  "source": "00aecaf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
