# 00bdda7c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdd9e0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd9e0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-feb49f3f76328d55cbfedb6b3eb78678)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bdea70`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdea70.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-c29733d81f2e0bc1931d60a22d26da12)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdda7c",
  "name": "_ZN8firebase4auth8metadata14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7dd8ff67e3e740dbc2e073d8995bb04b7ecdbf26d57de23a08ad82ac9f8d87bf",
  "source_text_sha256": "7dd8ff67e3e740dbc2e073d8995bb04b7ecdbf26d57de23a08ad82ac9f8d87bf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdda7c",
        "00bddaeb"
      ]
    ],
    "bytes_sha256": "d2238ddda62e4a881ed392e443dcb2906c8d73fd511ef0d1c75c76b8d4935d7c",
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
"%PG%com/google/firebase/auth/FirebaseUserMetadata"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 695 bytes

~~~c

void _ZN8firebase4auth8metadata14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126f00 == 0) {
    DAT_01126f00 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseUserMetadata",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126f00,&PTR_s_getLastSignInTimestamp_00c928d8,2,&DAT_01126f10,
             "com/google/firebase/auth/FirebaseUserMetadata");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdda7c"></a> `00bdda7c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdda80"></a> `00bdda80` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdda84"></a> `00bdda84` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdda88"></a> `00bdda88` | `54 2a 00 b0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdda8c"></a> `00bdda8c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bdda90"></a> `00bdda90` | `81 82 47 f9` | ldr x1,[x20, #0xf00] | `FALL_THROUGH`
<a id="insn-00bdda94"></a> `00bdda94` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdda98"></a> `00bdda98` | `41 01 00 b5` | cbnz x1,0x00bddac0 | `CONDITIONAL_JUMP`
<a id="insn-00bdda9c"></a> `00bdda9c` | `03 b7 ff b0` | adrp x3,0x2be000 | `FALL_THROUGH`
<a id="insn-00bddaa0"></a> `00bddaa0` | `63 64 25 91` | add x3,x3,#0x959 | `FALL_THROUGH`
<a id="insn-00bddaa4"></a> `00bddaa4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddaa8"></a> `00bddaa8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bddaac"></a> `00bddaac` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bddab0"></a> `00bddab0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bddab4"></a> `00bddab4` | `4b f5 01 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bddab8"></a> `00bddab8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bddabc"></a> `00bddabc` | `80 82 07 f9` | str x0,[x20, #0xf00] | `FALL_THROUGH`
<a id="insn-00bddac0"></a> `00bddac0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddac4"></a> `00bddac4` | `a2 05 00 b0` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bddac8"></a> `00bddac8` | `44 2a 00 b0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddacc"></a> `00bddacc` | `05 b7 ff b0` | adrp x5,0x2be000 | `FALL_THROUGH`
<a id="insn-00bddad0"></a> `00bddad0` | `42 60 23 91` | add x2,x2,#0x8d8 | `FALL_THROUGH`
<a id="insn-00bddad4"></a> `00bddad4` | `84 40 3c 91` | add x4,x4,#0xf10 | `FALL_THROUGH`
<a id="insn-00bddad8"></a> `00bddad8` | `a5 64 25 91` | add x5,x5,#0x959 | `FALL_THROUGH`
<a id="insn-00bddadc"></a> `00bddadc` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00bddae0"></a> `00bddae0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddae4"></a> `00bddae4` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bddae8"></a> `00bddae8` | `46 f5 01 14` | b 0x00c5b000 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdda7c`](#insn-00bdda7c) 範囲 `[['00bdda7c', '00bdda9b']]`
  - `CONDITIONAL_JUMP` [`00bdda98`](#insn-00bdda98) → [`00bddac0`](#insn-00bddac0)
  - `FALL_THROUGH` [`00bdda98`](#insn-00bdda98) → [`00bdda9c`](#insn-00bdda9c)
- ブロック [`00bdda9c`](#insn-00bdda9c) 範囲 `[['00bdda9c', '00bddabf']]`
  - `FALL_THROUGH` [`00bddabc`](#insn-00bddabc) → [`00bddac0`](#insn-00bddac0)
- ブロック [`00bddac0`](#insn-00bddac0) 範囲 `[['00bddac0', '00bddaeb']]`

## 命令位置別の参照

- [`00bdda7c`](#insn-00bdda7c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda80`](#insn-00bdda80) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda90`](#insn-00bdda90) → `01126f00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdda98`](#insn-00bdda98) → [`00bddac0`](#insn-00bddac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddaa0`](#insn-00bddaa0) → `002be959`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddab4`](#insn-00bddab4) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bddabc`](#insn-00bddabc) → `01126f00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddac0`](#insn-00bddac0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddad0`](#insn-00bddad0) → `00c928d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddad4`](#insn-00bddad4) → `01126f10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddad8`](#insn-00bddad8) → `002be959`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddae8`](#insn-00bddae8) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdda7c`](#insn-00bdda7c)

~~~json
{
  "source": "00bdda7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda80`](#insn-00bdda80)

~~~json
{
  "source": "00bdda80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda90`](#insn-00bdda90)

~~~json
{
  "source": "00bdda90",
  "target": "01126f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdda98`](#insn-00bdda98)

~~~json
{
  "source": "00bdda98",
  "target": "00bddac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddaa0`](#insn-00bddaa0)

~~~json
{
  "source": "00bddaa0",
  "target": "002be959",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be955",
  "offset": 4,
  "size": 50,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002be955",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddab4`](#insn-00bddab4)

~~~json
{
  "source": "00bddab4",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddabc`](#insn-00bddabc)

~~~json
{
  "source": "00bddabc",
  "target": "01126f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddac0`](#insn-00bddac0)

~~~json
{
  "source": "00bddac0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddad0`](#insn-00bddad0)

~~~json
{
  "source": "00bddad0",
  "target": "00c928d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c928d8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddad4`](#insn-00bddad4)

~~~json
{
  "source": "00bddad4",
  "target": "01126f10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddad8`](#insn-00bddad8)

~~~json
{
  "source": "00bddad8",
  "target": "002be959",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be955",
  "offset": 4,
  "size": 50,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002be955",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddae8`](#insn-00bddae8)

~~~json
{
  "source": "00bddae8",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
