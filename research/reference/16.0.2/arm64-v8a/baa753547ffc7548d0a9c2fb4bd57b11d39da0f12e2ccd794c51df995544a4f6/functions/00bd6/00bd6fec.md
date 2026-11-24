# 00bd6fec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd6f50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6f50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0084.md#compare-286a391eed7cd4f7942cf7f6750b7a2d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd7fe0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7fe0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0084.md#compare-e4bff0bb3981706f2cf04c6a0768495d)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd6fec",
  "name": "_ZN8firebase4auth17phoneauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "95e71d14aa1f09131622fb44e49c50fb7a832392eba0e88adbb8f23a471e8f48",
  "source_text_sha256": "95e71d14aa1f09131622fb44e49c50fb7a832392eba0e88adbb8f23a471e8f48",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd6fec",
        "00bd702b"
      ]
    ],
    "bytes_sha256": "ee1695385648262d229e18f23488cb9ab5dd8352733046a2bac1e8bb744a9e3e",
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
"%PG%com/google/firebase/auth/PhoneAuthProvider"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 464 bytes

~~~c

long _ZN8firebase4auth17phoneauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE
               (void)

{
  if (DAT_01126cd0 == 0) {
    DAT_01126cd0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126cd0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd6fec"></a> `00bd6fec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd6ff0"></a> `00bd6ff0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd6ff4"></a> `00bd6ff4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd6ff8"></a> `00bd6ff8` | `93 2a 00 90` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd6ffc"></a> `00bd6ffc` | `68 6a 46 f9` | ldr x8,[x19, #0xcd0] | `FALL_THROUGH`
<a id="insn-00bd7000"></a> `00bd7000` | `e8 00 00 b5` | cbnz x8,0x00bd701c | `CONDITIONAL_JUMP`
<a id="insn-00bd7004"></a> `00bd7004` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00bd7008"></a> `00bd7008` | `43 b6 ff d0` | adrp x3,0x2a1000 | `FALL_THROUGH`
<a id="insn-00bd700c"></a> `00bd700c` | `63 f0 33 91` | add x3,x3,#0xcfc | `FALL_THROUGH`
<a id="insn-00bd7010"></a> `00bd7010` | `f4 0f 02 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd7014"></a> `00bd7014` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bd7018"></a> `00bd7018` | `60 6a 06 f9` | str x0,[x19, #0xcd0] | `FALL_THROUGH`
<a id="insn-00bd701c"></a> `00bd701c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd7020"></a> `00bd7020` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bd7024"></a> `00bd7024` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd7028"></a> `00bd7028` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd6fec`](#insn-00bd6fec) 範囲 `[['00bd6fec', '00bd7003']]`
  - `CONDITIONAL_JUMP` [`00bd7000`](#insn-00bd7000) → [`00bd701c`](#insn-00bd701c)
  - `FALL_THROUGH` [`00bd7000`](#insn-00bd7000) → [`00bd7004`](#insn-00bd7004)
- ブロック [`00bd7004`](#insn-00bd7004) 範囲 `[['00bd7004', '00bd701b']]`
  - `FALL_THROUGH` [`00bd7018`](#insn-00bd7018) → [`00bd701c`](#insn-00bd701c)
- ブロック [`00bd701c`](#insn-00bd701c) 範囲 `[['00bd701c', '00bd702b']]`

## 命令位置別の参照

- [`00bd6fec`](#insn-00bd6fec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6ff0`](#insn-00bd6ff0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6ffc`](#insn-00bd6ffc) → `01126cd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd7000`](#insn-00bd7000) → [`00bd701c`](#insn-00bd701c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd700c`](#insn-00bd700c) → `002a1cfc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd7010`](#insn-00bd7010) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bd7018`](#insn-00bd7018) → `01126cd0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd701c`](#insn-00bd701c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd6fec`](#insn-00bd6fec)

~~~json
{
  "source": "00bd6fec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6ff0`](#insn-00bd6ff0)

~~~json
{
  "source": "00bd6ff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6ffc`](#insn-00bd6ffc)

~~~json
{
  "source": "00bd6ffc",
  "target": "01126cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126cd0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd7000`](#insn-00bd7000)

~~~json
{
  "source": "00bd7000",
  "target": "00bd701c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd700c`](#insn-00bd700c)

~~~json
{
  "source": "00bd700c",
  "target": "002a1cfc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1cf8",
  "offset": 4,
  "size": 47,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f50686f",
  "capture_start": "002a1cf8",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd7010`](#insn-00bd7010)

~~~json
{
  "source": "00bd7010",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd7018`](#insn-00bd7018)

~~~json
{
  "source": "00bd7018",
  "target": "01126cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126cd0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd701c`](#insn-00bd701c)

~~~json
{
  "source": "00bd701c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
