# 00aebdb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aebd6c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebd6c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-72c609ae4c6259c464a072b538e40051)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4bb34`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bb34.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-e546cc5e3aceef02fa6b408b91bffef7)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebdb0",
  "name": "_ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7212d6518e3e312d3090089b84f58bd06ebde23831aac3802da1f435e19524a0",
  "source_text_sha256": "7212d6518e3e312d3090089b84f58bd06ebde23831aac3802da1f435e19524a0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebdb0",
        "00aebe1f"
      ]
    ],
    "bytes_sha256": "5e3b19d75c94a34153bf041d02372646613c1992e8281d3f40642504c8cc8934",
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

- [00bde090](../00bde/00bde090.md)
- [00bde0b0](../00bde/00bde0b0.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Iterator"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 612 bytes

~~~c

void _ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a08f8 == 0) {
    DAT_010a08f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Iterator",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a08f8,&PTR_s_hasNext_00c10490,2,&DAT_010a0908,"java/util/Iterator");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebdb0"></a> `00aebdb0` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebdb4"></a> `00aebdb4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebdb8"></a> `00aebdb8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebdbc"></a> `00aebdbc` | `b4 2d 00 b0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebdc0"></a> `00aebdc0` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aebdc4"></a> `00aebdc4` | `81 7e 44 f9` | ldr x1,[x20, #0x8f8] | `FALL_THROUGH`
<a id="insn-00aebdc8"></a> `00aebdc8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aebdcc"></a> `00aebdcc` | `41 01 00 b5` | cbnz x1,0x00aebdf4 | `CONDITIONAL_JUMP`
<a id="insn-00aebdd0"></a> `00aebdd0` | `63 bd ff 90` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aebdd4"></a> `00aebdd4` | `63 68 13 91` | add x3,x3,#0x4da | `FALL_THROUGH`
<a id="insn-00aebdd8"></a> `00aebdd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebddc"></a> `00aebddc` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aebde0"></a> `00aebde0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aebde4"></a> `00aebde4` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aebde8"></a> `00aebde8` | `aa c8 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aebdec"></a> `00aebdec` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aebdf0"></a> `00aebdf0` | `80 7e 04 f9` | str x0,[x20, #0x8f8] | `FALL_THROUGH`
<a id="insn-00aebdf4"></a> `00aebdf4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebdf8"></a> `00aebdf8` | `22 09 00 b0` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aebdfc"></a> `00aebdfc` | `a4 2d 00 b0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebe00"></a> `00aebe00` | `65 bd ff 90` | adrp x5,0x297000 | `FALL_THROUGH`
<a id="insn-00aebe04"></a> `00aebe04` | `42 40 12 91` | add x2,x2,#0x490 | `FALL_THROUGH`
<a id="insn-00aebe08"></a> `00aebe08` | `84 20 24 91` | add x4,x4,#0x908 | `FALL_THROUGH`
<a id="insn-00aebe0c"></a> `00aebe0c` | `a5 68 13 91` | add x5,x5,#0x4da | `FALL_THROUGH`
<a id="insn-00aebe10"></a> `00aebe10` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00aebe14"></a> `00aebe14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebe18"></a> `00aebe18` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebe1c"></a> `00aebe1c` | `a5 c8 03 14` | b 0x00bde0b0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebdb0`](#insn-00aebdb0) 範囲 `[['00aebdb0', '00aebdcf']]`
  - `CONDITIONAL_JUMP` [`00aebdcc`](#insn-00aebdcc) → [`00aebdf4`](#insn-00aebdf4)
  - `FALL_THROUGH` [`00aebdcc`](#insn-00aebdcc) → [`00aebdd0`](#insn-00aebdd0)
- ブロック [`00aebdd0`](#insn-00aebdd0) 範囲 `[['00aebdd0', '00aebdf3']]`
  - `FALL_THROUGH` [`00aebdf0`](#insn-00aebdf0) → [`00aebdf4`](#insn-00aebdf4)
- ブロック [`00aebdf4`](#insn-00aebdf4) 範囲 `[['00aebdf4', '00aebe1f']]`

## 命令位置別の参照

- [`00aebdb0`](#insn-00aebdb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebdb4`](#insn-00aebdb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebdc4`](#insn-00aebdc4) → `010a08f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebdcc`](#insn-00aebdcc) → [`00aebdf4`](#insn-00aebdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebdd4`](#insn-00aebdd4) → `002974da`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebde8`](#insn-00aebde8) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aebdf0`](#insn-00aebdf0) → `010a08f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebdf4`](#insn-00aebdf4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe04`](#insn-00aebe04) → `00c10490`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aebe08`](#insn-00aebe08) → `010a0908`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebe0c`](#insn-00aebe0c) → `002974da`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebe1c`](#insn-00aebe1c) → [`00bde0b0`](../00bde/00bde0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0b0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebdb0`](#insn-00aebdb0)

~~~json
{
  "source": "00aebdb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebdb4`](#insn-00aebdb4)

~~~json
{
  "source": "00aebdb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebdc4`](#insn-00aebdc4)

~~~json
{
  "source": "00aebdc4",
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
- 参照命令 [`00aebdcc`](#insn-00aebdcc)

~~~json
{
  "source": "00aebdcc",
  "target": "00aebdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebdd4`](#insn-00aebdd4)

~~~json
{
  "source": "00aebdd4",
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
- 参照命令 [`00aebde8`](#insn-00aebde8)

~~~json
{
  "source": "00aebde8",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebdf0`](#insn-00aebdf0)

~~~json
{
  "source": "00aebdf0",
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
- 参照命令 [`00aebdf4`](#insn-00aebdf4)

~~~json
{
  "source": "00aebdf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe04`](#insn-00aebe04)

~~~json
{
  "source": "00aebe04",
  "target": "00c10490",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10490",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aebe08`](#insn-00aebe08)

~~~json
{
  "source": "00aebe08",
  "target": "010a0908",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0908",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebe0c`](#insn-00aebe0c)

~~~json
{
  "source": "00aebe0c",
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
- 参照命令 [`00aebe1c`](#insn-00aebe1c)

~~~json
{
  "source": "00aebe1c",
  "target": "00bde0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
