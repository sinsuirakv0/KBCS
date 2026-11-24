# 00bd1abc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bd1694`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1694.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0082.md#compare-9edf18d35343f6bd5574e4bfb9cffde3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd1b58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd1b58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0082.md#compare-5af6b83305f487697b052833939110f6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd1abc",
  "name": "_ZN8firebase4auth29invalid_credentials_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "da0f03ea6ddc3705f9c7ad7479411c015a8fe36ec81216af543ba21c95725946",
  "source_text_sha256": "da0f03ea6ddc3705f9c7ad7479411c015a8fe36ec81216af543ba21c95725946",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd1abc",
        "00bd1afb"
      ]
    ],
    "bytes_sha256": "ceee492207361e3d47d48b6e3e040777be1ba0eb167a22239d4efa8b2ce75a21",
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

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseAuthInvalidCredentialsException"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 449 bytes

~~~c

long _ZN8firebase4auth29invalid_credentials_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_01126928 == 0) {
    DAT_01126928 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126928;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd1abc"></a> `00bd1abc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd1ac0"></a> `00bd1ac0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1ac4"></a> `00bd1ac4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd1ac8"></a> `00bd1ac8` | `b3 2a 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd1acc"></a> `00bd1acc` | `68 96 44 f9` | ldr x8,[x19, #0x928] | `FALL_THROUGH`
<a id="insn-00bd1ad0"></a> `00bd1ad0` | `e8 00 00 b5` | cbnz x8,0x00bd1aec | `CONDITIONAL_JUMP`
<a id="insn-00bd1ad4"></a> `00bd1ad4` | `43 b7 ff 90` | adrp x3,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bd1ad8"></a> `00bd1ad8` | `63 38 32 91` | add x3,x3,#0xc8e | `FALL_THROUGH`
<a id="insn-00bd1adc"></a> `00bd1adc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bd1ae0"></a> `00bd1ae0` | `0c 25 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bd1ae4"></a> `00bd1ae4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bd1ae8"></a> `00bd1ae8` | `60 96 04 f9` | str x0,[x19, #0x928] | `FALL_THROUGH`
<a id="insn-00bd1aec"></a> `00bd1aec` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1af0"></a> `00bd1af0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bd1af4"></a> `00bd1af4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd1af8"></a> `00bd1af8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd1abc`](#insn-00bd1abc) 範囲 `[['00bd1abc', '00bd1ad3']]`
  - `CONDITIONAL_JUMP` [`00bd1ad0`](#insn-00bd1ad0) → [`00bd1aec`](#insn-00bd1aec)
  - `FALL_THROUGH` [`00bd1ad0`](#insn-00bd1ad0) → [`00bd1ad4`](#insn-00bd1ad4)
- ブロック [`00bd1ad4`](#insn-00bd1ad4) 範囲 `[['00bd1ad4', '00bd1aeb']]`
  - `FALL_THROUGH` [`00bd1ae8`](#insn-00bd1ae8) → [`00bd1aec`](#insn-00bd1aec)
- ブロック [`00bd1aec`](#insn-00bd1aec) 範囲 `[['00bd1aec', '00bd1afb']]`

## 命令位置別の参照

- [`00bd1abc`](#insn-00bd1abc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1ac0`](#insn-00bd1ac0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1acc`](#insn-00bd1acc) → `01126928`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd1ad0`](#insn-00bd1ad0) → [`00bd1aec`](#insn-00bd1aec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1ad8`](#insn-00bd1ad8) → `002b9c8e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd1ae0`](#insn-00bd1ae0) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bd1ae8`](#insn-00bd1ae8) → `01126928`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd1aec`](#insn-00bd1aec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd1abc`](#insn-00bd1abc)

~~~json
{
  "source": "00bd1abc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1ac0`](#insn-00bd1ac0)

~~~json
{
  "source": "00bd1ac0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1acc`](#insn-00bd1acc)

~~~json
{
  "source": "00bd1acc",
  "target": "01126928",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126928",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd1ad0`](#insn-00bd1ad0)

~~~json
{
  "source": "00bd1ad0",
  "target": "00bd1aec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1ad8`](#insn-00bd1ad8)

~~~json
{
  "source": "00bd1ad8",
  "target": "002b9c8e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9c8a",
  "offset": 4,
  "size": 69,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002b9c8a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd1ae0`](#insn-00bd1ae0)

~~~json
{
  "source": "00bd1ae0",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd1ae8`](#insn-00bd1ae8)

~~~json
{
  "source": "00bd1ae8",
  "target": "01126928",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126928",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd1aec`](#insn-00bd1aec)

~~~json
{
  "source": "00bd1aec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
