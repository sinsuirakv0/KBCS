# 00bddbd4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bddb38`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddb38.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-73f2fa1a6b2e934e6a9374a425d62865)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bdebc8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdebc8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-35a5ca1d7cef5bf5e43e2f9cfc0097b9)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddbd4",
  "name": "_ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6fb6d63ce932b5b162f169cb94eecffe6f561e0baf25fd42b2518a238ee28138",
  "source_text_sha256": "6fb6d63ce932b5b162f169cb94eecffe6f561e0baf25fd42b2518a238ee28138",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddbd4",
        "00bddc13"
      ]
    ],
    "bytes_sha256": "93cc75034e26b66980f22b16fd5b99b33d4a1c24bc7e51254ccf1695d80c3853",
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
"%PG%com/google/firebase/auth/UserProfileChangeRequest$Builder"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 465 bytes

~~~c

long _ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE
               (void)

{
  if (DAT_01126f28 == 0) {
    DAT_01126f28 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126f28;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddbd4"></a> `00bddbd4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bddbd8"></a> `00bddbd8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddbdc"></a> `00bddbdc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bddbe0"></a> `00bddbe0` | `53 2a 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddbe4"></a> `00bddbe4` | `68 96 47 f9` | ldr x8,[x19, #0xf28] | `FALL_THROUGH`
<a id="insn-00bddbe8"></a> `00bddbe8` | `e8 00 00 b5` | cbnz x8,0x00bddc04 | `CONDITIONAL_JUMP`
<a id="insn-00bddbec"></a> `00bddbec` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00bddbf0"></a> `00bddbf0` | `83 b6 ff 90` | adrp x3,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bddbf4"></a> `00bddbf4` | `63 b0 10 91` | add x3,x3,#0x42c | `FALL_THROUGH`
<a id="insn-00bddbf8"></a> `00bddbf8` | `fa f4 01 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bddbfc"></a> `00bddbfc` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bddc00"></a> `00bddc00` | `60 96 07 f9` | str x0,[x19, #0xf28] | `FALL_THROUGH`
<a id="insn-00bddc04"></a> `00bddc04` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddc08"></a> `00bddc08` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bddc0c"></a> `00bddc0c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bddc10"></a> `00bddc10` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddbd4`](#insn-00bddbd4) 範囲 `[['00bddbd4', '00bddbeb']]`
  - `CONDITIONAL_JUMP` [`00bddbe8`](#insn-00bddbe8) → [`00bddc04`](#insn-00bddc04)
  - `FALL_THROUGH` [`00bddbe8`](#insn-00bddbe8) → [`00bddbec`](#insn-00bddbec)
- ブロック [`00bddbec`](#insn-00bddbec) 範囲 `[['00bddbec', '00bddc03']]`
  - `FALL_THROUGH` [`00bddc00`](#insn-00bddc00) → [`00bddc04`](#insn-00bddc04)
- ブロック [`00bddc04`](#insn-00bddc04) 範囲 `[['00bddc04', '00bddc13']]`

## 命令位置別の参照

- [`00bddbd4`](#insn-00bddbd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddbd8`](#insn-00bddbd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddbe4`](#insn-00bddbe4) → `01126f28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddbe8`](#insn-00bddbe8) → [`00bddc04`](#insn-00bddc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddbf4`](#insn-00bddbf4) → `002ad42c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddbf8`](#insn-00bddbf8) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bddc00`](#insn-00bddc00) → `01126f28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddc04`](#insn-00bddc04) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddbd4`](#insn-00bddbd4)

~~~json
{
  "source": "00bddbd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddbd8`](#insn-00bddbd8)

~~~json
{
  "source": "00bddbd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddbe4`](#insn-00bddbe4)

~~~json
{
  "source": "00bddbe4",
  "target": "01126f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddbe8`](#insn-00bddbe8)

~~~json
{
  "source": "00bddbe8",
  "target": "00bddc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddbf4`](#insn-00bddbf4)

~~~json
{
  "source": "00bddbf4",
  "target": "002ad42c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad428",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002ad428",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddbf8`](#insn-00bddbf8)

~~~json
{
  "source": "00bddbf8",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddc00`](#insn-00bddc00)

~~~json
{
  "source": "00bddc00",
  "target": "01126f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddc04`](#insn-00bddc04)

~~~json
{
  "source": "00bddc04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
