# 00bfbdb4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfb98c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb98c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/reference_unresolved-0001.md#compare-074299586fc913bf4f5689e27439931f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbe50`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbe50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/reference_unresolved-0001.md#compare-ddb9e62889cce56ffdd231a60e5d85e3)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbdb4",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sgetcEv",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0f95e795623d246432c6d584f81ecd706d7f9da055d4bfe8d453e1b2e6a0806e",
  "source_text_sha256": "0f95e795623d246432c6d584f81ecd706d7f9da055d4bfe8d453e1b2e6a0806e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbdb4",
        "00bfbdd7"
      ]
    ],
    "bytes_sha256": "0dec77bac5ab7ead546adfc012522fff14c88463d2b8d3c41dedba18e5397f7d",
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

## 疑似コード / UTF-8 422 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sgetcEv(long *param_1)

{
  ulong uVar1;
  
  if ((byte *)param_1[3] != (byte *)param_1[4]) {
    return (ulong)*(byte *)param_1[3];
  }
                    /* WARNING: Could not recover jumptable at 0x00bfbdd4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar1 = (**(code **)(*param_1 + 0x48))();
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbdb4"></a> `00bfbdb4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfbdb8"></a> `00bfbdb8` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfbdbc"></a> `00bfbdbc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfbdc0"></a> `00bfbdc0` | `60 00 00 54` | b.eq 0x00bfbdcc | `CONDITIONAL_JUMP`
<a id="insn-00bfbdc4"></a> `00bfbdc4` | `00 01 40 39` | ldrb w0,[x8] | `FALL_THROUGH`
<a id="insn-00bfbdc8"></a> `00bfbdc8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfbdcc"></a> `00bfbdcc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfbdd0"></a> `00bfbdd0` | `10 25 40 f9` | ldr x16,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfbdd4"></a> `00bfbdd4` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bfbdb4`](#insn-00bfbdb4) 範囲 `[['00bfbdb4', '00bfbdc3']]`
  - `CONDITIONAL_JUMP` [`00bfbdc0`](#insn-00bfbdc0) → [`00bfbdcc`](#insn-00bfbdcc)
  - `FALL_THROUGH` [`00bfbdc0`](#insn-00bfbdc0) → [`00bfbdc4`](#insn-00bfbdc4)
- ブロック [`00bfbdc4`](#insn-00bfbdc4) 範囲 `[['00bfbdc4', '00bfbdcb']]`
- ブロック [`00bfbdcc`](#insn-00bfbdcc) 範囲 `[['00bfbdcc', '00bfbdd7']]`

## 命令位置別の参照

- [`00bfbdc0`](#insn-00bfbdc0) → [`00bfbdcc`](#insn-00bfbdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbdc0`](#insn-00bfbdc0)

~~~json
{
  "source": "00bfbdc0",
  "target": "00bfbdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
