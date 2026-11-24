# 00bfcee0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbeec`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbeec.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/reference_unresolved-0001.md#compare-b1747ae2627467c46e89208c0bce99be)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcee0",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sputcEc",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "613906a5f90ca8fc14a5ee900ae25d693de32555b0ddd4eed5a9b8e90274020b",
  "source_text_sha256": "613906a5f90ca8fc14a5ee900ae25d693de32555b0ddd4eed5a9b8e90274020b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcee0",
        "00bfcf1b"
      ]
    ],
    "bytes_sha256": "f7c3a4703f0915a5e6799b752d70f36b90bd767c9efe8af43489930afe5a15be",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 533 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sputcEc(long *param_1,byte param_2)

{
  byte *pbVar1;
  ulong uVar2;
  
  pbVar1 = (byte *)param_1[6];
  if (pbVar1 != (byte *)param_1[7]) {
    param_1[6] = (long)(pbVar1 + 1);
    *pbVar1 = param_2;
    return (ulong)param_2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bfcf18. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar2 = (**(code **)(*param_1 + 0x68))(param_1,param_2);
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfcee0"></a> `00bfcee0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfcee4"></a> `00bfcee4` | `09 28 43 a9` | ldp x9,x10,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00bfcee8"></a> `00bfcee8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bfceec"></a> `00bfceec` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bfcef0"></a> `00bfcef0` | `c0 00 00 54` | b.eq 0x00bfcf08 | `CONDITIONAL_JUMP`
<a id="insn-00bfcef4"></a> `00bfcef4` | `2a 05 00 91` | add x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfcef8"></a> `00bfcef8` | `20 1c 00 12` | and w0,w1,#0xff | `FALL_THROUGH`
<a id="insn-00bfcefc"></a> `00bfcefc` | `0a 19 00 f9` | str x10,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00bfcf00"></a> `00bfcf00` | `21 01 00 39` | strb w1,[x9] | `FALL_THROUGH`
<a id="insn-00bfcf04"></a> `00bfcf04` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfcf08"></a> `00bfcf08` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00bfcf0c"></a> `00bfcf0c` | `21 1c 00 12` | and w1,w1,#0xff | `FALL_THROUGH`
<a id="insn-00bfcf10"></a> `00bfcf10` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bfcf14"></a> `00bfcf14` | `30 35 40 f9` | ldr x16,[x9, #0x68] | `FALL_THROUGH`
<a id="insn-00bfcf18"></a> `00bfcf18` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bfcee0`](#insn-00bfcee0) 範囲 `[['00bfcee0', '00bfcef3']]`
  - `CONDITIONAL_JUMP` [`00bfcef0`](#insn-00bfcef0) → [`00bfcf08`](#insn-00bfcf08)
  - `FALL_THROUGH` [`00bfcef0`](#insn-00bfcef0) → [`00bfcef4`](#insn-00bfcef4)
- ブロック [`00bfcef4`](#insn-00bfcef4) 範囲 `[['00bfcef4', '00bfcf07']]`
- ブロック [`00bfcf08`](#insn-00bfcf08) 範囲 `[['00bfcf08', '00bfcf1b']]`

## 命令位置別の参照

- [`00bfcef0`](#insn-00bfcef0) → [`00bfcf08`](#insn-00bfcf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcef0`](#insn-00bfcef0)

~~~json
{
  "source": "00bfcef0",
  "target": "00bfcf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
