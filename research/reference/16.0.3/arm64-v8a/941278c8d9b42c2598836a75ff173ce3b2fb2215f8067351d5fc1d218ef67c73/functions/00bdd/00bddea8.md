# 00bddea8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdceb4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdceb4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-9c32cf8a8e4fcd3de47c08e3f36f7794)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddea8",
  "name": "_ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5956d4badc4d9ccc8a88aacbc0c89e9934e80644c637eb969372e100881b7476",
  "source_text_sha256": "5956d4badc4d9ccc8a88aacbc0c89e9934e80644c637eb969372e100881b7476",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddea8",
        "00bddee7"
      ]
    ],
    "bytes_sha256": "bce803b11c55a81da62b3e3b7ba1a74d4e7df7d9cfd91059e73a10bb38d8aa95",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
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
"%PG%com/google/firebase/auth/GetTokenResult"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 458 bytes

~~~c

long _ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE
               (void)

{
  if (DAT_01127dc0 == 0) {
    DAT_01127dc0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01127dc0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddea8"></a> `00bddea8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bddeac"></a> `00bddeac` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddeb0"></a> `00bddeb0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bddeb4"></a> `00bddeb4` | `53 2a 00 d0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bddeb8"></a> `00bddeb8` | `68 e2 46 f9` | ldr x8,[x19, #0xdc0] | `FALL_THROUGH`
<a id="insn-00bddebc"></a> `00bddebc` | `e8 00 00 b5` | cbnz x8,0x00bdded8 | `CONDITIONAL_JUMP`
<a id="insn-00bddec0"></a> `00bddec0` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00bddec4"></a> `00bddec4` | `e3 b6 ff f0` | adrp x3,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bddec8"></a> `00bddec8` | `63 68 0b 91` | add x3,x3,#0x2da | `FALL_THROUGH`
<a id="insn-00bddecc"></a> `00bddecc` | `39 f8 01 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdded0"></a> `00bdded0` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bdded4"></a> `00bdded4` | `60 e2 06 f9` | str x0,[x19, #0xdc0] | `FALL_THROUGH`
<a id="insn-00bdded8"></a> `00bdded8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddedc"></a> `00bddedc` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bddee0"></a> `00bddee0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bddee4"></a> `00bddee4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddea8`](#insn-00bddea8) 範囲 `[['00bddea8', '00bddebf']]`
  - `CONDITIONAL_JUMP` [`00bddebc`](#insn-00bddebc) → [`00bdded8`](#insn-00bdded8)
  - `FALL_THROUGH` [`00bddebc`](#insn-00bddebc) → [`00bddec0`](#insn-00bddec0)
- ブロック [`00bddec0`](#insn-00bddec0) 範囲 `[['00bddec0', '00bdded7']]`
  - `FALL_THROUGH` [`00bdded4`](#insn-00bdded4) → [`00bdded8`](#insn-00bdded8)
- ブロック [`00bdded8`](#insn-00bdded8) 範囲 `[['00bdded8', '00bddee7']]`

## 命令位置別の参照

- [`00bddea8`](#insn-00bddea8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddeac`](#insn-00bddeac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddeb8`](#insn-00bddeb8) → `01127dc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddebc`](#insn-00bddebc) → [`00bdded8`](#insn-00bdded8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddec8`](#insn-00bddec8) → `002bc2da`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddecc`](#insn-00bddecc) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bdded4`](#insn-00bdded4) → `01127dc0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdded8`](#insn-00bdded8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddea8`](#insn-00bddea8)

~~~json
{
  "source": "00bddea8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddeac`](#insn-00bddeac)

~~~json
{
  "source": "00bddeac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddeb8`](#insn-00bddeb8)

~~~json
{
  "source": "00bddeb8",
  "target": "01127dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127dc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddebc`](#insn-00bddebc)

~~~json
{
  "source": "00bddebc",
  "target": "00bdded8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddec8`](#insn-00bddec8)

~~~json
{
  "source": "00bddec8",
  "target": "002bc2da",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc2d6",
  "offset": 4,
  "size": 44,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f476574",
  "capture_start": "002bc2d6",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddecc`](#insn-00bddecc)

~~~json
{
  "source": "00bddecc",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdded4`](#insn-00bdded4)

~~~json
{
  "source": "00bdded4",
  "target": "01127dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127dc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdded8`](#insn-00bdded8)

~~~json
{
  "source": "00bdded8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
