# 00acadac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acabb0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acabb0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-6ecb283157bd416854cb24e8aa3e30e5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acae1c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acae1c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0008.md#compare-7450d1b44ac25de725ee1b0eb806a257)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acadac",
  "name": "FUN_00acadac",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4cfca376a8422fdb563d57e24dbc93b7bb11c1f0313ee0dedb662ecb15e8772b",
  "source_text_sha256": "4cfca376a8422fdb563d57e24dbc93b7bb11c1f0313ee0dedb662ecb15e8772b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acadac",
        "00acafb3"
      ]
    ],
    "bytes_sha256": "9c6784ddaa1ad2edda62fbc79836e68e6036bf893293bdee5683697337b982b8",
    "instruction_count": 130,
    "instruction_bytes": 520,
    "body_bytes": 520,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00680e08](../00680/00680e08.md)
- [006b5404](../006b5/006b5404.md)
- [0073ee34](../0073e/0073ee34.md)
- [00773894](../00773/00773894.md)
- [00789de0](../00789/00789de0.md)
- [007df0e8](../007df/007df0e8.md)
- [0082fb6c](../0082f/0082fb6c.md)
- [008cb644](../008cb/008cb644.md)
- [008d389c](../008d3/008d389c.md)
- [008dea58](../008de/008dea58.md)
- [008f7e78](../008f7/008f7e78.md)
- [008ff040](../008ff/008ff040.md)
- [0091ab78](../0091a/0091ab78.md)
- [0099703c](../00997/0099703c.md)
- [00a3e524](../00a3e/00a3e524.md)
- [00a79c04](../00a79/00a79c04.md)
- [00ab6740](../00ab6/00ab6740.md)
- [00ac0a9c](../00ac0/00ac0a9c.md)
- [00ae128c](../00ae1/00ae128c.md)

## 呼び出し先

- [00467860](../00467/00467860.md)
- [00469c04](../00469/00469c04.md)
- [0046c9c4](../0046c/0046c9c4.md)
- [00489f4c](../00489/00489f4c.md)
- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1838 bytes

~~~c

void FUN_00acadac(undefined8 param_1,undefined8 param_2,int param_3)

{
  int iVar1;
  undefined8 uVar2;
  long lVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  float fVar7;
  
  uVar2 = FUN_00467860();
  lVar3 = FUN_00489f4c(param_2,0);
  iVar4 = (int)((float)*(int *)(lVar3 + 0xc) * 1.25);
  lVar3 = FUN_008514f8();
  fVar7 = (float)*(int *)(lVar3 + 0x44e364) * 1.25;
  iVar5 = (int)fVar7;
  FUN_008514f8();
  iVar1 = FUN_0046c9c4();
  lVar3 = FUN_008514f8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514f8();
  FUN_00469c04(uVar2,param_2,
               (int)((((float)iVar1 * 0.5 + -572.0) - (float)iVar6) -
                    (float)(*(int *)(lVar3 + 0x44e360) << 1)),0,iVar5,iVar4,0);
  FUN_008514f8();
  iVar1 = FUN_0046c9c4();
  lVar3 = FUN_008514f8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514f8();
  FUN_00469c04(uVar2,param_2,
               (int)(((float)iVar6 + (float)iVar1 * 0.5 + (float)param_3) -
                    (float)*(int *)(lVar3 + 0x44e360)),0,iVar5,iVar4,1);
  FUN_008514f8();
  iVar1 = FUN_0046c9c4();
  lVar3 = FUN_008514f8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514f8();
  fVar7 = (float)(int)fVar7;
  FUN_00469c04(uVar2,param_2,
               (int)(((((float)iVar1 * 0.5 + -572.0) - (float)iVar6) -
                     (float)(*(int *)(lVar3 + 0x44e360) << 1)) - fVar7),0,iVar5,iVar4,1);
  FUN_008514f8();
  iVar1 = FUN_0046c9c4();
  lVar3 = FUN_008514f8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514f8();
  FUN_00469c04(uVar2,param_2,
               (int)((((float)iVar6 + (float)iVar1 * 0.5 + (float)param_3) -
                     (float)*(int *)(lVar3 + 0x44e360)) + fVar7),0,iVar5,iVar4,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acadac"></a> `00acadac` | `ec 0f 19 fc` | str d12,[sp, #-0x70]! | `FALL_THROUGH`
<a id="insn-00acadb0"></a> `00acadb0` | `eb ab 00 6d` | stp d11,d10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acadb4"></a> `00acadb4` | `e9 a3 01 6d` | stp d9,d8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acadb8"></a> `00acadb8` | `fd fb 02 a9` | stp x29,x30,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acadbc"></a> `00acadbc` | `f9 1f 00 f9` | str x25,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00acadc0"></a> `00acadc0` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acadc4"></a> `00acadc4` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acadc8"></a> `00acadc8` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acadcc"></a> `00acadcc` | `fd a3 00 91` | add x29,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00acadd0"></a> `00acadd0` | `f7 03 02 2a` | mov w23,w2 | `FALL_THROUGH`
<a id="insn-00acadd4"></a> `00acadd4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00acadd8"></a> `00acadd8` | `a2 72 e6 97` | bl 0x00467860 | `UNCONDITIONAL_CALL`
<a id="insn-00acaddc"></a> `00acaddc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acade0"></a> `00acade0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acade4"></a> `00acade4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acade8"></a> `00acade8` | `59 fc e6 97` | bl 0x00489f4c | `UNCONDITIONAL_CALL`
<a id="insn-00acadec"></a> `00acadec` | `00 0c 40 bd` | ldr s0,[x0, #0xc] | `FALL_THROUGH`
<a id="insn-00acadf0"></a> `00acadf0` | `08 90 2e 1e` | fmov s8,0x3fa00000 | `FALL_THROUGH`
<a id="insn-00acadf4"></a> `00acadf4` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acadf8"></a> `00acadf8` | `00 08 28 1e` | fmul s0,s0,s8 | `FALL_THROUGH`
<a id="insn-00acadfc"></a> `00acadfc` | `15 00 38 1e` | fcvtzs w21,s0 | `FALL_THROUGH`
<a id="insn-00acae00"></a> `00acae00` | `be 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acae04"></a> `00acae04` | `88 6c 9c 52` | mov w8,#0xe364 | `FALL_THROUGH`
<a id="insn-00acae08"></a> `00acae08` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-00acae0c"></a> `00acae0c` | `00 68 68 bc` | ldr s0,[x0,x8] | `FALL_THROUGH`
<a id="insn-00acae10"></a> `00acae10` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acae14"></a> `00acae14` | `09 08 28 1e` | fmul s9,s0,s8 | `FALL_THROUGH`
<a id="insn-00acae18"></a> `00acae18` | `36 01 38 1e` | fcvtzs w22,s9 | `FALL_THROUGH`
<a id="insn-00acae1c"></a> `00acae1c` | `b7 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acae20"></a> `00acae20` | `e9 86 e6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-00acae24"></a> `00acae24` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00acae28"></a> `00acae28` | `e8 81 b8 52` | mov w8,#0xc40f0000 | `FALL_THROUGH`
<a id="insn-00acae2c"></a> `00acae2c` | `08 10 2c 1e` | fmov s8,0x3f000000 | `FALL_THROUGH`
<a id="insn-00acae30"></a> `00acae30` | `0b 01 27 1e` | fmov s11,w8 | `FALL_THROUGH`
<a id="insn-00acae34"></a> `00acae34` | `0a 2c 08 1f` | fmadd s10,s0,s8,s11 | `FALL_THROUGH`
<a id="insn-00acae38"></a> `00acae38` | `b0 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acae3c"></a> `00acae3c` | `98 f0 87 52` | mov w24,#0x3f84 | `FALL_THROUGH`
<a id="insn-00acae40"></a> `00acae40` | `78 06 a0 72` | movk w24,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acae44"></a> `00acae44` | `00 68 78 bc` | ldr s0,[x0,x24] | `FALL_THROUGH`
<a id="insn-00acae48"></a> `00acae48` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acae4c"></a> `00acae4c` | `4a 39 20 1e` | fsub s10,s10,s0 | `FALL_THROUGH`
<a id="insn-00acae50"></a> `00acae50` | `aa 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acae54"></a> `00acae54` | `19 6c 9c 52` | mov w25,#0xe360 | `FALL_THROUGH`
<a id="insn-00acae58"></a> `00acae58` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acae5c"></a> `00acae5c` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acae60"></a> `00acae60` | `99 08 a0 72` | movk w25,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-00acae64"></a> `00acae64` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00acae68"></a> `00acae68` | `e5 03 15 2a` | mov w5,w21 | `FALL_THROUGH`
<a id="insn-00acae6c"></a> `00acae6c` | `08 68 79 b8` | ldr w8,[x0, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acae70"></a> `00acae70` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acae74"></a> `00acae74` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00acae78"></a> `00acae78` | `08 79 1f 53` | lsl w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acae7c"></a> `00acae7c` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-00acae80"></a> `00acae80` | `40 39 20 1e` | fsub s0,s10,s0 | `FALL_THROUGH`
<a id="insn-00acae84"></a> `00acae84` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00acae88"></a> `00acae88` | `5f 7b e6 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-00acae8c"></a> `00acae8c` | `9b 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acae90"></a> `00acae90` | `cd 86 e6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-00acae94"></a> `00acae94` | `0c 00 22 1e` | scvtf s12,w0 | `FALL_THROUGH`
<a id="insn-00acae98"></a> `00acae98` | `98 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acae9c"></a> `00acae9c` | `00 68 78 bc` | ldr s0,[x0,x24] | `FALL_THROUGH`
<a id="insn-00acaea0"></a> `00acaea0` | `ea 02 22 1e` | scvtf s10,w23 | `FALL_THROUGH`
<a id="insn-00acaea4"></a> `00acaea4` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acaea8"></a> `00acaea8` | `80 01 08 1f` | fmadd s0,s12,s8,s0 | `FALL_THROUGH`
<a id="insn-00acaeac"></a> `00acaeac` | `0c 28 2a 1e` | fadd s12,s0,s10 | `FALL_THROUGH`
<a id="insn-00acaeb0"></a> `00acaeb0` | `92 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acaeb4"></a> `00acaeb4` | `00 68 79 bc` | ldr s0,[x0,x25] | `FALL_THROUGH`
<a id="insn-00acaeb8"></a> `00acaeb8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acaebc"></a> `00acaebc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acaec0"></a> `00acaec0` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acaec4"></a> `00acaec4` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00acaec8"></a> `00acaec8` | `e5 03 15 2a` | mov w5,w21 | `FALL_THROUGH`
<a id="insn-00acaecc"></a> `00acaecc` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acaed0"></a> `00acaed0` | `26 00 80 52` | mov w6,#0x1 | `FALL_THROUGH`
<a id="insn-00acaed4"></a> `00acaed4` | `80 39 20 1e` | fsub s0,s12,s0 | `FALL_THROUGH`
<a id="insn-00acaed8"></a> `00acaed8` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00acaedc"></a> `00acaedc` | `4a 7b e6 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-00acaee0"></a> `00acaee0` | `86 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acaee4"></a> `00acaee4` | `b8 86 e6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-00acaee8"></a> `00acaee8` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00acaeec"></a> `00acaeec` | `0b 2c 08 1f` | fmadd s11,s0,s8,s11 | `FALL_THROUGH`
<a id="insn-00acaef0"></a> `00acaef0` | `82 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acaef4"></a> `00acaef4` | `00 68 78 bc` | ldr s0,[x0,x24] | `FALL_THROUGH`
<a id="insn-00acaef8"></a> `00acaef8` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acaefc"></a> `00acaefc` | `6b 39 20 1e` | fsub s11,s11,s0 | `FALL_THROUGH`
<a id="insn-00acaf00"></a> `00acaf00` | `7e 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf04"></a> `00acaf04` | `20 b9 a1 5e` | fcvtzs s0,s9 | `FALL_THROUGH`
<a id="insn-00acaf08"></a> `00acaf08` | `08 68 79 b8` | ldr w8,[x0, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acaf0c"></a> `00acaf0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acaf10"></a> `00acaf10` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acaf14"></a> `00acaf14` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acaf18"></a> `00acaf18` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00acaf1c"></a> `00acaf1c` | `08 79 1f 53` | lsl w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acaf20"></a> `00acaf20` | `e5 03 15 2a` | mov w5,w21 | `FALL_THROUGH`
<a id="insn-00acaf24"></a> `00acaf24` | `26 00 80 52` | mov w6,#0x1 | `FALL_THROUGH`
<a id="insn-00acaf28"></a> `00acaf28` | `09 d8 21 5e` | scvtf s9,s0 | `FALL_THROUGH`
<a id="insn-00acaf2c"></a> `00acaf2c` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-00acaf30"></a> `00acaf30` | `60 39 20 1e` | fsub s0,s11,s0 | `FALL_THROUGH`
<a id="insn-00acaf34"></a> `00acaf34` | `00 38 29 1e` | fsub s0,s0,s9 | `FALL_THROUGH`
<a id="insn-00acaf38"></a> `00acaf38` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00acaf3c"></a> `00acaf3c` | `32 7b e6 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf40"></a> `00acaf40` | `6e 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf44"></a> `00acaf44` | `a0 86 e6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf48"></a> `00acaf48` | `0b 00 22 1e` | scvtf s11,w0 | `FALL_THROUGH`
<a id="insn-00acaf4c"></a> `00acaf4c` | `6b 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf50"></a> `00acaf50` | `00 68 78 bc` | ldr s0,[x0,x24] | `FALL_THROUGH`
<a id="insn-00acaf54"></a> `00acaf54` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acaf58"></a> `00acaf58` | `60 01 08 1f` | fmadd s0,s11,s8,s0 | `FALL_THROUGH`
<a id="insn-00acaf5c"></a> `00acaf5c` | `08 28 2a 1e` | fadd s8,s0,s10 | `FALL_THROUGH`
<a id="insn-00acaf60"></a> `00acaf60` | `66 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf64"></a> `00acaf64` | `00 68 79 bc` | ldr s0,[x0,x25] | `FALL_THROUGH`
<a id="insn-00acaf68"></a> `00acaf68` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acaf6c"></a> `00acaf6c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acaf70"></a> `00acaf70` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acaf74"></a> `00acaf74` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00acaf78"></a> `00acaf78` | `e5 03 15 2a` | mov w5,w21 | `FALL_THROUGH`
<a id="insn-00acaf7c"></a> `00acaf7c` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acaf80"></a> `00acaf80` | `00 39 20 1e` | fsub s0,s8,s0 | `FALL_THROUGH`
<a id="insn-00acaf84"></a> `00acaf84` | `00 28 29 1e` | fadd s0,s0,s9 | `FALL_THROUGH`
<a id="insn-00acaf88"></a> `00acaf88` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00acaf8c"></a> `00acaf8c` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00acaf90"></a> `00acaf90` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acaf94"></a> `00acaf94` | `f9 1f 40 f9` | ldr x25,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00acaf98"></a> `00acaf98` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acaf9c"></a> `00acaf9c` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acafa0"></a> `00acafa0` | `fd fb 42 a9` | ldp x29,x30,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acafa4"></a> `00acafa4` | `e9 a3 41 6d` | ldp d9,d8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acafa8"></a> `00acafa8` | `eb ab 40 6d` | ldp d11,d10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acafac"></a> `00acafac` | `ec 07 47 fc` | ldr d12,[sp], #0x70 | `FALL_THROUGH`
<a id="insn-00acafb0"></a> `00acafb0` | `15 7b e6 17` | b 0x00469c04 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acadac`](#insn-00acadac) 範囲 `[['00acadac', '00acafb3']]`

## 命令位置別の参照

- [`00acadac`](#insn-00acadac) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadb0`](#insn-00acadb0) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadb4`](#insn-00acadb4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadb8`](#insn-00acadb8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadbc`](#insn-00acadbc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadc0`](#insn-00acadc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadc4`](#insn-00acadc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadc8`](#insn-00acadc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadd8`](#insn-00acadd8) → [`00467860`](../00467/00467860.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467860` · 推定シンボル `None` · 推定型 `None`
- [`00acade8`](#insn-00acade8) → [`00489f4c`](../00489/00489f4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f4c` · 推定シンボル `None` · 推定型 `None`
- [`00acae00`](#insn-00acae00) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acae1c`](#insn-00acae1c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acae20`](#insn-00acae20) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`00acae38`](#insn-00acae38) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acae44`](#insn-00acae44) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acae50`](#insn-00acae50) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acae88`](#insn-00acae88) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`00acae8c`](#insn-00acae8c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acae90`](#insn-00acae90) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`00acae98`](#insn-00acae98) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acae9c`](#insn-00acae9c) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acaeb0`](#insn-00acaeb0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acaedc`](#insn-00acaedc) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`00acaee0`](#insn-00acaee0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acaee4`](#insn-00acaee4) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`00acaef0`](#insn-00acaef0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acaef4`](#insn-00acaef4) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acaf00`](#insn-00acaf00) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acaf3c`](#insn-00acaf3c) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`00acaf40`](#insn-00acaf40) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acaf44`](#insn-00acaf44) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`00acaf4c`](#insn-00acaf4c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acaf50`](#insn-00acaf50) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acaf60`](#insn-00acaf60) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acaf90`](#insn-00acaf90) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf94`](#insn-00acaf94) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf98`](#insn-00acaf98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf9c`](#insn-00acaf9c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafa0`](#insn-00acafa0) → `Stack[-0x48]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafa4`](#insn-00acafa4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafa8`](#insn-00acafa8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafb0`](#insn-00acafb0) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acadac`](#insn-00acadac)

~~~json
{
  "source": "00acadac",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadb0`](#insn-00acadb0)

~~~json
{
  "source": "00acadb0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadb4`](#insn-00acadb4)

~~~json
{
  "source": "00acadb4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadb8`](#insn-00acadb8)

~~~json
{
  "source": "00acadb8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadbc`](#insn-00acadbc)

~~~json
{
  "source": "00acadbc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadc0`](#insn-00acadc0)

~~~json
{
  "source": "00acadc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadc4`](#insn-00acadc4)

~~~json
{
  "source": "00acadc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadc8`](#insn-00acadc8)

~~~json
{
  "source": "00acadc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadd8`](#insn-00acadd8)

~~~json
{
  "source": "00acadd8",
  "target": "00467860",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acade8`](#insn-00acade8)

~~~json
{
  "source": "00acade8",
  "target": "00489f4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae00`](#insn-00acae00)

~~~json
{
  "source": "00acae00",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae1c`](#insn-00acae1c)

~~~json
{
  "source": "00acae1c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae20`](#insn-00acae20)

~~~json
{
  "source": "00acae20",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae38`](#insn-00acae38)

~~~json
{
  "source": "00acae38",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae44`](#insn-00acae44)

~~~json
{
  "source": "00acae44",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "4cb56c0058261100",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acae50`](#insn-00acae50)

~~~json
{
  "source": "00acae50",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae88`](#insn-00acae88)

~~~json
{
  "source": "00acae88",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae8c`](#insn-00acae8c)

~~~json
{
  "source": "00acae8c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae90`](#insn-00acae90)

~~~json
{
  "source": "00acae90",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae98`](#insn-00acae98)

~~~json
{
  "source": "00acae98",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae9c`](#insn-00acae9c)

~~~json
{
  "source": "00acae9c",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "4cb56c0058261100",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acaeb0`](#insn-00acaeb0)

~~~json
{
  "source": "00acaeb0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaedc`](#insn-00acaedc)

~~~json
{
  "source": "00acaedc",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaee0`](#insn-00acaee0)

~~~json
{
  "source": "00acaee0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaee4`](#insn-00acaee4)

~~~json
{
  "source": "00acaee4",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaef0`](#insn-00acaef0)

~~~json
{
  "source": "00acaef0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaef4`](#insn-00acaef4)

~~~json
{
  "source": "00acaef4",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "4cb56c0058261100",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acaf00`](#insn-00acaf00)

~~~json
{
  "source": "00acaf00",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf3c`](#insn-00acaf3c)

~~~json
{
  "source": "00acaf3c",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf40`](#insn-00acaf40)

~~~json
{
  "source": "00acaf40",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf44`](#insn-00acaf44)

~~~json
{
  "source": "00acaf44",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf4c`](#insn-00acaf4c)

~~~json
{
  "source": "00acaf4c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf50`](#insn-00acaf50)

~~~json
{
  "source": "00acaf50",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "4cb56c0058261100",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acaf60`](#insn-00acaf60)

~~~json
{
  "source": "00acaf60",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf90`](#insn-00acaf90)

~~~json
{
  "source": "00acaf90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf94`](#insn-00acaf94)

~~~json
{
  "source": "00acaf94",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf98`](#insn-00acaf98)

~~~json
{
  "source": "00acaf98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf9c`](#insn-00acaf9c)

~~~json
{
  "source": "00acaf9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafa0`](#insn-00acafa0)

~~~json
{
  "source": "00acafa0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafa4`](#insn-00acafa4)

~~~json
{
  "source": "00acafa4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafa8`](#insn-00acafa8)

~~~json
{
  "source": "00acafa8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafb0`](#insn-00acafb0)

~~~json
{
  "source": "00acafb0",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
