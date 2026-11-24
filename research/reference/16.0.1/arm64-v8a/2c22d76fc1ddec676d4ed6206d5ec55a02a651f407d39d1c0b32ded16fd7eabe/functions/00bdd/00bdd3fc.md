# 00bdd3fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdcfd4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcfd4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-1720f937dbe70fd872111a6dda27fb51)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdd498`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd498.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-baa4a51b5d15b350d2d39f7c95d5ae39)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdd3fc",
  "name": "_ZN8firebase4auth4user13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c90a4a46ba6435203718bcd63b68ca217ba39eeed3712dcb7c7c1a29f482a358",
  "source_text_sha256": "c90a4a46ba6435203718bcd63b68ca217ba39eeed3712dcb7c7c1a29f482a358",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdd3fc",
        "00bdd46b"
      ]
    ],
    "bytes_sha256": "262f0704ef0d1ded21b723621fc171544048323f88380b31d179d2927ebe04ca",
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

- [00c5aef0](../00c5a/00c5aef0.md)
- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseUser"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 642 bytes

~~~c

void _ZN8firebase4auth4user13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126d20 == 0) {
    DAT_01126d20 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseUser",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_01126d20,&DAT_003101e8,1,&DAT_01126da8,
             "com/google/firebase/auth/FirebaseUser");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdd3fc"></a> `00bdd3fc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdd400"></a> `00bdd400` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd404"></a> `00bdd404` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdd408"></a> `00bdd408` | `54 2a 00 b0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdd40c"></a> `00bdd40c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bdd410"></a> `00bdd410` | `81 92 46 f9` | ldr x1,[x20, #0xd20] | `FALL_THROUGH`
<a id="insn-00bdd414"></a> `00bdd414` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdd418"></a> `00bdd418` | `41 01 00 b5` | cbnz x1,0x00bdd440 | `CONDITIONAL_JUMP`
<a id="insn-00bdd41c"></a> `00bdd41c` | `63 b6 ff 90` | adrp x3,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdd420"></a> `00bdd420` | `63 1c 22 91` | add x3,x3,#0x887 | `FALL_THROUGH`
<a id="insn-00bdd424"></a> `00bdd424` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdd428"></a> `00bdd428` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bdd42c"></a> `00bdd42c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdd430"></a> `00bdd430` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdd434"></a> `00bdd434` | `b7 f6 01 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd438"></a> `00bdd438` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bdd43c"></a> `00bdd43c` | `80 92 06 f9` | str x0,[x20, #0xd20] | `FALL_THROUGH`
<a id="insn-00bdd440"></a> `00bdd440` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd444"></a> `00bdd444` | `82 b9 ff f0` | adrp x2,0x310000 | `FALL_THROUGH`
<a id="insn-00bdd448"></a> `00bdd448` | `44 2a 00 b0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdd44c"></a> `00bdd44c` | `65 b6 ff 90` | adrp x5,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdd450"></a> `00bdd450` | `42 a0 07 91` | add x2,x2,#0x1e8 | `FALL_THROUGH`
<a id="insn-00bdd454"></a> `00bdd454` | `84 a0 36 91` | add x4,x4,#0xda8 | `FALL_THROUGH`
<a id="insn-00bdd458"></a> `00bdd458` | `a5 1c 22 91` | add x5,x5,#0x887 | `FALL_THROUGH`
<a id="insn-00bdd45c"></a> `00bdd45c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bdd460"></a> `00bdd460` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdd464"></a> `00bdd464` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdd468"></a> `00bdd468` | `a2 f6 01 14` | b 0x00c5aef0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdd3fc`](#insn-00bdd3fc) 範囲 `[['00bdd3fc', '00bdd41b']]`
  - `CONDITIONAL_JUMP` [`00bdd418`](#insn-00bdd418) → [`00bdd440`](#insn-00bdd440)
  - `FALL_THROUGH` [`00bdd418`](#insn-00bdd418) → [`00bdd41c`](#insn-00bdd41c)
- ブロック [`00bdd41c`](#insn-00bdd41c) 範囲 `[['00bdd41c', '00bdd43f']]`
  - `FALL_THROUGH` [`00bdd43c`](#insn-00bdd43c) → [`00bdd440`](#insn-00bdd440)
- ブロック [`00bdd440`](#insn-00bdd440) 範囲 `[['00bdd440', '00bdd46b']]`

## 命令位置別の参照

- [`00bdd3fc`](#insn-00bdd3fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd400`](#insn-00bdd400) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd410`](#insn-00bdd410) → `01126d20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd418`](#insn-00bdd418) → [`00bdd440`](#insn-00bdd440) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd420`](#insn-00bdd420) → `002a9887`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdd434`](#insn-00bdd434) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bdd43c`](#insn-00bdd43c) → `01126d20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd440`](#insn-00bdd440) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd450`](#insn-00bdd450) → `003101e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd454`](#insn-00bdd454) → `01126da8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd458`](#insn-00bdd458) → `002a9887`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdd468`](#insn-00bdd468) → [`00c5aef0`](../00c5a/00c5aef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aef0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdd3fc`](#insn-00bdd3fc)

~~~json
{
  "source": "00bdd3fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd400`](#insn-00bdd400)

~~~json
{
  "source": "00bdd400",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd410`](#insn-00bdd410)

~~~json
{
  "source": "00bdd410",
  "target": "01126d20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd418`](#insn-00bdd418)

~~~json
{
  "source": "00bdd418",
  "target": "00bdd440",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd420`](#insn-00bdd420)

~~~json
{
  "source": "00bdd420",
  "target": "002a9887",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9883",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002a9883",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdd434`](#insn-00bdd434)

~~~json
{
  "source": "00bdd434",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd43c`](#insn-00bdd43c)

~~~json
{
  "source": "00bdd43c",
  "target": "01126d20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd440`](#insn-00bdd440)

~~~json
{
  "source": "00bdd440",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd450`](#insn-00bdd450)

~~~json
{
  "source": "00bdd450",
  "target": "003101e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd454`](#insn-00bdd454)

~~~json
{
  "source": "00bdd454",
  "target": "01126da8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd458`](#insn-00bdd458)

~~~json
{
  "source": "00bdd458",
  "target": "002a9887",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9883",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002a9883",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdd468`](#insn-00bdd468)

~~~json
{
  "source": "00bdd468",
  "target": "00c5aef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
