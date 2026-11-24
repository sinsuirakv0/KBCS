# 00bc2bec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bc27c4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc27c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0080.md#compare-337b797adef621c3b72fd8f84bc64130)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc2c88`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2c88.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0080.md#compare-4c20f61230394ebc5c443701591e8187)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc2bec",
  "name": "_ZN8firebase13remote_config8internal22custom_signals_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "79f5f27e5e3b883ab8433acc967f91f2ac883f7c661c78d941ace76d8151a418",
  "source_text_sha256": "79f5f27e5e3b883ab8433acc967f91f2ac883f7c661c78d941ace76d8151a418",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc2bec",
        "00bc2c2b"
      ]
    ],
    "bytes_sha256": "c6bae66c6652e31a6cc19c0954ba9f129852fa4315462cc7332186f6c86c6881",
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

## 疑似コード / UTF-8 461 bytes

~~~c

long _ZN8firebase13remote_config8internal22custom_signals_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEE
               (void)

{
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
<a id="insn-00bc2bec"></a> `00bc2bec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bc2bf0"></a> `00bc2bf0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2bf4"></a> `00bc2bf4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bc2bf8"></a> `00bc2bf8` | `33 2b 00 90` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bc2bfc"></a> `00bc2bfc` | `68 fe 42 f9` | ldr x8,[x19, #0x5f8] | `FALL_THROUGH`
<a id="insn-00bc2c00"></a> `00bc2c00` | `e8 00 00 b5` | cbnz x8,0x00bc2c1c | `CONDITIONAL_JUMP`
<a id="insn-00bc2c04"></a> `00bc2c04` | `63 b7 ff 90` | adrp x3,0x2ae000 | `FALL_THROUGH`
<a id="insn-00bc2c08"></a> `00bc2c08` | `63 ac 0f 91` | add x3,x3,#0x3eb | `FALL_THROUGH`
<a id="insn-00bc2c0c"></a> `00bc2c0c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bc2c10"></a> `00bc2c10` | `c0 60 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bc2c14"></a> `00bc2c14` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bc2c18"></a> `00bc2c18` | `60 fe 02 f9` | str x0,[x19, #0x5f8] | `FALL_THROUGH`
<a id="insn-00bc2c1c"></a> `00bc2c1c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2c20"></a> `00bc2c20` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bc2c24"></a> `00bc2c24` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bc2c28"></a> `00bc2c28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc2bec`](#insn-00bc2bec) 範囲 `[['00bc2bec', '00bc2c03']]`
  - `CONDITIONAL_JUMP` [`00bc2c00`](#insn-00bc2c00) → [`00bc2c1c`](#insn-00bc2c1c)
  - `FALL_THROUGH` [`00bc2c00`](#insn-00bc2c00) → [`00bc2c04`](#insn-00bc2c04)
- ブロック [`00bc2c04`](#insn-00bc2c04) 範囲 `[['00bc2c04', '00bc2c1b']]`
  - `FALL_THROUGH` [`00bc2c18`](#insn-00bc2c18) → [`00bc2c1c`](#insn-00bc2c1c)
- ブロック [`00bc2c1c`](#insn-00bc2c1c) 範囲 `[['00bc2c1c', '00bc2c2b']]`

## 命令位置別の参照

- [`00bc2bec`](#insn-00bc2bec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2bf0`](#insn-00bc2bf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2bfc`](#insn-00bc2bfc) → `011265f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc2c00`](#insn-00bc2c00) → [`00bc2c1c`](#insn-00bc2c1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2c08`](#insn-00bc2c08) → `002ae3eb`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc2c10`](#insn-00bc2c10) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bc2c18`](#insn-00bc2c18) → `011265f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc2c1c`](#insn-00bc2c1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc2bec`](#insn-00bc2bec)

~~~json
{
  "source": "00bc2bec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2bf0`](#insn-00bc2bf0)

~~~json
{
  "source": "00bc2bf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2bfc`](#insn-00bc2bfc)

~~~json
{
  "source": "00bc2bfc",
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
- 参照命令 [`00bc2c00`](#insn-00bc2c00)

~~~json
{
  "source": "00bc2c00",
  "target": "00bc2c1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2c08`](#insn-00bc2c08)

~~~json
{
  "source": "00bc2c08",
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
- 参照命令 [`00bc2c10`](#insn-00bc2c10)

~~~json
{
  "source": "00bc2c10",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc2c18`](#insn-00bc2c18)

~~~json
{
  "source": "00bc2c18",
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
- 参照命令 [`00bc2c1c`](#insn-00bc2c1c)

~~~json
{
  "source": "00bc2c1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
