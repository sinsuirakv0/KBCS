# 00bffbf4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bff7cc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff7cc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/reference_unresolved-0001.md#compare-04c873b9f923ad7b0513d83c3c4127b7)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bffc90`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffc90.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/reference_unresolved-0001.md#compare-e9aade3dbe41b626e18230b04359e92a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffbf4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6sbumpcEv",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35f5f9e55973879c4032ee37e40c14e211d96f74aad3aece7104e7ce179e6f4f",
  "source_text_sha256": "35f5f9e55973879c4032ee37e40c14e211d96f74aad3aece7104e7ce179e6f4f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffbf4",
        "00bffc23"
      ]
    ],
    "bytes_sha256": "50c8fbd1d0864ab3f5810e76e72a8e86ad219c6c6fb653d158062352597375ce",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
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

## 疑似コード / UTF-8 523 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6sbumpcEv(long *param_1)

{
  uint *puVar1;
  uint uVar2;
  ulong uVar3;
  
  puVar1 = (uint *)param_1[3];
  if (puVar1 != (uint *)param_1[4]) {
    uVar2 = *puVar1;
    param_1[3] = (long)(puVar1 + 1);
    return (ulong)uVar2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bffc20. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar3 = (**(code **)(*param_1 + 0x50))(param_1);
  return uVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bffbf4"></a> `00bffbf4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bffbf8"></a> `00bffbf8` | `09 a8 41 a9` | ldp x9,x10,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bffbfc"></a> `00bffbfc` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bffc00"></a> `00bffc00` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bffc04"></a> `00bffc04` | `80 00 00 54` | b.eq 0x00bffc14 | `CONDITIONAL_JUMP`
<a id="insn-00bffc08"></a> `00bffc08` | `20 45 40 b8` | ldr w0,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-00bffc0c"></a> `00bffc0c` | `09 0d 00 f9` | str x9,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bffc10"></a> `00bffc10` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bffc14"></a> `00bffc14` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00bffc18"></a> `00bffc18` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bffc1c"></a> `00bffc1c` | `30 29 40 f9` | ldr x16,[x9, #0x50] | `FALL_THROUGH`
<a id="insn-00bffc20"></a> `00bffc20` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bffbf4`](#insn-00bffbf4) 範囲 `[['00bffbf4', '00bffc07']]`
  - `CONDITIONAL_JUMP` [`00bffc04`](#insn-00bffc04) → [`00bffc14`](#insn-00bffc14)
  - `FALL_THROUGH` [`00bffc04`](#insn-00bffc04) → [`00bffc08`](#insn-00bffc08)
- ブロック [`00bffc08`](#insn-00bffc08) 範囲 `[['00bffc08', '00bffc13']]`
- ブロック [`00bffc14`](#insn-00bffc14) 範囲 `[['00bffc14', '00bffc23']]`

## 命令位置別の参照

- [`00bffc04`](#insn-00bffc04) → [`00bffc14`](#insn-00bffc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffc04`](#insn-00bffc04)

~~~json
{
  "source": "00bffc04",
  "target": "00bffc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
