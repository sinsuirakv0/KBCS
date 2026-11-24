# 00bf2bec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bf27c4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf27c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0022.md#compare-b7ab7566ecf029f8a0687b79bfda0742)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf2c88`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2c88.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/machine_only_observed-0022.md#compare-9653ee77de2b62d686a4405790cbc8dd)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf2bec",
  "name": "_ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEC1ERKS5_",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a6ea5e4cbd93b059d643b3ca897931257c271867b8bc420a91f8962ef75d10d5",
  "source_text_sha256": "a6ea5e4cbd93b059d643b3ca897931257c271867b8bc420a91f8962ef75d10d5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf2bec",
        "00bf2c17"
      ]
    ],
    "bytes_sha256": "17350fbd5b106e1ac62015d2117e478231b1a1865f4d2288c500b7f7b2e4feb4",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [006d76e4](../006d7/006d76e4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 496 bytes

~~~c

void _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEC1ERKS5_
               (undefined8 *param_1,byte *param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if ((*param_2 & 1) == 0) {
    uVar2 = *(undefined8 *)(param_2 + 8);
    uVar1 = *(undefined8 *)param_2;
    param_1[2] = *(undefined8 *)(param_2 + 0x10);
    param_1[1] = uVar2;
    *param_1 = uVar1;
    return;
  }
  FUN_006d76e4(param_1,*(undefined8 *)(param_2 + 0x10),*(undefined8 *)(param_2 + 8));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf2bec"></a> `00bf2bec` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bf2bf0"></a> `00bf2bf0` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00bf2bf4"></a> `00bf2bf4` | `c8 00 00 37` | tbnz w8,#0x0,0x00bf2c0c | `CONDITIONAL_JUMP`
<a id="insn-00bf2bf8"></a> `00bf2bf8` | `28 08 40 f9` | ldr x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bf2bfc"></a> `00bf2bfc` | `20 00 c0 3d` | ldr q0,[x1] | `FALL_THROUGH`
<a id="insn-00bf2c00"></a> `00bf2c00` | `08 08 00 f9` | str x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bf2c04"></a> `00bf2c04` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-00bf2c08"></a> `00bf2c08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf2c0c"></a> `00bf2c0c` | `22 a0 40 a9` | ldp x2,x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bf2c10"></a> `00bf2c10` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bf2c14"></a> `00bf2c14` | `b4 92 eb 17` | b 0x006d76e4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf2bec`](#insn-00bf2bec) 範囲 `[['00bf2bec', '00bf2bf7']]`
  - `CONDITIONAL_JUMP` [`00bf2bf4`](#insn-00bf2bf4) → [`00bf2c0c`](#insn-00bf2c0c)
  - `FALL_THROUGH` [`00bf2bf4`](#insn-00bf2bf4) → [`00bf2bf8`](#insn-00bf2bf8)
- ブロック [`00bf2bf8`](#insn-00bf2bf8) 範囲 `[['00bf2bf8', '00bf2c0b']]`
- ブロック [`00bf2c0c`](#insn-00bf2c0c) 範囲 `[['00bf2c0c', '00bf2c17']]`

## 命令位置別の参照

- [`00bf2bf4`](#insn-00bf2bf4) → [`00bf2c0c`](#insn-00bf2c0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2c14`](#insn-00bf2c14) → [`006d76e4`](../006d7/006d76e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006d76e4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf2bf4`](#insn-00bf2bf4)

~~~json
{
  "source": "00bf2bf4",
  "target": "00bf2c0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2c14`](#insn-00bf2c14)

~~~json
{
  "source": "00bf2c14",
  "target": "006d76e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
