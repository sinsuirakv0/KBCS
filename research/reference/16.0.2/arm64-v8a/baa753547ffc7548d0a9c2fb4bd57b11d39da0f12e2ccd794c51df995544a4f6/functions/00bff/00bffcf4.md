# 00bffcf4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffc58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffc58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/reference_unresolved-0001.md#compare-edf712ddd5d28531c47f79844b31686e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c00ce8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00ce8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/reference_unresolved-0001.md#compare-d9d87f56d1d2aac17f57848a6295dd42)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffcf4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE9sputbackcEw",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "99a147f332c44e4b2a67a5b71a02db0c3925e0f4636d54bfb5b1a64a65c60024",
  "source_text_sha256": "99a147f332c44e4b2a67a5b71a02db0c3925e0f4636d54bfb5b1a64a65c60024",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffcf4",
        "00bffd2b"
      ]
    ],
    "bytes_sha256": "4943460ac28ff680364c2f067e2b0c34bd748c8f79b17fb8bc07f01cf2863fdd",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
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

## 疑似コード / UTF-8 520 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE9sputbackcEw(long *param_1,uint param_2)

{
  ulong uVar1;
  uint *puVar2;
  
  if ((param_1[2] != param_1[3]) && (puVar2 = (uint *)(param_1[3] + -4), *puVar2 == param_2)) {
    param_1[3] = (long)puVar2;
    return (ulong)param_2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bffd28. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar1 = (**(code **)(*param_1 + 0x58))();
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bffcf4"></a> `00bffcf4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bffcf8"></a> `00bffcf8` | `09 20 41 a9` | ldp x9,x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bffcfc"></a> `00bffcfc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bffd00"></a> `00bffd00` | `00 01 00 54` | b.eq 0x00bffd20 | `CONDITIONAL_JUMP`
<a id="insn-00bffd04"></a> `00bffd04` | `09 cd 5f b8` | ldr w9,[x8, #-0x4]! | `FALL_THROUGH`
<a id="insn-00bffd08"></a> `00bffd08` | `3f 01 01 6b` | cmp w9,w1 | `FALL_THROUGH`
<a id="insn-00bffd0c"></a> `00bffd0c` | `a1 00 00 54` | b.ne 0x00bffd20 | `CONDITIONAL_JUMP`
<a id="insn-00bffd10"></a> `00bffd10` | `e9 03 00 aa` | mov x9,x0 | `FALL_THROUGH`
<a id="insn-00bffd14"></a> `00bffd14` | `e0 03 01 2a` | mov w0,w1 | `FALL_THROUGH`
<a id="insn-00bffd18"></a> `00bffd18` | `28 0d 00 f9` | str x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00bffd1c"></a> `00bffd1c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bffd20"></a> `00bffd20` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bffd24"></a> `00bffd24` | `10 2d 40 f9` | ldr x16,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00bffd28"></a> `00bffd28` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bffcf4`](#insn-00bffcf4) 範囲 `[['00bffcf4', '00bffd03']]`
  - `CONDITIONAL_JUMP` [`00bffd00`](#insn-00bffd00) → [`00bffd20`](#insn-00bffd20)
  - `FALL_THROUGH` [`00bffd00`](#insn-00bffd00) → [`00bffd04`](#insn-00bffd04)
- ブロック [`00bffd04`](#insn-00bffd04) 範囲 `[['00bffd04', '00bffd0f']]`
  - `CONDITIONAL_JUMP` [`00bffd0c`](#insn-00bffd0c) → [`00bffd20`](#insn-00bffd20)
  - `FALL_THROUGH` [`00bffd0c`](#insn-00bffd0c) → [`00bffd10`](#insn-00bffd10)
- ブロック [`00bffd10`](#insn-00bffd10) 範囲 `[['00bffd10', '00bffd1f']]`
- ブロック [`00bffd20`](#insn-00bffd20) 範囲 `[['00bffd20', '00bffd2b']]`

## 命令位置別の参照

- [`00bffd00`](#insn-00bffd00) → [`00bffd20`](#insn-00bffd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffd0c`](#insn-00bffd0c) → [`00bffd20`](#insn-00bffd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffd00`](#insn-00bffd00)

~~~json
{
  "source": "00bffd00",
  "target": "00bffd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffd0c`](#insn-00bffd0c)

~~~json
{
  "source": "00bffd0c",
  "target": "00bffd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
