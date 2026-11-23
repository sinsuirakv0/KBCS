# 00aedd8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aede54`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aede54.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-c908841d5655c268cfe605f2cfec33a5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedd8c",
  "name": "_ZN8firebase4util3uri14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e30da6f6cb0726620398d584f4873561be9c78a8c7d9f17918017a94eeed6749",
  "source_text_sha256": "e30da6f6cb0726620398d584f4873561be9c78a8c7d9f17918017a94eeed6749",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedd8c",
        "00aeddfb"
      ]
    ],
    "bytes_sha256": "2aa34905716d8fee5197a45e44e3939ca507b68f59de677c76a5e1a1c101aeb6",
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
"android/net/Uri"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 602 bytes

~~~c

void _ZN8firebase4util3uri14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0960 == 0) {
    DAT_010a0960 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/net/Uri",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0960,&PTR_s_toString_00c10540,2,&DAT_010a0970,"android/net/Uri");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedd8c"></a> `00aedd8c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedd90"></a> `00aedd90` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedd94"></a> `00aedd94` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedd98"></a> `00aedd98` | `94 2d 00 f0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedd9c"></a> `00aedd9c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aedda0"></a> `00aedda0` | `81 b2 44 f9` | ldr x1,[x20, #0x960] | `FALL_THROUGH`
<a id="insn-00aedda4"></a> `00aedda4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aedda8"></a> `00aedda8` | `41 01 00 b5` | cbnz x1,0x00aeddd0 | `CONDITIONAL_JUMP`
<a id="insn-00aeddac"></a> `00aeddac` | `43 bd ff d0` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aeddb0"></a> `00aeddb0` | `63 e0 13 91` | add x3,x3,#0x4f8 | `FALL_THROUGH`
<a id="insn-00aeddb4"></a> `00aeddb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeddb8"></a> `00aeddb8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aeddbc"></a> `00aeddbc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeddc0"></a> `00aeddc0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aeddc4"></a> `00aeddc4` | `73 c0 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeddc8"></a> `00aeddc8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aeddcc"></a> `00aeddcc` | `80 b2 04 f9` | str x0,[x20, #0x960] | `FALL_THROUGH`
<a id="insn-00aeddd0"></a> `00aeddd0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeddd4"></a> `00aeddd4` | `02 09 00 f0` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aeddd8"></a> `00aeddd8` | `84 2d 00 f0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedddc"></a> `00aedddc` | `45 bd ff d0` | adrp x5,0x297000 | `FALL_THROUGH`
<a id="insn-00aedde0"></a> `00aedde0` | `42 00 15 91` | add x2,x2,#0x540 | `FALL_THROUGH`
<a id="insn-00aedde4"></a> `00aedde4` | `84 c0 25 91` | add x4,x4,#0x970 | `FALL_THROUGH`
<a id="insn-00aedde8"></a> `00aedde8` | `a5 e0 13 91` | add x5,x5,#0x4f8 | `FALL_THROUGH`
<a id="insn-00aeddec"></a> `00aeddec` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00aeddf0"></a> `00aeddf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeddf4"></a> `00aeddf4` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeddf8"></a> `00aeddf8` | `6e c0 03 14` | b 0x00bddfb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedd8c`](#insn-00aedd8c) 範囲 `[['00aedd8c', '00aeddab']]`
  - `CONDITIONAL_JUMP` [`00aedda8`](#insn-00aedda8) → [`00aeddd0`](#insn-00aeddd0)
  - `FALL_THROUGH` [`00aedda8`](#insn-00aedda8) → [`00aeddac`](#insn-00aeddac)
- ブロック [`00aeddac`](#insn-00aeddac) 範囲 `[['00aeddac', '00aeddcf']]`
  - `FALL_THROUGH` [`00aeddcc`](#insn-00aeddcc) → [`00aeddd0`](#insn-00aeddd0)
- ブロック [`00aeddd0`](#insn-00aeddd0) 範囲 `[['00aeddd0', '00aeddfb']]`

## 命令位置別の参照

- [`00aedd8c`](#insn-00aedd8c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd90`](#insn-00aedd90) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedda0`](#insn-00aedda0) → `010a0960`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedda8`](#insn-00aedda8) → [`00aeddd0`](#insn-00aeddd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeddb0`](#insn-00aeddb0) → `002974f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeddc4`](#insn-00aeddc4) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aeddcc`](#insn-00aeddcc) → `010a0960`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeddd0`](#insn-00aeddd0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedde0`](#insn-00aedde0) → `00c10540`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aedde4`](#insn-00aedde4) → `010a0970`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedde8`](#insn-00aedde8) → `002974f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeddf8`](#insn-00aeddf8) → [`00bddfb0`](../00bdd/00bddfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedd8c`](#insn-00aedd8c)

~~~json
{
  "source": "00aedd8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd90`](#insn-00aedd90)

~~~json
{
  "source": "00aedd90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedda0`](#insn-00aedda0)

~~~json
{
  "source": "00aedda0",
  "target": "010a0960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0960",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedda8`](#insn-00aedda8)

~~~json
{
  "source": "00aedda8",
  "target": "00aeddd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeddb0`](#insn-00aeddb0)

~~~json
{
  "source": "00aeddb0",
  "target": "002974f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002974f8",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "616e64726f69642f6e65742f55726900",
  "capture_start": "002974f8",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeddc4`](#insn-00aeddc4)

~~~json
{
  "source": "00aeddc4",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeddcc`](#insn-00aeddcc)

~~~json
{
  "source": "00aeddcc",
  "target": "010a0960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0960",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeddd0`](#insn-00aeddd0)

~~~json
{
  "source": "00aeddd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedde0`](#insn-00aedde0)

~~~json
{
  "source": "00aedde0",
  "target": "00c10540",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10540",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aedde4`](#insn-00aedde4)

~~~json
{
  "source": "00aedde4",
  "target": "010a0970",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0970",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedde8`](#insn-00aedde8)

~~~json
{
  "source": "00aedde8",
  "target": "002974f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002974f8",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "616e64726f69642f6e65742f55726900",
  "capture_start": "002974f8",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeddf8`](#insn-00aeddf8)

~~~json
{
  "source": "00aeddf8",
  "target": "00bddfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
