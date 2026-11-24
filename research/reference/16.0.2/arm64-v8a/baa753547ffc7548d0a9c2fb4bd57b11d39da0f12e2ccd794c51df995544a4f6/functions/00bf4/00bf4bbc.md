# 00bf4bbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf4b20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4b20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-6a1b55a67e6284cdc9c703e4a95df668)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf5bb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5bb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-72a09f9e4a48604d7e71c8b4cc1161fa)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf4bbc",
  "name": "_ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmRKS5_mm",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ccc5786ed455bd26e9f98ba6a5d4d7794dfcffe160e20b99f05d952a810f5732",
  "source_text_sha256": "ccc5786ed455bd26e9f98ba6a5d4d7794dfcffe160e20b99f05d952a810f5732",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf4bbc",
        "00bf4c0b"
      ]
    ],
    "bytes_sha256": "535566123122f763f4476349ed41933452f457d76393a2b49d66a9d5b2a01bdd",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bf2974](../00bf2/00bf2974.md)
- [00c5e0f0](../00c5e/00c5e0f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 838 bytes

~~~c

void _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmRKS5_mm
               (undefined8 param_1,undefined8 param_2,byte *param_3,ulong param_4,ulong param_5)

{
  ulong uVar1;
  byte *pbVar2;
  ulong uVar3;
  byte bVar4;
  
  bVar4 = *param_3;
  uVar1 = (ulong)(bVar4 >> 1);
  if ((bVar4 & 1) != 0) {
    uVar1 = *(ulong *)(param_3 + 8);
  }
  if (param_4 <= uVar1) {
    pbVar2 = param_3 + 4;
    if ((bVar4 & 1) != 0) {
      pbVar2 = *(byte **)(param_3 + 0x10);
    }
    uVar3 = uVar1 - param_4;
    if (param_5 <= uVar1 - param_4) {
      uVar3 = param_5;
    }
    _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKwm
              (param_1,param_2,pbVar2 + param_4 * 4,uVar3);
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00bf2974();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf4bbc"></a> `00bf4bbc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bf4bc0"></a> `00bf4bc0` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00bf4bc4"></a> `00bf4bc4` | `49 04 40 f9` | ldr x9,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00bf4bc8"></a> `00bf4bc8` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf4bcc"></a> `00bf4bcc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf4bd0"></a> `00bf4bd0` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bf4bd4"></a> `00bf4bd4` | `29 01 03 eb` | subs x9,x9,x3 | `FALL_THROUGH`
<a id="insn-00bf4bd8"></a> `00bf4bd8` | `23 01 00 54` | b.cc 0x00bf4bfc | `CONDITIONAL_JUMP`
<a id="insn-00bf4bdc"></a> `00bf4bdc` | `4a 08 40 f9` | ldr x10,[x2, #0x10] | `FALL_THROUGH`
<a id="insn-00bf4be0"></a> `00bf4be0` | `4b 10 00 91` | add x11,x2,#0x4 | `FALL_THROUGH`
<a id="insn-00bf4be4"></a> `00bf4be4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf4be8"></a> `00bf4be8` | `68 01 8a 9a` | csel x8,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bf4bec"></a> `00bf4bec` | `3f 01 04 eb` | cmp x9,x4 | `FALL_THROUGH`
<a id="insn-00bf4bf0"></a> `00bf4bf0` | `02 09 03 8b` | add x2,x8,x3, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bf4bf4"></a> `00bf4bf4` | `23 31 84 9a` | csel x3,x9,x4,cc | `FALL_THROUGH`
<a id="insn-00bf4bf8"></a> `00bf4bf8` | `3e a5 01 14` | b 0x00c5e0f0 | `CALL_TERMINATOR`
<a id="insn-00bf4bfc"></a> `00bf4bfc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf4c00"></a> `00bf4c00` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bf4c04"></a> `00bf4c04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf4c08"></a> `00bf4c08` | `5b f7 ff 97` | bl 0x00bf2974 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf4bbc`](#insn-00bf4bbc) 範囲 `[['00bf4bbc', '00bf4bdb']]`
  - `CONDITIONAL_JUMP` [`00bf4bd8`](#insn-00bf4bd8) → [`00bf4bfc`](#insn-00bf4bfc)
  - `FALL_THROUGH` [`00bf4bd8`](#insn-00bf4bd8) → [`00bf4bdc`](#insn-00bf4bdc)
- ブロック [`00bf4bdc`](#insn-00bf4bdc) 範囲 `[['00bf4bdc', '00bf4bfb']]`
- ブロック [`00bf4bfc`](#insn-00bf4bfc) 範囲 `[['00bf4bfc', '00bf4c0b']]`

## 命令位置別の参照

- [`00bf4bd8`](#insn-00bf4bd8) → [`00bf4bfc`](#insn-00bf4bfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4bf8`](#insn-00bf4bf8) → [`00c5e0f0`](../00c5e/00c5e0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bf4c00`](#insn-00bf4c00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4c08`](#insn-00bf4c08) → [`00bf2974`](../00bf2/00bf2974.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bf2974` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf4bd8`](#insn-00bf4bd8)

~~~json
{
  "source": "00bf4bd8",
  "target": "00bf4bfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4bf8`](#insn-00bf4bf8)

~~~json
{
  "source": "00bf4bf8",
  "target": "00c5e0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf4c00`](#insn-00bf4c00)

~~~json
{
  "source": "00bf4c00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4c08`](#insn-00bf4c08)

~~~json
{
  "source": "00bf4c08",
  "target": "00bf2974",
  "target_space": "ram",
  "resolution": "function"
}
~~~
