# 00bdddc4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bddd28`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddd28.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-94f819089fc8ff1345e3e76c605bcc46)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bdedb8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdedb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-b9af46344420b71a5bf8188f4c8b4383)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdddc4",
  "name": "_ZN8firebase4auth18userprofilebuilder14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fed0ebb23ceee1b6f44265a4e4b61039dbdee756b2b7842d4f73ebcf8e0188b8",
  "source_text_sha256": "fed0ebb23ceee1b6f44265a4e4b61039dbdee756b2b7842d4f73ebcf8e0188b8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdddc4",
        "00bdde33"
      ]
    ],
    "bytes_sha256": "cd0ae8a09c26a1d42eaabbcaeb2906b95651208490be311fe3303ddeec66bbe5",
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
"%PG%com/google/firebase/auth/UserProfileChangeRequest$Builder"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 745 bytes

~~~c

void _ZN8firebase4auth18userprofilebuilder14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126f28 == 0) {
    DAT_01126f28 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/UserProfileChangeRequest$Builder",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126f28,&PTR_s_<init>_00c92908,4,&DAT_01126f38,
             "com/google/firebase/auth/UserProfileChangeRequest$Builder");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdddc4"></a> `00bdddc4` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdddc8"></a> `00bdddc8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdddcc"></a> `00bdddcc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdddd0"></a> `00bdddd0` | `54 2a 00 b0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdddd4"></a> `00bdddd4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bdddd8"></a> `00bdddd8` | `81 96 47 f9` | ldr x1,[x20, #0xf28] | `FALL_THROUGH`
<a id="insn-00bddddc"></a> `00bddddc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bddde0"></a> `00bddde0` | `41 01 00 b5` | cbnz x1,0x00bdde08 | `CONDITIONAL_JUMP`
<a id="insn-00bddde4"></a> `00bddde4` | `83 b6 ff 90` | adrp x3,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bddde8"></a> `00bddde8` | `63 b0 10 91` | add x3,x3,#0x42c | `FALL_THROUGH`
<a id="insn-00bdddec"></a> `00bdddec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdddf0"></a> `00bdddf0` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bdddf4"></a> `00bdddf4` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdddf8"></a> `00bdddf8` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdddfc"></a> `00bdddfc` | `79 f4 01 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdde00"></a> `00bdde00` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bdde04"></a> `00bdde04` | `80 96 07 f9` | str x0,[x20, #0xf28] | `FALL_THROUGH`
<a id="insn-00bdde08"></a> `00bdde08` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdde0c"></a> `00bdde0c` | `a2 05 00 b0` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bdde10"></a> `00bdde10` | `44 2a 00 b0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdde14"></a> `00bdde14` | `85 b6 ff 90` | adrp x5,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bdde18"></a> `00bdde18` | `42 20 24 91` | add x2,x2,#0x908 | `FALL_THROUGH`
<a id="insn-00bdde1c"></a> `00bdde1c` | `84 e0 3c 91` | add x4,x4,#0xf38 | `FALL_THROUGH`
<a id="insn-00bdde20"></a> `00bdde20` | `a5 b0 10 91` | add x5,x5,#0x42c | `FALL_THROUGH`
<a id="insn-00bdde24"></a> `00bdde24` | `83 00 80 52` | mov w3,#0x4 | `FALL_THROUGH`
<a id="insn-00bdde28"></a> `00bdde28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdde2c"></a> `00bdde2c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdde30"></a> `00bdde30` | `74 f4 01 14` | b 0x00c5b000 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdddc4`](#insn-00bdddc4) 範囲 `[['00bdddc4', '00bddde3']]`
  - `CONDITIONAL_JUMP` [`00bddde0`](#insn-00bddde0) → [`00bdde08`](#insn-00bdde08)
  - `FALL_THROUGH` [`00bddde0`](#insn-00bddde0) → [`00bddde4`](#insn-00bddde4)
- ブロック [`00bddde4`](#insn-00bddde4) 範囲 `[['00bddde4', '00bdde07']]`
  - `FALL_THROUGH` [`00bdde04`](#insn-00bdde04) → [`00bdde08`](#insn-00bdde08)
- ブロック [`00bdde08`](#insn-00bdde08) 範囲 `[['00bdde08', '00bdde33']]`

## 命令位置別の参照

- [`00bdddc4`](#insn-00bdddc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdddc8`](#insn-00bdddc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdddd8`](#insn-00bdddd8) → `01126f28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddde0`](#insn-00bddde0) → [`00bdde08`](#insn-00bdde08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddde8`](#insn-00bddde8) → `002ad42c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdddfc`](#insn-00bdddfc) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bdde04`](#insn-00bdde04) → `01126f28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdde08`](#insn-00bdde08) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdde18`](#insn-00bdde18) → `00c92908`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdde1c`](#insn-00bdde1c) → `01126f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdde20`](#insn-00bdde20) → `002ad42c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdde30`](#insn-00bdde30) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdddc4`](#insn-00bdddc4)

~~~json
{
  "source": "00bdddc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdddc8`](#insn-00bdddc8)

~~~json
{
  "source": "00bdddc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdddd8`](#insn-00bdddd8)

~~~json
{
  "source": "00bdddd8",
  "target": "01126f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddde0`](#insn-00bddde0)

~~~json
{
  "source": "00bddde0",
  "target": "00bdde08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddde8`](#insn-00bddde8)

~~~json
{
  "source": "00bddde8",
  "target": "002ad42c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad428",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002ad428",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdddfc`](#insn-00bdddfc)

~~~json
{
  "source": "00bdddfc",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdde04`](#insn-00bdde04)

~~~json
{
  "source": "00bdde04",
  "target": "01126f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdde08`](#insn-00bdde08)

~~~json
{
  "source": "00bdde08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdde18`](#insn-00bdde18)

~~~json
{
  "source": "00bdde18",
  "target": "00c92908",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92908",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdde1c`](#insn-00bdde1c)

~~~json
{
  "source": "00bdde1c",
  "target": "01126f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdde20`](#insn-00bdde20)

~~~json
{
  "source": "00bdde20",
  "target": "002ad42c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad428",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002ad428",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdde30`](#insn-00bdde30)

~~~json
{
  "source": "00bdde30",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
