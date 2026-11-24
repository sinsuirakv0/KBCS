# 00aee2ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aee2a8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee2a8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-453c9c84ff586cddf503c2d38c79c188)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4e070`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e070.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-374c11379917cfef7b472ce0d94b6a51)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aee2ec",
  "name": "_ZN8firebase4util6object13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "203b37b34227200907313abcce279cd0f255059a72c1e78813fd45544f0f32e0",
  "source_text_sha256": "203b37b34227200907313abcce279cd0f255059a72c1e78813fd45544f0f32e0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aee2ec",
        "00aee35b"
      ]
    ],
    "bytes_sha256": "0eb29a86cff8ef018009695a05edb9af34b940e7c99a80b4a5da1dfabcc9c1a7",
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
"java/lang/Object"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 588 bytes

~~~c

void _ZN8firebase4util6object13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0a88 == 0) {
    DAT_010a0a88 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Object",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a0a88,&DAT_002f5e18,1,&DAT_010a0aa0,"java/lang/Object");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aee2ec"></a> `00aee2ec` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aee2f0"></a> `00aee2f0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aee2f4"></a> `00aee2f4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aee2f8"></a> `00aee2f8` | `94 2d 00 d0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aee2fc"></a> `00aee2fc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aee300"></a> `00aee300` | `81 46 45 f9` | ldr x1,[x20, #0xa88] | `FALL_THROUGH`
<a id="insn-00aee304"></a> `00aee304` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aee308"></a> `00aee308` | `41 01 00 b5` | cbnz x1,0x00aee330 | `CONDITIONAL_JUMP`
<a id="insn-00aee30c"></a> `00aee30c` | `63 bd ff f0` | adrp x3,0x29d000 | `FALL_THROUGH`
<a id="insn-00aee310"></a> `00aee310` | `63 dc 37 91` | add x3,x3,#0xdf7 | `FALL_THROUGH`
<a id="insn-00aee314"></a> `00aee314` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aee318"></a> `00aee318` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aee31c"></a> `00aee31c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aee320"></a> `00aee320` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aee324"></a> `00aee324` | `5b bf 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aee328"></a> `00aee328` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aee32c"></a> `00aee32c` | `80 46 05 f9` | str x0,[x20, #0xa88] | `FALL_THROUGH`
<a id="insn-00aee330"></a> `00aee330` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aee334"></a> `00aee334` | `22 c0 ff f0` | adrp x2,0x2f5000 | `FALL_THROUGH`
<a id="insn-00aee338"></a> `00aee338` | `84 2d 00 d0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aee33c"></a> `00aee33c` | `65 bd ff f0` | adrp x5,0x29d000 | `FALL_THROUGH`
<a id="insn-00aee340"></a> `00aee340` | `42 60 38 91` | add x2,x2,#0xe18 | `FALL_THROUGH`
<a id="insn-00aee344"></a> `00aee344` | `84 80 2a 91` | add x4,x4,#0xaa0 | `FALL_THROUGH`
<a id="insn-00aee348"></a> `00aee348` | `a5 dc 37 91` | add x5,x5,#0xdf7 | `FALL_THROUGH`
<a id="insn-00aee34c"></a> `00aee34c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aee350"></a> `00aee350` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aee354"></a> `00aee354` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aee358"></a> `00aee358` | `46 bf 03 14` | b 0x00bde070 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aee2ec`](#insn-00aee2ec) 範囲 `[['00aee2ec', '00aee30b']]`
  - `CONDITIONAL_JUMP` [`00aee308`](#insn-00aee308) → [`00aee330`](#insn-00aee330)
  - `FALL_THROUGH` [`00aee308`](#insn-00aee308) → [`00aee30c`](#insn-00aee30c)
- ブロック [`00aee30c`](#insn-00aee30c) 範囲 `[['00aee30c', '00aee32f']]`
  - `FALL_THROUGH` [`00aee32c`](#insn-00aee32c) → [`00aee330`](#insn-00aee330)
- ブロック [`00aee330`](#insn-00aee330) 範囲 `[['00aee330', '00aee35b']]`

## 命令位置別の参照

- [`00aee2ec`](#insn-00aee2ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee2f0`](#insn-00aee2f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee300`](#insn-00aee300) → `010a0a88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aee308`](#insn-00aee308) → [`00aee330`](#insn-00aee330) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee310`](#insn-00aee310) → `0029ddf7`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aee324`](#insn-00aee324) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aee32c`](#insn-00aee32c) → `010a0a88`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aee330`](#insn-00aee330) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee340`](#insn-00aee340) → `002f5e18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee344`](#insn-00aee344) → `010a0aa0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee348`](#insn-00aee348) → `0029ddf7`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aee358`](#insn-00aee358) → [`00bde070`](../00bde/00bde070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde070` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aee2ec`](#insn-00aee2ec)

~~~json
{
  "source": "00aee2ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee2f0`](#insn-00aee2f0)

~~~json
{
  "source": "00aee2f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee300`](#insn-00aee300)

~~~json
{
  "source": "00aee300",
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
- 参照命令 [`00aee308`](#insn-00aee308)

~~~json
{
  "source": "00aee308",
  "target": "00aee330",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee310`](#insn-00aee310)

~~~json
{
  "source": "00aee310",
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
- 参照命令 [`00aee324`](#insn-00aee324)

~~~json
{
  "source": "00aee324",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aee32c`](#insn-00aee32c)

~~~json
{
  "source": "00aee32c",
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
- 参照命令 [`00aee330`](#insn-00aee330)

~~~json
{
  "source": "00aee330",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee340`](#insn-00aee340)

~~~json
{
  "source": "00aee340",
  "target": "002f5e18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee344`](#insn-00aee344)

~~~json
{
  "source": "00aee344",
  "target": "010a0aa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee348`](#insn-00aee348)

~~~json
{
  "source": "00aee348",
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
- 参照命令 [`00aee358`](#insn-00aee358)

~~~json
{
  "source": "00aee358",
  "target": "00bde070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
