# 00bc2bac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bc2784`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2784.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0080.md#compare-997e2e03786830e0b8609809df5c7961)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc2c48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2c48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0080.md#compare-ff04a6135aec3abe84844702b1d79b25)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc2bac",
  "name": "_ZN8firebase13remote_config8internal22custom_signals_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bce0890b4590d9ffd6085d4a9c8547d216df922922626dea809ccfddb4f16ce8",
  "source_text_sha256": "bce0890b4590d9ffd6085d4a9c8547d216df922922626dea809ccfddb4f16ce8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc2bac",
        "00bc2beb"
      ]
    ],
    "bytes_sha256": "20ff0532554f5ece1fa17d021a28af06e4fde129ec88861bbf9b97b3ecaf0abc",
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

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/remoteconfig/CustomSignals$Builder"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 585 bytes

~~~c

long _ZN8firebase13remote_config8internal22custom_signals_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEENS_4util16ClassRequirementE
               (void)

{
                    /* try { // try from 00bc2bb4 to 00cc2f9f has its CatchHandler @ 00bc22dc */
  if (DAT_011265f8 == 0) {
    DAT_011265f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_011265f8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc2bac"></a> `00bc2bac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bc2bb0"></a> `00bc2bb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2bb4"></a> `00bc2bb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bc2bb8"></a> `00bc2bb8` | `33 2b 00 90` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bc2bbc"></a> `00bc2bbc` | `68 fe 42 f9` | ldr x8,[x19, #0x5f8] | `FALL_THROUGH`
<a id="insn-00bc2bc0"></a> `00bc2bc0` | `e8 00 00 b5` | cbnz x8,0x00bc2bdc | `CONDITIONAL_JUMP`
<a id="insn-00bc2bc4"></a> `00bc2bc4` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00bc2bc8"></a> `00bc2bc8` | `63 b7 ff 90` | adrp x3,0x2ae000 | `FALL_THROUGH`
<a id="insn-00bc2bcc"></a> `00bc2bcc` | `63 ac 0f 91` | add x3,x3,#0x3eb | `FALL_THROUGH`
<a id="insn-00bc2bd0"></a> `00bc2bd0` | `d0 60 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bc2bd4"></a> `00bc2bd4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bc2bd8"></a> `00bc2bd8` | `60 fe 02 f9` | str x0,[x19, #0x5f8] | `FALL_THROUGH`
<a id="insn-00bc2bdc"></a> `00bc2bdc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2be0"></a> `00bc2be0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bc2be4"></a> `00bc2be4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bc2be8"></a> `00bc2be8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc2bac`](#insn-00bc2bac) 範囲 `[['00bc2bac', '00bc2bb3']]`
  - `FALL_THROUGH` [`00bc2bb0`](#insn-00bc2bb0) → [`00bc2bb4`](#insn-00bc2bb4)
- ブロック [`00bc2bb4`](#insn-00bc2bb4) 範囲 `[['00bc2bb4', '00bc2bc3']]`
  - `CONDITIONAL_JUMP` [`00bc2bc0`](#insn-00bc2bc0) → [`00bc2bdc`](#insn-00bc2bdc)
  - `FALL_THROUGH` [`00bc2bc0`](#insn-00bc2bc0) → [`00bc2bc4`](#insn-00bc2bc4)
- ブロック [`00bc2bc4`](#insn-00bc2bc4) 範囲 `[['00bc2bc4', '00bc2bdb']]`
  - `FALL_THROUGH` [`00bc2bd8`](#insn-00bc2bd8) → [`00bc2bdc`](#insn-00bc2bdc)
- ブロック [`00bc2bdc`](#insn-00bc2bdc) 範囲 `[['00bc2bdc', '00bc2beb']]`

## 命令位置別の参照

- [`00bc2bac`](#insn-00bc2bac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2bb0`](#insn-00bc2bb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2bbc`](#insn-00bc2bbc) → `011265f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc2bc0`](#insn-00bc2bc0) → [`00bc2bdc`](#insn-00bc2bdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2bcc`](#insn-00bc2bcc) → `002ae3eb`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc2bd0`](#insn-00bc2bd0) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bc2bd8`](#insn-00bc2bd8) → `011265f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc2bdc`](#insn-00bc2bdc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc2bac`](#insn-00bc2bac)

~~~json
{
  "source": "00bc2bac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2bb0`](#insn-00bc2bb0)

~~~json
{
  "source": "00bc2bb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2bbc`](#insn-00bc2bbc)

~~~json
{
  "source": "00bc2bbc",
  "target": "011265f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011265f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc2bc0`](#insn-00bc2bc0)

~~~json
{
  "source": "00bc2bc0",
  "target": "00bc2bdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2bcc`](#insn-00bc2bcc)

~~~json
{
  "source": "00bc2bcc",
  "target": "002ae3eb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ae3e7",
  "offset": 4,
  "size": 59,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f72656d6f7465636f",
  "capture_start": "002ae3e7",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bc2bd0`](#insn-00bc2bd0)

~~~json
{
  "source": "00bc2bd0",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc2bd8`](#insn-00bc2bd8)

~~~json
{
  "source": "00bc2bd8",
  "target": "011265f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011265f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc2bdc`](#insn-00bc2bdc)

~~~json
{
  "source": "00bc2bdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
