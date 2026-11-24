# 00bdd1fc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdd160`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd160.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-1388b6d98916ba729bb2fab0effd1024)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bde1f0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde1f0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-f9f308045489f57cacaafc3f6e0acf47)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdd1fc",
  "name": "_ZN8firebase4auth4user19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "16c1fa7e1ae3a2f556dc59837236185c611638e48177aa97854d6a526ba91c45",
  "source_text_sha256": "16c1fa7e1ae3a2f556dc59837236185c611638e48177aa97854d6a526ba91c45",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdd1fc",
        "00bdd23b"
      ]
    ],
    "bytes_sha256": "772f7d6f13c94fddb0367f1068a267eb71b2d47d407ca5a9c50655017806808d",
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
"%PG%com/google/firebase/auth/FirebaseUser"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 450 bytes

~~~c

long _ZN8firebase4auth4user19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE
               (void)

{
  if (DAT_01126e20 == 0) {
    DAT_01126e20 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126e20;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdd1fc"></a> `00bdd1fc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdd200"></a> `00bdd200` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd204"></a> `00bdd204` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdd208"></a> `00bdd208` | `53 2a 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdd20c"></a> `00bdd20c` | `68 12 47 f9` | ldr x8,[x19, #0xe20] | `FALL_THROUGH`
<a id="insn-00bdd210"></a> `00bdd210` | `e8 00 00 b5` | cbnz x8,0x00bdd22c | `CONDITIONAL_JUMP`
<a id="insn-00bdd214"></a> `00bdd214` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00bdd218"></a> `00bdd218` | `63 b6 ff 90` | adrp x3,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdd21c"></a> `00bdd21c` | `63 d8 22 91` | add x3,x3,#0x8b6 | `FALL_THROUGH`
<a id="insn-00bdd220"></a> `00bdd220` | `70 f7 01 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd224"></a> `00bdd224` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bdd228"></a> `00bdd228` | `60 12 07 f9` | str x0,[x19, #0xe20] | `FALL_THROUGH`
<a id="insn-00bdd22c"></a> `00bdd22c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd230"></a> `00bdd230` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bdd234"></a> `00bdd234` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdd238"></a> `00bdd238` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdd1fc`](#insn-00bdd1fc) 範囲 `[['00bdd1fc', '00bdd213']]`
  - `CONDITIONAL_JUMP` [`00bdd210`](#insn-00bdd210) → [`00bdd22c`](#insn-00bdd22c)
  - `FALL_THROUGH` [`00bdd210`](#insn-00bdd210) → [`00bdd214`](#insn-00bdd214)
- ブロック [`00bdd214`](#insn-00bdd214) 範囲 `[['00bdd214', '00bdd22b']]`
  - `FALL_THROUGH` [`00bdd228`](#insn-00bdd228) → [`00bdd22c`](#insn-00bdd22c)
- ブロック [`00bdd22c`](#insn-00bdd22c) 範囲 `[['00bdd22c', '00bdd23b']]`

## 命令位置別の参照

- [`00bdd1fc`](#insn-00bdd1fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd200`](#insn-00bdd200) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd20c`](#insn-00bdd20c) → `01126e20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd210`](#insn-00bdd210) → [`00bdd22c`](#insn-00bdd22c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd21c`](#insn-00bdd21c) → `002a98b6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdd220`](#insn-00bdd220) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bdd228`](#insn-00bdd228) → `01126e20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd22c`](#insn-00bdd22c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdd1fc`](#insn-00bdd1fc)

~~~json
{
  "source": "00bdd1fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd200`](#insn-00bdd200)

~~~json
{
  "source": "00bdd200",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd20c`](#insn-00bdd20c)

~~~json
{
  "source": "00bdd20c",
  "target": "01126e20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd210`](#insn-00bdd210)

~~~json
{
  "source": "00bdd210",
  "target": "00bdd22c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd21c`](#insn-00bdd21c)

~~~json
{
  "source": "00bdd21c",
  "target": "002a98b6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a98b2",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002a98b2",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdd220`](#insn-00bdd220)

~~~json
{
  "source": "00bdd220",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd228`](#insn-00bdd228)

~~~json
{
  "source": "00bdd228",
  "target": "01126e20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd22c`](#insn-00bdd22c)

~~~json
{
  "source": "00bdd22c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
