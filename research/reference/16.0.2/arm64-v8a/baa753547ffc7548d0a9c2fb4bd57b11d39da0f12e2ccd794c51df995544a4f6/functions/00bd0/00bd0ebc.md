# 00bd0ebc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd0e20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0e20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0082.md#compare-4e7bdcb3f34d74e2d257a945e50d738a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd1eb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd1eb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0082.md#compare-cd5db42458c7b2fdf5b42e1daf8febdc)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd0ebc",
  "name": "_ZN8firebase4auth27api_not_available_exception10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "126be4242c4afbf2e0daa33ab79501ada9cb5bd8d8143ed819303ae4d5afc264",
  "source_text_sha256": "126be4242c4afbf2e0daa33ab79501ada9cb5bd8d8143ed819303ae4d5afc264",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd0ebc",
        "00bd0eff"
      ]
    ],
    "bytes_sha256": "3859d582b109a12ddabac2ff4d7f846e12b1abb8bea588a20f975d694d78b961",
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
"%PG%com/google/firebase/FirebaseApiNotAvailableException"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 604 bytes

~~~c

long _ZN8firebase4auth27api_not_available_exception10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_011269a8 == 0) {
                    /* try { // try from 00bd0ee4 to 00cd0eeb has its CatchHandler @ 00bd67c8 */
    DAT_011269a8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/FirebaseApiNotAvailableException",0);
  }
  return DAT_011269a8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd0ebc"></a> `00bd0ebc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd0ec0"></a> `00bd0ec0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0ec4"></a> `00bd0ec4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd0ec8"></a> `00bd0ec8` | `b3 2a 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd0ecc"></a> `00bd0ecc` | `68 d6 44 f9` | ldr x8,[x19, #0x9a8] | `FALL_THROUGH`
<a id="insn-00bd0ed0"></a> `00bd0ed0` | `08 01 00 b5` | cbnz x8,0x00bd0ef0 | `CONDITIONAL_JUMP`
<a id="insn-00bd0ed4"></a> `00bd0ed4` | `a3 b6 ff f0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bd0ed8"></a> `00bd0ed8` | `63 d0 0f 91` | add x3,x3,#0x3f4 | `FALL_THROUGH`
<a id="insn-00bd0edc"></a> `00bd0edc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bd0ee0"></a> `00bd0ee0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bd0ee4"></a> `00bd0ee4` | `3f 28 02 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0ee8"></a> `00bd0ee8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bd0eec"></a> `00bd0eec` | `60 d6 04 f9` | str x0,[x19, #0x9a8] | `FALL_THROUGH`
<a id="insn-00bd0ef0"></a> `00bd0ef0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0ef4"></a> `00bd0ef4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bd0ef8"></a> `00bd0ef8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd0efc"></a> `00bd0efc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd0ebc`](#insn-00bd0ebc) 範囲 `[['00bd0ebc', '00bd0ed3']]`
  - `CONDITIONAL_JUMP` [`00bd0ed0`](#insn-00bd0ed0) → [`00bd0ef0`](#insn-00bd0ef0)
  - `FALL_THROUGH` [`00bd0ed0`](#insn-00bd0ed0) → [`00bd0ed4`](#insn-00bd0ed4)
- ブロック [`00bd0ed4`](#insn-00bd0ed4) 範囲 `[['00bd0ed4', '00bd0ee3']]`
  - `FALL_THROUGH` [`00bd0ee0`](#insn-00bd0ee0) → [`00bd0ee4`](#insn-00bd0ee4)
- ブロック [`00bd0ee4`](#insn-00bd0ee4) 範囲 `[['00bd0ee4', '00bd0eef']]`
  - `FALL_THROUGH` [`00bd0eec`](#insn-00bd0eec) → [`00bd0ef0`](#insn-00bd0ef0)
- ブロック [`00bd0ef0`](#insn-00bd0ef0) 範囲 `[['00bd0ef0', '00bd0eff']]`

## 命令位置別の参照

- [`00bd0ebc`](#insn-00bd0ebc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0ec0`](#insn-00bd0ec0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0ecc`](#insn-00bd0ecc) → `011269a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd0ed0`](#insn-00bd0ed0) → [`00bd0ef0`](#insn-00bd0ef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0ed8`](#insn-00bd0ed8) → `002a73f4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd0ee4`](#insn-00bd0ee4) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bd0eec`](#insn-00bd0eec) → `011269a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd0ef0`](#insn-00bd0ef0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd0ebc`](#insn-00bd0ebc)

~~~json
{
  "source": "00bd0ebc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0ec0`](#insn-00bd0ec0)

~~~json
{
  "source": "00bd0ec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0ecc`](#insn-00bd0ecc)

~~~json
{
  "source": "00bd0ecc",
  "target": "011269a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0ed0`](#insn-00bd0ed0)

~~~json
{
  "source": "00bd0ed0",
  "target": "00bd0ef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0ed8`](#insn-00bd0ed8)

~~~json
{
  "source": "00bd0ed8",
  "target": "002a73f4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a73f0",
  "offset": 4,
  "size": 57,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f4669726562617365",
  "capture_start": "002a73f0",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd0ee4`](#insn-00bd0ee4)

~~~json
{
  "source": "00bd0ee4",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0eec`](#insn-00bd0eec)

~~~json
{
  "source": "00bd0eec",
  "target": "011269a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0ef0`](#insn-00bd0ef0)

~~~json
{
  "source": "00bd0ef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
