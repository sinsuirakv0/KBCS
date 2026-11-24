# 00bddbb8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdd790`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd790.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-273fcca2c70e3f6882810040cc3dc0a7)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bddc54`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc54.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-ee18a04115681de27b8b31ecb587787a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddbb8",
  "name": "_ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d136c6f15fb0a8ed4e023653cc16395c5fc7d513651067c3dce12f2a490420c2",
  "source_text_sha256": "d136c6f15fb0a8ed4e023653cc16395c5fc7d513651067c3dce12f2a490420c2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddbb8",
        "00bddbfb"
      ]
    ],
    "bytes_sha256": "45a18badf2ce3b936b80e27867551f4051b4e3b92ec4bc29a62cd908e9a97071",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/UserProfileChangeRequest$Builder"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 555 bytes

~~~c

long _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_01126e28 == 0) {
    DAT_01126e28 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/UserProfileChangeRequest$Builder",param_3);
  }
  return DAT_01126e28;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddbb8"></a> `00bddbb8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bddbbc"></a> `00bddbbc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddbc0"></a> `00bddbc0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bddbc4"></a> `00bddbc4` | `53 2a 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddbc8"></a> `00bddbc8` | `68 16 47 f9` | ldr x8,[x19, #0xe28] | `FALL_THROUGH`
<a id="insn-00bddbcc"></a> `00bddbcc` | `08 01 00 b5` | cbnz x8,0x00bddbec | `CONDITIONAL_JUMP`
<a id="insn-00bddbd0"></a> `00bddbd0` | `83 b6 ff 90` | adrp x3,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bddbd4"></a> `00bddbd4` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00bddbd8"></a> `00bddbd8` | `63 20 12 91` | add x3,x3,#0x488 | `FALL_THROUGH`
<a id="insn-00bddbdc"></a> `00bddbdc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bddbe0"></a> `00bddbe0` | `cc f4 01 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bddbe4"></a> `00bddbe4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bddbe8"></a> `00bddbe8` | `60 16 07 f9` | str x0,[x19, #0xe28] | `FALL_THROUGH`
<a id="insn-00bddbec"></a> `00bddbec` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddbf0"></a> `00bddbf0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bddbf4"></a> `00bddbf4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bddbf8"></a> `00bddbf8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddbb8`](#insn-00bddbb8) 範囲 `[['00bddbb8', '00bddbcf']]`
  - `CONDITIONAL_JUMP` [`00bddbcc`](#insn-00bddbcc) → [`00bddbec`](#insn-00bddbec)
  - `FALL_THROUGH` [`00bddbcc`](#insn-00bddbcc) → [`00bddbd0`](#insn-00bddbd0)
- ブロック [`00bddbd0`](#insn-00bddbd0) 範囲 `[['00bddbd0', '00bddbeb']]`
  - `FALL_THROUGH` [`00bddbe8`](#insn-00bddbe8) → [`00bddbec`](#insn-00bddbec)
- ブロック [`00bddbec`](#insn-00bddbec) 範囲 `[['00bddbec', '00bddbfb']]`

## 命令位置別の参照

- [`00bddbb8`](#insn-00bddbb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddbbc`](#insn-00bddbbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddbc8`](#insn-00bddbc8) → `01126e28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddbcc`](#insn-00bddbcc) → [`00bddbec`](#insn-00bddbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddbd8`](#insn-00bddbd8) → `002ad488`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddbe0`](#insn-00bddbe0) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bddbe8`](#insn-00bddbe8) → `01126e28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddbec`](#insn-00bddbec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddbb8`](#insn-00bddbb8)

~~~json
{
  "source": "00bddbb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddbbc`](#insn-00bddbbc)

~~~json
{
  "source": "00bddbbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddbc8`](#insn-00bddbc8)

~~~json
{
  "source": "00bddbc8",
  "target": "01126e28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddbcc`](#insn-00bddbcc)

~~~json
{
  "source": "00bddbcc",
  "target": "00bddbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddbd8`](#insn-00bddbd8)

~~~json
{
  "source": "00bddbd8",
  "target": "002ad488",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad484",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002ad484",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddbe0`](#insn-00bddbe0)

~~~json
{
  "source": "00bddbe0",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddbe8`](#insn-00bddbe8)

~~~json
{
  "source": "00bddbe8",
  "target": "01126e28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddbec`](#insn-00bddbec)

~~~json
{
  "source": "00bddbec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
