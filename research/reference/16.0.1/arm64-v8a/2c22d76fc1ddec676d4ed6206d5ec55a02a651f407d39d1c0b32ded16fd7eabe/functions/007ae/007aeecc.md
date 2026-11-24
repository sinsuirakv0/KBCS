# 007aeecc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `007aee8c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aee8c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0038.md#compare-8982ed257522cdd5164374dfec560820)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `007aef24`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aef24.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0039.md#compare-68c5e25a645480b7ea0081020684b08d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007aeecc",
  "name": "FUN_007aeecc",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eba589f2cdcd30c10f97306385f911ab1347f9bc439f0abfcab593a1a28fab0f",
  "source_text_sha256": "eba589f2cdcd30c10f97306385f911ab1347f9bc439f0abfcab593a1a28fab0f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007aeecc",
        "007aef07"
      ]
    ],
    "bytes_sha256": "ff4458186d12d093f0ae124f61277161f5eb5203bed5959d0feaa8ade43d2d1e",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0043bb20](../0043b/0043bb20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 568 bytes

~~~c

void FUN_007aeecc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  *param_2 = &PTR_FUN_00c7a718;
  if ((*(byte *)(param_1 + 8) & 1) == 0) {
    uVar2 = *(undefined8 *)(param_1 + 0x10);
    uVar1 = *(undefined8 *)(param_1 + 8);
    param_2[3] = *(undefined8 *)(param_1 + 0x18);
                    /* catch() { ... } // from try @ 007ae04c with catch @ 007aeef0 */
    param_2[2] = uVar2;
    param_2[1] = uVar1;
    return;
  }
  FUN_0043bb20(param_2 + 1,*(undefined8 *)(param_1 + 0x18),*(undefined8 *)(param_1 + 0x10));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007aeecc"></a> `007aeecc` | `68 26 00 90` | adrp x8,0xc7a000 | `FALL_THROUGH`
<a id="insn-007aeed0"></a> `007aeed0` | `08 61 1c 91` | add x8,x8,#0x718 | `FALL_THROUGH`
<a id="insn-007aeed4"></a> `007aeed4` | `28 84 00 f8` | str x8,[x1], #0x8 | `FALL_THROUGH`
<a id="insn-007aeed8"></a> `007aeed8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-007aeedc"></a> `007aeedc` | `09 8d 40 38` | ldrb w9,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-007aeee0"></a> `007aeee0` | `c9 00 00 37` | tbnz w9,#0x0,0x007aeef8 | `CONDITIONAL_JUMP`
<a id="insn-007aeee4"></a> `007aeee4` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007aeee8"></a> `007aeee8` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-007aeeec"></a> `007aeeec` | `29 08 00 f9` | str x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-007aeef0"></a> `007aeef0` | `20 00 80 3d` | str q0,[x1] | `FALL_THROUGH`
<a id="insn-007aeef4"></a> `007aeef4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007aeef8"></a> `007aeef8` | `02 20 41 a9` | ldp x2,x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-007aeefc"></a> `007aeefc` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-007aef00"></a> `007aef00` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-007aef04"></a> `007aef04` | `07 33 f2 17` | b 0x0043bb20 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007aeecc`](#insn-007aeecc) 範囲 `[['007aeecc', '007aeee3']]`
  - `CONDITIONAL_JUMP` [`007aeee0`](#insn-007aeee0) → [`007aeef8`](#insn-007aeef8)
  - `FALL_THROUGH` [`007aeee0`](#insn-007aeee0) → [`007aeee4`](#insn-007aeee4)
- ブロック [`007aeee4`](#insn-007aeee4) 範囲 `[['007aeee4', '007aeeef']]`
  - `FALL_THROUGH` [`007aeeec`](#insn-007aeeec) → [`007aeef0`](#insn-007aeef0)
- ブロック [`007aeef0`](#insn-007aeef0) 範囲 `[['007aeef0', '007aeef7']]`
- ブロック [`007aeef8`](#insn-007aeef8) 範囲 `[['007aeef8', '007aef07']]`

## 命令位置別の参照

- [`007aeed4`](#insn-007aeed4) → `00c7a718`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007aeee0`](#insn-007aeee0) → [`007aeef8`](#insn-007aeef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aef04`](#insn-007aef04) → [`0043bb20`](../0043b/0043bb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb20` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007aeed4`](#insn-007aeed4)

~~~json
{
  "source": "007aeed4",
  "target": "00c7a718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7a718",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007aeee0`](#insn-007aeee0)

~~~json
{
  "source": "007aeee0",
  "target": "007aeef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aef04`](#insn-007aef04)

~~~json
{
  "source": "007aef04",
  "target": "0043bb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
