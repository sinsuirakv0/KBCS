# 00bd1bdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd1b40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1b40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0082.md#compare-4756c31eba169aa68083a8c0c064cd62)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd2bd0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd2/00bd2bd0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0082.md#compare-87d4c0ae29757d6e2c17018eedc6bf3c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd1bdc",
  "name": "_ZN8firebase4auth29invalid_credentials_exception10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "69e501a83510070b4844419bf09349bfd21574c92c4977eba1cf4e4018837b9b",
  "source_text_sha256": "69e501a83510070b4844419bf09349bfd21574c92c4977eba1cf4e4018837b9b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd1bdc",
        "00bd1c1f"
      ]
    ],
    "bytes_sha256": "931547374176387560817034315bb84737bb50947ab412eeca2c7d610fd19143",
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

- [00c5afe0](../00c5a/00c5afe0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseAuthInvalidCredentialsException"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 618 bytes

~~~c

long _ZN8firebase4auth29invalid_credentials_exception10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00bd1be0 to 00cd1f33 has its CatchHandler @ 00bd6a24 */
  if (DAT_01126a28 == 0) {
    DAT_01126a28 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/FirebaseAuthInvalidCredentialsException",0);
  }
  return DAT_01126a28;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd1bdc"></a> `00bd1bdc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd1be0"></a> `00bd1be0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1be4"></a> `00bd1be4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd1be8"></a> `00bd1be8` | `b3 2a 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd1bec"></a> `00bd1bec` | `68 16 45 f9` | ldr x8,[x19, #0xa28] | `FALL_THROUGH`
<a id="insn-00bd1bf0"></a> `00bd1bf0` | `08 01 00 b5` | cbnz x8,0x00bd1c10 | `CONDITIONAL_JUMP`
<a id="insn-00bd1bf4"></a> `00bd1bf4` | `43 b7 ff 90` | adrp x3,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bd1bf8"></a> `00bd1bf8` | `63 e8 30 91` | add x3,x3,#0xc3a | `FALL_THROUGH`
<a id="insn-00bd1bfc"></a> `00bd1bfc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bd1c00"></a> `00bd1c00` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bd1c04"></a> `00bd1c04` | `f7 24 02 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd1c08"></a> `00bd1c08` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bd1c0c"></a> `00bd1c0c` | `60 16 05 f9` | str x0,[x19, #0xa28] | `FALL_THROUGH`
<a id="insn-00bd1c10"></a> `00bd1c10` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1c14"></a> `00bd1c14` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bd1c18"></a> `00bd1c18` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd1c1c"></a> `00bd1c1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd1bdc`](#insn-00bd1bdc) 範囲 `[['00bd1bdc', '00bd1bdf']]`
  - `FALL_THROUGH` [`00bd1bdc`](#insn-00bd1bdc) → [`00bd1be0`](#insn-00bd1be0)
- ブロック [`00bd1be0`](#insn-00bd1be0) 範囲 `[['00bd1be0', '00bd1bf3']]`
  - `CONDITIONAL_JUMP` [`00bd1bf0`](#insn-00bd1bf0) → [`00bd1c10`](#insn-00bd1c10)
  - `FALL_THROUGH` [`00bd1bf0`](#insn-00bd1bf0) → [`00bd1bf4`](#insn-00bd1bf4)
- ブロック [`00bd1bf4`](#insn-00bd1bf4) 範囲 `[['00bd1bf4', '00bd1c0f']]`
  - `FALL_THROUGH` [`00bd1c0c`](#insn-00bd1c0c) → [`00bd1c10`](#insn-00bd1c10)
- ブロック [`00bd1c10`](#insn-00bd1c10) 範囲 `[['00bd1c10', '00bd1c1f']]`

## 命令位置別の参照

- [`00bd1bdc`](#insn-00bd1bdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1be0`](#insn-00bd1be0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1bec`](#insn-00bd1bec) → `01126a28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd1bf0`](#insn-00bd1bf0) → [`00bd1c10`](#insn-00bd1c10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1bf8`](#insn-00bd1bf8) → `002b9c3a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd1c04`](#insn-00bd1c04) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c0c`](#insn-00bd1c0c) → `01126a28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd1c10`](#insn-00bd1c10) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd1bdc`](#insn-00bd1bdc)

~~~json
{
  "source": "00bd1bdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1be0`](#insn-00bd1be0)

~~~json
{
  "source": "00bd1be0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1bec`](#insn-00bd1bec)

~~~json
{
  "source": "00bd1bec",
  "target": "01126a28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd1bf0`](#insn-00bd1bf0)

~~~json
{
  "source": "00bd1bf0",
  "target": "00bd1c10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1bf8`](#insn-00bd1bf8)

~~~json
{
  "source": "00bd1bf8",
  "target": "002b9c3a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9c36",
  "offset": 4,
  "size": 69,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002b9c36",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd1c04`](#insn-00bd1c04)

~~~json
{
  "source": "00bd1c04",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd1c0c`](#insn-00bd1c0c)

~~~json
{
  "source": "00bd1c0c",
  "target": "01126a28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd1c10`](#insn-00bd1c10)

~~~json
{
  "source": "00bd1c10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
