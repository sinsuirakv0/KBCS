# 00bd7bec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd6bf8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6bf8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0084.md#compare-43922c5e616f492f8e778d2805457a1a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd7bec",
  "name": "_ZN8firebase4auth8timeunit13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "afd301ef1ad8d504fe29963f0a6a938afc13aea3bf389a73c45a31b797b2ac1e",
  "source_text_sha256": "afd301ef1ad8d504fe29963f0a6a938afc13aea3bf389a73c45a31b797b2ac1e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd7bec",
        "00bd7c5b"
      ]
    ],
    "bytes_sha256": "6cf121adcf3f57832375aae1260669722f6f915896be649ff4fd2831ea86ccbe",
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

- [00c5bf90](../00c5b/00c5bf90.md)
- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%java/util/concurrent/TimeUnit"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 645 bytes

~~~c

void _ZN8firebase4auth8timeunit13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01127c18 == 0) {
    DAT_01127c18 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/concurrent/TimeUnit",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_01127c18,&PTR_s_MILLISECONDS_00c93318,1,&DAT_01127c30,
             "java/util/concurrent/TimeUnit");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd7bec"></a> `00bd7bec` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd7bf0"></a> `00bd7bf0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd7bf4"></a> `00bd7bf4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd7bf8"></a> `00bd7bf8` | `94 2a 00 90` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd7bfc"></a> `00bd7bfc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bd7c00"></a> `00bd7c00` | `81 0e 46 f9` | ldr x1,[x20, #0xc18] | `FALL_THROUGH`
<a id="insn-00bd7c04"></a> `00bd7c04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd7c08"></a> `00bd7c08` | `41 01 00 b5` | cbnz x1,0x00bd7c30 | `CONDITIONAL_JUMP`
<a id="insn-00bd7c0c"></a> `00bd7c0c` | `e3 b6 ff 90` | adrp x3,0x2b3000 | `FALL_THROUGH`
<a id="insn-00bd7c10"></a> `00bd7c10` | `63 14 21 91` | add x3,x3,#0x845 | `FALL_THROUGH`
<a id="insn-00bd7c14"></a> `00bd7c14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd7c18"></a> `00bd7c18` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bd7c1c"></a> `00bd7c1c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bd7c20"></a> `00bd7c20` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bd7c24"></a> `00bd7c24` | `e3 10 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd7c28"></a> `00bd7c28` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bd7c2c"></a> `00bd7c2c` | `80 0e 06 f9` | str x0,[x20, #0xc18] | `FALL_THROUGH`
<a id="insn-00bd7c30"></a> `00bd7c30` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd7c34"></a> `00bd7c34` | `e2 05 00 90` | adrp x2,0xc93000 | `FALL_THROUGH`
<a id="insn-00bd7c38"></a> `00bd7c38` | `84 2a 00 90` | adrp x4,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd7c3c"></a> `00bd7c3c` | `e5 b6 ff 90` | adrp x5,0x2b3000 | `FALL_THROUGH`
<a id="insn-00bd7c40"></a> `00bd7c40` | `42 60 0c 91` | add x2,x2,#0x318 | `FALL_THROUGH`
<a id="insn-00bd7c44"></a> `00bd7c44` | `84 c0 30 91` | add x4,x4,#0xc30 | `FALL_THROUGH`
<a id="insn-00bd7c48"></a> `00bd7c48` | `a5 14 21 91` | add x5,x5,#0x845 | `FALL_THROUGH`
<a id="insn-00bd7c4c"></a> `00bd7c4c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bd7c50"></a> `00bd7c50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd7c54"></a> `00bd7c54` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd7c58"></a> `00bd7c58` | `ce 10 02 14` | b 0x00c5bf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd7bec`](#insn-00bd7bec) 範囲 `[['00bd7bec', '00bd7c0b']]`
  - `CONDITIONAL_JUMP` [`00bd7c08`](#insn-00bd7c08) → [`00bd7c30`](#insn-00bd7c30)
  - `FALL_THROUGH` [`00bd7c08`](#insn-00bd7c08) → [`00bd7c0c`](#insn-00bd7c0c)
- ブロック [`00bd7c0c`](#insn-00bd7c0c) 範囲 `[['00bd7c0c', '00bd7c2f']]`
  - `FALL_THROUGH` [`00bd7c2c`](#insn-00bd7c2c) → [`00bd7c30`](#insn-00bd7c30)
- ブロック [`00bd7c30`](#insn-00bd7c30) 範囲 `[['00bd7c30', '00bd7c5b']]`

## 命令位置別の参照

- [`00bd7bec`](#insn-00bd7bec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7bf0`](#insn-00bd7bf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7c00`](#insn-00bd7c00) → `01127c18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd7c08`](#insn-00bd7c08) → [`00bd7c30`](#insn-00bd7c30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7c10`](#insn-00bd7c10) → `002b3845`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd7c24`](#insn-00bd7c24) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bd7c2c`](#insn-00bd7c2c) → `01127c18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd7c30`](#insn-00bd7c30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7c40`](#insn-00bd7c40) → `00c93318`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bd7c44`](#insn-00bd7c44) → `01127c30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd7c48`](#insn-00bd7c48) → `002b3845`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd7c58`](#insn-00bd7c58) → [`00c5bf90`](../00c5b/00c5bf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd7bec`](#insn-00bd7bec)

~~~json
{
  "source": "00bd7bec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7bf0`](#insn-00bd7bf0)

~~~json
{
  "source": "00bd7bf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7c00`](#insn-00bd7c00)

~~~json
{
  "source": "00bd7c00",
  "target": "01127c18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd7c08`](#insn-00bd7c08)

~~~json
{
  "source": "00bd7c08",
  "target": "00bd7c30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7c10`](#insn-00bd7c10)

~~~json
{
  "source": "00bd7c10",
  "target": "002b3845",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b3841",
  "offset": 4,
  "size": 34,
  "datatype": "string",
  "bytes": "255047256a6176612f7574696c2f636f6e63757272656e742f54696d65556e69",
  "capture_start": "002b3841",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd7c24`](#insn-00bd7c24)

~~~json
{
  "source": "00bd7c24",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd7c2c`](#insn-00bd7c2c)

~~~json
{
  "source": "00bd7c2c",
  "target": "01127c18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd7c30`](#insn-00bd7c30)

~~~json
{
  "source": "00bd7c30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7c40`](#insn-00bd7c40)

~~~json
{
  "source": "00bd7c40",
  "target": "00c93318",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93318",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bd7c44`](#insn-00bd7c44)

~~~json
{
  "source": "00bd7c44",
  "target": "01127c30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd7c48`](#insn-00bd7c48)

~~~json
{
  "source": "00bd7c48",
  "target": "002b3845",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b3841",
  "offset": 4,
  "size": 34,
  "datatype": "string",
  "bytes": "255047256a6176612f7574696c2f636f6e63757272656e742f54696d65556e69",
  "capture_start": "002b3841",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd7c58`](#insn-00bd7c58)

~~~json
{
  "source": "00bd7c58",
  "target": "00c5bf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
