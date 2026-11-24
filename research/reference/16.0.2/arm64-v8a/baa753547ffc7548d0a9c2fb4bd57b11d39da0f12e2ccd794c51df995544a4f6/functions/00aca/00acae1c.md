# 00acae1c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acadac`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acadac.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0008.md#compare-7450d1b44ac25de725ee1b0eb806a257)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00acbe10`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acb/00acbe10.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0006.md#compare-989288fd92254bb33e77975d75d96c80)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acae1c",
  "name": "FUN_00acae1c",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1cf2b7717ccb3ccdb353f3d841145c33a8fdac91d9fadec558bc972cd3aaa989",
  "source_text_sha256": "1cf2b7717ccb3ccdb353f3d841145c33a8fdac91d9fadec558bc972cd3aaa989",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acae1c",
        "00acb023"
      ]
    ],
    "bytes_sha256": "23e878fc876df1f2d2b9d17232195898d622904ae72b9d455b981320572c16d5",
    "instruction_count": 130,
    "instruction_bytes": 520,
    "body_bytes": 520,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00680e48](../00680/00680e48.md)
- [006b545c](../006b5/006b545c.md)
- [0073ee8c](../0073e/0073ee8c.md)
- [007738ec](../00773/007738ec.md)
- [00789e38](../00789/00789e38.md)
- [007df140](../007df/007df140.md)
- [0082fbc4](../0082f/0082fbc4.md)
- [008cb698](../008cb/008cb698.md)
- [008d38f0](../008d3/008d38f0.md)
- [008deaac](../008de/008deaac.md)
- [008f7ecc](../008f7/008f7ecc.md)
- [008ff094](../008ff/008ff094.md)
- [0091abcc](../0091a/0091abcc.md)
- [00997090](../00997/00997090.md)
- [00a3e578](../00a3e/00a3e578.md)
- [00a79c74](../00a79/00a79c74.md)
- [00ab67b0](../00ab6/00ab67b0.md)
- [00ac0b0c](../00ac0/00ac0b0c.md)
- [00ae1328](../00ae1/00ae1328.md)

## 呼び出し先

- [004678a0](../00467/004678a0.md)
- [00469c44](../00469/00469c44.md)
- [0046ca04](../0046c/0046ca04.md)
- [00489f8c](../00489/00489f8c.md)
- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1838 bytes

~~~c

void FUN_00acae1c(undefined8 param_1,undefined8 param_2,int param_3)

{
  int iVar1;
  undefined8 uVar2;
  long lVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  float fVar7;
  
  uVar2 = FUN_004678a0();
  lVar3 = FUN_00489f8c(param_2,0);
  iVar4 = (int)((float)*(int *)(lVar3 + 0xc) * 1.25);
  lVar3 = FUN_00851550();
  fVar7 = (float)*(int *)(lVar3 + 0x44e364) * 1.25;
  iVar5 = (int)fVar7;
  FUN_00851550();
  iVar1 = FUN_0046ca04();
  lVar3 = FUN_00851550();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_00851550();
  FUN_00469c44(uVar2,param_2,
               (int)((((float)iVar1 * 0.5 + -572.0) - (float)iVar6) -
                    (float)(*(int *)(lVar3 + 0x44e360) << 1)),0,iVar5,iVar4,0);
  FUN_00851550();
  iVar1 = FUN_0046ca04();
  lVar3 = FUN_00851550();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_00851550();
  FUN_00469c44(uVar2,param_2,
               (int)(((float)iVar6 + (float)iVar1 * 0.5 + (float)param_3) -
                    (float)*(int *)(lVar3 + 0x44e360)),0,iVar5,iVar4,1);
  FUN_00851550();
  iVar1 = FUN_0046ca04();
  lVar3 = FUN_00851550();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_00851550();
  fVar7 = (float)(int)fVar7;
  FUN_00469c44(uVar2,param_2,
               (int)(((((float)iVar1 * 0.5 + -572.0) - (float)iVar6) -
                     (float)(*(int *)(lVar3 + 0x44e360) << 1)) - fVar7),0,iVar5,iVar4,1);
  FUN_00851550();
  iVar1 = FUN_0046ca04();
  lVar3 = FUN_00851550();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_00851550();
  FUN_00469c44(uVar2,param_2,
               (int)((((float)iVar6 + (float)iVar1 * 0.5 + (float)param_3) -
                     (float)*(int *)(lVar3 + 0x44e360)) + fVar7),0,iVar5,iVar4,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acae1c"></a> `00acae1c` | `ec 0f 19 fc` | str d12,[sp, #-0x70]! | `FALL_THROUGH`
<a id="insn-00acae20"></a> `00acae20` | `eb ab 00 6d` | stp d11,d10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acae24"></a> `00acae24` | `e9 a3 01 6d` | stp d9,d8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acae28"></a> `00acae28` | `fd fb 02 a9` | stp x29,x30,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acae2c"></a> `00acae2c` | `f9 1f 00 f9` | str x25,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00acae30"></a> `00acae30` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acae34"></a> `00acae34` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acae38"></a> `00acae38` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acae3c"></a> `00acae3c` | `fd a3 00 91` | add x29,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00acae40"></a> `00acae40` | `f7 03 02 2a` | mov w23,w2 | `FALL_THROUGH`
<a id="insn-00acae44"></a> `00acae44` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00acae48"></a> `00acae48` | `96 72 e6 97` | bl 0x004678a0 | `UNCONDITIONAL_CALL`
<a id="insn-00acae4c"></a> `00acae4c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acae50"></a> `00acae50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acae54"></a> `00acae54` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acae58"></a> `00acae58` | `4d fc e6 97` | bl 0x00489f8c | `UNCONDITIONAL_CALL`
<a id="insn-00acae5c"></a> `00acae5c` | `00 0c 40 bd` | ldr s0,[x0, #0xc] | `FALL_THROUGH`
<a id="insn-00acae60"></a> `00acae60` | `08 90 2e 1e` | fmov s8,0x3fa00000 | `FALL_THROUGH`
<a id="insn-00acae64"></a> `00acae64` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acae68"></a> `00acae68` | `00 08 28 1e` | fmul s0,s0,s8 | `FALL_THROUGH`
<a id="insn-00acae6c"></a> `00acae6c` | `15 00 38 1e` | fcvtzs w21,s0 | `FALL_THROUGH`
<a id="insn-00acae70"></a> `00acae70` | `b8 19 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acae74"></a> `00acae74` | `88 6c 9c 52` | mov w8,#0xe364 | `FALL_THROUGH`
<a id="insn-00acae78"></a> `00acae78` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-00acae7c"></a> `00acae7c` | `00 68 68 bc` | ldr s0,[x0,x8] | `FALL_THROUGH`
<a id="insn-00acae80"></a> `00acae80` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acae84"></a> `00acae84` | `09 08 28 1e` | fmul s9,s0,s8 | `FALL_THROUGH`
<a id="insn-00acae88"></a> `00acae88` | `36 01 38 1e` | fcvtzs w22,s9 | `FALL_THROUGH`
<a id="insn-00acae8c"></a> `00acae8c` | `b1 19 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acae90"></a> `00acae90` | `dd 86 e6 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-00acae94"></a> `00acae94` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00acae98"></a> `00acae98` | `e8 81 b8 52` | mov w8,#0xc40f0000 | `FALL_THROUGH`
<a id="insn-00acae9c"></a> `00acae9c` | `08 10 2c 1e` | fmov s8,0x3f000000 | `FALL_THROUGH`
<a id="insn-00acaea0"></a> `00acaea0` | `0b 01 27 1e` | fmov s11,w8 | `FALL_THROUGH`
<a id="insn-00acaea4"></a> `00acaea4` | `0a 2c 08 1f` | fmadd s10,s0,s8,s11 | `FALL_THROUGH`
<a id="insn-00acaea8"></a> `00acaea8` | `aa 19 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acaeac"></a> `00acaeac` | `98 f0 87 52` | mov w24,#0x3f84 | `FALL_THROUGH`
<a id="insn-00acaeb0"></a> `00acaeb0` | `78 06 a0 72` | movk w24,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acaeb4"></a> `00acaeb4` | `00 68 78 bc` | ldr s0,[x0,x24] | `FALL_THROUGH`
<a id="insn-00acaeb8"></a> `00acaeb8` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acaebc"></a> `00acaebc` | `4a 39 20 1e` | fsub s10,s10,s0 | `FALL_THROUGH`
<a id="insn-00acaec0"></a> `00acaec0` | `a4 19 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acaec4"></a> `00acaec4` | `19 6c 9c 52` | mov w25,#0xe360 | `FALL_THROUGH`
<a id="insn-00acaec8"></a> `00acaec8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acaecc"></a> `00acaecc` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acaed0"></a> `00acaed0` | `99 08 a0 72` | movk w25,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-00acaed4"></a> `00acaed4` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00acaed8"></a> `00acaed8` | `e5 03 15 2a` | mov w5,w21 | `FALL_THROUGH`
<a id="insn-00acaedc"></a> `00acaedc` | `08 68 79 b8` | ldr w8,[x0, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acaee0"></a> `00acaee0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acaee4"></a> `00acaee4` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00acaee8"></a> `00acaee8` | `08 79 1f 53` | lsl w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acaeec"></a> `00acaeec` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-00acaef0"></a> `00acaef0` | `40 39 20 1e` | fsub s0,s10,s0 | `FALL_THROUGH`
<a id="insn-00acaef4"></a> `00acaef4` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00acaef8"></a> `00acaef8` | `53 7b e6 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-00acaefc"></a> `00acaefc` | `95 19 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf00"></a> `00acaf00` | `c1 86 e6 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf04"></a> `00acaf04` | `0c 00 22 1e` | scvtf s12,w0 | `FALL_THROUGH`
<a id="insn-00acaf08"></a> `00acaf08` | `92 19 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf0c"></a> `00acaf0c` | `00 68 78 bc` | ldr s0,[x0,x24] | `FALL_THROUGH`
<a id="insn-00acaf10"></a> `00acaf10` | `ea 02 22 1e` | scvtf s10,w23 | `FALL_THROUGH`
<a id="insn-00acaf14"></a> `00acaf14` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acaf18"></a> `00acaf18` | `80 01 08 1f` | fmadd s0,s12,s8,s0 | `FALL_THROUGH`
<a id="insn-00acaf1c"></a> `00acaf1c` | `0c 28 2a 1e` | fadd s12,s0,s10 | `FALL_THROUGH`
<a id="insn-00acaf20"></a> `00acaf20` | `8c 19 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf24"></a> `00acaf24` | `00 68 79 bc` | ldr s0,[x0,x25] | `FALL_THROUGH`
<a id="insn-00acaf28"></a> `00acaf28` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acaf2c"></a> `00acaf2c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acaf30"></a> `00acaf30` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acaf34"></a> `00acaf34` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00acaf38"></a> `00acaf38` | `e5 03 15 2a` | mov w5,w21 | `FALL_THROUGH`
<a id="insn-00acaf3c"></a> `00acaf3c` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acaf40"></a> `00acaf40` | `26 00 80 52` | mov w6,#0x1 | `FALL_THROUGH`
<a id="insn-00acaf44"></a> `00acaf44` | `80 39 20 1e` | fsub s0,s12,s0 | `FALL_THROUGH`
<a id="insn-00acaf48"></a> `00acaf48` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00acaf4c"></a> `00acaf4c` | `3e 7b e6 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf50"></a> `00acaf50` | `80 19 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf54"></a> `00acaf54` | `ac 86 e6 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf58"></a> `00acaf58` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00acaf5c"></a> `00acaf5c` | `0b 2c 08 1f` | fmadd s11,s0,s8,s11 | `FALL_THROUGH`
<a id="insn-00acaf60"></a> `00acaf60` | `7c 19 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf64"></a> `00acaf64` | `00 68 78 bc` | ldr s0,[x0,x24] | `FALL_THROUGH`
<a id="insn-00acaf68"></a> `00acaf68` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acaf6c"></a> `00acaf6c` | `6b 39 20 1e` | fsub s11,s11,s0 | `FALL_THROUGH`
<a id="insn-00acaf70"></a> `00acaf70` | `78 19 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf74"></a> `00acaf74` | `20 b9 a1 5e` | fcvtzs s0,s9 | `FALL_THROUGH`
<a id="insn-00acaf78"></a> `00acaf78` | `08 68 79 b8` | ldr w8,[x0, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acaf7c"></a> `00acaf7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acaf80"></a> `00acaf80` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acaf84"></a> `00acaf84` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acaf88"></a> `00acaf88` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00acaf8c"></a> `00acaf8c` | `08 79 1f 53` | lsl w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acaf90"></a> `00acaf90` | `e5 03 15 2a` | mov w5,w21 | `FALL_THROUGH`
<a id="insn-00acaf94"></a> `00acaf94` | `26 00 80 52` | mov w6,#0x1 | `FALL_THROUGH`
<a id="insn-00acaf98"></a> `00acaf98` | `09 d8 21 5e` | scvtf s9,s0 | `FALL_THROUGH`
<a id="insn-00acaf9c"></a> `00acaf9c` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-00acafa0"></a> `00acafa0` | `60 39 20 1e` | fsub s0,s11,s0 | `FALL_THROUGH`
<a id="insn-00acafa4"></a> `00acafa4` | `00 38 29 1e` | fsub s0,s0,s9 | `FALL_THROUGH`
<a id="insn-00acafa8"></a> `00acafa8` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00acafac"></a> `00acafac` | `26 7b e6 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-00acafb0"></a> `00acafb0` | `68 19 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acafb4"></a> `00acafb4` | `94 86 e6 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-00acafb8"></a> `00acafb8` | `0b 00 22 1e` | scvtf s11,w0 | `FALL_THROUGH`
<a id="insn-00acafbc"></a> `00acafbc` | `65 19 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acafc0"></a> `00acafc0` | `00 68 78 bc` | ldr s0,[x0,x24] | `FALL_THROUGH`
<a id="insn-00acafc4"></a> `00acafc4` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acafc8"></a> `00acafc8` | `60 01 08 1f` | fmadd s0,s11,s8,s0 | `FALL_THROUGH`
<a id="insn-00acafcc"></a> `00acafcc` | `08 28 2a 1e` | fadd s8,s0,s10 | `FALL_THROUGH`
<a id="insn-00acafd0"></a> `00acafd0` | `60 19 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acafd4"></a> `00acafd4` | `00 68 79 bc` | ldr s0,[x0,x25] | `FALL_THROUGH`
<a id="insn-00acafd8"></a> `00acafd8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acafdc"></a> `00acafdc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acafe0"></a> `00acafe0` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acafe4"></a> `00acafe4` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00acafe8"></a> `00acafe8` | `e5 03 15 2a` | mov w5,w21 | `FALL_THROUGH`
<a id="insn-00acafec"></a> `00acafec` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acaff0"></a> `00acaff0` | `00 39 20 1e` | fsub s0,s8,s0 | `FALL_THROUGH`
<a id="insn-00acaff4"></a> `00acaff4` | `00 28 29 1e` | fadd s0,s0,s9 | `FALL_THROUGH`
<a id="insn-00acaff8"></a> `00acaff8` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00acaffc"></a> `00acaffc` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00acb000"></a> `00acb000` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acb004"></a> `00acb004` | `f9 1f 40 f9` | ldr x25,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00acb008"></a> `00acb008` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acb00c"></a> `00acb00c` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acb010"></a> `00acb010` | `fd fb 42 a9` | ldp x29,x30,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acb014"></a> `00acb014` | `e9 a3 41 6d` | ldp d9,d8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acb018"></a> `00acb018` | `eb ab 40 6d` | ldp d11,d10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acb01c"></a> `00acb01c` | `ec 07 47 fc` | ldr d12,[sp], #0x70 | `FALL_THROUGH`
<a id="insn-00acb020"></a> `00acb020` | `09 7b e6 17` | b 0x00469c44 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acae1c`](#insn-00acae1c) 範囲 `[['00acae1c', '00acb023']]`

## 命令位置別の参照

- [`00acae1c`](#insn-00acae1c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae20`](#insn-00acae20) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae24`](#insn-00acae24) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae28`](#insn-00acae28) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae2c`](#insn-00acae2c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae30`](#insn-00acae30) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae34`](#insn-00acae34) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae38`](#insn-00acae38) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae48`](#insn-00acae48) → [`004678a0`](../00467/004678a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004678a0` · 推定シンボル `None` · 推定型 `None`
- [`00acae58`](#insn-00acae58) → [`00489f8c`](../00489/00489f8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f8c` · 推定シンボル `None` · 推定型 `None`
- [`00acae70`](#insn-00acae70) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acae8c`](#insn-00acae8c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acae90`](#insn-00acae90) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`00acaea8`](#insn-00acaea8) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acaeb4`](#insn-00acaeb4) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acaec0`](#insn-00acaec0) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acaef8`](#insn-00acaef8) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`00acaefc`](#insn-00acaefc) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acaf00`](#insn-00acaf00) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`00acaf08`](#insn-00acaf08) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acaf0c`](#insn-00acaf0c) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acaf20`](#insn-00acaf20) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acaf4c`](#insn-00acaf4c) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`00acaf50`](#insn-00acaf50) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acaf54`](#insn-00acaf54) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`00acaf60`](#insn-00acaf60) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acaf64`](#insn-00acaf64) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acaf70`](#insn-00acaf70) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acafac`](#insn-00acafac) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`00acafb0`](#insn-00acafb0) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acafb4`](#insn-00acafb4) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`00acafbc`](#insn-00acafbc) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acafc0`](#insn-00acafc0) → `00333f84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acafd0`](#insn-00acafd0) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb000`](#insn-00acb000) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb004`](#insn-00acb004) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb008`](#insn-00acb008) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb00c`](#insn-00acb00c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb010`](#insn-00acb010) → `Stack[-0x48]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb014`](#insn-00acb014) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb018`](#insn-00acb018) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb020`](#insn-00acb020) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acae1c`](#insn-00acae1c)

~~~json
{
  "source": "00acae1c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae20`](#insn-00acae20)

~~~json
{
  "source": "00acae20",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae24`](#insn-00acae24)

~~~json
{
  "source": "00acae24",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae28`](#insn-00acae28)

~~~json
{
  "source": "00acae28",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae2c`](#insn-00acae2c)

~~~json
{
  "source": "00acae2c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae30`](#insn-00acae30)

~~~json
{
  "source": "00acae30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae34`](#insn-00acae34)

~~~json
{
  "source": "00acae34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae38`](#insn-00acae38)

~~~json
{
  "source": "00acae38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae48`](#insn-00acae48)

~~~json
{
  "source": "00acae48",
  "target": "004678a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae58`](#insn-00acae58)

~~~json
{
  "source": "00acae58",
  "target": "00489f8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae70`](#insn-00acae70)

~~~json
{
  "source": "00acae70",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae8c`](#insn-00acae8c)

~~~json
{
  "source": "00acae8c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae90`](#insn-00acae90)

~~~json
{
  "source": "00acae90",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaea8`](#insn-00acaea8)

~~~json
{
  "source": "00acaea8",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaeb4`](#insn-00acaeb4)

~~~json
{
  "source": "00acaeb4",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f0a56c00a48c0900",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acaec0`](#insn-00acaec0)

~~~json
{
  "source": "00acaec0",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaef8`](#insn-00acaef8)

~~~json
{
  "source": "00acaef8",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaefc`](#insn-00acaefc)

~~~json
{
  "source": "00acaefc",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf00`](#insn-00acaf00)

~~~json
{
  "source": "00acaf00",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf08`](#insn-00acaf08)

~~~json
{
  "source": "00acaf08",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf0c`](#insn-00acaf0c)

~~~json
{
  "source": "00acaf0c",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f0a56c00a48c0900",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acaf20`](#insn-00acaf20)

~~~json
{
  "source": "00acaf20",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf4c`](#insn-00acaf4c)

~~~json
{
  "source": "00acaf4c",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf50`](#insn-00acaf50)

~~~json
{
  "source": "00acaf50",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf54`](#insn-00acaf54)

~~~json
{
  "source": "00acaf54",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf60`](#insn-00acaf60)

~~~json
{
  "source": "00acaf60",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf64`](#insn-00acaf64)

~~~json
{
  "source": "00acaf64",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f0a56c00a48c0900",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acaf70`](#insn-00acaf70)

~~~json
{
  "source": "00acaf70",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acafac`](#insn-00acafac)

~~~json
{
  "source": "00acafac",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acafb0`](#insn-00acafb0)

~~~json
{
  "source": "00acafb0",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acafb4`](#insn-00acafb4)

~~~json
{
  "source": "00acafb4",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acafbc`](#insn-00acafbc)

~~~json
{
  "source": "00acafbc",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acafc0`](#insn-00acafc0)

~~~json
{
  "source": "00acafc0",
  "target": "00333f84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f80",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f0a56c00a48c0900",
  "capture_start": "00333f80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acafd0`](#insn-00acafd0)

~~~json
{
  "source": "00acafd0",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb000`](#insn-00acb000)

~~~json
{
  "source": "00acb000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb004`](#insn-00acb004)

~~~json
{
  "source": "00acb004",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb008`](#insn-00acb008)

~~~json
{
  "source": "00acb008",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb00c`](#insn-00acb00c)

~~~json
{
  "source": "00acb00c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb010`](#insn-00acb010)

~~~json
{
  "source": "00acb010",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb014`](#insn-00acb014)

~~~json
{
  "source": "00acb014",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb018`](#insn-00acb018)

~~~json
{
  "source": "00acb018",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb020`](#insn-00acb020)

~~~json
{
  "source": "00acb020",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
