# 00bd0cbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b617bc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b617bc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0017.md#compare-1d143625bddcb740c54c8c6335d35d98)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd10e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd10e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-780e49760fcf61c2d8657c3f148ab569)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd0cbc",
  "name": "_ZN8firebase4auth21action_code_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "81d95053edf923cbec0b7027e247832931842d02df54a1c05406d0e286603090",
  "source_text_sha256": "81d95053edf923cbec0b7027e247832931842d02df54a1c05406d0e286603090",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd0cbc",
        "00bd0cfb"
      ]
    ],
    "bytes_sha256": "d655f487f67f6e69c91bf324e10f358466b9745a9aa124ad0d903d5a3f871f2b",
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

- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseAuthActionCodeException"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 635 bytes

~~~c

long _ZN8firebase4auth21action_code_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
                    /* try { // try from 00bd0ccc to 00cd0ce7 has its CatchHandler @ 00bd65d0 */
  if (DAT_011264c8 == 0) {
    DAT_011264c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
                    /* try { // try from 00bd0ce8 to 00cd0d7f has its CatchHandler @ 00bd075c */
  }
  return DAT_011264c8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd0cbc"></a> `00bd0cbc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd0cc0"></a> `00bd0cc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0cc4"></a> `00bd0cc4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd0cc8"></a> `00bd0cc8` | `b3 2a 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd0ccc"></a> `00bd0ccc` | `68 66 42 f9` | ldr x8,[x19, #0x4c8] | `FALL_THROUGH`
<a id="insn-00bd0cd0"></a> `00bd0cd0` | `e8 00 00 b5` | cbnz x8,0x00bd0cec | `CONDITIONAL_JUMP`
<a id="insn-00bd0cd4"></a> `00bd0cd4` | `a3 b6 ff 90` | adrp x3,0x2a4000 | `FALL_THROUGH`
<a id="insn-00bd0cd8"></a> `00bd0cd8` | `63 cc 3c 91` | add x3,x3,#0xf33 | `FALL_THROUGH`
<a id="insn-00bd0cdc"></a> `00bd0cdc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bd0ce0"></a> `00bd0ce0` | `8c 27 02 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0ce4"></a> `00bd0ce4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bd0ce8"></a> `00bd0ce8` | `60 66 02 f9` | str x0,[x19, #0x4c8] | `FALL_THROUGH`
<a id="insn-00bd0cec"></a> `00bd0cec` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0cf0"></a> `00bd0cf0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bd0cf4"></a> `00bd0cf4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd0cf8"></a> `00bd0cf8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd0cbc`](#insn-00bd0cbc) 範囲 `[['00bd0cbc', '00bd0ccb']]`
  - `FALL_THROUGH` [`00bd0cc8`](#insn-00bd0cc8) → [`00bd0ccc`](#insn-00bd0ccc)
- ブロック [`00bd0ccc`](#insn-00bd0ccc) 範囲 `[['00bd0ccc', '00bd0cd3']]`
  - `CONDITIONAL_JUMP` [`00bd0cd0`](#insn-00bd0cd0) → [`00bd0cec`](#insn-00bd0cec)
  - `FALL_THROUGH` [`00bd0cd0`](#insn-00bd0cd0) → [`00bd0cd4`](#insn-00bd0cd4)
- ブロック [`00bd0cd4`](#insn-00bd0cd4) 範囲 `[['00bd0cd4', '00bd0ce7']]`
  - `FALL_THROUGH` [`00bd0ce4`](#insn-00bd0ce4) → [`00bd0ce8`](#insn-00bd0ce8)
- ブロック [`00bd0ce8`](#insn-00bd0ce8) 範囲 `[['00bd0ce8', '00bd0ceb']]`
  - `FALL_THROUGH` [`00bd0ce8`](#insn-00bd0ce8) → [`00bd0cec`](#insn-00bd0cec)
- ブロック [`00bd0cec`](#insn-00bd0cec) 範囲 `[['00bd0cec', '00bd0cfb']]`

## 命令位置別の参照

- [`00bd0cbc`](#insn-00bd0cbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0cc0`](#insn-00bd0cc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0ccc`](#insn-00bd0ccc) → `011264c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd0cd0`](#insn-00bd0cd0) → [`00bd0cec`](#insn-00bd0cec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0cd8`](#insn-00bd0cd8) → `002a4f33`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd0ce0`](#insn-00bd0ce0) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bd0ce8`](#insn-00bd0ce8) → `011264c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd0cec`](#insn-00bd0cec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd0cbc`](#insn-00bd0cbc)

~~~json
{
  "source": "00bd0cbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0cc0`](#insn-00bd0cc0)

~~~json
{
  "source": "00bd0cc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0ccc`](#insn-00bd0ccc)

~~~json
{
  "source": "00bd0ccc",
  "target": "011264c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011264c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0cd0`](#insn-00bd0cd0)

~~~json
{
  "source": "00bd0cd0",
  "target": "00bd0cec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0cd8`](#insn-00bd0cd8)

~~~json
{
  "source": "00bd0cd8",
  "target": "002a4f33",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4f2f",
  "offset": 4,
  "size": 61,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002a4f2f",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd0ce0`](#insn-00bd0ce0)

~~~json
{
  "source": "00bd0ce0",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0ce8`](#insn-00bd0ce8)

~~~json
{
  "source": "00bd0ce8",
  "target": "011264c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011264c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd0cec`](#insn-00bd0cec)

~~~json
{
  "source": "00bd0cec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
