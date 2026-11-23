# 00aeaa5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeab24`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeab24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-2f8816ff271ab5b29cc31c66c6f1c659)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeaa5c",
  "name": "_ZN8firebase4util11float_class14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cd14ab0cbe1473b69fc4c75c0da3d77c4a7b308dc77b5dbf46ba47044a359c53",
  "source_text_sha256": "cd14ab0cbe1473b69fc4c75c0da3d77c4a7b308dc77b5dbf46ba47044a359c53",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeaa5c",
        "00aeaacb"
      ]
    ],
    "bytes_sha256": "50a7f5a0f65195364b8bc097a00fb97519956034ae8c434d72ae8ce35851d304",
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

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Float"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 609 bytes

~~~c

void _ZN8firebase4util11float_class14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0728 == 0) {
    DAT_010a0728 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Float",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0728,&PTR_s_<init>_00c10288,2,&DAT_010a0738,"java/lang/Float");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeaa5c"></a> `00aeaa5c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeaa60"></a> `00aeaa60` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaa64"></a> `00aeaa64` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeaa68"></a> `00aeaa68` | `b4 2d 00 d0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeaa6c"></a> `00aeaa6c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aeaa70"></a> `00aeaa70` | `81 96 43 f9` | ldr x1,[x20, #0x728] | `FALL_THROUGH`
<a id="insn-00aeaa74"></a> `00aeaa74` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeaa78"></a> `00aeaa78` | `41 01 00 b5` | cbnz x1,0x00aeaaa0 | `CONDITIONAL_JUMP`
<a id="insn-00aeaa7c"></a> `00aeaa7c` | `63 bd ff f0` | adrp x3,0x299000 | `FALL_THROUGH`
<a id="insn-00aeaa80"></a> `00aeaa80` | `63 50 19 91` | add x3,x3,#0x654 | `FALL_THROUGH`
<a id="insn-00aeaa84"></a> `00aeaa84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaa88"></a> `00aeaa88` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aeaa8c"></a> `00aeaa8c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeaa90"></a> `00aeaa90` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aeaa94"></a> `00aeaa94` | `3f cd 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeaa98"></a> `00aeaa98` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aeaa9c"></a> `00aeaa9c` | `80 96 03 f9` | str x0,[x20, #0x728] | `FALL_THROUGH`
<a id="insn-00aeaaa0"></a> `00aeaaa0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaaa4"></a> `00aeaaa4` | `22 09 00 d0` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aeaaa8"></a> `00aeaaa8` | `a4 2d 00 d0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeaaac"></a> `00aeaaac` | `65 bd ff f0` | adrp x5,0x299000 | `FALL_THROUGH`
<a id="insn-00aeaab0"></a> `00aeaab0` | `42 20 0a 91` | add x2,x2,#0x288 | `FALL_THROUGH`
<a id="insn-00aeaab4"></a> `00aeaab4` | `84 e0 1c 91` | add x4,x4,#0x738 | `FALL_THROUGH`
<a id="insn-00aeaab8"></a> `00aeaab8` | `a5 50 19 91` | add x5,x5,#0x654 | `FALL_THROUGH`
<a id="insn-00aeaabc"></a> `00aeaabc` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00aeaac0"></a> `00aeaac0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaac4"></a> `00aeaac4` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeaac8"></a> `00aeaac8` | `3a cd 03 14` | b 0x00bddfb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeaa5c`](#insn-00aeaa5c) 範囲 `[['00aeaa5c', '00aeaa7b']]`
  - `CONDITIONAL_JUMP` [`00aeaa78`](#insn-00aeaa78) → [`00aeaaa0`](#insn-00aeaaa0)
  - `FALL_THROUGH` [`00aeaa78`](#insn-00aeaa78) → [`00aeaa7c`](#insn-00aeaa7c)
- ブロック [`00aeaa7c`](#insn-00aeaa7c) 範囲 `[['00aeaa7c', '00aeaa9f']]`
  - `FALL_THROUGH` [`00aeaa9c`](#insn-00aeaa9c) → [`00aeaaa0`](#insn-00aeaaa0)
- ブロック [`00aeaaa0`](#insn-00aeaaa0) 範囲 `[['00aeaaa0', '00aeaacb']]`

## 命令位置別の参照

- [`00aeaa5c`](#insn-00aeaa5c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaa60`](#insn-00aeaa60) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaa70`](#insn-00aeaa70) → `010a0728`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaa78`](#insn-00aeaa78) → [`00aeaaa0`](#insn-00aeaaa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaa80`](#insn-00aeaa80) → `00299654`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeaa94`](#insn-00aeaa94) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aeaa9c`](#insn-00aeaa9c) → `010a0728`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaaa0`](#insn-00aeaaa0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaab0`](#insn-00aeaab0) → `00c10288`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aeaab4`](#insn-00aeaab4) → `010a0738`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaab8`](#insn-00aeaab8) → `00299654`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeaac8`](#insn-00aeaac8) → [`00bddfb0`](../00bdd/00bddfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeaa5c`](#insn-00aeaa5c)

~~~json
{
  "source": "00aeaa5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaa60`](#insn-00aeaa60)

~~~json
{
  "source": "00aeaa60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaa70`](#insn-00aeaa70)

~~~json
{
  "source": "00aeaa70",
  "target": "010a0728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0728",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaa78`](#insn-00aeaa78)

~~~json
{
  "source": "00aeaa78",
  "target": "00aeaaa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaa80`](#insn-00aeaa80)

~~~json
{
  "source": "00aeaa80",
  "target": "00299654",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00299654",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f466c6f617400",
  "capture_start": "00299654",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeaa94`](#insn-00aeaa94)

~~~json
{
  "source": "00aeaa94",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaa9c`](#insn-00aeaa9c)

~~~json
{
  "source": "00aeaa9c",
  "target": "010a0728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0728",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaaa0`](#insn-00aeaaa0)

~~~json
{
  "source": "00aeaaa0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaab0`](#insn-00aeaab0)

~~~json
{
  "source": "00aeaab0",
  "target": "00c10288",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10288",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeaab4`](#insn-00aeaab4)

~~~json
{
  "source": "00aeaab4",
  "target": "010a0738",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaab8`](#insn-00aeaab8)

~~~json
{
  "source": "00aeaab8",
  "target": "00299654",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00299654",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f466c6f617400",
  "capture_start": "00299654",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeaac8`](#insn-00aeaac8)

~~~json
{
  "source": "00aeaac8",
  "target": "00bddfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
