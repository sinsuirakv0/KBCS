# 00bdda8c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdd664`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd664.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-f37491ae1bff5982d7c9c762552c8687)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bddb28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddb28.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-8e335176b1900d5ebce627e6159b5dde)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdda8c",
  "name": "_ZN8firebase4auth8metadata13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e596ec2818b43926186f865de3d142594f1ad0a142e1e69f6b7751fe225bbd1a",
  "source_text_sha256": "e596ec2818b43926186f865de3d142594f1ad0a142e1e69f6b7751fe225bbd1a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdda8c",
        "00bddafb"
      ]
    ],
    "bytes_sha256": "8c86078f54da0f919871b850a2da3e3b3b6859e82751bfbf39ba69b99d7cab2d",
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
"%PG%com/google/firebase/auth/FirebaseUserMetadata"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 662 bytes

~~~c

void _ZN8firebase4auth8metadata13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126e00 == 0) {
    DAT_01126e00 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseUserMetadata",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_01126e00,&DAT_00310218,1,&DAT_01126e20,
             "com/google/firebase/auth/FirebaseUserMetadata");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdda8c"></a> `00bdda8c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdda90"></a> `00bdda90` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdda94"></a> `00bdda94` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdda98"></a> `00bdda98` | `54 2a 00 b0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdda9c"></a> `00bdda9c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bddaa0"></a> `00bddaa0` | `81 02 47 f9` | ldr x1,[x20, #0xe00] | `FALL_THROUGH`
<a id="insn-00bddaa4"></a> `00bddaa4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bddaa8"></a> `00bddaa8` | `41 01 00 b5` | cbnz x1,0x00bddad0 | `CONDITIONAL_JUMP`
<a id="insn-00bddaac"></a> `00bddaac` | `03 b7 ff b0` | adrp x3,0x2be000 | `FALL_THROUGH`
<a id="insn-00bddab0"></a> `00bddab0` | `63 b4 26 91` | add x3,x3,#0x9ad | `FALL_THROUGH`
<a id="insn-00bddab4"></a> `00bddab4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddab8"></a> `00bddab8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bddabc"></a> `00bddabc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bddac0"></a> `00bddac0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bddac4"></a> `00bddac4` | `13 f5 01 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bddac8"></a> `00bddac8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bddacc"></a> `00bddacc` | `80 02 07 f9` | str x0,[x20, #0xe00] | `FALL_THROUGH`
<a id="insn-00bddad0"></a> `00bddad0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddad4"></a> `00bddad4` | `82 b9 ff f0` | adrp x2,0x310000 | `FALL_THROUGH`
<a id="insn-00bddad8"></a> `00bddad8` | `44 2a 00 b0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddadc"></a> `00bddadc` | `05 b7 ff b0` | adrp x5,0x2be000 | `FALL_THROUGH`
<a id="insn-00bddae0"></a> `00bddae0` | `42 60 08 91` | add x2,x2,#0x218 | `FALL_THROUGH`
<a id="insn-00bddae4"></a> `00bddae4` | `84 80 38 91` | add x4,x4,#0xe20 | `FALL_THROUGH`
<a id="insn-00bddae8"></a> `00bddae8` | `a5 b4 26 91` | add x5,x5,#0x9ad | `FALL_THROUGH`
<a id="insn-00bddaec"></a> `00bddaec` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bddaf0"></a> `00bddaf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddaf4"></a> `00bddaf4` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bddaf8"></a> `00bddaf8` | `fe f4 01 14` | b 0x00c5aef0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdda8c`](#insn-00bdda8c) 範囲 `[['00bdda8c', '00bddaab']]`
  - `CONDITIONAL_JUMP` [`00bddaa8`](#insn-00bddaa8) → [`00bddad0`](#insn-00bddad0)
  - `FALL_THROUGH` [`00bddaa8`](#insn-00bddaa8) → [`00bddaac`](#insn-00bddaac)
- ブロック [`00bddaac`](#insn-00bddaac) 範囲 `[['00bddaac', '00bddacf']]`
  - `FALL_THROUGH` [`00bddacc`](#insn-00bddacc) → [`00bddad0`](#insn-00bddad0)
- ブロック [`00bddad0`](#insn-00bddad0) 範囲 `[['00bddad0', '00bddafb']]`

## 命令位置別の参照

- [`00bdda8c`](#insn-00bdda8c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda90`](#insn-00bdda90) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddaa0`](#insn-00bddaa0) → `01126e00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddaa8`](#insn-00bddaa8) → [`00bddad0`](#insn-00bddad0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddab0`](#insn-00bddab0) → `002be9ad`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddac4`](#insn-00bddac4) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bddacc`](#insn-00bddacc) → `01126e00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddad0`](#insn-00bddad0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddae0`](#insn-00bddae0) → `00310218`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddae4`](#insn-00bddae4) → `01126e20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddae8`](#insn-00bddae8) → `002be9ad`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddaf8`](#insn-00bddaf8) → [`00c5aef0`](../00c5a/00c5aef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aef0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdda8c`](#insn-00bdda8c)

~~~json
{
  "source": "00bdda8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda90`](#insn-00bdda90)

~~~json
{
  "source": "00bdda90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddaa0`](#insn-00bddaa0)

~~~json
{
  "source": "00bddaa0",
  "target": "01126e00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddaa8`](#insn-00bddaa8)

~~~json
{
  "source": "00bddaa8",
  "target": "00bddad0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddab0`](#insn-00bddab0)

~~~json
{
  "source": "00bddab0",
  "target": "002be9ad",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be9a9",
  "offset": 4,
  "size": 50,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002be9a9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddac4`](#insn-00bddac4)

~~~json
{
  "source": "00bddac4",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddacc`](#insn-00bddacc)

~~~json
{
  "source": "00bddacc",
  "target": "01126e00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddad0`](#insn-00bddad0)

~~~json
{
  "source": "00bddad0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddae0`](#insn-00bddae0)

~~~json
{
  "source": "00bddae0",
  "target": "00310218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddae4`](#insn-00bddae4)

~~~json
{
  "source": "00bddae4",
  "target": "01126e20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddae8`](#insn-00bddae8)

~~~json
{
  "source": "00bddae8",
  "target": "002be9ad",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be9a9",
  "offset": 4,
  "size": 50,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002be9a9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddaf8`](#insn-00bddaf8)

~~~json
{
  "source": "00bddaf8",
  "target": "00c5aef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
