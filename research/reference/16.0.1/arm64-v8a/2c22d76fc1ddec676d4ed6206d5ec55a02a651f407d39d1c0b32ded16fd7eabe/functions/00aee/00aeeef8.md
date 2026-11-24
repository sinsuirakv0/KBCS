# 00aeeef8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aeead0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeead0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0065.md#compare-f1143d6370ce8db1ba79bd202a27bdcb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aeef94`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeef94.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0066.md#compare-433596309085ad9ce031c501ba4857ca)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeeef8",
  "name": "FUN_00aeeef8",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b172516f4df4ea1a4a6c7f40da0bb96b11c154ef365faea44ad12ea3da868fe2",
  "source_text_sha256": "b172516f4df4ea1a4a6c7f40da0bb96b11c154ef365faea44ad12ea3da868fe2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeeef8",
        "00aeefeb"
      ],
      [
        "00aef038",
        "00aef03b"
      ]
    ],
    "bytes_sha256": "6890e32ed7e76f63ac19311cc9c9ae2b921b221a91ead7973602c4c744a2be08",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [00658dac](../00658/00658dac.md)
- [00aef0b8](../00aef/00aef0b8.md)
- [00aef0bc](../00aef/00aef0bc.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1646 bytes

~~~c

void FUN_00aeeef8(long param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  undefined ***pppuVar4;
  undefined8 uVar5;
  long lVar6;
  undefined **local_60;
  long lStack_58;
  undefined8 local_50;
  long *local_40;
  long local_28;
  
  pppuVar4 = &local_60;
                    /* try { // try from 00aeef00 to 00beef07 has its CatchHandler @ 00aeeff4 */
                    /* try { // try from 00aeef08 to 00bef023 has its CatchHandler @ 00aeee28 */
  lVar2 = tpidr_el0;
  local_28 = *(long *)(lVar2 + 0x28);
  iVar1 = *param_3;
  if (iVar1 == 4) {
    lStack_58 = *(long *)(param_1 + 8);
    local_50 = *(undefined8 *)(param_1 + 0x10);
    local_60 = &PTR_FUN_00c8df68;
    local_40 = (long *)&local_60;
    FUN_00658dac(lStack_58 + 0x1fd8,local_50,&local_60);
    if ((undefined ***)local_40 == &local_60) {
      lVar6 = 0x20;
    }
    else {
      if (local_40 == (long *)0x0) goto LAB_00aeefcc;
      lVar6 = 0x28;
      pppuVar4 = (undefined ***)local_40;
    }
    (**(code **)((long)*pppuVar4 + lVar6))();
  }
  else {
    if (iVar1 == 3) {
      uVar3 = FUN_0047acf4();
      if (*(long *)(lVar2 + 0x28) == local_28) {
        uVar5 = 0xb;
        goto LAB_00aeef60;
      }
      goto LAB_00aef038;
    }
    if (iVar1 == 0) {
      uVar3 = FUN_0047acf4();
      if (*(long *)(lVar2 + 0x28) != local_28) goto LAB_00aef038;
      uVar5 = 10;
LAB_00aeef60:
      FUN_0047cdd4(uVar3,uVar5,0);
      return;
    }
  }
LAB_00aeefcc:
  if (*(long *)(lVar2 + 0x28) == local_28) {
    return;
  }
LAB_00aef038:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeeef8"></a> `00aeeef8` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00aeeefc"></a> `00aeeefc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aeef00"></a> `00aeef00` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeef04"></a> `00aeef04` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00aeef08"></a> `00aeef08` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aeef0c"></a> `00aeef0c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aeef10"></a> `00aeef10` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeef14"></a> `00aeef14` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aeef18"></a> `00aeef18` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00aeef1c"></a> `00aeef1c` | `c0 02 00 54` | b.eq 0x00aeef74 | `CONDITIONAL_JUMP`
<a id="insn-00aeef20"></a> `00aeef20` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aeef24"></a> `00aeef24` | `20 01 00 54` | b.eq 0x00aeef48 | `CONDITIONAL_JUMP`
<a id="insn-00aeef28"></a> `00aeef28` | `28 05 00 35` | cbnz w8,0x00aeefcc | `CONDITIONAL_JUMP`
<a id="insn-00aeef2c"></a> `00aeef2c` | `72 2f e6 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-00aeef30"></a> `00aeef30` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aeef34"></a> `00aeef34` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeef38"></a> `00aeef38` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aeef3c"></a> `00aeef3c` | `e1 07 00 54` | b.ne 0x00aef038 | `CONDITIONAL_JUMP`
<a id="insn-00aeef40"></a> `00aeef40` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00aeef44"></a> `00aeef44` | `07 00 00 14` | b 0x00aeef60 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeef48"></a> `00aeef48` | `6b 2f e6 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-00aeef4c"></a> `00aeef4c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aeef50"></a> `00aeef50` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeef54"></a> `00aeef54` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aeef58"></a> `00aeef58` | `01 07 00 54` | b.ne 0x00aef038 | `CONDITIONAL_JUMP`
<a id="insn-00aeef5c"></a> `00aeef5c` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00aeef60"></a> `00aeef60` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeef64"></a> `00aeef64` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeef68"></a> `00aeef68` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aeef6c"></a> `00aeef6c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00aeef70"></a> `00aeef70` | `99 37 e6 17` | b 0x0047cdd4 | `CALL_TERMINATOR`
<a id="insn-00aeef74"></a> `00aeef74` | `08 84 40 a9` | ldp x8,x1,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aeef78"></a> `00aeef78` | `e9 0c 00 f0` | adrp x9,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aeef7c"></a> `00aeef7c` | `29 a1 3d 91` | add x9,x9,#0xf68 | `FALL_THROUGH`
<a id="insn-00aeef80"></a> `00aeef80` | `f3 03 00 91` | mov x19,sp | `FALL_THROUGH`
<a id="insn-00aeef84"></a> `00aeef84` | `f3 13 00 f9` | str x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeef88"></a> `00aeef88` | `e9 23 00 a9` | stp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00aeef8c"></a> `00aeef8c` | `09 fb 83 52` | mov w9,#0x1fd8 | `FALL_THROUGH`
<a id="insn-00aeef90"></a> `00aeef90` | `e1 0b 00 f9` | str x1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeef94"></a> `00aeef94` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aeef98"></a> `00aeef98` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00aeef9c"></a> `00aeef9c` | `84 a7 ed 97` | bl 0x00658dac | `UNCONDITIONAL_CALL`
<a id="insn-00aeefa0"></a> `00aeefa0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeefa4"></a> `00aeefa4` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-00aeefa8"></a> `00aeefa8` | `80 00 00 54` | b.eq 0x00aeefb8 | `CONDITIONAL_JUMP`
<a id="insn-00aeefac"></a> `00aeefac` | `00 01 00 b4` | cbz x0,0x00aeefcc | `CONDITIONAL_JUMP`
<a id="insn-00aeefb0"></a> `00aeefb0` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00aeefb4"></a> `00aeefb4` | `03 00 00 14` | b 0x00aeefc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeefb8"></a> `00aeefb8` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00aeefbc"></a> `00aeefbc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aeefc0"></a> `00aeefc0` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00aeefc4"></a> `00aeefc4` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aeefc8"></a> `00aeefc8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeefcc"></a> `00aeefcc` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aeefd0"></a> `00aeefd0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeefd4"></a> `00aeefd4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aeefd8"></a> `00aeefd8` | `01 03 00 54` | b.ne 0x00aef038 | `CONDITIONAL_JUMP`
<a id="insn-00aeefdc"></a> `00aeefdc` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeefe0"></a> `00aeefe0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aeefe4"></a> `00aeefe4` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00aeefe8"></a> `00aeefe8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aef038"></a> `00aef038` | `aa a3 05 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeeef8`](#insn-00aeeef8) 範囲 `[['00aeeef8', '00aeeeff']]`
  - `FALL_THROUGH` [`00aeeefc`](#insn-00aeeefc) → [`00aeef00`](#insn-00aeef00)
- ブロック [`00aeef00`](#insn-00aeef00) 範囲 `[['00aeef00', '00aeef07']]`
  - `FALL_THROUGH` [`00aeef04`](#insn-00aeef04) → [`00aeef08`](#insn-00aeef08)
- ブロック [`00aeef08`](#insn-00aeef08) 範囲 `[['00aeef08', '00aeef1f']]`
  - `CONDITIONAL_JUMP` [`00aeef1c`](#insn-00aeef1c) → [`00aeef74`](#insn-00aeef74)
  - `FALL_THROUGH` [`00aeef1c`](#insn-00aeef1c) → [`00aeef20`](#insn-00aeef20)
- ブロック [`00aeef20`](#insn-00aeef20) 範囲 `[['00aeef20', '00aeef27']]`
  - `CONDITIONAL_JUMP` [`00aeef24`](#insn-00aeef24) → [`00aeef48`](#insn-00aeef48)
  - `FALL_THROUGH` [`00aeef24`](#insn-00aeef24) → [`00aeef28`](#insn-00aeef28)
- ブロック [`00aeef28`](#insn-00aeef28) 範囲 `[['00aeef28', '00aeef2b']]`
  - `CONDITIONAL_JUMP` [`00aeef28`](#insn-00aeef28) → [`00aeefcc`](#insn-00aeefcc)
  - `FALL_THROUGH` [`00aeef28`](#insn-00aeef28) → [`00aeef2c`](#insn-00aeef2c)
- ブロック [`00aeef2c`](#insn-00aeef2c) 範囲 `[['00aeef2c', '00aeef3f']]`
  - `CONDITIONAL_JUMP` [`00aeef3c`](#insn-00aeef3c) → [`00aef038`](#insn-00aef038)
  - `FALL_THROUGH` [`00aeef3c`](#insn-00aeef3c) → [`00aeef40`](#insn-00aeef40)
- ブロック [`00aeef40`](#insn-00aeef40) 範囲 `[['00aeef40', '00aeef47']]`
  - `UNCONDITIONAL_JUMP` [`00aeef44`](#insn-00aeef44) → [`00aeef60`](#insn-00aeef60)
- ブロック [`00aeef48`](#insn-00aeef48) 範囲 `[['00aeef48', '00aeef5b']]`
  - `CONDITIONAL_JUMP` [`00aeef58`](#insn-00aeef58) → [`00aef038`](#insn-00aef038)
  - `FALL_THROUGH` [`00aeef58`](#insn-00aeef58) → [`00aeef5c`](#insn-00aeef5c)
- ブロック [`00aeef5c`](#insn-00aeef5c) 範囲 `[['00aeef5c', '00aeef5f']]`
  - `FALL_THROUGH` [`00aeef5c`](#insn-00aeef5c) → [`00aeef60`](#insn-00aeef60)
- ブロック [`00aeef60`](#insn-00aeef60) 範囲 `[['00aeef60', '00aeef73']]`
- ブロック [`00aeef74`](#insn-00aeef74) 範囲 `[['00aeef74', '00aeefab']]`
  - `CONDITIONAL_JUMP` [`00aeefa8`](#insn-00aeefa8) → [`00aeefb8`](#insn-00aeefb8)
  - `FALL_THROUGH` [`00aeefa8`](#insn-00aeefa8) → [`00aeefac`](#insn-00aeefac)
- ブロック [`00aeefac`](#insn-00aeefac) 範囲 `[['00aeefac', '00aeefaf']]`
  - `CONDITIONAL_JUMP` [`00aeefac`](#insn-00aeefac) → [`00aeefcc`](#insn-00aeefcc)
  - `FALL_THROUGH` [`00aeefac`](#insn-00aeefac) → [`00aeefb0`](#insn-00aeefb0)
- ブロック [`00aeefb0`](#insn-00aeefb0) 範囲 `[['00aeefb0', '00aeefb7']]`
  - `UNCONDITIONAL_JUMP` [`00aeefb4`](#insn-00aeefb4) → [`00aeefc0`](#insn-00aeefc0)
- ブロック [`00aeefb8`](#insn-00aeefb8) 範囲 `[['00aeefb8', '00aeefbf']]`
  - `FALL_THROUGH` [`00aeefbc`](#insn-00aeefbc) → [`00aeefc0`](#insn-00aeefc0)
- ブロック [`00aeefc0`](#insn-00aeefc0) 範囲 `[['00aeefc0', '00aeefcb']]`
  - `FALL_THROUGH` [`00aeefc8`](#insn-00aeefc8) → [`00aeefcc`](#insn-00aeefcc)
- ブロック [`00aeefcc`](#insn-00aeefcc) 範囲 `[['00aeefcc', '00aeefdb']]`
  - `CONDITIONAL_JUMP` [`00aeefd8`](#insn-00aeefd8) → [`00aef038`](#insn-00aef038)
  - `FALL_THROUGH` [`00aeefd8`](#insn-00aeefd8) → [`00aeefdc`](#insn-00aeefdc)
- ブロック [`00aeefdc`](#insn-00aeefdc) 範囲 `[['00aeefdc', '00aeefeb']]`
- ブロック [`00aef038`](#insn-00aef038) 範囲 `[['00aef038', '00aef03b']]`

## 命令位置別の参照

- [`00aeeefc`](#insn-00aeeefc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef00`](#insn-00aeef00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef10`](#insn-00aeef10) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef1c`](#insn-00aeef1c) → [`00aeef74`](#insn-00aeef74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef24`](#insn-00aeef24) → [`00aeef48`](#insn-00aeef48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef28`](#insn-00aeef28) → [`00aeefcc`](#insn-00aeefcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef2c`](#insn-00aeef2c) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`00aeef34`](#insn-00aeef34) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef3c`](#insn-00aeef3c) → [`00aef038`](#insn-00aef038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef44`](#insn-00aeef44) → [`00aeef60`](#insn-00aeef60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef48`](#insn-00aeef48) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`00aeef50`](#insn-00aeef50) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef58`](#insn-00aeef58) → [`00aef038`](#insn-00aef038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef64`](#insn-00aeef64) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef68`](#insn-00aeef68) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef70`](#insn-00aeef70) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`00aeef84`](#insn-00aeef84) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef88`](#insn-00aeef88) → `00c8df68`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aeef88`](#insn-00aeef88) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef90`](#insn-00aeef90) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef9c`](#insn-00aeef9c) → [`00658dac`](../00658/00658dac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00658dac` · 推定シンボル `None` · 推定型 `None`
- [`00aeefa0`](#insn-00aeefa0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeefa8`](#insn-00aeefa8) → [`00aeefb8`](#insn-00aeefb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeefac`](#insn-00aeefac) → [`00aeefcc`](#insn-00aeefcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeefb4`](#insn-00aeefb4) → [`00aeefc0`](#insn-00aeefc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeefc0`](#insn-00aeefc0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeefc4`](#insn-00aeefc4) → `00c8df88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aeefc4`](#insn-00aeefc4) → `00c8df90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aeefc8`](#insn-00aeefc8) → [`00aef0b8`](../00aef/00aef0b8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aef0b8` · 推定シンボル `None` · 推定型 `None`
- [`00aeefc8`](#insn-00aeefc8) → [`00aef0bc`](../00aef/00aef0bc.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aef0bc` · 推定シンボル `None` · 推定型 `None`
- [`00aeefd0`](#insn-00aeefd0) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeefd8`](#insn-00aeefd8) → [`00aef038`](#insn-00aef038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeefdc`](#insn-00aeefdc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeefe0`](#insn-00aeefe0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef038`](#insn-00aef038) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeeefc`](#insn-00aeeefc)

~~~json
{
  "source": "00aeeefc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef00`](#insn-00aeef00)

~~~json
{
  "source": "00aeef00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef10`](#insn-00aeef10)

~~~json
{
  "source": "00aeef10",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef1c`](#insn-00aeef1c)

~~~json
{
  "source": "00aeef1c",
  "target": "00aeef74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef24`](#insn-00aeef24)

~~~json
{
  "source": "00aeef24",
  "target": "00aeef48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef28`](#insn-00aeef28)

~~~json
{
  "source": "00aeef28",
  "target": "00aeefcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef2c`](#insn-00aeef2c)

~~~json
{
  "source": "00aeef2c",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeef34`](#insn-00aeef34)

~~~json
{
  "source": "00aeef34",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef3c`](#insn-00aeef3c)

~~~json
{
  "source": "00aeef3c",
  "target": "00aef038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef44`](#insn-00aeef44)

~~~json
{
  "source": "00aeef44",
  "target": "00aeef60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef48`](#insn-00aeef48)

~~~json
{
  "source": "00aeef48",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeef50`](#insn-00aeef50)

~~~json
{
  "source": "00aeef50",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef58`](#insn-00aeef58)

~~~json
{
  "source": "00aeef58",
  "target": "00aef038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef64`](#insn-00aeef64)

~~~json
{
  "source": "00aeef64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef68`](#insn-00aeef68)

~~~json
{
  "source": "00aeef68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef70`](#insn-00aeef70)

~~~json
{
  "source": "00aeef70",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeef84`](#insn-00aeef84)

~~~json
{
  "source": "00aeef84",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef88`](#insn-00aeef88)

~~~json
{
  "source": "00aeef88",
  "target": "00c8df68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8df68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeef88`](#insn-00aeef88)

~~~json
{
  "source": "00aeef88",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef90`](#insn-00aeef90)

~~~json
{
  "source": "00aeef90",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef9c`](#insn-00aeef9c)

~~~json
{
  "source": "00aeef9c",
  "target": "00658dac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeefa0`](#insn-00aeefa0)

~~~json
{
  "source": "00aeefa0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeefa8`](#insn-00aeefa8)

~~~json
{
  "source": "00aeefa8",
  "target": "00aeefb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeefac`](#insn-00aeefac)

~~~json
{
  "source": "00aeefac",
  "target": "00aeefcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeefb4`](#insn-00aeefb4)

~~~json
{
  "source": "00aeefb4",
  "target": "00aeefc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeefc0`](#insn-00aeefc0)

~~~json
{
  "source": "00aeefc0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeefc4`](#insn-00aeefc4)

~~~json
{
  "source": "00aeefc4",
  "target": "00c8df88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8df88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeefc4`](#insn-00aeefc4)

~~~json
{
  "source": "00aeefc4",
  "target": "00c8df90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8df90",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeefc8`](#insn-00aeefc8)

~~~json
{
  "source": "00aeefc8",
  "target": "00aef0b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeefc8`](#insn-00aeefc8)

~~~json
{
  "source": "00aeefc8",
  "target": "00aef0bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeefd0`](#insn-00aeefd0)

~~~json
{
  "source": "00aeefd0",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeefd8`](#insn-00aeefd8)

~~~json
{
  "source": "00aeefd8",
  "target": "00aef038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeefdc`](#insn-00aeefdc)

~~~json
{
  "source": "00aeefdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeefe0`](#insn-00aeefe0)

~~~json
{
  "source": "00aeefe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef038`](#insn-00aef038)

~~~json
{
  "source": "00aef038",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
