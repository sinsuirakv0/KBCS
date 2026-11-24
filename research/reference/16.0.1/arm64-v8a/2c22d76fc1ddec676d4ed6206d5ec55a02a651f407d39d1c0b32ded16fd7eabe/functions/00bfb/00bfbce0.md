# 00bfbce0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfb8b8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb8b8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/reference_unresolved-0001.md#compare-ba35a38fb75944f13c8238ea5c7380a5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbd7c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbd7c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/reference_unresolved-0001.md#compare-65c1b8479955538c426a9f86e4a6f690)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbce0",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8in_availEv",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c0c9ebbaf6c83b4323e22fb6df15407b22eb707470e894ed19c7f51f71a94385",
  "source_text_sha256": "c0c9ebbaf6c83b4323e22fb6df15407b22eb707470e894ed19c7f51f71a94385",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbce0",
        "00bfbd03"
      ]
    ],
    "bytes_sha256": "dd2ec22c9dc3b866fe2bde634e2ff493d8c08390b7bde8fed0df555cd79f8014",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
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

## 疑似コード / UTF-8 417 bytes

~~~c

long _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8in_availEv(long *param_1)

{
  long lVar1;
  
  if ((ulong)param_1[3] < (ulong)param_1[4]) {
    return param_1[4] - param_1[3];
  }
                    /* WARNING: Could not recover jumptable at 0x00bfbd00. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  lVar1 = (**(code **)(*param_1 + 0x38))();
  return lVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbce0"></a> `00bfbce0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfbce4"></a> `00bfbce4` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfbce8"></a> `00bfbce8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfbcec"></a> `00bfbcec` | `62 00 00 54` | b.cs 0x00bfbcf8 | `CONDITIONAL_JUMP`
<a id="insn-00bfbcf0"></a> `00bfbcf0` | `20 01 08 cb` | sub x0,x9,x8 | `FALL_THROUGH`
<a id="insn-00bfbcf4"></a> `00bfbcf4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfbcf8"></a> `00bfbcf8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfbcfc"></a> `00bfbcfc` | `10 1d 40 f9` | ldr x16,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bfbd00"></a> `00bfbd00` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bfbce0`](#insn-00bfbce0) 範囲 `[['00bfbce0', '00bfbcef']]`
  - `CONDITIONAL_JUMP` [`00bfbcec`](#insn-00bfbcec) → [`00bfbcf8`](#insn-00bfbcf8)
  - `FALL_THROUGH` [`00bfbcec`](#insn-00bfbcec) → [`00bfbcf0`](#insn-00bfbcf0)
- ブロック [`00bfbcf0`](#insn-00bfbcf0) 範囲 `[['00bfbcf0', '00bfbcf7']]`
- ブロック [`00bfbcf8`](#insn-00bfbcf8) 範囲 `[['00bfbcf8', '00bfbd03']]`

## 命令位置別の参照

- [`00bfbcec`](#insn-00bfbcec) → [`00bfbcf8`](#insn-00bfbcf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbcec`](#insn-00bfbcec)

~~~json
{
  "source": "00bfbcec",
  "target": "00bfbcf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
