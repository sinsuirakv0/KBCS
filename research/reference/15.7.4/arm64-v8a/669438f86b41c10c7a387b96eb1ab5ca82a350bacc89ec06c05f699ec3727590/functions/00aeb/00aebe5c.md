# 00aebe5c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aebe18`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebe18.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-b7d5b009c35a924507201f2c19ae12db)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4bbe0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bbe0.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-6db8e169846c4442ff9d6bd81155938a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebe5c",
  "name": "_ZN8firebase4util8iterator13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d5d99068e23006658f2707746f002a05337fabbc864c9a591702a43f4df507da",
  "source_text_sha256": "d5d99068e23006658f2707746f002a05337fabbc864c9a591702a43f4df507da",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebe5c",
        "00aebecb"
      ]
    ],
    "bytes_sha256": "956bb82980490a90d61f38f138401452a472e52ed4f4d87eb5cc16a034b908c0",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde070](../00bde/00bde070.md)
- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Iterator"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 594 bytes

~~~c

void _ZN8firebase4util8iterator13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a08f8 == 0) {
    DAT_010a08f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Iterator",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a08f8,&DAT_002f5d28,1,&DAT_010a0918,"java/util/Iterator");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebe5c"></a> `00aebe5c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebe60"></a> `00aebe60` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebe64"></a> `00aebe64` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebe68"></a> `00aebe68` | `b4 2d 00 b0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebe6c"></a> `00aebe6c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aebe70"></a> `00aebe70` | `81 7e 44 f9` | ldr x1,[x20, #0x8f8] | `FALL_THROUGH`
<a id="insn-00aebe74"></a> `00aebe74` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aebe78"></a> `00aebe78` | `41 01 00 b5` | cbnz x1,0x00aebea0 | `CONDITIONAL_JUMP`
<a id="insn-00aebe7c"></a> `00aebe7c` | `63 bd ff 90` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aebe80"></a> `00aebe80` | `63 68 13 91` | add x3,x3,#0x4da | `FALL_THROUGH`
<a id="insn-00aebe84"></a> `00aebe84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebe88"></a> `00aebe88` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aebe8c"></a> `00aebe8c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aebe90"></a> `00aebe90` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aebe94"></a> `00aebe94` | `7f c8 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aebe98"></a> `00aebe98` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aebe9c"></a> `00aebe9c` | `80 7e 04 f9` | str x0,[x20, #0x8f8] | `FALL_THROUGH`
<a id="insn-00aebea0"></a> `00aebea0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebea4"></a> `00aebea4` | `42 c0 ff d0` | adrp x2,0x2f5000 | `FALL_THROUGH`
<a id="insn-00aebea8"></a> `00aebea8` | `a4 2d 00 b0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebeac"></a> `00aebeac` | `65 bd ff 90` | adrp x5,0x297000 | `FALL_THROUGH`
<a id="insn-00aebeb0"></a> `00aebeb0` | `42 a0 34 91` | add x2,x2,#0xd28 | `FALL_THROUGH`
<a id="insn-00aebeb4"></a> `00aebeb4` | `84 60 24 91` | add x4,x4,#0x918 | `FALL_THROUGH`
<a id="insn-00aebeb8"></a> `00aebeb8` | `a5 68 13 91` | add x5,x5,#0x4da | `FALL_THROUGH`
<a id="insn-00aebebc"></a> `00aebebc` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aebec0"></a> `00aebec0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebec4"></a> `00aebec4` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebec8"></a> `00aebec8` | `6a c8 03 14` | b 0x00bde070 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebe5c`](#insn-00aebe5c) 範囲 `[['00aebe5c', '00aebe7b']]`
  - `CONDITIONAL_JUMP` [`00aebe78`](#insn-00aebe78) → [`00aebea0`](#insn-00aebea0)
  - `FALL_THROUGH` [`00aebe78`](#insn-00aebe78) → [`00aebe7c`](#insn-00aebe7c)
- ブロック [`00aebe7c`](#insn-00aebe7c) 範囲 `[['00aebe7c', '00aebe9f']]`
  - `FALL_THROUGH` [`00aebe9c`](#insn-00aebe9c) → [`00aebea0`](#insn-00aebea0)
- ブロック [`00aebea0`](#insn-00aebea0) 範囲 `[['00aebea0', '00aebecb']]`

## 命令位置別の参照

- [`00aebe5c`](#insn-00aebe5c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe60`](#insn-00aebe60) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe70`](#insn-00aebe70) → `010a08f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebe78`](#insn-00aebe78) → [`00aebea0`](#insn-00aebea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe80`](#insn-00aebe80) → `002974da`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebe94`](#insn-00aebe94) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aebe9c`](#insn-00aebe9c) → `010a08f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebea0`](#insn-00aebea0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebeb0`](#insn-00aebeb0) → `002f5d28`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebeb4`](#insn-00aebeb4) → `010a0918`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebeb8`](#insn-00aebeb8) → `002974da`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebec8`](#insn-00aebec8) → [`00bde070`](../00bde/00bde070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde070` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebe5c`](#insn-00aebe5c)

~~~json
{
  "source": "00aebe5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe60`](#insn-00aebe60)

~~~json
{
  "source": "00aebe60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe70`](#insn-00aebe70)

~~~json
{
  "source": "00aebe70",
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
- 参照命令 [`00aebe78`](#insn-00aebe78)

~~~json
{
  "source": "00aebe78",
  "target": "00aebea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe80`](#insn-00aebe80)

~~~json
{
  "source": "00aebe80",
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
- 参照命令 [`00aebe94`](#insn-00aebe94)

~~~json
{
  "source": "00aebe94",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebe9c`](#insn-00aebe9c)

~~~json
{
  "source": "00aebe9c",
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
- 参照命令 [`00aebea0`](#insn-00aebea0)

~~~json
{
  "source": "00aebea0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebeb0`](#insn-00aebeb0)

~~~json
{
  "source": "00aebeb0",
  "target": "002f5d28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebeb4`](#insn-00aebeb4)

~~~json
{
  "source": "00aebeb4",
  "target": "010a0918",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebeb8`](#insn-00aebeb8)

~~~json
{
  "source": "00aebeb8",
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
- 参照命令 [`00aebec8`](#insn-00aebec8)

~~~json
{
  "source": "00aebec8",
  "target": "00bde070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
