# 00aeafbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeaf78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaf78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-4c11bfd5ba25245bb5eae11e451e1798)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4ad40`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ad40.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-a4d1fb77ce4e6e76735ef03f62544cf6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeafbc",
  "name": "_ZN8firebase4util8hash_map13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "517e0b0ae5bdfd1bc1707d82abba6044c623f340437cbd4cb790cd4fe82af878",
  "source_text_sha256": "517e0b0ae5bdfd1bc1707d82abba6044c623f340437cbd4cb790cd4fe82af878",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeafbc",
        "00aeb02b"
      ]
    ],
    "bytes_sha256": "007ac7ab919d67375b42f6ce8479b67cd296fbadcdbc4cff8773579ecb063642",
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
"java/util/HashMap"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 592 bytes

~~~c

void _ZN8firebase4util8hash_map13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0850 == 0) {
    DAT_010a0850 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/HashMap",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a0850,&DAT_002f5cc8,1,&DAT_010a0868,"java/util/HashMap");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeafbc"></a> `00aeafbc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeafc0"></a> `00aeafc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeafc4"></a> `00aeafc4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeafc8"></a> `00aeafc8` | `b4 2d 00 d0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeafcc"></a> `00aeafcc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aeafd0"></a> `00aeafd0` | `81 2a 44 f9` | ldr x1,[x20, #0x850] | `FALL_THROUGH`
<a id="insn-00aeafd4"></a> `00aeafd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeafd8"></a> `00aeafd8` | `41 01 00 b5` | cbnz x1,0x00aeb000 | `CONDITIONAL_JUMP`
<a id="insn-00aeafdc"></a> `00aeafdc` | `63 bd ff 90` | adrp x3,0x296000 | `FALL_THROUGH`
<a id="insn-00aeafe0"></a> `00aeafe0` | `63 54 2f 91` | add x3,x3,#0xbd5 | `FALL_THROUGH`
<a id="insn-00aeafe4"></a> `00aeafe4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeafe8"></a> `00aeafe8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aeafec"></a> `00aeafec` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeaff0"></a> `00aeaff0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aeaff4"></a> `00aeaff4` | `27 cc 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aeaff8"></a> `00aeaff8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aeaffc"></a> `00aeaffc` | `80 2a 04 f9` | str x0,[x20, #0x850] | `FALL_THROUGH`
<a id="insn-00aeb000"></a> `00aeb000` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeb004"></a> `00aeb004` | `42 c0 ff d0` | adrp x2,0x2f5000 | `FALL_THROUGH`
<a id="insn-00aeb008"></a> `00aeb008` | `a4 2d 00 b0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeb00c"></a> `00aeb00c` | `45 bd ff f0` | adrp x5,0x296000 | `FALL_THROUGH`
<a id="insn-00aeb010"></a> `00aeb010` | `42 20 33 91` | add x2,x2,#0xcc8 | `FALL_THROUGH`
<a id="insn-00aeb014"></a> `00aeb014` | `84 a0 21 91` | add x4,x4,#0x868 | `FALL_THROUGH`
<a id="insn-00aeb018"></a> `00aeb018` | `a5 54 2f 91` | add x5,x5,#0xbd5 | `FALL_THROUGH`
<a id="insn-00aeb01c"></a> `00aeb01c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aeb020"></a> `00aeb020` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeb024"></a> `00aeb024` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeb028"></a> `00aeb028` | `12 cc 03 14` | b 0x00bde070 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeafbc`](#insn-00aeafbc) 範囲 `[['00aeafbc', '00aeafdb']]`
  - `CONDITIONAL_JUMP` [`00aeafd8`](#insn-00aeafd8) → [`00aeb000`](#insn-00aeb000)
  - `FALL_THROUGH` [`00aeafd8`](#insn-00aeafd8) → [`00aeafdc`](#insn-00aeafdc)
- ブロック [`00aeafdc`](#insn-00aeafdc) 範囲 `[['00aeafdc', '00aeafff']]`
  - `FALL_THROUGH` [`00aeaffc`](#insn-00aeaffc) → [`00aeb000`](#insn-00aeb000)
- ブロック [`00aeb000`](#insn-00aeb000) 範囲 `[['00aeb000', '00aeb02b']]`

## 命令位置別の参照

- [`00aeafbc`](#insn-00aeafbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafc0`](#insn-00aeafc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafd0`](#insn-00aeafd0) → `010a0850`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeafd8`](#insn-00aeafd8) → [`00aeb000`](#insn-00aeb000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafe0`](#insn-00aeafe0) → `00296bd5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeaff4`](#insn-00aeaff4) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aeaffc`](#insn-00aeaffc) → `010a0850`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeb000`](#insn-00aeb000) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb010`](#insn-00aeb010) → `002f5cc8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb014`](#insn-00aeb014) → `010a0868`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb018`](#insn-00aeb018) → `00296bd5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeb028`](#insn-00aeb028) → [`00bde070`](../00bde/00bde070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde070` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeafbc`](#insn-00aeafbc)

~~~json
{
  "source": "00aeafbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafc0`](#insn-00aeafc0)

~~~json
{
  "source": "00aeafc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafd0`](#insn-00aeafd0)

~~~json
{
  "source": "00aeafd0",
  "target": "010a0850",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0850",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeafd8`](#insn-00aeafd8)

~~~json
{
  "source": "00aeafd8",
  "target": "00aeb000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafe0`](#insn-00aeafe0)

~~~json
{
  "source": "00aeafe0",
  "target": "00296bd5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00296bd5",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f486173684d617000",
  "capture_start": "00296bd5",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeaff4`](#insn-00aeaff4)

~~~json
{
  "source": "00aeaff4",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaffc`](#insn-00aeaffc)

~~~json
{
  "source": "00aeaffc",
  "target": "010a0850",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0850",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeb000`](#insn-00aeb000)

~~~json
{
  "source": "00aeb000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb010`](#insn-00aeb010)

~~~json
{
  "source": "00aeb010",
  "target": "002f5cc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb014`](#insn-00aeb014)

~~~json
{
  "source": "00aeb014",
  "target": "010a0868",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb018`](#insn-00aeb018)

~~~json
{
  "source": "00aeb018",
  "target": "00296bd5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00296bd5",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f486173684d617000",
  "capture_start": "00296bd5",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeb028`](#insn-00aeb028)

~~~json
{
  "source": "00aeb028",
  "target": "00bde070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
