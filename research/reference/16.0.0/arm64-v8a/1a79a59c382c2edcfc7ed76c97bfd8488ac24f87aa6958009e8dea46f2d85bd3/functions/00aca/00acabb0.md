# 00acabb0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0162.md#review-f9a0f7ba606ff9f347961c760dbccdf0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acadac`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acadac.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-6ecb283157bd416854cb24e8aa3e30e5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acabb0",
  "name": "FUN_00acabb0",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d4bd94e9c1ca4dfc4e4c825e29405b472826d02f5326a79816346cbd9e6a35b2",
  "source_text_sha256": "d4bd94e9c1ca4dfc4e4c825e29405b472826d02f5326a79816346cbd9e6a35b2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acabb0",
        "00acadb7"
      ]
    ],
    "bytes_sha256": "e08f80586b66650270d1b709b16bff34ebc04234d1d1e000abe41bbd05c42ae9",
    "instruction_count": 130,
    "instruction_bytes": 520,
    "body_bytes": 520,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00680dc8](../00680/00680dc8.md)
- [006b53c4](../006b5/006b53c4.md)
- [0073edf4](../0073e/0073edf4.md)
- [00773854](../00773/00773854.md)
- [00789da0](../00789/00789da0.md)
- [007df0a8](../007df/007df0a8.md)
- [0082fb2c](../0082f/0082fb2c.md)
- [008cb4a8](../008cb/008cb4a8.md)
- [008d3700](../008d3/008d3700.md)
- [008de8bc](../008de/008de8bc.md)
- [008f7cdc](../008f7/008f7cdc.md)
- [008feea4](../008fe/008feea4.md)
- [0091a9dc](../0091a/0091a9dc.md)
- [00996ea0](../00996/00996ea0.md)
- [00a3e32c](../00a3e/00a3e32c.md)
- [00a79a0c](../00a79/00a79a0c.md)
- [00ab6544](../00ab6/00ab6544.md)
- [00ac08a0](../00ac0/00ac08a0.md)
- [00ae0e64](../00ae0/00ae0e64.md)

## 呼び出し先

- [00467820](../00467/00467820.md)
- [00469bc4](../00469/00469bc4.md)
- [0046c984](../0046c/0046c984.md)
- [00489f0c](../00489/00489f0c.md)
- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1838 bytes

~~~c

void FUN_00acabb0(undefined8 param_1,undefined8 param_2,int param_3)

{
  int iVar1;
  undefined8 uVar2;
  long lVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  float fVar7;
  
  uVar2 = FUN_00467820();
  lVar3 = FUN_00489f0c(param_2,0);
  iVar4 = (int)((float)*(int *)(lVar3 + 0xc) * 1.25);
  lVar3 = FUN_008514b8();
  fVar7 = (float)*(int *)(lVar3 + 0x44e364) * 1.25;
  iVar5 = (int)fVar7;
  FUN_008514b8();
  iVar1 = FUN_0046c984();
  lVar3 = FUN_008514b8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514b8();
  FUN_00469bc4(uVar2,param_2,
               (int)((((float)iVar1 * 0.5 + -572.0) - (float)iVar6) -
                    (float)(*(int *)(lVar3 + 0x44e360) << 1)),0,iVar5,iVar4,0);
  FUN_008514b8();
  iVar1 = FUN_0046c984();
  lVar3 = FUN_008514b8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514b8();
  FUN_00469bc4(uVar2,param_2,
               (int)(((float)iVar6 + (float)iVar1 * 0.5 + (float)param_3) -
                    (float)*(int *)(lVar3 + 0x44e360)),0,iVar5,iVar4,1);
  FUN_008514b8();
  iVar1 = FUN_0046c984();
  lVar3 = FUN_008514b8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514b8();
  fVar7 = (float)(int)fVar7;
  FUN_00469bc4(uVar2,param_2,
               (int)(((((float)iVar1 * 0.5 + -572.0) - (float)iVar6) -
                     (float)(*(int *)(lVar3 + 0x44e360) << 1)) - fVar7),0,iVar5,iVar4,1);
  FUN_008514b8();
  iVar1 = FUN_0046c984();
  lVar3 = FUN_008514b8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514b8();
  FUN_00469bc4(uVar2,param_2,
               (int)((((float)iVar6 + (float)iVar1 * 0.5 + (float)param_3) -
                     (float)*(int *)(lVar3 + 0x44e360)) + fVar7),0,iVar5,iVar4,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acabb0"></a> `00acabb0` | `ec 0f 19 fc` | str d12,[sp, #-0x70]! | `FALL_THROUGH`
<a id="insn-00acabb4"></a> `00acabb4` | `eb ab 00 6d` | stp d11,d10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acabb8"></a> `00acabb8` | `e9 a3 01 6d` | stp d9,d8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acabbc"></a> `00acabbc` | `fd fb 02 a9` | stp x29,x30,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acabc0"></a> `00acabc0` | `f9 1f 00 f9` | str x25,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00acabc4"></a> `00acabc4` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acabc8"></a> `00acabc8` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acabcc"></a> `00acabcc` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acabd0"></a> `00acabd0` | `fd a3 00 91` | add x29,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00acabd4"></a> `00acabd4` | `f7 03 02 2a` | mov w23,w2 | `FALL_THROUGH`
<a id="insn-00acabd8"></a> `00acabd8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00acabdc"></a> `00acabdc` | `11 73 e6 97` | bl 0x00467820 | `UNCONDITIONAL_CALL`
<a id="insn-00acabe0"></a> `00acabe0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acabe4"></a> `00acabe4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acabe8"></a> `00acabe8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acabec"></a> `00acabec` | `c8 fc e6 97` | bl 0x00489f0c | `UNCONDITIONAL_CALL`
<a id="insn-00acabf0"></a> `00acabf0` | `00 0c 40 bd` | ldr s0,[x0, #0xc] | `FALL_THROUGH`
<a id="insn-00acabf4"></a> `00acabf4` | `08 90 2e 1e` | fmov s8,0x3fa00000 | `FALL_THROUGH`
<a id="insn-00acabf8"></a> `00acabf8` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acabfc"></a> `00acabfc` | `00 08 28 1e` | fmul s0,s0,s8 | `FALL_THROUGH`
<a id="insn-00acac00"></a> `00acac00` | `15 00 38 1e` | fcvtzs w21,s0 | `FALL_THROUGH`
<a id="insn-00acac04"></a> `00acac04` | `2d 1a f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acac08"></a> `00acac08` | `88 6c 9c 52` | mov w8,#0xe364 | `FALL_THROUGH`
<a id="insn-00acac0c"></a> `00acac0c` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-00acac10"></a> `00acac10` | `00 68 68 bc` | ldr s0,[x0,x8] | `FALL_THROUGH`
<a id="insn-00acac14"></a> `00acac14` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acac18"></a> `00acac18` | `09 08 28 1e` | fmul s9,s0,s8 | `FALL_THROUGH`
<a id="insn-00acac1c"></a> `00acac1c` | `36 01 38 1e` | fcvtzs w22,s9 | `FALL_THROUGH`
<a id="insn-00acac20"></a> `00acac20` | `26 1a f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acac24"></a> `00acac24` | `58 87 e6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-00acac28"></a> `00acac28` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00acac2c"></a> `00acac2c` | `e8 81 b8 52` | mov w8,#0xc40f0000 | `FALL_THROUGH`
<a id="insn-00acac30"></a> `00acac30` | `08 10 2c 1e` | fmov s8,0x3f000000 | `FALL_THROUGH`
<a id="insn-00acac34"></a> `00acac34` | `0b 01 27 1e` | fmov s11,w8 | `FALL_THROUGH`
<a id="insn-00acac38"></a> `00acac38` | `0a 2c 08 1f` | fmadd s10,s0,s8,s11 | `FALL_THROUGH`
<a id="insn-00acac3c"></a> `00acac3c` | `1f 1a f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acac40"></a> `00acac40` | `98 f0 87 52` | mov w24,#0x3f84 | `FALL_THROUGH`
<a id="insn-00acac44"></a> `00acac44` | `78 06 a0 72` | movk w24,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acac48"></a> `00acac48` | `00 68 78 bc` | ldr s0,[x0,x24] | `FALL_THROUGH`
<a id="insn-00acac4c"></a> `00acac4c` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acac50"></a> `00acac50` | `4a 39 20 1e` | fsub s10,s10,s0 | `FALL_THROUGH`
<a id="insn-00acac54"></a> `00acac54` | `19 1a f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acac58"></a> `00acac58` | `19 6c 9c 52` | mov w25,#0xe360 | `FALL_THROUGH`
<a id="insn-00acac5c"></a> `00acac5c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acac60"></a> `00acac60` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acac64"></a> `00acac64` | `99 08 a0 72` | movk w25,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-00acac68"></a> `00acac68` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00acac6c"></a> `00acac6c` | `e5 03 15 2a` | mov w5,w21 | `FALL_THROUGH`
<a id="insn-00acac70"></a> `00acac70` | `08 68 79 b8` | ldr w8,[x0, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acac74"></a> `00acac74` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acac78"></a> `00acac78` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00acac7c"></a> `00acac7c` | `08 79 1f 53` | lsl w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acac80"></a> `00acac80` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-00acac84"></a> `00acac84` | `40 39 20 1e` | fsub s0,s10,s0 | `FALL_THROUGH`
<a id="insn-00acac88"></a> `00acac88` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00acac8c"></a> `00acac8c` | `ce 7b e6 97` | bl 0x00469bc4 | `UNCONDITIONAL_CALL`
<a id="insn-00acac90"></a> `00acac90` | `0a 1a f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acac94"></a> `00acac94` | `3c 87 e6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-00acac98"></a> `00acac98` | `0c 00 22 1e` | scvtf s12,w0 | `FALL_THROUGH`
<a id="insn-00acac9c"></a> `00acac9c` | `07 1a f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acaca0"></a> `00acaca0` | `00 68 78 bc` | ldr s0,[x0,x24] | `FALL_THROUGH`
<a id="insn-00acaca4"></a> `00acaca4` | `ea 02 22 1e` | scvtf s10,w23 | `FALL_THROUGH`
<a id="insn-00acaca8"></a> `00acaca8` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acacac"></a> `00acacac` | `80 01 08 1f` | fmadd s0,s12,s8,s0 | `FALL_THROUGH`
<a id="insn-00acacb0"></a> `00acacb0` | `0c 28 2a 1e` | fadd s12,s0,s10 | `FALL_THROUGH`
<a id="insn-00acacb4"></a> `00acacb4` | `01 1a f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acacb8"></a> `00acacb8` | `00 68 79 bc` | ldr s0,[x0,x25] | `FALL_THROUGH`
<a id="insn-00acacbc"></a> `00acacbc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acacc0"></a> `00acacc0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acacc4"></a> `00acacc4` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acacc8"></a> `00acacc8` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00acaccc"></a> `00acaccc` | `e5 03 15 2a` | mov w5,w21 | `FALL_THROUGH`
<a id="insn-00acacd0"></a> `00acacd0` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acacd4"></a> `00acacd4` | `26 00 80 52` | mov w6,#0x1 | `FALL_THROUGH`
<a id="insn-00acacd8"></a> `00acacd8` | `80 39 20 1e` | fsub s0,s12,s0 | `FALL_THROUGH`
<a id="insn-00acacdc"></a> `00acacdc` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00acace0"></a> `00acace0` | `b9 7b e6 97` | bl 0x00469bc4 | `UNCONDITIONAL_CALL`
<a id="insn-00acace4"></a> `00acace4` | `f5 19 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acace8"></a> `00acace8` | `27 87 e6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-00acacec"></a> `00acacec` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00acacf0"></a> `00acacf0` | `0b 2c 08 1f` | fmadd s11,s0,s8,s11 | `FALL_THROUGH`
<a id="insn-00acacf4"></a> `00acacf4` | `f1 19 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acacf8"></a> `00acacf8` | `00 68 78 bc` | ldr s0,[x0,x24] | `FALL_THROUGH`
<a id="insn-00acacfc"></a> `00acacfc` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acad00"></a> `00acad00` | `6b 39 20 1e` | fsub s11,s11,s0 | `FALL_THROUGH`
<a id="insn-00acad04"></a> `00acad04` | `ed 19 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acad08"></a> `00acad08` | `20 b9 a1 5e` | fcvtzs s0,s9 | `FALL_THROUGH`
<a id="insn-00acad0c"></a> `00acad0c` | `08 68 79 b8` | ldr w8,[x0, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acad10"></a> `00acad10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acad14"></a> `00acad14` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acad18"></a> `00acad18` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acad1c"></a> `00acad1c` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00acad20"></a> `00acad20` | `08 79 1f 53` | lsl w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acad24"></a> `00acad24` | `e5 03 15 2a` | mov w5,w21 | `FALL_THROUGH`
<a id="insn-00acad28"></a> `00acad28` | `26 00 80 52` | mov w6,#0x1 | `FALL_THROUGH`
<a id="insn-00acad2c"></a> `00acad2c` | `09 d8 21 5e` | scvtf s9,s0 | `FALL_THROUGH`
<a id="insn-00acad30"></a> `00acad30` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-00acad34"></a> `00acad34` | `60 39 20 1e` | fsub s0,s11,s0 | `FALL_THROUGH`
<a id="insn-00acad38"></a> `00acad38` | `00 38 29 1e` | fsub s0,s0,s9 | `FALL_THROUGH`
<a id="insn-00acad3c"></a> `00acad3c` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00acad40"></a> `00acad40` | `a1 7b e6 97` | bl 0x00469bc4 | `UNCONDITIONAL_CALL`
<a id="insn-00acad44"></a> `00acad44` | `dd 19 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acad48"></a> `00acad48` | `0f 87 e6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-00acad4c"></a> `00acad4c` | `0b 00 22 1e` | scvtf s11,w0 | `FALL_THROUGH`
<a id="insn-00acad50"></a> `00acad50` | `da 19 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acad54"></a> `00acad54` | `00 68 78 bc` | ldr s0,[x0,x24] | `FALL_THROUGH`
<a id="insn-00acad58"></a> `00acad58` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acad5c"></a> `00acad5c` | `60 01 08 1f` | fmadd s0,s11,s8,s0 | `FALL_THROUGH`
<a id="insn-00acad60"></a> `00acad60` | `08 28 2a 1e` | fadd s8,s0,s10 | `FALL_THROUGH`
<a id="insn-00acad64"></a> `00acad64` | `d5 19 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acad68"></a> `00acad68` | `00 68 79 bc` | ldr s0,[x0,x25] | `FALL_THROUGH`
<a id="insn-00acad6c"></a> `00acad6c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acad70"></a> `00acad70` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acad74"></a> `00acad74` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acad78"></a> `00acad78` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00acad7c"></a> `00acad7c` | `e5 03 15 2a` | mov w5,w21 | `FALL_THROUGH`
<a id="insn-00acad80"></a> `00acad80` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acad84"></a> `00acad84` | `00 39 20 1e` | fsub s0,s8,s0 | `FALL_THROUGH`
<a id="insn-00acad88"></a> `00acad88` | `00 28 29 1e` | fadd s0,s0,s9 | `FALL_THROUGH`
<a id="insn-00acad8c"></a> `00acad8c` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00acad90"></a> `00acad90` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00acad94"></a> `00acad94` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acad98"></a> `00acad98` | `f9 1f 40 f9` | ldr x25,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00acad9c"></a> `00acad9c` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acada0"></a> `00acada0` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acada4"></a> `00acada4` | `fd fb 42 a9` | ldp x29,x30,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acada8"></a> `00acada8` | `e9 a3 41 6d` | ldp d9,d8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acadac"></a> `00acadac` | `eb ab 40 6d` | ldp d11,d10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acadb0"></a> `00acadb0` | `ec 07 47 fc` | ldr d12,[sp], #0x70 | `FALL_THROUGH`
<a id="insn-00acadb4"></a> `00acadb4` | `84 7b e6 17` | b 0x00469bc4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acabb0`](#insn-00acabb0) 範囲 `[['00acabb0', '00acadb7']]`

## 命令位置別の参照

- [`00acabb0`](#insn-00acabb0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabb4`](#insn-00acabb4) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabb8`](#insn-00acabb8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabbc`](#insn-00acabbc) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabc0`](#insn-00acabc0) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabc4`](#insn-00acabc4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabc8`](#insn-00acabc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabcc`](#insn-00acabcc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabdc`](#insn-00acabdc) → [`00467820`](../00467/00467820.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467820` · 推定シンボル `None` · 推定型 `None`
- [`00acabec`](#insn-00acabec) → [`00489f0c`](../00489/00489f0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f0c` · 推定シンボル `None` · 推定型 `None`
- [`00acac04`](#insn-00acac04) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acac20`](#insn-00acac20) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acac24`](#insn-00acac24) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`00acac3c`](#insn-00acac3c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acac48`](#insn-00acac48) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acac54`](#insn-00acac54) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acac8c`](#insn-00acac8c) → [`00469bc4`](../00469/00469bc4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469bc4` · 推定シンボル `None` · 推定型 `None`
- [`00acac90`](#insn-00acac90) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acac94`](#insn-00acac94) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`00acac9c`](#insn-00acac9c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acaca0`](#insn-00acaca0) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acacb4`](#insn-00acacb4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acace0`](#insn-00acace0) → [`00469bc4`](../00469/00469bc4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469bc4` · 推定シンボル `None` · 推定型 `None`
- [`00acace4`](#insn-00acace4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acace8`](#insn-00acace8) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`00acacf4`](#insn-00acacf4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acacf8`](#insn-00acacf8) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acad04`](#insn-00acad04) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acad40`](#insn-00acad40) → [`00469bc4`](../00469/00469bc4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469bc4` · 推定シンボル `None` · 推定型 `None`
- [`00acad44`](#insn-00acad44) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acad48`](#insn-00acad48) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`00acad50`](#insn-00acad50) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acad54`](#insn-00acad54) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acad64`](#insn-00acad64) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acad94`](#insn-00acad94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad98`](#insn-00acad98) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad9c`](#insn-00acad9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acada0`](#insn-00acada0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acada4`](#insn-00acada4) → `Stack[-0x48]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acada8`](#insn-00acada8) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadac`](#insn-00acadac) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadb4`](#insn-00acadb4) → [`00469bc4`](../00469/00469bc4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469bc4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acabb0`](#insn-00acabb0)

~~~json
{
  "source": "00acabb0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabb4`](#insn-00acabb4)

~~~json
{
  "source": "00acabb4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabb8`](#insn-00acabb8)

~~~json
{
  "source": "00acabb8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabbc`](#insn-00acabbc)

~~~json
{
  "source": "00acabbc",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabc0`](#insn-00acabc0)

~~~json
{
  "source": "00acabc0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabc4`](#insn-00acabc4)

~~~json
{
  "source": "00acabc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabc8`](#insn-00acabc8)

~~~json
{
  "source": "00acabc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabcc`](#insn-00acabcc)

~~~json
{
  "source": "00acabcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabdc`](#insn-00acabdc)

~~~json
{
  "source": "00acabdc",
  "target": "00467820",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acabec`](#insn-00acabec)

~~~json
{
  "source": "00acabec",
  "target": "00489f0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acac04`](#insn-00acac04)

~~~json
{
  "source": "00acac04",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acac20`](#insn-00acac20)

~~~json
{
  "source": "00acac20",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acac24`](#insn-00acac24)

~~~json
{
  "source": "00acac24",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acac3c`](#insn-00acac3c)

~~~json
{
  "source": "00acac3c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acac48`](#insn-00acac48)

~~~json
{
  "source": "00acac48",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "5cbf6c0048271100",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acac54`](#insn-00acac54)

~~~json
{
  "source": "00acac54",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acac8c`](#insn-00acac8c)

~~~json
{
  "source": "00acac8c",
  "target": "00469bc4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acac90`](#insn-00acac90)

~~~json
{
  "source": "00acac90",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acac94`](#insn-00acac94)

~~~json
{
  "source": "00acac94",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acac9c`](#insn-00acac9c)

~~~json
{
  "source": "00acac9c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaca0`](#insn-00acaca0)

~~~json
{
  "source": "00acaca0",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "5cbf6c0048271100",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acacb4`](#insn-00acacb4)

~~~json
{
  "source": "00acacb4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acace0`](#insn-00acace0)

~~~json
{
  "source": "00acace0",
  "target": "00469bc4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acace4`](#insn-00acace4)

~~~json
{
  "source": "00acace4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acace8`](#insn-00acace8)

~~~json
{
  "source": "00acace8",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acacf4`](#insn-00acacf4)

~~~json
{
  "source": "00acacf4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acacf8`](#insn-00acacf8)

~~~json
{
  "source": "00acacf8",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "5cbf6c0048271100",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acad04`](#insn-00acad04)

~~~json
{
  "source": "00acad04",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acad40`](#insn-00acad40)

~~~json
{
  "source": "00acad40",
  "target": "00469bc4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acad44`](#insn-00acad44)

~~~json
{
  "source": "00acad44",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acad48`](#insn-00acad48)

~~~json
{
  "source": "00acad48",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acad50`](#insn-00acad50)

~~~json
{
  "source": "00acad50",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acad54`](#insn-00acad54)

~~~json
{
  "source": "00acad54",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "5cbf6c0048271100",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acad64`](#insn-00acad64)

~~~json
{
  "source": "00acad64",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acad94`](#insn-00acad94)

~~~json
{
  "source": "00acad94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad98`](#insn-00acad98)

~~~json
{
  "source": "00acad98",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad9c`](#insn-00acad9c)

~~~json
{
  "source": "00acad9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acada0`](#insn-00acada0)

~~~json
{
  "source": "00acada0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acada4`](#insn-00acada4)

~~~json
{
  "source": "00acada4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acada8`](#insn-00acada8)

~~~json
{
  "source": "00acada8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadac`](#insn-00acadac)

~~~json
{
  "source": "00acadac",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadb4`](#insn-00acadb4)

~~~json
{
  "source": "00acadb4",
  "target": "00469bc4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
