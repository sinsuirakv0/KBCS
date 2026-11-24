# 00bd6ccc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bd68a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd68a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0084.md#compare-b7fd1e5b4b700a1e480919943ac04df4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd6d68`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6d68.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0084.md#compare-c38c4f0f9c35941ba46dbddbe3e16714)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd6ccc",
  "name": "_ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "daddb01462c08847ea69f43ed9ddf5611d959b145820943e293ae6a50e89b2e7",
  "source_text_sha256": "daddb01462c08847ea69f43ed9ddf5611d959b145820943e293ae6a50e89b2e7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd6ccc",
        "00bd6d0f"
      ]
    ],
    "bytes_sha256": "9176e6e0997b37717881f2a3200b27a96b71df5e18107afb7450f7eac4c1d55b",
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
"%PG%com/google/firebase/auth/PhoneAuthOptions$Builder"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 503 bytes

~~~c

long _ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126b78 == 0) {
    DAT_01126b78 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/PhoneAuthOptions$Builder",
                              0);
  }
  return DAT_01126b78;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd6ccc"></a> `00bd6ccc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd6cd0"></a> `00bd6cd0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd6cd4"></a> `00bd6cd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd6cd8"></a> `00bd6cd8` | `93 2a 00 90` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd6cdc"></a> `00bd6cdc` | `68 be 45 f9` | ldr x8,[x19, #0xb78] | `FALL_THROUGH`
<a id="insn-00bd6ce0"></a> `00bd6ce0` | `08 01 00 b5` | cbnz x8,0x00bd6d00 | `CONDITIONAL_JUMP`
<a id="insn-00bd6ce4"></a> `00bd6ce4` | `43 b6 ff b0` | adrp x3,0x29f000 | `FALL_THROUGH`
<a id="insn-00bd6ce8"></a> `00bd6ce8` | `63 c4 34 91` | add x3,x3,#0xd31 | `FALL_THROUGH`
<a id="insn-00bd6cec"></a> `00bd6cec` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bd6cf0"></a> `00bd6cf0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bd6cf4"></a> `00bd6cf4` | `87 10 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bd6cf8"></a> `00bd6cf8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bd6cfc"></a> `00bd6cfc` | `60 be 05 f9` | str x0,[x19, #0xb78] | `FALL_THROUGH`
<a id="insn-00bd6d00"></a> `00bd6d00` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd6d04"></a> `00bd6d04` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bd6d08"></a> `00bd6d08` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd6d0c"></a> `00bd6d0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd6ccc`](#insn-00bd6ccc) 範囲 `[['00bd6ccc', '00bd6ce3']]`
  - `CONDITIONAL_JUMP` [`00bd6ce0`](#insn-00bd6ce0) → [`00bd6d00`](#insn-00bd6d00)
  - `FALL_THROUGH` [`00bd6ce0`](#insn-00bd6ce0) → [`00bd6ce4`](#insn-00bd6ce4)
- ブロック [`00bd6ce4`](#insn-00bd6ce4) 範囲 `[['00bd6ce4', '00bd6cff']]`
  - `FALL_THROUGH` [`00bd6cfc`](#insn-00bd6cfc) → [`00bd6d00`](#insn-00bd6d00)
- ブロック [`00bd6d00`](#insn-00bd6d00) 範囲 `[['00bd6d00', '00bd6d0f']]`

## 命令位置別の参照

- [`00bd6ccc`](#insn-00bd6ccc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6cd0`](#insn-00bd6cd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6cdc`](#insn-00bd6cdc) → `01126b78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd6ce0`](#insn-00bd6ce0) → [`00bd6d00`](#insn-00bd6d00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6ce8`](#insn-00bd6ce8) → `0029fd31`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd6cf4`](#insn-00bd6cf4) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bd6cfc`](#insn-00bd6cfc) → `01126b78`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd6d00`](#insn-00bd6d00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd6ccc`](#insn-00bd6ccc)

~~~json
{
  "source": "00bd6ccc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6cd0`](#insn-00bd6cd0)

~~~json
{
  "source": "00bd6cd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6cdc`](#insn-00bd6cdc)

~~~json
{
  "source": "00bd6cdc",
  "target": "01126b78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126b78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd6ce0`](#insn-00bd6ce0)

~~~json
{
  "source": "00bd6ce0",
  "target": "00bd6d00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6ce8`](#insn-00bd6ce8)

~~~json
{
  "source": "00bd6ce8",
  "target": "0029fd31",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fd2d",
  "offset": 4,
  "size": 54,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f50686f",
  "capture_start": "0029fd2d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd6cf4`](#insn-00bd6cf4)

~~~json
{
  "source": "00bd6cf4",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd6cfc`](#insn-00bd6cfc)

~~~json
{
  "source": "00bd6cfc",
  "target": "01126b78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126b78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd6d00`](#insn-00bd6d00)

~~~json
{
  "source": "00bd6d00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
