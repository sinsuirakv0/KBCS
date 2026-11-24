# 006fbcac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `006fbc6c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbc6c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0033.md#compare-32967e116013e26acd9b20dc906c7762)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `006fbd04`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbd04.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0033.md#compare-5b0dd6ecb2dfffe2c62ebefe8bf91742)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fbcac",
  "name": "FUN_006fbcac",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "050b265eda0f381fe7403dcf9bc204d76ddc9893d9032ed43f53900f667bb255",
  "source_text_sha256": "050b265eda0f381fe7403dcf9bc204d76ddc9893d9032ed43f53900f667bb255",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006fbcac",
        "006fbda7"
      ]
    ],
    "bytes_sha256": "a2ca19c222e2adfb1fd7f8d6998e1b2bad6df2eac5e8255fa411660328fb8fed",
    "instruction_count": 63,
    "instruction_bytes": 252,
    "body_bytes": 252,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [006b2424](../006b2/006b2424.md)
- [006ea588](../006ea/006ea588.md)
- [006f0500](../006f0/006f0500.md)
- [006fb074](../006fb/006fb074.md)
- [008514f8](../00851/008514f8.md)
- [008b9178](../008b9/008b9178.md)
- [00a83260](../00a83/00a83260.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1199 bytes

~~~c

void FUN_006fbcac(long param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  long lVar2;
  undefined1 *puVar3;
  undefined8 uVar4;
  undefined8 *puVar5;
  
  puVar3 = *(undefined1 **)(param_1 + 8);
  if ((*param_3 == 2) && (*param_4 != -1)) {
    uVar4 = *param_2;
    uVar1 = FUN_0047acf4();
    FUN_0047cdd4(uVar1,0xb,0);
    FUN_008b9178(uVar4);
    return;
  }
  if ((*param_3 == 5) && (*param_4 == 0)) {
    *puVar3 = 0;
    puVar5 = (undefined8 *)(puVar3 + 0x28);
    FUN_006fb074(puVar3 + 0x20,*puVar5);
    *(undefined8 **)(puVar3 + 0x20) = puVar5;
    *(undefined8 *)(puVar3 + 0x30) = 0;
    *puVar5 = 0;
    lVar2 = FUN_008514f8();
    *(undefined4 *)((long)&fde_table_entry_00332070.data_loc + lVar2) = 0;
    lVar2 = FUN_008514f8();
    *(undefined4 *)((long)&fde_table_entry_00332098.initial_loc + lVar2) = 0;
    lVar2 = FUN_008514f8();
    FUN_00a83260(lVar2 + 0x3078,0x14);
    lVar2 = FUN_008514f8();
    FUN_006b2424(lVar2 + 0x42ef60);
    lVar2 = FUN_008514f8();
    FUN_006f0500(lVar2 + 0x42ef90,*(undefined4 *)(puVar3 + 4),*(undefined4 *)(puVar3 + 0x14));
    lVar2 = FUN_008514f8();
    FUN_006ea588(lVar2 + 0x42ef90,1);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006fbcac"></a> `006fbcac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-006fbcb0"></a> `006fbcb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fbcb4"></a> `006fbcb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006fbcb8"></a> `006fbcb8` | `49 00 40 b9` | ldr w9,[x2] | `FALL_THROUGH`
<a id="insn-006fbcbc"></a> `006fbcbc` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-006fbcc0"></a> `006fbcc0` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-006fbcc4"></a> `006fbcc4` | `3f 09 00 71` | cmp w9,#0x2 | `FALL_THROUGH`
<a id="insn-006fbcc8"></a> `006fbcc8` | `81 01 00 54` | b.ne 0x006fbcf8 | `CONDITIONAL_JUMP`
<a id="insn-006fbccc"></a> `006fbccc` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-006fbcd0"></a> `006fbcd0` | `40 01 00 54` | b.eq 0x006fbcf8 | `CONDITIONAL_JUMP`
<a id="insn-006fbcd4"></a> `006fbcd4` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-006fbcd8"></a> `006fbcd8` | `07 fc f5 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-006fbcdc"></a> `006fbcdc` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-006fbce0"></a> `006fbce0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-006fbce4"></a> `006fbce4` | `3c 04 f6 97` | bl 0x0047cdd4 | `UNCONDITIONAL_CALL`
<a id="insn-006fbce8"></a> `006fbce8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006fbcec"></a> `006fbcec` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fbcf0"></a> `006fbcf0` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-006fbcf4"></a> `006fbcf4` | `21 f5 06 14` | b 0x008b9178 | `CALL_TERMINATOR`
<a id="insn-006fbcf8"></a> `006fbcf8` | `3f 15 00 71` | cmp w9,#0x5 | `FALL_THROUGH`
<a id="insn-006fbcfc"></a> `006fbcfc` | `01 05 00 54` | b.ne 0x006fbd9c | `CONDITIONAL_JUMP`
<a id="insn-006fbd00"></a> `006fbd00` | `e8 04 00 35` | cbnz w8,0x006fbd9c | `CONDITIONAL_JUMP`
<a id="insn-006fbd04"></a> `006fbd04` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-006fbd08"></a> `006fbd08` | `60 82 00 91` | add x0,x19,#0x20 | `FALL_THROUGH`
<a id="insn-006fbd0c"></a> `006fbd0c` | `7f 02 00 39` | strb wzr,[x19] | `FALL_THROUGH`
<a id="insn-006fbd10"></a> `006fbd10` | `81 8e 42 f8` | ldr x1,[x20, #0x28]! | `FALL_THROUGH`
<a id="insn-006fbd14"></a> `006fbd14` | `d8 fc ff 97` | bl 0x006fb074 | `UNCONDITIONAL_CALL`
<a id="insn-006fbd18"></a> `006fbd18` | `74 12 00 f9` | str x20,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-006fbd1c"></a> `006fbd1c` | `7f 1a 00 f9` | str xzr,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-006fbd20"></a> `006fbd20` | `9f 02 00 f9` | str xzr,[x20] | `FALL_THROUGH`
<a id="insn-006fbd24"></a> `006fbd24` | `f5 55 05 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006fbd28"></a> `006fbd28` | `88 0e 84 52` | mov w8,#0x2074 | `FALL_THROUGH`
<a id="insn-006fbd2c"></a> `006fbd2c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-006fbd30"></a> `006fbd30` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006fbd34"></a> `006fbd34` | `f1 55 05 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006fbd38"></a> `006fbd38` | `08 13 84 52` | mov w8,#0x2098 | `FALL_THROUGH`
<a id="insn-006fbd3c"></a> `006fbd3c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-006fbd40"></a> `006fbd40` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006fbd44"></a> `006fbd44` | `ed 55 05 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006fbd48"></a> `006fbd48` | `08 0f 86 52` | mov w8,#0x3078 | `FALL_THROUGH`
<a id="insn-006fbd4c"></a> `006fbd4c` | `81 02 80 52` | mov w1,#0x14 | `FALL_THROUGH`
<a id="insn-006fbd50"></a> `006fbd50` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-006fbd54"></a> `006fbd54` | `43 1d 0e 94` | bl 0x00a83260 | `UNCONDITIONAL_CALL`
<a id="insn-006fbd58"></a> `006fbd58` | `e8 55 05 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006fbd5c"></a> `006fbd5c` | `08 b8 50 91` | add x8,x0,#0x42e, LSL #12 | `FALL_THROUGH`
<a id="insn-006fbd60"></a> `006fbd60` | `00 81 3d 91` | add x0,x8,#0xf60 | `FALL_THROUGH`
<a id="insn-006fbd64"></a> `006fbd64` | `b0 d9 fe 97` | bl 0x006b2424 | `UNCONDITIONAL_CALL`
<a id="insn-006fbd68"></a> `006fbd68` | `e4 55 05 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006fbd6c"></a> `006fbd6c` | `61 06 40 b9` | ldr w1,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-006fbd70"></a> `006fbd70` | `62 16 40 b9` | ldr w2,[x19, #0x14] | `FALL_THROUGH`
<a id="insn-006fbd74"></a> `006fbd74` | `13 f2 9d 52` | mov w19,#0xef90 | `FALL_THROUGH`
<a id="insn-006fbd78"></a> `006fbd78` | `53 08 a0 72` | movk w19,#0x42, LSL #16 | `FALL_THROUGH`
<a id="insn-006fbd7c"></a> `006fbd7c` | `00 00 13 8b` | add x0,x0,x19 | `FALL_THROUGH`
<a id="insn-006fbd80"></a> `006fbd80` | `e0 d1 ff 97` | bl 0x006f0500 | `UNCONDITIONAL_CALL`
<a id="insn-006fbd84"></a> `006fbd84` | `dd 55 05 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006fbd88"></a> `006fbd88` | `00 00 13 8b` | add x0,x0,x19 | `FALL_THROUGH`
<a id="insn-006fbd8c"></a> `006fbd8c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-006fbd90"></a> `006fbd90` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fbd94"></a> `006fbd94` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-006fbd98"></a> `006fbd98` | `fc b9 ff 17` | b 0x006ea588 | `CALL_TERMINATOR`
<a id="insn-006fbd9c"></a> `006fbd9c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fbda0"></a> `006fbda0` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-006fbda4"></a> `006fbda4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006fbcac`](#insn-006fbcac) 範囲 `[['006fbcac', '006fbccb']]`
  - `CONDITIONAL_JUMP` [`006fbcc8`](#insn-006fbcc8) → [`006fbcf8`](#insn-006fbcf8)
  - `FALL_THROUGH` [`006fbcc8`](#insn-006fbcc8) → [`006fbccc`](#insn-006fbccc)
- ブロック [`006fbccc`](#insn-006fbccc) 範囲 `[['006fbccc', '006fbcd3']]`
  - `CONDITIONAL_JUMP` [`006fbcd0`](#insn-006fbcd0) → [`006fbcf8`](#insn-006fbcf8)
  - `FALL_THROUGH` [`006fbcd0`](#insn-006fbcd0) → [`006fbcd4`](#insn-006fbcd4)
- ブロック [`006fbcd4`](#insn-006fbcd4) 範囲 `[['006fbcd4', '006fbcf7']]`
- ブロック [`006fbcf8`](#insn-006fbcf8) 範囲 `[['006fbcf8', '006fbcff']]`
  - `CONDITIONAL_JUMP` [`006fbcfc`](#insn-006fbcfc) → [`006fbd9c`](#insn-006fbd9c)
  - `FALL_THROUGH` [`006fbcfc`](#insn-006fbcfc) → [`006fbd00`](#insn-006fbd00)
- ブロック [`006fbd00`](#insn-006fbd00) 範囲 `[['006fbd00', '006fbd03']]`
  - `CONDITIONAL_JUMP` [`006fbd00`](#insn-006fbd00) → [`006fbd9c`](#insn-006fbd9c)
  - `FALL_THROUGH` [`006fbd00`](#insn-006fbd00) → [`006fbd04`](#insn-006fbd04)
- ブロック [`006fbd04`](#insn-006fbd04) 範囲 `[['006fbd04', '006fbd9b']]`
- ブロック [`006fbd9c`](#insn-006fbd9c) 範囲 `[['006fbd9c', '006fbda7']]`

## 命令位置別の参照

- [`006fbcac`](#insn-006fbcac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbcb0`](#insn-006fbcb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbcc8`](#insn-006fbcc8) → [`006fbcf8`](#insn-006fbcf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbcd0`](#insn-006fbcd0) → [`006fbcf8`](#insn-006fbcf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbcd8`](#insn-006fbcd8) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`006fbce4`](#insn-006fbce4) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`006fbcec`](#insn-006fbcec) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbcf0`](#insn-006fbcf0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbcf4`](#insn-006fbcf4) → [`008b9178`](../008b9/008b9178.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9178` · 推定シンボル `None` · 推定型 `None`
- [`006fbcfc`](#insn-006fbcfc) → [`006fbd9c`](#insn-006fbd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd00`](#insn-006fbd00) → [`006fbd9c`](#insn-006fbd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd14`](#insn-006fbd14) → [`006fb074`](006fb074.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006fb074` · 推定シンボル `None` · 推定型 `None`
- [`006fbd24`](#insn-006fbd24) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006fbd30`](#insn-006fbd30) → `00332074`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`006fbd34`](#insn-006fbd34) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006fbd40`](#insn-006fbd40) → `00332098`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`006fbd44`](#insn-006fbd44) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006fbd54`](#insn-006fbd54) → [`00a83260`](../00a83/00a83260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a83260` · 推定シンボル `None` · 推定型 `None`
- [`006fbd58`](#insn-006fbd58) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006fbd64`](#insn-006fbd64) → [`006b2424`](../006b2/006b2424.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006b2424` · 推定シンボル `None` · 推定型 `None`
- [`006fbd68`](#insn-006fbd68) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006fbd80`](#insn-006fbd80) → [`006f0500`](../006f0/006f0500.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006f0500` · 推定シンボル `None` · 推定型 `None`
- [`006fbd84`](#insn-006fbd84) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006fbd90`](#insn-006fbd90) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd94`](#insn-006fbd94) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd98`](#insn-006fbd98) → [`006ea588`](../006ea/006ea588.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006ea588` · 推定シンボル `None` · 推定型 `None`
- [`006fbd9c`](#insn-006fbd9c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbda0`](#insn-006fbda0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006fbcac`](#insn-006fbcac)

~~~json
{
  "source": "006fbcac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbcb0`](#insn-006fbcb0)

~~~json
{
  "source": "006fbcb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbcc8`](#insn-006fbcc8)

~~~json
{
  "source": "006fbcc8",
  "target": "006fbcf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbcd0`](#insn-006fbcd0)

~~~json
{
  "source": "006fbcd0",
  "target": "006fbcf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbcd8`](#insn-006fbcd8)

~~~json
{
  "source": "006fbcd8",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbce4`](#insn-006fbce4)

~~~json
{
  "source": "006fbce4",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbcec`](#insn-006fbcec)

~~~json
{
  "source": "006fbcec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbcf0`](#insn-006fbcf0)

~~~json
{
  "source": "006fbcf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbcf4`](#insn-006fbcf4)

~~~json
{
  "source": "006fbcf4",
  "target": "008b9178",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbcfc`](#insn-006fbcfc)

~~~json
{
  "source": "006fbcfc",
  "target": "006fbd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd00`](#insn-006fbd00)

~~~json
{
  "source": "006fbd00",
  "target": "006fbd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd14`](#insn-006fbd14)

~~~json
{
  "source": "006fbd14",
  "target": "006fb074",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbd24`](#insn-006fbd24)

~~~json
{
  "source": "006fbd24",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbd30`](#insn-006fbd30)

~~~json
{
  "source": "006fbd30",
  "target": "00332074",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332070",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e40462008c240900",
  "capture_start": "00332070",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006fbd34`](#insn-006fbd34)

~~~json
{
  "source": "006fbd34",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbd40`](#insn-006fbd40)

~~~json
{
  "source": "006fbd40",
  "target": "00332098",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332098",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "dc0562001c250900",
  "capture_start": "00332098",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006fbd44`](#insn-006fbd44)

~~~json
{
  "source": "006fbd44",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbd54`](#insn-006fbd54)

~~~json
{
  "source": "006fbd54",
  "target": "00a83260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbd58`](#insn-006fbd58)

~~~json
{
  "source": "006fbd58",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbd64`](#insn-006fbd64)

~~~json
{
  "source": "006fbd64",
  "target": "006b2424",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbd68`](#insn-006fbd68)

~~~json
{
  "source": "006fbd68",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbd80`](#insn-006fbd80)

~~~json
{
  "source": "006fbd80",
  "target": "006f0500",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbd84`](#insn-006fbd84)

~~~json
{
  "source": "006fbd84",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbd90`](#insn-006fbd90)

~~~json
{
  "source": "006fbd90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd94`](#insn-006fbd94)

~~~json
{
  "source": "006fbd94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd98`](#insn-006fbd98)

~~~json
{
  "source": "006fbd98",
  "target": "006ea588",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbd9c`](#insn-006fbd9c)

~~~json
{
  "source": "006fbd9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbda0`](#insn-006fbda0)

~~~json
{
  "source": "006fbda0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
