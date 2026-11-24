# 00bccafc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcca60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcca60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-7a31af082cb838f9657b9b516c1176b3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcdaf0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcdaf0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-624fd929d51a8fe2b6c4e1b628d3f6e1)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccafc",
  "name": "_ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "684f4ec45613a386bb5105fdaa7c169e9af78587809e51f933ac0a147a15304b",
  "source_text_sha256": "684f4ec45613a386bb5105fdaa7c169e9af78587809e51f933ac0a147a15304b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccafc",
        "00bccb3f"
      ]
    ],
    "bytes_sha256": "163ed2624b2fdb784f13f1b38e89e3cdffa0f15db3ea1b1c521142a0484048b3",
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
"com/google/firebase/auth/internal/cpp/JniAuthStateListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 497 bytes

~~~c

long _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_011268f0 == 0) {
    DAT_011268f0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniAuthStateListener",0);
  }
  return DAT_011268f0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccafc"></a> `00bccafc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bccb00"></a> `00bccb00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccb04"></a> `00bccb04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bccb08"></a> `00bccb08` | `d3 2a 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccb0c"></a> `00bccb0c` | `68 7a 44 f9` | ldr x8,[x19, #0x8f0] | `FALL_THROUGH`
<a id="insn-00bccb10"></a> `00bccb10` | `08 01 00 b5` | cbnz x8,0x00bccb30 | `CONDITIONAL_JUMP`
<a id="insn-00bccb14"></a> `00bccb14` | `43 b7 ff b0` | adrp x3,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bccb18"></a> `00bccb18` | `63 68 30 91` | add x3,x3,#0xc1a | `FALL_THROUGH`
<a id="insn-00bccb1c"></a> `00bccb1c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bccb20"></a> `00bccb20` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bccb24"></a> `00bccb24` | `2f 39 02 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bccb28"></a> `00bccb28` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bccb2c"></a> `00bccb2c` | `60 7a 04 f9` | str x0,[x19, #0x8f0] | `FALL_THROUGH`
<a id="insn-00bccb30"></a> `00bccb30` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccb34"></a> `00bccb34` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bccb38"></a> `00bccb38` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bccb3c"></a> `00bccb3c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccafc`](#insn-00bccafc) 範囲 `[['00bccafc', '00bccb13']]`
  - `CONDITIONAL_JUMP` [`00bccb10`](#insn-00bccb10) → [`00bccb30`](#insn-00bccb30)
  - `FALL_THROUGH` [`00bccb10`](#insn-00bccb10) → [`00bccb14`](#insn-00bccb14)
- ブロック [`00bccb14`](#insn-00bccb14) 範囲 `[['00bccb14', '00bccb2f']]`
  - `FALL_THROUGH` [`00bccb2c`](#insn-00bccb2c) → [`00bccb30`](#insn-00bccb30)
- ブロック [`00bccb30`](#insn-00bccb30) 範囲 `[['00bccb30', '00bccb3f']]`

## 命令位置別の参照

- [`00bccafc`](#insn-00bccafc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb00`](#insn-00bccb00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb0c`](#insn-00bccb0c) → `011268f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccb10`](#insn-00bccb10) → [`00bccb30`](#insn-00bccb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb18`](#insn-00bccb18) → `002b5c1a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccb24`](#insn-00bccb24) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bccb2c`](#insn-00bccb2c) → `011268f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccb30`](#insn-00bccb30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccafc`](#insn-00bccafc)

~~~json
{
  "source": "00bccafc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb00`](#insn-00bccb00)

~~~json
{
  "source": "00bccb00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb0c`](#insn-00bccb0c)

~~~json
{
  "source": "00bccb0c",
  "target": "011268f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccb10`](#insn-00bccb10)

~~~json
{
  "source": "00bccb10",
  "target": "00bccb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb18`](#insn-00bccb18)

~~~json
{
  "source": "00bccb18",
  "target": "002b5c1a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5c1a",
  "offset": 0,
  "size": 59,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002b5c1a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bccb24`](#insn-00bccb24)

~~~json
{
  "source": "00bccb24",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccb2c`](#insn-00bccb2c)

~~~json
{
  "source": "00bccb2c",
  "target": "011268f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccb30`](#insn-00bccb30)

~~~json
{
  "source": "00bccb30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
