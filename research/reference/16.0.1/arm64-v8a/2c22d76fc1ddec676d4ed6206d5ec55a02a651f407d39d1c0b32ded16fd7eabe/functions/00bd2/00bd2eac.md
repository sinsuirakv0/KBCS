# 00bd2eac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bd2a84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a84.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0083.md#compare-30ae11e1dc886b8ca45eafd0bb93a15a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd2f48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd2/00bd2f48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0083.md#compare-47eeb142a3a8d1da7caa878e62b02f29)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd2eac",
  "name": "_ZN8firebase4auth26firebase_network_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2084fb3c265c8c96a3bcaae1244b7ff900fb999278c5752703f94a34d90aea70",
  "source_text_sha256": "2084fb3c265c8c96a3bcaae1244b7ff900fb999278c5752703f94a34d90aea70",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd2eac",
        "00bd2eef"
      ]
    ],
    "bytes_sha256": "345314dd1eb3d0520d89c056bc21a7e7bcd6b1285b91da6db6b5d2c16a0c246d",
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
"%PG%com/google/firebase/FirebaseNetworkException"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 550 bytes

~~~c

long _ZN8firebase4auth26firebase_network_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_011269e8 == 0) {
    DAT_011269e8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/FirebaseNetworkException",
                              param_3);
  }
  return DAT_011269e8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd2eac"></a> `00bd2eac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd2eb0"></a> `00bd2eb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2eb4"></a> `00bd2eb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd2eb8"></a> `00bd2eb8` | `b3 2a 00 90` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd2ebc"></a> `00bd2ebc` | `68 f6 44 f9` | ldr x8,[x19, #0x9e8] | `FALL_THROUGH`
<a id="insn-00bd2ec0"></a> `00bd2ec0` | `08 01 00 b5` | cbnz x8,0x00bd2ee0 | `CONDITIONAL_JUMP`
<a id="insn-00bd2ec4"></a> `00bd2ec4` | `63 b7 ff b0` | adrp x3,0x2bf000 | `FALL_THROUGH`
<a id="insn-00bd2ec8"></a> `00bd2ec8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00bd2ecc"></a> `00bd2ecc` | `63 5c 29 91` | add x3,x3,#0xa57 | `FALL_THROUGH`
<a id="insn-00bd2ed0"></a> `00bd2ed0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bd2ed4"></a> `00bd2ed4` | `0f 20 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2ed8"></a> `00bd2ed8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bd2edc"></a> `00bd2edc` | `60 f6 04 f9` | str x0,[x19, #0x9e8] | `FALL_THROUGH`
<a id="insn-00bd2ee0"></a> `00bd2ee0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2ee4"></a> `00bd2ee4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bd2ee8"></a> `00bd2ee8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd2eec"></a> `00bd2eec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd2eac`](#insn-00bd2eac) 範囲 `[['00bd2eac', '00bd2ec3']]`
  - `CONDITIONAL_JUMP` [`00bd2ec0`](#insn-00bd2ec0) → [`00bd2ee0`](#insn-00bd2ee0)
  - `FALL_THROUGH` [`00bd2ec0`](#insn-00bd2ec0) → [`00bd2ec4`](#insn-00bd2ec4)
- ブロック [`00bd2ec4`](#insn-00bd2ec4) 範囲 `[['00bd2ec4', '00bd2edf']]`
  - `FALL_THROUGH` [`00bd2edc`](#insn-00bd2edc) → [`00bd2ee0`](#insn-00bd2ee0)
- ブロック [`00bd2ee0`](#insn-00bd2ee0) 範囲 `[['00bd2ee0', '00bd2eef']]`

## 命令位置別の参照

- [`00bd2eac`](#insn-00bd2eac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2eb0`](#insn-00bd2eb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2ebc`](#insn-00bd2ebc) → `011269e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd2ec0`](#insn-00bd2ec0) → [`00bd2ee0`](#insn-00bd2ee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2ecc`](#insn-00bd2ecc) → `002bfa57`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd2ed4`](#insn-00bd2ed4) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bd2edc`](#insn-00bd2edc) → `011269e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd2ee0`](#insn-00bd2ee0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd2eac`](#insn-00bd2eac)

~~~json
{
  "source": "00bd2eac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2eb0`](#insn-00bd2eb0)

~~~json
{
  "source": "00bd2eb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2ebc`](#insn-00bd2ebc)

~~~json
{
  "source": "00bd2ebc",
  "target": "011269e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd2ec0`](#insn-00bd2ec0)

~~~json
{
  "source": "00bd2ec0",
  "target": "00bd2ee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2ecc`](#insn-00bd2ecc)

~~~json
{
  "source": "00bd2ecc",
  "target": "002bfa57",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bfa53",
  "offset": 4,
  "size": 49,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f4669726562617365",
  "capture_start": "002bfa53",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd2ed4`](#insn-00bd2ed4)

~~~json
{
  "source": "00bd2ed4",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2edc`](#insn-00bd2edc)

~~~json
{
  "source": "00bd2edc",
  "target": "011269e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd2ee0`](#insn-00bd2ee0)

~~~json
{
  "source": "00bd2ee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
