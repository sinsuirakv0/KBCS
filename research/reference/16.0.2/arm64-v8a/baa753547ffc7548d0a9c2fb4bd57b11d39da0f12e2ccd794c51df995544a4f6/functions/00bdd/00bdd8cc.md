# 00bdd8cc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdd830`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd830.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-4f65db2d0b169dd24b159943ab6ec341)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bde8c0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde8c0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-a7905bf875ea5e6a86afa84221b28805)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdd8cc",
  "name": "_ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d8d3c138518da70dd550bd3963d0b7eedeeb7d41483df71f1263832e9147e8a",
  "source_text_sha256": "5d8d3c138518da70dd550bd3963d0b7eedeeb7d41483df71f1263832e9147e8a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdd8cc",
        "00bdd90b"
      ]
    ],
    "bytes_sha256": "515f9d60f02c823f077d72f1cb296d691d40152074dbf96b31b3c2cb5280058c",
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
"%PG%com/google/firebase/auth/FirebaseUserMetadata"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 427 bytes

~~~c

long _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_01126f00 == 0) {
    DAT_01126f00 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126f00;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdd8cc"></a> `00bdd8cc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdd8d0"></a> `00bdd8d0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd8d4"></a> `00bdd8d4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdd8d8"></a> `00bdd8d8` | `53 2a 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdd8dc"></a> `00bdd8dc` | `68 82 47 f9` | ldr x8,[x19, #0xf00] | `FALL_THROUGH`
<a id="insn-00bdd8e0"></a> `00bdd8e0` | `e8 00 00 b5` | cbnz x8,0x00bdd8fc | `CONDITIONAL_JUMP`
<a id="insn-00bdd8e4"></a> `00bdd8e4` | `03 b7 ff b0` | adrp x3,0x2be000 | `FALL_THROUGH`
<a id="insn-00bdd8e8"></a> `00bdd8e8` | `63 64 25 91` | add x3,x3,#0x959 | `FALL_THROUGH`
<a id="insn-00bdd8ec"></a> `00bdd8ec` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdd8f0"></a> `00bdd8f0` | `bc f5 01 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd8f4"></a> `00bdd8f4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bdd8f8"></a> `00bdd8f8` | `60 82 07 f9` | str x0,[x19, #0xf00] | `FALL_THROUGH`
<a id="insn-00bdd8fc"></a> `00bdd8fc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd900"></a> `00bdd900` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bdd904"></a> `00bdd904` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdd908"></a> `00bdd908` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdd8cc`](#insn-00bdd8cc) 範囲 `[['00bdd8cc', '00bdd8e3']]`
  - `CONDITIONAL_JUMP` [`00bdd8e0`](#insn-00bdd8e0) → [`00bdd8fc`](#insn-00bdd8fc)
  - `FALL_THROUGH` [`00bdd8e0`](#insn-00bdd8e0) → [`00bdd8e4`](#insn-00bdd8e4)
- ブロック [`00bdd8e4`](#insn-00bdd8e4) 範囲 `[['00bdd8e4', '00bdd8fb']]`
  - `FALL_THROUGH` [`00bdd8f8`](#insn-00bdd8f8) → [`00bdd8fc`](#insn-00bdd8fc)
- ブロック [`00bdd8fc`](#insn-00bdd8fc) 範囲 `[['00bdd8fc', '00bdd90b']]`

## 命令位置別の参照

- [`00bdd8cc`](#insn-00bdd8cc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd8d0`](#insn-00bdd8d0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd8dc`](#insn-00bdd8dc) → `01126f00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd8e0`](#insn-00bdd8e0) → [`00bdd8fc`](#insn-00bdd8fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd8e8`](#insn-00bdd8e8) → `002be959`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdd8f0`](#insn-00bdd8f0) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bdd8f8`](#insn-00bdd8f8) → `01126f00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd8fc`](#insn-00bdd8fc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdd8cc`](#insn-00bdd8cc)

~~~json
{
  "source": "00bdd8cc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd8d0`](#insn-00bdd8d0)

~~~json
{
  "source": "00bdd8d0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd8dc`](#insn-00bdd8dc)

~~~json
{
  "source": "00bdd8dc",
  "target": "01126f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd8e0`](#insn-00bdd8e0)

~~~json
{
  "source": "00bdd8e0",
  "target": "00bdd8fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd8e8`](#insn-00bdd8e8)

~~~json
{
  "source": "00bdd8e8",
  "target": "002be959",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be955",
  "offset": 4,
  "size": 50,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002be955",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdd8f0`](#insn-00bdd8f0)

~~~json
{
  "source": "00bdd8f0",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd8f8`](#insn-00bdd8f8)

~~~json
{
  "source": "00bdd8f8",
  "target": "01126f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd8fc`](#insn-00bdd8fc)

~~~json
{
  "source": "00bdd8fc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
