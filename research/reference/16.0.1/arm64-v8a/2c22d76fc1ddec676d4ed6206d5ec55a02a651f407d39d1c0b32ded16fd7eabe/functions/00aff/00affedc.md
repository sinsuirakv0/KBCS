# 00affedc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00affab4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00affab4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-4b2c04c0ab5d08a4af66f44f5f678b59)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afff78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aff/00afff78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0008.md#compare-2b8b335c8af32e0a2d36850d37f28fc8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affedc",
  "name": "FUN_00affedc",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "af5a2662d8f83cc95094d35993ddb5fde654ce72ffe496b5fecf7926be2d7e90",
  "source_text_sha256": "af5a2662d8f83cc95094d35993ddb5fde654ce72ffe496b5fecf7926be2d7e90",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affedc",
        "00afff63"
      ]
    ],
    "bytes_sha256": "c6149d2f7dfba09cf39a4542b2d5a9cb10358cca197d0d55f4faf4bb000e20e9",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [005e7420](../005e7/005e7420.md)
- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 479 bytes

~~~c

undefined4 FUN_00affedc(int param_1,int param_2,int param_3)

{
  undefined4 *puVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008514f8();
  uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  lVar2 = FUN_008514f8();
  puVar1 = (undefined4 *)((long)__DT_JMPREL + lVar2 + ((long)param_2 + 2) * 0x1c4 + 0x180c);
  if ((uVar3 & 1) != 0) {
    puVar1 = (undefined4 *)(lVar2 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f6e4);
  }
  return *puVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affedc"></a> `00affedc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00affee0"></a> `00affee0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affee4"></a> `00affee4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affee8"></a> `00affee8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00affeec"></a> `00affeec` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00affef0"></a> `00affef0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00affef4"></a> `00affef4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00affef8"></a> `00affef8` | `80 45 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00affefc"></a> `00affefc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afff00"></a> `00afff00` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afff04"></a> `00afff04` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afff08"></a> `00afff08` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afff0c"></a> `00afff0c` | `45 9d eb 97` | bl 0x005e7420 | `UNCONDITIONAL_CALL`
<a id="insn-00afff10"></a> `00afff10` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afff14"></a> `00afff14` | `79 45 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afff18"></a> `00afff18` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00afff1c"></a> `00afff1c` | `09 ee 80 52` | mov w9,#0x770 | `FALL_THROUGH`
<a id="insn-00afff20"></a> `00afff20` | `8a 38 80 52` | mov w10,#0x1c4 | `FALL_THROUGH`
<a id="insn-00afff24"></a> `00afff24` | `bf 02 00 72` | tst w21,#0x1 | `FALL_THROUGH`
<a id="insn-00afff28"></a> `00afff28` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00afff2c"></a> `00afff2c` | `09 01 09 9b` | madd x9,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00afff30"></a> `00afff30` | `08 01 0a 9b` | madd x8,x8,x10,x0 | `FALL_THROUGH`
<a id="insn-00afff34"></a> `00afff34` | `8a 3b 80 52` | mov w10,#0x1dc | `FALL_THROUGH`
<a id="insn-00afff38"></a> `00afff38` | `69 26 2a 9b` | smaddl x9,w19,w10,x9 | `FALL_THROUGH`
<a id="insn-00afff3c"></a> `00afff3c` | `29 7d 42 91` | add x9,x9,#0x9f, LSL #12 | `FALL_THROUGH`
<a id="insn-00afff40"></a> `00afff40` | `08 f5 48 91` | add x8,x8,#0x23d, LSL #12 | `FALL_THROUGH`
<a id="insn-00afff44"></a> `00afff44` | `29 91 1b 91` | add x9,x9,#0x6e4 | `FALL_THROUGH`
<a id="insn-00afff48"></a> `00afff48` | `08 91 0a 91` | add x8,x8,#0x2a4 | `FALL_THROUGH`
<a id="insn-00afff4c"></a> `00afff4c` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-00afff50"></a> `00afff50` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00afff54"></a> `00afff54` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afff58"></a> `00afff58` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afff5c"></a> `00afff5c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afff60"></a> `00afff60` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00affedc`](#insn-00affedc) 範囲 `[['00affedc', '00afff63']]`

## 命令位置別の参照

- [`00affedc`](#insn-00affedc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affee0`](#insn-00affee0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affee4`](#insn-00affee4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affef8`](#insn-00affef8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afff0c`](#insn-00afff0c) → [`005e7420`](../005e7/005e7420.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7420` · 推定シンボル `None` · 推定型 `None`
- [`00afff14`](#insn-00afff14) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afff50`](#insn-00afff50) → `0023d2a4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afff54`](#insn-00afff54) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff58`](#insn-00afff58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff5c`](#insn-00afff5c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affedc`](#insn-00affedc)

~~~json
{
  "source": "00affedc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affee0`](#insn-00affee0)

~~~json
{
  "source": "00affee0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affee4`](#insn-00affee4)

~~~json
{
  "source": "00affee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affef8`](#insn-00affef8)

~~~json
{
  "source": "00affef8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afff0c`](#insn-00afff0c)

~~~json
{
  "source": "00afff0c",
  "target": "005e7420",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afff14`](#insn-00afff14)

~~~json
{
  "source": "00afff14",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afff50`](#insn-00afff50)

~~~json
{
  "source": "00afff50",
  "target": "0023d2a4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6156,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afff54`](#insn-00afff54)

~~~json
{
  "source": "00afff54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff58`](#insn-00afff58)

~~~json
{
  "source": "00afff58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff5c`](#insn-00afff5c)

~~~json
{
  "source": "00afff5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
