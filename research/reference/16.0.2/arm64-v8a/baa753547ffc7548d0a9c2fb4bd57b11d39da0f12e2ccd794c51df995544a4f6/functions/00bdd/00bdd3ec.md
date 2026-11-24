# 00bdd3ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdd350`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd350.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-6996b1dbf4306fb51a8065f9234e638c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bde3e0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde3e0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-7c3b40085bd1397895ae5a00c3bff49f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdd3ec",
  "name": "_ZN8firebase4auth4user14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "82921e8144b40e9b7a59d3f1b0fa774eec6657a923a7233d0d54243191d80e68",
  "source_text_sha256": "82921e8144b40e9b7a59d3f1b0fa774eec6657a923a7233d0d54243191d80e68",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdd3ec",
        "00bdd45b"
      ]
    ],
    "bytes_sha256": "c4b8112b7573b5e2a90f6a99b40195d0a7607e58dfd8a88251169d0323f42a87",
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

- [00c5afe0](../00c5a/00c5afe0.md)
- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseUser"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 666 bytes

~~~c

void _ZN8firebase4auth4user14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126e20 == 0) {
    DAT_01126e20 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseUser",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126e20,&PTR_s_isAnonymous_00c926c8,0xf,&DAT_01126e30,
             "com/google/firebase/auth/FirebaseUser");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdd3ec"></a> `00bdd3ec` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdd3f0"></a> `00bdd3f0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd3f4"></a> `00bdd3f4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdd3f8"></a> `00bdd3f8` | `54 2a 00 b0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdd3fc"></a> `00bdd3fc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bdd400"></a> `00bdd400` | `81 12 47 f9` | ldr x1,[x20, #0xe20] | `FALL_THROUGH`
<a id="insn-00bdd404"></a> `00bdd404` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdd408"></a> `00bdd408` | `41 01 00 b5` | cbnz x1,0x00bdd430 | `CONDITIONAL_JUMP`
<a id="insn-00bdd40c"></a> `00bdd40c` | `63 b6 ff 90` | adrp x3,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdd410"></a> `00bdd410` | `63 d8 22 91` | add x3,x3,#0x8b6 | `FALL_THROUGH`
<a id="insn-00bdd414"></a> `00bdd414` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdd418"></a> `00bdd418` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bdd41c"></a> `00bdd41c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdd420"></a> `00bdd420` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdd424"></a> `00bdd424` | `ef f6 01 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd428"></a> `00bdd428` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bdd42c"></a> `00bdd42c` | `80 12 07 f9` | str x0,[x20, #0xe20] | `FALL_THROUGH`
<a id="insn-00bdd430"></a> `00bdd430` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd434"></a> `00bdd434` | `a2 05 00 b0` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bdd438"></a> `00bdd438` | `44 2a 00 b0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdd43c"></a> `00bdd43c` | `65 b6 ff 90` | adrp x5,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdd440"></a> `00bdd440` | `42 20 1b 91` | add x2,x2,#0x6c8 | `FALL_THROUGH`
<a id="insn-00bdd444"></a> `00bdd444` | `84 c0 38 91` | add x4,x4,#0xe30 | `FALL_THROUGH`
<a id="insn-00bdd448"></a> `00bdd448` | `a5 d8 22 91` | add x5,x5,#0x8b6 | `FALL_THROUGH`
<a id="insn-00bdd44c"></a> `00bdd44c` | `e3 01 80 52` | mov w3,#0xf | `FALL_THROUGH`
<a id="insn-00bdd450"></a> `00bdd450` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdd454"></a> `00bdd454` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdd458"></a> `00bdd458` | `ea f6 01 14` | b 0x00c5b000 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdd3ec`](#insn-00bdd3ec) 範囲 `[['00bdd3ec', '00bdd40b']]`
  - `CONDITIONAL_JUMP` [`00bdd408`](#insn-00bdd408) → [`00bdd430`](#insn-00bdd430)
  - `FALL_THROUGH` [`00bdd408`](#insn-00bdd408) → [`00bdd40c`](#insn-00bdd40c)
- ブロック [`00bdd40c`](#insn-00bdd40c) 範囲 `[['00bdd40c', '00bdd42f']]`
  - `FALL_THROUGH` [`00bdd42c`](#insn-00bdd42c) → [`00bdd430`](#insn-00bdd430)
- ブロック [`00bdd430`](#insn-00bdd430) 範囲 `[['00bdd430', '00bdd45b']]`

## 命令位置別の参照

- [`00bdd3ec`](#insn-00bdd3ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd3f0`](#insn-00bdd3f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd400`](#insn-00bdd400) → `01126e20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd408`](#insn-00bdd408) → [`00bdd430`](#insn-00bdd430) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd410`](#insn-00bdd410) → `002a98b6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdd424`](#insn-00bdd424) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bdd42c`](#insn-00bdd42c) → `01126e20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd430`](#insn-00bdd430) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd440`](#insn-00bdd440) → `00c926c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdd444`](#insn-00bdd444) → `01126e30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd448`](#insn-00bdd448) → `002a98b6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdd458`](#insn-00bdd458) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdd3ec`](#insn-00bdd3ec)

~~~json
{
  "source": "00bdd3ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd3f0`](#insn-00bdd3f0)

~~~json
{
  "source": "00bdd3f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd400`](#insn-00bdd400)

~~~json
{
  "source": "00bdd400",
  "target": "01126e20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd408`](#insn-00bdd408)

~~~json
{
  "source": "00bdd408",
  "target": "00bdd430",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd410`](#insn-00bdd410)

~~~json
{
  "source": "00bdd410",
  "target": "002a98b6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a98b2",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002a98b2",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdd424`](#insn-00bdd424)

~~~json
{
  "source": "00bdd424",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd42c`](#insn-00bdd42c)

~~~json
{
  "source": "00bdd42c",
  "target": "01126e20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd430`](#insn-00bdd430)

~~~json
{
  "source": "00bdd430",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd440`](#insn-00bdd440)

~~~json
{
  "source": "00bdd440",
  "target": "00c926c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c926c8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdd444`](#insn-00bdd444)

~~~json
{
  "source": "00bdd444",
  "target": "01126e30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd448`](#insn-00bdd448)

~~~json
{
  "source": "00bdd448",
  "target": "002a98b6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a98b2",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002a98b2",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdd458`](#insn-00bdd458)

~~~json
{
  "source": "00bdd458",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
