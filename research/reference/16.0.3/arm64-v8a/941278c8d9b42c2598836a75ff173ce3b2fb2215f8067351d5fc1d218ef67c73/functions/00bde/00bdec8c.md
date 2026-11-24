# 00bdec8c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bddc98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc98.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-9c6c18c19395bff6dd3ffa341e4344a1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdec8c",
  "name": "_ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "06e0cda50a760d681fc3de3376299c7d09dd7ec6c3c5d5f89cb5b3409e5d4f24",
  "source_text_sha256": "06e0cda50a760d681fc3de3376299c7d09dd7ec6c3c5d5f89cb5b3409e5d4f24",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdec8c",
        "00bdeccf"
      ]
    ],
    "bytes_sha256": "96bcff40e5760e0b804a90bd877a14861d72b87c1b0cd71f776390d12c9aa1ea",
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

- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/UserProfileChangeRequest$Builder"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 503 bytes

~~~c

long _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01127ee8 == 0) {
    DAT_01127ee8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/UserProfileChangeRequest$Builder",0);
  }
  return DAT_01127ee8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdec8c"></a> `00bdec8c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdec90"></a> `00bdec90` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdec94"></a> `00bdec94` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdec98"></a> `00bdec98` | `53 2a 00 b0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdec9c"></a> `00bdec9c` | `68 76 47 f9` | ldr x8,[x19, #0xee8] | `FALL_THROUGH`
<a id="insn-00bdeca0"></a> `00bdeca0` | `08 01 00 b5` | cbnz x8,0x00bdecc0 | `CONDITIONAL_JUMP`
<a id="insn-00bdeca4"></a> `00bdeca4` | `63 b6 ff f0` | adrp x3,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bdeca8"></a> `00bdeca8` | `63 e4 13 91` | add x3,x3,#0x4f9 | `FALL_THROUGH`
<a id="insn-00bdecac"></a> `00bdecac` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdecb0"></a> `00bdecb0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdecb4"></a> `00bdecb4` | `bf f4 01 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdecb8"></a> `00bdecb8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bdecbc"></a> `00bdecbc` | `60 76 07 f9` | str x0,[x19, #0xee8] | `FALL_THROUGH`
<a id="insn-00bdecc0"></a> `00bdecc0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdecc4"></a> `00bdecc4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bdecc8"></a> `00bdecc8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdeccc"></a> `00bdeccc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdec8c`](#insn-00bdec8c) 範囲 `[['00bdec8c', '00bdeca3']]`
  - `CONDITIONAL_JUMP` [`00bdeca0`](#insn-00bdeca0) → [`00bdecc0`](#insn-00bdecc0)
  - `FALL_THROUGH` [`00bdeca0`](#insn-00bdeca0) → [`00bdeca4`](#insn-00bdeca4)
- ブロック [`00bdeca4`](#insn-00bdeca4) 範囲 `[['00bdeca4', '00bdecbf']]`
  - `FALL_THROUGH` [`00bdecbc`](#insn-00bdecbc) → [`00bdecc0`](#insn-00bdecc0)
- ブロック [`00bdecc0`](#insn-00bdecc0) 範囲 `[['00bdecc0', '00bdeccf']]`

## 命令位置別の参照

- [`00bdec8c`](#insn-00bdec8c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdec90`](#insn-00bdec90) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdec9c`](#insn-00bdec9c) → `01127ee8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdeca0`](#insn-00bdeca0) → [`00bdecc0`](#insn-00bdecc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeca8`](#insn-00bdeca8) → `002ad4f9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdecb4`](#insn-00bdecb4) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bdecbc`](#insn-00bdecbc) → `01127ee8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdecc0`](#insn-00bdecc0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdec8c`](#insn-00bdec8c)

~~~json
{
  "source": "00bdec8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdec90`](#insn-00bdec90)

~~~json
{
  "source": "00bdec90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdec9c`](#insn-00bdec9c)

~~~json
{
  "source": "00bdec9c",
  "target": "01127ee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdeca0`](#insn-00bdeca0)

~~~json
{
  "source": "00bdeca0",
  "target": "00bdecc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeca8`](#insn-00bdeca8)

~~~json
{
  "source": "00bdeca8",
  "target": "002ad4f9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad4f5",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002ad4f5",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdecb4`](#insn-00bdecb4)

~~~json
{
  "source": "00bdecb4",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdecbc`](#insn-00bdecbc)

~~~json
{
  "source": "00bdecbc",
  "target": "01127ee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdecc0`](#insn-00bdecc0)

~~~json
{
  "source": "00bdecc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
