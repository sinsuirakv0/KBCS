# 00bcca1c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc5f4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-384d015984c70cb56358b95c49d2c7b1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccab8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccab8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-ddcc870def1bf538414c8f5b2a32f01d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcca1c",
  "name": "_ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d124abc80a44f48a0b0284c1d7424db0c93e16a3c4b5159b936081e75adda0d",
  "source_text_sha256": "7d124abc80a44f48a0b0284c1d7424db0c93e16a3c4b5159b936081e75adda0d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcca1c",
        "00bcca5f"
      ]
    ],
    "bytes_sha256": "8bf11175d446c20cf5f8afaa78e15ecded5966af3eb96087f8c682c819fb5aa9",
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
"com/google/firebase/auth/internal/cpp/JniAuthStateListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 743 bytes

~~~c

long _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
                    /* try { // try from 00bcca24 to 00ccca3b has its CatchHandler @ 00bce90c */
  if (DAT_011267f0 == 0) {
                    /* try { // try from 00bcca3c to 00cccaef has its CatchHandler @ 00bcc5d0 */
    DAT_011267f0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniAuthStateListener",param_3);
  }
  return DAT_011267f0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcca1c"></a> `00bcca1c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcca20"></a> `00bcca20` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcca24"></a> `00bcca24` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcca28"></a> `00bcca28` | `d3 2a 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcca2c"></a> `00bcca2c` | `68 fa 43 f9` | ldr x8,[x19, #0x7f0] | `FALL_THROUGH`
<a id="insn-00bcca30"></a> `00bcca30` | `08 01 00 b5` | cbnz x8,0x00bcca50 | `CONDITIONAL_JUMP`
<a id="insn-00bcca34"></a> `00bcca34` | `43 b7 ff b0` | adrp x3,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bcca38"></a> `00bcca38` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00bcca3c"></a> `00bcca3c` | `63 68 2f 91` | add x3,x3,#0xbda | `FALL_THROUGH`
<a id="insn-00bcca40"></a> `00bcca40` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bcca44"></a> `00bcca44` | `33 39 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcca48"></a> `00bcca48` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcca4c"></a> `00bcca4c` | `60 fa 03 f9` | str x0,[x19, #0x7f0] | `FALL_THROUGH`
<a id="insn-00bcca50"></a> `00bcca50` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcca54"></a> `00bcca54` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcca58"></a> `00bcca58` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcca5c"></a> `00bcca5c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcca1c`](#insn-00bcca1c) 範囲 `[['00bcca1c', '00bcca23']]`
  - `FALL_THROUGH` [`00bcca20`](#insn-00bcca20) → [`00bcca24`](#insn-00bcca24)
- ブロック [`00bcca24`](#insn-00bcca24) 範囲 `[['00bcca24', '00bcca33']]`
  - `CONDITIONAL_JUMP` [`00bcca30`](#insn-00bcca30) → [`00bcca50`](#insn-00bcca50)
  - `FALL_THROUGH` [`00bcca30`](#insn-00bcca30) → [`00bcca34`](#insn-00bcca34)
- ブロック [`00bcca34`](#insn-00bcca34) 範囲 `[['00bcca34', '00bcca3b']]`
  - `FALL_THROUGH` [`00bcca38`](#insn-00bcca38) → [`00bcca3c`](#insn-00bcca3c)
- ブロック [`00bcca3c`](#insn-00bcca3c) 範囲 `[['00bcca3c', '00bcca4f']]`
  - `FALL_THROUGH` [`00bcca4c`](#insn-00bcca4c) → [`00bcca50`](#insn-00bcca50)
- ブロック [`00bcca50`](#insn-00bcca50) 範囲 `[['00bcca50', '00bcca5f']]`

## 命令位置別の参照

- [`00bcca1c`](#insn-00bcca1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcca20`](#insn-00bcca20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcca2c`](#insn-00bcca2c) → `011267f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcca30`](#insn-00bcca30) → [`00bcca50`](#insn-00bcca50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcca3c`](#insn-00bcca3c) → `002b5bda`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcca44`](#insn-00bcca44) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bcca4c`](#insn-00bcca4c) → `011267f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcca50`](#insn-00bcca50) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcca1c`](#insn-00bcca1c)

~~~json
{
  "source": "00bcca1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcca20`](#insn-00bcca20)

~~~json
{
  "source": "00bcca20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcca2c`](#insn-00bcca2c)

~~~json
{
  "source": "00bcca2c",
  "target": "011267f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcca30`](#insn-00bcca30)

~~~json
{
  "source": "00bcca30",
  "target": "00bcca50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcca3c`](#insn-00bcca3c)

~~~json
{
  "source": "00bcca3c",
  "target": "002b5bda",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5bda",
  "offset": 0,
  "size": 59,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002b5bda",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcca44`](#insn-00bcca44)

~~~json
{
  "source": "00bcca44",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcca4c`](#insn-00bcca4c)

~~~json
{
  "source": "00bcca4c",
  "target": "011267f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcca50`](#insn-00bcca50)

~~~json
{
  "source": "00bcca50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
