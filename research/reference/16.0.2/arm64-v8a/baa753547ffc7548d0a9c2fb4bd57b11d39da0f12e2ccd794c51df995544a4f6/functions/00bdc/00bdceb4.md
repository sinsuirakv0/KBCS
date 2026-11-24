# 00bdceb4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdce18`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce18.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-29b6a65d9746ffc5f163786ea4450db0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bddea8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bddea8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-9c32cf8a8e4fcd3de47c08e3f36f7794)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdceb4",
  "name": "_ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "474badc6523bf3484b1b211a417ef74e19339ab7266782329bd223399d6bea84",
  "source_text_sha256": "474badc6523bf3484b1b211a417ef74e19339ab7266782329bd223399d6bea84",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdceb4",
        "00bdcef3"
      ]
    ],
    "bytes_sha256": "9b52ab147457452bd8b9157aaed6e53db2c133e72392996be9e913ffc26e7fa5",
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

- [00c5afe0](../00c5a/00c5afe0.md)

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
  if (DAT_01126e00 == 0) {
    DAT_01126e00 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126e00;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdceb4"></a> `00bdceb4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdceb8"></a> `00bdceb8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcebc"></a> `00bdcebc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdcec0"></a> `00bdcec0` | `53 2a 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdcec4"></a> `00bdcec4` | `68 02 47 f9` | ldr x8,[x19, #0xe00] | `FALL_THROUGH`
<a id="insn-00bdcec8"></a> `00bdcec8` | `e8 00 00 b5` | cbnz x8,0x00bdcee4 | `CONDITIONAL_JUMP`
<a id="insn-00bdcecc"></a> `00bdcecc` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00bdced0"></a> `00bdced0` | `03 b7 ff 90` | adrp x3,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bdced4"></a> `00bdced4` | `63 f0 07 91` | add x3,x3,#0x1fc | `FALL_THROUGH`
<a id="insn-00bdced8"></a> `00bdced8` | `42 f8 01 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcedc"></a> `00bdcedc` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bdcee0"></a> `00bdcee0` | `60 02 07 f9` | str x0,[x19, #0xe00] | `FALL_THROUGH`
<a id="insn-00bdcee4"></a> `00bdcee4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcee8"></a> `00bdcee8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bdceec"></a> `00bdceec` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdcef0"></a> `00bdcef0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdceb4`](#insn-00bdceb4) 範囲 `[['00bdceb4', '00bdcecb']]`
  - `CONDITIONAL_JUMP` [`00bdcec8`](#insn-00bdcec8) → [`00bdcee4`](#insn-00bdcee4)
  - `FALL_THROUGH` [`00bdcec8`](#insn-00bdcec8) → [`00bdcecc`](#insn-00bdcecc)
- ブロック [`00bdcecc`](#insn-00bdcecc) 範囲 `[['00bdcecc', '00bdcee3']]`
  - `FALL_THROUGH` [`00bdcee0`](#insn-00bdcee0) → [`00bdcee4`](#insn-00bdcee4)
- ブロック [`00bdcee4`](#insn-00bdcee4) 範囲 `[['00bdcee4', '00bdcef3']]`

## 命令位置別の参照

- [`00bdceb4`](#insn-00bdceb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdceb8`](#insn-00bdceb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcec4`](#insn-00bdcec4) → `01126e00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcec8`](#insn-00bdcec8) → [`00bdcee4`](#insn-00bdcee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdced4`](#insn-00bdced4) → `002bc1fc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdced8`](#insn-00bdced8) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bdcee0`](#insn-00bdcee0) → `01126e00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcee4`](#insn-00bdcee4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdceb4`](#insn-00bdceb4)

~~~json
{
  "source": "00bdceb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdceb8`](#insn-00bdceb8)

~~~json
{
  "source": "00bdceb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcec4`](#insn-00bdcec4)

~~~json
{
  "source": "00bdcec4",
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
- 参照命令 [`00bdcec8`](#insn-00bdcec8)

~~~json
{
  "source": "00bdcec8",
  "target": "00bdcee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdced4`](#insn-00bdced4)

~~~json
{
  "source": "00bdced4",
  "target": "002bc1fc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc1f8",
  "offset": 4,
  "size": 44,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f476574",
  "capture_start": "002bc1f8",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdced8`](#insn-00bdced8)

~~~json
{
  "source": "00bdced8",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcee0`](#insn-00bdcee0)

~~~json
{
  "source": "00bdcee0",
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
- 参照命令 [`00bdcee4`](#insn-00bdcee4)

~~~json
{
  "source": "00bdcee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
