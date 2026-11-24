# 00bccda8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc980`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc980.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-af9f9fa5e88d0c36bcbfd70d856cc030)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcce44`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcce44.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-2f3ddce33cb415c20250c0ee48493b51)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccda8",
  "name": "_ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c57563c06547892f6b01a59fb822524dcc33838dfdeb649f5d0878ee5fd5820e",
  "source_text_sha256": "c57563c06547892f6b01a59fb822524dcc33838dfdeb649f5d0878ee5fd5820e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccda8",
        "00bccdeb"
      ]
    ],
    "bytes_sha256": "d0f018fe02f7ad28e62168215f24bbbc46f4a51b5b5a09730091615f293fbbc6",
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
"com/google/firebase/auth/internal/cpp/JniIdTokenListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 699 bytes

~~~c

long _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126818 == 0) {
                    /* try { // try from 00bccdcc to 00cccde3 has its CatchHandler @ 00bce8f8 */
    DAT_01126818 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniIdTokenListener",0);
  }
                    /* try { // try from 00bccde4 to 00ccce8f has its CatchHandler @ 00bcc5d0 */
  return DAT_01126818;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccda8"></a> `00bccda8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bccdac"></a> `00bccdac` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccdb0"></a> `00bccdb0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bccdb4"></a> `00bccdb4` | `d3 2a 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccdb8"></a> `00bccdb8` | `68 0e 44 f9` | ldr x8,[x19, #0x818] | `FALL_THROUGH`
<a id="insn-00bccdbc"></a> `00bccdbc` | `08 01 00 b5` | cbnz x8,0x00bccddc | `CONDITIONAL_JUMP`
<a id="insn-00bccdc0"></a> `00bccdc0` | `e3 b6 ff d0` | adrp x3,0x2aa000 | `FALL_THROUGH`
<a id="insn-00bccdc4"></a> `00bccdc4` | `63 28 26 91` | add x3,x3,#0x98a | `FALL_THROUGH`
<a id="insn-00bccdc8"></a> `00bccdc8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bccdcc"></a> `00bccdcc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bccdd0"></a> `00bccdd0` | `50 38 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bccdd4"></a> `00bccdd4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bccdd8"></a> `00bccdd8` | `60 0e 04 f9` | str x0,[x19, #0x818] | `FALL_THROUGH`
<a id="insn-00bccddc"></a> `00bccddc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccde0"></a> `00bccde0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bccde4"></a> `00bccde4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bccde8"></a> `00bccde8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccda8`](#insn-00bccda8) 範囲 `[['00bccda8', '00bccdbf']]`
  - `CONDITIONAL_JUMP` [`00bccdbc`](#insn-00bccdbc) → [`00bccddc`](#insn-00bccddc)
  - `FALL_THROUGH` [`00bccdbc`](#insn-00bccdbc) → [`00bccdc0`](#insn-00bccdc0)
- ブロック [`00bccdc0`](#insn-00bccdc0) 範囲 `[['00bccdc0', '00bccdcb']]`
  - `FALL_THROUGH` [`00bccdc8`](#insn-00bccdc8) → [`00bccdcc`](#insn-00bccdcc)
- ブロック [`00bccdcc`](#insn-00bccdcc) 範囲 `[['00bccdcc', '00bccddb']]`
  - `FALL_THROUGH` [`00bccdd8`](#insn-00bccdd8) → [`00bccddc`](#insn-00bccddc)
- ブロック [`00bccddc`](#insn-00bccddc) 範囲 `[['00bccddc', '00bccde3']]`
  - `FALL_THROUGH` [`00bccde0`](#insn-00bccde0) → [`00bccde4`](#insn-00bccde4)
- ブロック [`00bccde4`](#insn-00bccde4) 範囲 `[['00bccde4', '00bccdeb']]`

## 命令位置別の参照

- [`00bccda8`](#insn-00bccda8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccdac`](#insn-00bccdac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccdb8`](#insn-00bccdb8) → `01126818`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccdbc`](#insn-00bccdbc) → [`00bccddc`](#insn-00bccddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccdc4`](#insn-00bccdc4) → `002aa98a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccdd0`](#insn-00bccdd0) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bccdd8`](#insn-00bccdd8) → `01126818`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccddc`](#insn-00bccddc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccda8`](#insn-00bccda8)

~~~json
{
  "source": "00bccda8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccdac`](#insn-00bccdac)

~~~json
{
  "source": "00bccdac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccdb8`](#insn-00bccdb8)

~~~json
{
  "source": "00bccdb8",
  "target": "01126818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccdbc`](#insn-00bccdbc)

~~~json
{
  "source": "00bccdbc",
  "target": "00bccddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccdc4`](#insn-00bccdc4)

~~~json
{
  "source": "00bccdc4",
  "target": "002aa98a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa98a",
  "offset": 0,
  "size": 57,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002aa98a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bccdd0`](#insn-00bccdd0)

~~~json
{
  "source": "00bccdd0",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccdd8`](#insn-00bccdd8)

~~~json
{
  "source": "00bccdd8",
  "target": "01126818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccddc`](#insn-00bccddc)

~~~json
{
  "source": "00bccddc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
